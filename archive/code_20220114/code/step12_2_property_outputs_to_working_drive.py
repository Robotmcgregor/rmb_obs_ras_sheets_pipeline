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


def prop_code_extraction_fn(prop, pastoral_estate):
    property_list = pastoral_estate.PROPERTY.tolist()

    prop_upper_ = prop.upper().replace('_', ' ')
    prop_upper = prop_upper_.strip()

    if prop_upper in property_list:

        prop_code = pastoral_estate.loc[pastoral_estate['PROPERTY'] == prop_upper, 'PROP_TAG'].iloc[0]

    elif prop_upper == 'LA BELLE DOWNS':
        # todo La Belle Downs folder issue
        prop_code = 'LBD'

    else:
        prop_code = ''

    return prop_code


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


def date_column_fn(gdf):
    new_date_list = []

    date_list = gdf.date.tolist()

    for date in date_list:
        date_time_obj = datetime.strptime(date, '%d/%m/%Y')
        year = date_time_obj.strftime("%Y")
        month = date_time_obj.strftime("%m")
        day = date_time_obj.strftime("%d")
        new_date = '{0}-{1}-{2}'.format(year, month, day)
        new_date_list.append(new_date)

    return new_date_list


def infrastructure_formatting_fn(gdf):
    new_date_list = date_column_fn(gdf)

    gdf['FEATGROUP'] = "Monitoring Sites"
    gdf['FEATURE'] = "Integrated"
    gdf['DATE_CURR'] = 'nan'
    gdf['DATE_INSP'] = new_date_list
    gdf['PROP_TAG'] = 'nan'
    gdf['PROPERTY'] = gdf['final_prop'].str.upper()
    del gdf['final_prop']
    del gdf['date']

    gdf.insert(8, 'SOURCE', 'NTG Rangeland Monitoring Branch')
    gdf.insert(9, 'CONFIDENCE', 2)
    gdf.insert(10, 'MAPDISPLAY', 'Yes')

    gdf.rename(columns={'site_orig': 'LABEL', 'district': 'DISTRICT'}, inplace=True)

    final_gdf = gdf[
        ['FEATURE', 'LABEL', 'DATE_INSP', 'DATE_CURR', 'DISTRICT', 'PROPERTY', 'PROP_TAG', 'SOURCE', 'CONFIDENCE',
         'MAPDISPLAY', 'geometry']]

    return final_gdf


