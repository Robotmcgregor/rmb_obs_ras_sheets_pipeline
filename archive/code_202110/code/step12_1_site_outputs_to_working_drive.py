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

from __future__ import print_function, division
import pandas as pd
import glob
import os
import geopandas as gpd
from datetime import datetime
import shutil
import warnings


def add_values_in_dict_fn(site_dict, key, list_of_values):
    """Append multiple values to a key in the given dictionary.

    :param site_dict: dictionary object containing the key site (property_site) and multiple values in a list.
    :param key: string object containing the site name.
    :param list_of_values: list object containing three values: district, property and site.
    :return site_dict: updated dictionary"""

    if key not in site_dict:
        site_dict[key] = list()
    site_dict[key].extend(list_of_values)

    return site_dict


def prop_code_extraction_fn(prop, pastoral_estate):
    property_list = pastoral_estate.PROPERTY.tolist()

    prop_upper = prop.upper().replace('_', ' ')

    if prop_upper in property_list:

        prop_code = pastoral_estate.loc[pastoral_estate['PROPERTY'] == prop_upper, 'PROP_TAG'].iloc[0]
    else:
        prop_code = ''

    return prop_code


def search_for_files_fn(site_dict, search_criteria, directory, pastoral_estate):

    csv_list = []

    for dirpath, subdirs, files in os.walk(directory):

        csv_list.extend(os.path.join(dirpath, x) for x in files if x.endswith(search_criteria))

    for i in csv_list:
        df = pd.read_csv(i)
        site = df.site.iloc[0]
        dist = df.district.iloc[0].replace(' ', '_')
        if dist == 'Northern_Alice_Springs':
            district = 'Northern_Alice'
        elif dist == 'Southern_Alice_Springs':
            district = 'Southern_Alice'
        elif dist == 'Victoria_River':
            district = 'VRD'
        else:
            district = dist

        prop = df.final_prop.iloc[0]
        prop_name = prop.replace(" ", "_")
        site_orig = df.site_orig.iloc[0]
        date = df.date.iloc[0]
        print('-'*50)
        print('date: ', date)
        str_date = str(date)
        print(str_date)
        year2 = str_date[-2:]
        year2_final = '20' + str(year2)
        print('year2_final: ', year2_final)
        year4 = str_date[-4:]
        print('year4: ', year4)
        # convert str to datetime
        date_time_obj = datetime.strptime(str(date), '%d/%m/%Y')
        print('date_time_obj: ', date_time_obj)
        # extract year
        year = date_time_obj.strftime("%Y")
        #year = date_time_obj.year
        print('year: ', year)

        prop_code = prop_code_extraction_fn(prop, pastoral_estate)

        list_values = [district, prop_code, prop_name, site_orig, str(year)]

        site_dict = add_values_in_dict_fn(site_dict, site, list_values)

    return site_dict, csv_list


def check_create_folders_fn(path):
    """Check if directory exists, if not, create it
    :param path:
    """

    # Check for directory.

    check_folder = os.path.isdir(path)
    # Create directory if it does not exist.
    if not check_folder:

        # create directory
        os.mkdir(path)
        # create sub folder
        raw = os.path.join(path, 'Raw')
        os.mkdir(raw)
        # create sub folder
        draft = os.path.join(path, 'Draft')
        os.mkdir(draft)
        # create sub folder
        final = os.path.join(path, 'Final')
        os.mkdir(final)


    else:

        # create sub folder
        raw = os.path.join(path, 'Raw')
        check_raw_folder = os.path.isdir(raw)
        if not check_raw_folder:
            # create directory
            os.mkdir(raw)

        # create sub folder
        draft = os.path.join(path, 'Draft')
        check_draft_folder = os.path.isdir(draft)
        if not check_draft_folder:
            # create directory
            os.mkdir(draft)
        # create sub folder
        final = os.path.join(path, 'Final')
        check_final_folder = os.path.isdir(final)
        if not check_final_folder:
            # create directory
            os.mkdir(final)

    return raw


