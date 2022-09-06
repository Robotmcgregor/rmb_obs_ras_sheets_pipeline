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

# import modules
import os
import shutil
from glob import glob
import sys


def search_html_files_fn(transect_dir, site):
    """ Search for all html files within a directory.

    :param transect_dir: string object containing the path to the directory containing all html transect tables.
    :param site: string object containing the site name currently being worked on.
    :return html_list: list object containing all located html paths.
    """
    # create an empty list
    html_list = []

    for file in glob(transect_dir + '//' + site + '_transect?.html'):
        # append file paths to list
        html_list.append(file)

    return html_list


def move_html_files(html_list, site_dir):
    """ Copy html tables into site specific directories.

    :param html_list: list object containing all located html paths.
    :param site_dir: string object containing the path to the site specific directory.
    """
    for i in html_list:
        _, file = i.rsplit('\\', 1)

        shutil.copy(i, site_dir + '//' + file)


def main_routine(obs_data_list, property_name, site_code, site_dir, star, remote_desktop, html_dir,
                 photo_date):
    """Extract the URL's contained within the Star Transect ODK Aggregate .csv for the star transect repeats (transect).
    Open and log into ODK Aggregate using the testodk username and password,
    navigate and open the transect tables, and download the table data as a .html so that it can be imported as a Pandas
    DataFrame in the following script.

    :param obs_data_list: nested list object containing observational sheet inputs.
    :param property_name: string object containing teh property name.
    :param site_code: string object containing the site code (i.e. RHD01A)
    :param site_dir: string object containing the path to the site sub-directory within the export directory.
    :param star:
    :param remote_desktop: string object variable used to define the workflow (command argument)
    :param html_dir: string object containing the path to the html directory.
    :param photo_date: string object containing the photo date YYYYMMDD.
    """

    print('9_1, star: ', star)
    prop, site = site_code.rsplit('_', 1)

    transect_dir = html_dir

    html_list = search_html_files_fn(transect_dir, site)

    if html_list:
        move_html_files(html_list, site_dir)
    else:
        print('You are processing sheets locally or offline; as such, you are required to manually download and have '
              'transect data as an html file. The naming convention must be:'
              ' (site name (CAPS) + underscore + transect + 1, 2 or 3 (i.e."ADR01A_transect2"')
        print('No html transect files for site: ', site, ' were located.')
        print('------------------------ system abort. -------------------------')
        sys.exit()

    # call the step10_1_site_observation_sheet_processing_workflow.py script.
    import step10_1_site_observation_sheet_processing_workflow
    step10_1_site_observation_sheet_processing_workflow.main_routine(obs_data_list, property_name, site, site_dir, star,
                                                                     remote_desktop, photo_date)


if __name__ == "__main__":
    main_routine()