def main_routine(temp_dir, pastoral_estate_path, pastoral_districts_path):
    prop_output_dir = '{0}\\{1}'.format(temp_dir, 'prop_output')
    print('prop_output_dir: ', prop_output_dir)
    pastoral_estate = gpd.read_file(pastoral_estate_path)

    subfolder_list = next(os.walk(prop_output_dir))[0]
    # extract the property name
    subfolder_list = os.listdir(prop_output_dir)

    list_subfolders_with_paths = [f.path for f in os.scandir(prop_output_dir) if f.is_dir()]
    site_dict = {}
    print('list_subfolders_with_paths: ', list_subfolders_with_paths)
    for i in list_subfolders_with_paths:
        _, prop = i.rsplit('\\', 1)
        print('_', _)
        print('prop: ', prop)
        subfolder_list = next(os.walk(i))[1]
        for dir_path in subfolder_list:
            src_path = os.path.join(i, dir_path)

            file_list2 = []
            for files in os.walk(src_path):

                file_list1 = []
                for file in files:
                    file_path = os.path.join(src_path, file)
                    file_list2.append(file_path)

            for file_path in file_list2:

                if file_path.endswith('star_transect.csv'):
                    df = pd.read_csv(file_path)
                    date = df.date.iloc[0]
                    # convert str to datetime
                    date_time_obj = datetime.strptime(date, '%d/%m/%Y')
                    # extract year
                    year = date_time_obj.year

                    site_orig = df.site_orig.iloc[0]

                    dist = df.district.iloc[0].replace(' ', '_')

                    if dist == 'Northern_Alice_Springs':
                        district = 'Northern_Alice'
                    elif dist == 'Southern_Alice_Springs':
                        district = 'Southern_Alice'
                    elif dist == 'Victoria_River':
                        district = 'VRD'
                    else:
                        district = dist

                    prop_code = prop_code_extraction_fn(prop, pastoral_estate)

                    list_values = [district, prop_code, prop, str(year)]

                    site_dict = add_values_in_dict_fn(site_dict, prop, list_values)

                elif file_path.endswith('ras.csv'):
                    df = pd.read_csv(file_path)

                    date = df.date.iloc[0]
                    # convert str to datetime
                    date_time_obj = datetime.strptime(date, '%d/%m/%Y')
                    # extract year
                    year = date_time_obj.year

                    site_orig = df.site_orig.iloc[0]

                    dist = df.district.iloc[0].replace(' ', '_')

                    if dist == 'Northern_Alice_Springs':
                        district = 'Northern_Alice'
                    elif dist == 'Southern_Alice_Springs':
                        district = 'Southern_Alice'
                    elif dist == 'Victoria_River':
                        district = 'VRD'
                    else:
                        district = dist

                    prop_code = prop_code_extraction_fn(prop, pastoral_estate)

                    list_values = [district, prop_code, prop, str(year)]

                    site_dict = add_values_in_dict_fn(site_dict, prop, list_values)

            for file_path in file_list2:

                if file_path.endswith('.csv'):
                    file_type = 'Csv'

                    orig_file_path, file_name = file_path.rsplit("\\", 1)

                    values_ = site_dict[prop]

                    output_file_path = os.path.join(pastoral_districts_path, values_[0],
                                                    str(values_[1]) + '_' + str(values_[2]),
                                                    'Data', 'Processed_Odk')

                    check_file_type_folder = os.path.isdir(output_file_path)

                    if not check_file_type_folder:
                        # create directory
                        os.mkdir(output_file_path)

                    # create sub folder
                    file_property_path = os.path.join(output_file_path, 'Property')
                    check_property_type_folder = os.path.isdir(file_property_path)

                    if not check_property_type_folder:
                        # create directory
                        os.mkdir(file_property_path)

                    # create sub folder
                    file_year_path = os.path.join(file_property_path, str(values_[3]))
                    check_year_type_folder = os.path.isdir(file_year_path)

                    if not check_year_type_folder:
                        # create directory
                        os.mkdir(file_year_path)

                    # create sub folder
                    file_type_path = os.path.join(file_year_path, file_type)
                    check_file_type_folder = os.path.isdir(file_type_path)

                    if not check_file_type_folder:
                        # create directory
                        os.mkdir(file_type_path)

                    shutil.copy(file_path, "{0}\\{1}".format(file_type_path, file_name))

                    # load offset to field data directory
                    print('orig_file_path: ', orig_file_path)
                    print('file_name: ', file_name)

                    if file_name.endswith('star_transect.csv'):
                        print('star transect located')
                        offset_df = pd.read_csv(file_path)

                        offset_gdf = gpd.GeoDataFrame(
                            offset_df, geometry=gpd.points_from_xy(offset_df.gda_o_lon, offset_df.gda_o_lat))

                        offset_gdf_gda94 = offset_gdf.set_crs(epsg=4283)

                        offset_gdf_gda94_ = infrastructure_formatting_fn(offset_gdf_gda94)

                        output_file_path = os.path.join(pastoral_districts_path, values_[0],
                                                        str(values_[1]) + '_' + str(values_[2]),
                                                        'Infrastructure', 'Field_Data')
                        check_file_type_folder = os.path.isdir(output_file_path)

                        if not check_file_type_folder:
                            # create directory
                            os.mkdir(output_file_path)

                        # create sub folder
                        file_year_path3 = os.path.join(output_file_path, str(values_[3]))

                        check_year_type_folder = os.path.isdir(file_year_path3)

                        if not check_year_type_folder:
                            # create directory
                            os.mkdir(file_year_path3)

                        # create sub folder
                        raw_path = os.path.join(file_year_path3, 'Raw')
                        check_file_type_folder = os.path.isdir(raw_path)

                        if not check_file_type_folder:
                            # create directory
                            os.mkdir(raw_path)

                        # create sub folder
                        offset_path = os.path.join(raw_path, 'offset_mon_points')
                        check_file_type_folder = os.path.isdir(offset_path)

                        if not check_file_type_folder:
                            # create directory
                            os.mkdir(offset_path)

                        # create sub folder
                        shp_path = os.path.join(offset_path, 'Shp')
                        check_property_type_folder = os.path.isdir(shp_path)

                        if not check_property_type_folder:
                            # create directory
                            os.mkdir(shp_path)

                        offset_gdf_gda94_.to_file(
                            '{0}\\{1}_{2}_offset_inter_points_gda94.shp'.format(shp_path, str(values_[1]),
                                                                                str(values_[2])))
                        shutil.copy(file_path, "{0}\\{1}".format(file_type_path, file_name))

                        # filter only new properties
                        '''new = offset_gdf_gda94_[offset_gdf_gda94_['establish']=='new']
                        if len(new.index) > 0:
                            new.to_file(
                                '{0}\\{1}_{2}_offset_new_inter_points_gda94.shp'.format(shp_path, str(values_[1]),
                                                                                    str(values_[2])))'''

                else:
                    file_type = 'Shp'

                    orig_file_path, file_name = file_path.rsplit("\\", 1)

                    values_ = site_dict[prop]
                    output_file_path = os.path.join(pastoral_districts_path, values_[0],
                                                    str(values_[1]) + '_' + str(values_[2]),
                                                    'Data', 'Processed_Odk')

                    check_file_type_folder = os.path.isdir(output_file_path)

                    if not check_file_type_folder:
                        # create directory
                        os.mkdir(output_file_path)

                    # create sub folder
                    file_property_path = os.path.join(output_file_path, 'Property')
                    check_property_type_folder = os.path.isdir(file_property_path)

                    if not check_property_type_folder:
                        # create directory
                        os.mkdir(file_property_path)

                    # create sub folder
                    file_year_path = os.path.join(file_property_path, str(values_[3]))
                    check_year_type_folder = os.path.isdir(file_year_path)

                    if not check_year_type_folder:
                        # create directory
                        os.mkdir(file_year_path)

                    # create sub folder
                    file_type_path = os.path.join(file_year_path, file_type)
                    check_file_type_folder = os.path.isdir(file_type_path)

                    if not check_file_type_folder:
                        # create directory
                        os.mkdir(file_type_path)

                    shutil.copy(file_path, "{0}\\{1}".format(file_type_path, file_name))


if __name__ == "__main__":
    main_routine()