def join_ras_site_photo_file_path_2_fn(pathway, output_drive, values_, search_criteria, site_type):
    files = glob.glob(pathway + search_criteria)

    for f in files:
        photo_file_path = os.path.join(output_drive, values_[0],
                                       str(values_[1]) + '_' + str(values_[2]),
                                       'Photos', str(site_type), str(values_[4]))

        # Check for directory.
        check_folder = os.path.isdir(photo_file_path)

        # Create directory if it does not exist.
        if not check_folder:
            # create directory
            os.mkdir(photo_file_path)

        shutil.copy(f, photo_file_path)


def join_transect_site_html_file_path_fn(pathway, output_drive, values_, search_criteria, site_type, file_type):
    files = glob.glob(pathway + search_criteria)

    if files:
        for f in files:
            processed_odk_path = os.path.join(output_drive, values_[0],
                                              str(values_[1]) + '_' + str(values_[2]),
                                              'Data', 'Processed_Odk')  # str(site_type), str(values_[4]))

            # Check for directory.
            check_folder = os.path.isdir(processed_odk_path)

            # Create directory if it does not exist.
            if not check_folder:
                # create directory
                os.mkdir(processed_odk_path)

            # create sub folder
            measured = os.path.join(processed_odk_path, str(site_type))
            check_measured_folder = os.path.isdir(measured)
            if not check_measured_folder:
                # create directory
                os.mkdir(measured)

            year = os.path.join(measured, str(values_[4]))
            check_year_folder = os.path.isdir(year)
            if not check_year_folder:
                # create directory
                os.mkdir(year)

            # create sub folder
            transect = os.path.join(year, str(file_type))
            check_transect_folder = os.path.isdir(transect)
            if not check_transect_folder:
                # create directory
                os.mkdir(transect)

            shutil.copy(f, transect)
    else:
        pass


def join_xlsx_site_file_path_fn(pathway, output_drive, values_, search_criteria, site_type):
    """

    :param pathway:
    :param output_drive:
    :param values_:
    :param search_criteria:
    :param site_type:
    """
    files = glob.glob(pathway + search_criteria)

    if files:
        for f in files:
            processed_odk_path = os.path.join(output_drive, values_[0],
                                              str(values_[1]) + '_' + str(values_[2]),
                                              'Data', str(site_type), str(values_[4]))

            # Check for directory.
            check_folder = os.path.isdir(processed_odk_path)

            # Create directory if it does not exist.
            if not check_folder:
                # create directory
                os.mkdir(processed_odk_path)

            # create sub folder
            raw = os.path.join(processed_odk_path, 'Raw')
            check_measured_folder = os.path.isdir(raw)
            if not check_measured_folder:
                # create directory
                os.mkdir(raw)
                #print('f: ', f)
                #print('raw: ', raw)
            shutil.copy(f, raw)
    else:
        pass


def join_csv_file_path_fn(search_criteria, output_drive, directory, geo_series, n, location):
    """

    :param search_criteria: string object containing a variable of the file path name
    :param output_drive:
    :param directory:
    :param geo_series:
    :param n:
    :param location:
    """

    site_dict = {}

    site_dict, csv_list = search_for_files_fn(site_dict, search_criteria, directory, geo_series)
    print(' line 265')
    for i in csv_list:

        # split filename from path and split by "_"
        pathway, file = i.rsplit('\\', 1)
        prop, file_name = file.split('_' + search_criteria)

        values_ = site_dict[prop]

        ras_file_path = os.path.join(output_drive, values_[0],
                                     str(values_[1]) + '_' + str(values_[2]),
                                     str(location), str(n), str(values_[4]))

        ('ras_file_path: ', ras_file_path)

        raw = check_create_folders_fn(ras_file_path)

        print('values_: ', values_)
        if values_[3].endswith('A'):
            if n != 'Ras':
                site_type_xlsx = 'Observation_Sheets'
                site_type_other = 'Measured'
                join_xlsx_site_file_path_fn(pathway, output_drive, values_, '\\*xlsx', site_type_xlsx)
                join_transect_site_html_file_path_fn(pathway, output_drive, values_, '\\*.csv', site_type_other, 'Csv')
                join_transect_site_html_file_path_fn(pathway, output_drive, values_, '\\*.html', site_type_other,
                                                     'Transect')
                join_ras_site_photo_file_path_2_fn(pathway, output_drive, values_, '\\*.jpg', site_type_other)

            else:
                site_type_xlsx = 'Ras'
                site_type_other = 'Ras'
                join_xlsx_site_file_path_fn(pathway, output_drive, values_, '\\*xlsx', site_type_xlsx)
                join_ras_site_photo_file_path_2_fn(pathway, output_drive, values_, '\\*.jpg', site_type_other)

        elif values_[3].startswith('RAS'):
            site_type_xlsx = 'Ras'
            site_type_other = 'Ras'
            join_xlsx_site_file_path_fn(pathway, output_drive, values_, '\\*xlsx', site_type_xlsx)
            join_ras_site_photo_file_path_2_fn(pathway, output_drive, values_, '\\*.jpg', site_type_other)

        else:
            site_type_xlsx = 'Ras'
            site_type_other = 'Tier1'
            join_xlsx_site_file_path_fn(pathway, output_drive, values_, '\\*xlsx',
                                        site_type_xlsx)  # todo check that tier 1 should not be filed separately
            join_ras_site_photo_file_path_2_fn(pathway, output_drive, values_, '\\*.jpg', site_type_other)


