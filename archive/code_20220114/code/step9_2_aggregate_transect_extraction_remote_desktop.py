#!/usr/bin/env python

"""
Copyright 2021 Robert McGregor

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Import modules
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


def collate_transect_urls_fn(df):
    """
    Extract the transect URL's from the odk star transect results csv.

    :param df: pandas dataframe object.
    :return tran_url_list: list object containing the urls for each transect html.
    """

    tran1, tran2, tran3 = df.tran1_url[0], df.tran2_url[0], df.tran3_url[0]
    tran_url_list = [tran1, tran2, tran3]

    return tran_url_list


def odk_aggregate_log_in_fn(chrome_driver):
    """ Log in to ODK Aggregate using Selenium.
    :param chrome_driver: string variable containing the path to the chrome driver.
    :return driver: selenium driver object managing the open website.
    """

    driver = webdriver.Chrome(chrome_driver)
    time.sleep(5)
    # open and log in to ODK Aggregate
    driver.get("https://odktest:odktest@pgb-bas14.nt.gov.au:8443/ODKAggregate")

    # allow a five second time interval before the next function
    time.sleep(5)

    return driver


def transect_table_fn(driver, i, loop, site_folder_path, site):
    """ Open, download and save a transect html table.

    :param driver: selenium driver object managing the open website.
    :param i: string object containing the current url.
    :param loop: integer object containing the transect number 1, 2 or 3
    :param site_folder_path: string object containing the path to the site sub-directory within the export directory.
    :param site: string object containing the site name.
    """

    # open transect 1 table webpage
    time.sleep(5)
    driver.get(i)
    time.sleep(5)

    transect_label = 'transect' + str(loop)
    # copy and save the transect table as an html
    with open(site_folder_path + "//" + site + '_' + transect_label + ".html", "w") as f:
        f.write(driver.page_source)

    return driver


def close_diver_fn(driver):
    """ Close and quite the chrome driver.

    :param driver: selenium driver object managing the open website.
    """
    # close the chrome driver.
    time.sleep(5)
    driver.close()
    driver.quit()


def main_routine(obs_data_list, property_name, site_code, site_dir, star, remote_desktop, chrome_driver, photo_date):
    """
    Extract the URL's contained within the Star Transect ODK Aggregate .csv for the star transect repeats (transects).
    Open and log into ODK Aggregate using the testodk username and password,
    navigate and open the transect tables, and download the table data as a .html so that it can be imported as a Pandas
    data frame in the following script.
    :param photo_date: string object containing the photo date YYYYMMDD.
    :param chrome_driver: string object containing the path to the required
    :param obs_data_list: nested list object containing observational sheet inputs.
    :param property_name: string object containing teh property name.
    :param site_code: string object containing the site code (i.e. RHD01A)
    :param site_dir: string object containing the path to the site sub-directory within the export directory.
    :param star: pandas dataframe containing the processed star transect information produced by
    step2_1_star_transect_processing_workflow.py
    :param remote_desktop: string object variable used to define the workflow (command argument)
    """

    prop, site = site_code.rsplit('_', 1)

    # call the collate_transect_urls_fn function to extract the transect URL's from the odk star transect results csv.
    tran_url_list = collate_transect_urls_fn(star)

    # call the odk_aggregate_log_in_fn function to log in to ODK Aggregate using Selenium.
    driver = odk_aggregate_log_in_fn(chrome_driver)

    loop = 1

    for i in tran_url_list:
        # call the transect_table_fn function to open, download and save a transect html table.
        driver = transect_table_fn(driver, i, loop, site_dir, site)

        loop += 1

    close_diver_fn(driver)

    # call the step10_1_site_observation_sheet_processing_workflow.py script.
    import step10_1_site_observation_sheet_processing_workflow
    step10_1_site_observation_sheet_processing_workflow.main_routine(obs_data_list, property_name, site, site_dir, star,
                                                                     remote_desktop, photo_date)


if __name__ == "__main__":
    main_routine()
