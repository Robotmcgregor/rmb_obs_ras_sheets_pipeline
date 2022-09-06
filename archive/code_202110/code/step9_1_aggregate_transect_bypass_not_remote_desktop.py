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

"""
Extract the URL's contained within the Star Transect ODK Aggregate .csv for the star transect repeats (transects).
Open and log into ODK Aggregate using the testodk username and password, 
navigate and open the transect tables, and download the table data as a .html so that it can be imported as a Pandas DataFrame in the following script.


Command arguments:
------------------

--siteStarDF
The odk star transect csv downloaded from ODK Aggregate.

--chromedriver
The file path for the chrome extension driver, default location is set to: r"Z:\Scratch\Rob\chrome\chromedriver.exe"


======================================================================================================

Variables:

--siteStarDF: DataFrame
DataFrame object containing the ODK Star Transect results .csv - Csv is retrieved from ODK Aggregate and it retrieval can be achieved manually or by running the xxxx.py script (Rob McGregor, 2020)

--i: URL
URL object containing the url for an individual transect 1 table stored within ODK Aggregate - this varible is used as a base for transect2 and transect3.

--meta: str
String object containing the metadata key, extracted from the df DafaFrame which matches the transectUrl information.

--metaKey: str
String object containing the final metadata key, extracted from the meta variable.

--prefex: str
String object containing unnecessary information at the beginning of the metadata key, extracted from the meta variable.

--chrome_driver: str
String object containing the path to the Chrome Driver required for Selenium.

--site: str
String object containing the site name, extracted from the df DafaFrame which matches the transectUrl information.

--transect: URL
URL object containing the url for an individual transect 1 table stored within ODK Aggregate with the last character removed.

--transect2: URL
URL object containing the url for an individual transect 2 table stored within ODK Aggregate.

--transect3: URL
URL object containing the url for an individual transect 3 table stored within ODK Aggregate.

--tranUrlList: list
List object containing the URL's to access the transect (repeat) table from ODK Aggregate.



========================================================================================================
"""
# import modules
import os
import shutil
from glob import glob
import sys



def search_html_files_fn(transect_dir, site):
    """ Search for all html files within a directory. """
    # create an empty list
    html_list = []

    for file in glob(transect_dir + '//' + site + '_transect?.html'):
        # append file paths to list
        html_list.append(file)

    return html_list


def move_html_files(html_list, site, site_dir):

    for i in html_list:
        _, file = i.rsplit('\\', 1)
        # print('file: ', file)

        shutil.copy(i, site_dir + '//' + file)
        #print(file, ' has been copied to: ', site_dir)


def main_routine(directory_odk, obs_data_list, property_name, site_code, site_dir, star, remote_desktop, html_dir, photo_date):
    """Extract the URL's contained within the Star Transect ODK Aggregate .csv for the star transect repeats (transects).
    Open and log into ODK Aggregate using the testodk username and password,
    navigate and open the transect tables, and download the table data as a .html so that it can be imported as a Pandas
    DataFrame in the following script.
    """

    #print('step9_1_aggregate_transect_bypass_not_remote_desktop.py INITIATED.')

    prop, site = site_code.rsplit('_', 1)

    transect_dir = html_dir

    html_list = search_html_files_fn(transect_dir, site)

    if html_list:
        move_html_files(html_list, site, site_dir)
    else:
        print('You are processing sheets locally or offline; as such, you are required to manually download and have '
              'transect data as an html file. The naming convention must be:'
              ' (site name (CAPS) + underscore + transect + 1, 2 or 3 (i.e."ADR01A_transect2"')
        print('No html transect files for site: ', site, ' were located.')
        print('------------------------ system abort. -------------------------')

        sys.exit()

    #print('step9_1_aggregate_transect_bypass_not_remote_desktop.py  COMPLETED.')
    #print('step10_1_site_observation_sheet_processing_workflow.py initiating..........')

    # call the step10_1_site_observation_sheet_processing_workflow.py script.
    import step10_1_site_observation_sheet_processing_workflow
    step10_1_site_observation_sheet_processing_workflow.main_routine(obs_data_list, property_name, site, site_dir, star,
                                                                     remote_desktop, photo_date)


if __name__ == "__main__":
    main_routine()