def join_processed_csv_file_path_fn(pathway, output_drive, values_, search_criteria, site_type):
    """

    :param pathway:
    :param output_drive:
    :param values_:
    :param search_criteria:
    :param site_type:
    """

    files = glob.glob(pathway + search_criteria)

    for f in files:
        processed_odk_path = os.path.join(output_drive, values_[0],
                                          str(values_[1]) + '_' + str(values_[2]),
                                          'Data', 'Processed_Odk',
                                          'Measured')  # str(site_type), str(values_[4]))

        # Check for directory.
        check_folder = os.path.isdir(processed_odk_path)

        # Create directory if it does not exist.
        if not check_folder:

            # create directory
            os.mkdir(processed_odk_path)
            # create sub folder
            year = os.path.join(processed_odk_path, str(values_[4]), 'Csv')
            os.mkdir(year)

        else:

            # create sub folder
            year = os.path.join(processed_odk_path, str(values_[4]), 'Csv')
            check_raw_folder = os.path.isdir(year)
            if not check_raw_folder:
                # create directory
                os.mkdir(year)

        shutil.copy(f, year)


def join_prop_dir_file_path_fn(pathway, output_drive, values_, geo_series, search_criteria, param2):
    files = glob.glob(pathway + search_criteria)
    #print(files)

    for f in files:
        processed_odk_path = os.path.join(output_drive, values_[0],
                                          str(values_[1]) + '_' + str(values_[2]),
                                          'Data', 'Processed_Odk',
                                          'Measured')  # str(site_type), str(values_[4]))
        #print('---processed_odk_path: ', processed_odk_path)
    pass


def main_routine(export_site_dir, pastoral_estate, pastoral_districts_path, temp_dir):

    path_parent = os.path.dirname(os.getcwd())

    geo_df = gpd.read_file(pastoral_estate)

    geo_series = geo_df[['PROPERTY', 'PROP_TAG']]
    print('375')
    join_csv_file_path_fn('clean_ras.csv', pastoral_districts_path, export_site_dir, geo_series, 'Ras', 'Data')

    join_csv_file_path_fn('clean_star_transect.csv', pastoral_districts_path, export_site_dir, geo_series,
                          'Observation_sheets', 'Data')

    #prop_outputs_dir = '{}\\{}'.format(temp_dir, 'prop_outputs')
    #join_csv_file_path_fn('ras.csv', pastoral_districts_path, prop_outputs_dir, geo_series, 'Ras', 'Data')

    """join_csv_file_path_fn('clean_star_transect.csv', pastoral_districts_path, prop_outputs_dir, geo_series,
                          'Observation_sheets', 'Data')"""

    """# extract shapefiles and file per property
    output_list = ['\\clean_ras_gda94.shp', '\\clean_integrated_gda94.shp', '\\clean_star_transect_gda94.shp',
                   '\\clean_basal_gda94.shp', '\\clean_woody_thickening_gda94.shp']

    for search_criteria in output_list:
        for file in glob(export_site_dir + search_criteria):
            print(file)
            gdf = gpd.read_file(file)"""

    #print('step12_1_site_outputs_to_working_drive.py COMPLETED.')


if __name__ == "__main__":
    main_routine()
