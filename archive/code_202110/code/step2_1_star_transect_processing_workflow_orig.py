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
import warnings
from datetime import datetime
import pandas as pd
import numpy as np
import geopandas as gpd

warnings.filterwarnings("ignore")


def string_clean_upper_fn(dirty_string):
    """ Remove whitespaces and clean strings.

            :param dirty_string: string object.
            :return clean_string: processed string object. """

    str1 = dirty_string.replace('_', ' ')
    str2 = str1.replace('-', ' ')
    str3 = str2.replace('  ', ' ')
    str4 = str3.upper()
    clean_str = str4.strip()

    if clean_str == 'End selection':
        clean_string = 'nan'
    else:
        clean_string = clean_str

    return clean_string


def string_clean_capital_fn(dirty_string):
    """ Remove whitespaces and clean strings.

            :param dirty_string: string object.
            :return clean_string: processed string object."""

    str1 = dirty_string.replace('_', ' ')
    str2 = str1.replace('-', ' ')
    str3 = str2.replace('  ', ' ')
    str4 = str3.capitalize()
    clean_str = str4.strip()

    if clean_str == 'End selection':
        clean_string = 'nan'
    else:
        clean_string = clean_str

    return clean_string


def string_clean_title_fn(dirty_string):
    """ Remove whitespaces and clean strings.

            :param dirty_string: string object.
            :return clean_string: processed string object. """

    str1 = dirty_string.replace('_', ' ')
    str2 = str1.replace('-', ' ')
    str3 = str2.replace('  ', ' ')
    str4 = str3.title()
    clean_str = str4.strip()

    if clean_str == 'End selection':
        clean_string = 'nan'
    else:
        clean_string = clean_str

    return clean_string


def date_time_fn(row):
    """ Extract and reformat date and time fields.

            :param row: pandas dataframe row value object.
            :return date_time_list: list object containing two string variables: s_date2, obs_date_time. """

    s_date, s_time = row['START'].split('T')

    # date clean
    s_date2 = s_date[-2:] + '/' + s_date[-5:-3] + '/' + s_date[2:4]
    photo_date = s_date.replace("-", "")

    # time clean
    s_hms, _ = s_time.split('.')
    s_hm = s_hms[:8]
    if s_hm[:1] == '0':
        s_hm2 = s_hm[1:8]
    else:
        s_hm2 = s_hm[:8]

    dirty_obs_time = datetime.strptime(s_hm2, '%H:%M:%S')

    obs_time = dirty_obs_time.strftime("%I:%M:%S %p")
    obs_date_time = s_date2 + ' ' + obs_time

    date_time_list = [s_date2, obs_date_time]

    return date_time_list, photo_date


def recorder_fn(row):
    """ Extract recorder information.

            :param row: pandas dataframe row value object.
            :return obs_recorder: string object containing recorder name. """
    recorder = str(row['OFFICER_ONE:RECORDER'])
    # clean and incorporate recorder other
    if recorder == 'other':
        recorder = recorder.replace('other', str((row['OFFICER_ONE:OTHER_RECORDER'])))
    # clean variable, remove white space and possible typos
    recorder = string_clean_title_fn(recorder)
    first, second = recorder.split(' ')
    obs_recorder = second + ', ' + first

    return obs_recorder


def estimator_fn(row):
    """ Extract estimator information.

        :param row: pandas dataframe row value object.
        :return obs_estimator: string object containing estimator name.
        """
    estimator = str(row['OFFICER_TWO:ESTIMATOR'])
    #print('estimator: ', estimator)
    # clean variable, remove white space and possible typos
    if estimator == 'other':
        estimator = estimator.replace('other', str((row['OFFICER_TWO:OTHER_ESTIMATOR'])))
    estimator = string_clean_title_fn(estimator)

    first, second = estimator.split(' ')
    obs_estimator = second + ', ' + first

    return obs_estimator


def location_fn(row):
    """ extract the district, property and site information.

            :param row: pandas dataframe row value object.
            :return location_list: list object containing five string variables:
            district, listed_property, unlisted_property, final_property and site. """

    # district
    district = string_clean_title_fn(str(row['DISTRICT']))

    listed_property = str(row['PROP:PROPERTY'])

    # property name
    if str(row['PROP:PROPERTY']) in set(
            ('NP_prop_new', 'B_property_outside', 'D_property_outside', 'G_property_outside',
             'K_property_outside', 'NAS_property_outside', 'P_property_outside', 'R_property_outside',
             'SAS_property_outside', 'SP_property_outside', 'TC_property_outside', 'VR_property_outside',
             'NP_property_outside')):

        listed_property = np.nan
        unlisted_property = string_clean_title_fn(str(row['PROP:NOT_PASTORAL_NAME2']))
        final_property = string_clean_title_fn(str(row['PROP:NOT_PASTORAL_NAME2']))
    else:
        listed_property = string_clean_title_fn(str(row['PROP:PROPERTY']))
        unlisted_property = np.nan
        final_property = string_clean_title_fn(str(row['PROP:PROPERTY']))

    site1 = str(row['GROUP_SITE:SITE_FINAL'])
    # call the stringCleanFN function
    site = string_clean_upper_fn(site1)

    if str(row['GROUP_SITE:SITE']) in set(('B_new', 'D_new', 'G_new', 'K_new', 'NAS_new', 'P_new', 'R_new', 'SAS_new',
                                           'SP_new', 'TC_new', 'VR_new', 'NP_new', 'new')):
        establish = 'new'
    else:
        establish = 'existing'

    # create a variable with property name and site to loop through.
    site_code = final_property.replace(' ', '_') + '_' + site

    location_list = [district, listed_property, unlisted_property, final_property, establish, site_code, site]
    return location_list


def gps_points_fn(row):
    """ Extract the coordinate information.

            :param row: pandas dataframe row value object.
            :return gps: string object containing the gps device information.
            :return c_lat: float object containing the center point latitude information.
            :return c_lon: float object containing the center point longitude information.
            :return c_acc: float object containing the center point accuracy information (mobile device only).
            :return off_direct: string object containing the offset direction information.
            :return o_lat: float object containing the offset point latitude information.
            :return o_lon: float object containing the offset point longitude information.
            :return o_acc: float object containing the center point accuracy information. """

    gps = str(row['GPS_SELECT'])
    # mobile device - collectd at the beginning of the odk form.
    if gps == 'now_device':
        datum = 'wgs84'
        c_lat = float(row['CENTRE_GPS1:Latitude'])
        c_lon = float(row['CENTRE_GPS1:Longitude'])
        c_acc = float(row['CENTRE_GPS1:Accuracy'])

        off_direct = string_clean_capital_fn(str(row['OFFSET1:OFFSET_DIRECTION1']))

        o_lat = float(row['OFFSET1:OFFSET_GPS1:Latitude'])
        o_lon = float(row['OFFSET1:OFFSET_GPS1:Longitude'])
        o_acc = float(row['OFFSET1:OFFSET_GPS1:Accuracy'])

    # mobile device - collected at the end of the odk form.
    elif gps == 'later_device':
        datum = 'wgs84'
        c_lat = float(row['CENTRE_GPS3:Latitude'])
        c_lon = float(row['CENTRE_GPS3:Longitude'])
        c_acc = float(row['CENTRE_GPS3:Accuracy'])

        off_direct = string_clean_capital_fn(str(row['OFFSET3:OFFSET_DIRECTION3']))

        o_lat = float(row['OFFSET3:OFFSET_GPS3:Latitude'])
        o_lon = float(row['OFFSET3:OFFSET_GPS3:Longitude'])
        o_acc = float(row['OFFSET3:OFFSET_GPS3:Accuracy'])

    # External device - collectd at the beginning of the odk form.
    elif gps == 'now_gps':
        datum = 'wgs84'

        # datum = str(row['EXT_GPS_COORD_CENTRE2:EXT_GPS_COORD_CENTRE_LAT2'])
        c_lat = float(row['EXT_GPS_COORD_CENTRE2:EXT_GPS_COORD_CENTRE_LAT2'])
        c_lon = float(row['EXT_GPS_COORD_CENTRE2:EXT_GPS_COORD_CENTRE_LONG2'])
        c_acc = np.nan

        off_direct = string_clean_capital_fn(str(row['EXT_GPS_COORD_OFFSET2:OFFSET_DIRECTION2']))

        o_lat = float(row['EXT_GPS_COORD_OFFSET2:EXT_GPS_COORD_OFFSET_LAT2'])
        o_lon = float(row['EXT_GPS_COORD_OFFSET2:EXT_GPS_COORD_OFFSET_LONG2'])
        o_acc = np.nan

    # External device - collectd at the end of the odk form.
    else:
        datum = 'wgs84'
        # datum = str(row['EXT_GPS_COORD_CENTRE4:DATUM2'])
        c_lat = float(row['EXT_GPS_COORD_CENTRE4:EXT_GPS_COORD_CENTRE_LAT4'])
        c_lon = float(row['EXT_GPS_COORD_CENTRE4:EXT_GPS_COORD_CENTRE_LONG4'])
        c_acc = np.nan

        off_direct = string_clean_capital_fn(str(row['EXT_GPS_COORD_OFFSET4:OFFSET_DIRECTION4']))

        o_lat = float(row['EXT_GPS_COORD_OFFSET4:EXT_GPS_COORD_OFFSET_LAT4'])
        o_lon = float(row['EXT_GPS_COORD_OFFSET4:EXT_GPS_COORD_OFFSET_LONG4'])
        o_acc = np.nan

    lat_lon_list = [datum, gps, c_lat, c_lon, c_acc, off_direct, o_lat, o_lon, o_acc]

    return lat_lon_list


def meta_data_fn(row):
    """ Extract and clean the form key information.

            :param row: pandas dataframe row value object.
            :return meta_key: string object containing the odk form identifier key.
            :return clean_meta_key: string object containing the cleaned odk form identifier key.
            :return form_name: string object containing the odk form identifier key. """

    meta_key = str(row['meta:instanceID'])
    clean_meta_key = meta_key[5:]
    form_name = str(row['meta:instanceName'])

    meta_data_list = [meta_key, clean_meta_key, form_name]
    return meta_data_list


def main_routine(file_path, temp_dir, veg_list_excel, odk_complete_dir, property_enquire):
    """ Control the star transect data extraction workflow producing five outputs:

            :param odk_complete_dir: string object containing the path to a directory within temp_dir.
            :param file_path: string object containing the dir_path concatenated with search_criteria.
            :param temp_dir: string object path to the created output directory (date_time).
            :param veg_list_excel: string object path to the odk veg list excel file (botanical and common names).
            :return clean_star_transect.csv: clean csv file output to the command argument export directory.
            :return photo_star_url.csv:  csv file containing photo url information to the command argument export
            directory.
            :return clean_star_transect.shp: clean shapefile output to the command argument export directory
            - contains all information lat lon set to transect center points.
            :return clean_offset.shp: shapefile output to the command argument export directory
            - contains minor information lat lon set to transect offset points."""

    #('step2_1_star_transect_processing_workflow.py INITIATED.')
    #print(file_path)
    # Read in the star transect csv as a Pandas DataFrame.
    df = pd.read_csv(file_path)

    if property_enquire:
        #print('You have requested to only process property: ', property_enquire)
        df_filter = df[df['PROP:PROPERTY'] == property_enquire]
    else:
        #print('You have NOT specified a property -- ALL properties will be processed.')
        df_filter = df

    length_df_filter = len(df_filter.index)

    #print('You have requested to only process property: ', property_enquire)
    if length_df_filter == 0:
        print('The property you have selected ('
              + property_enquire +
              ') does NOT exist within the RAS dataframe - No Star Transect output will be produced.')
        pass

    else:

        final_star_list = []
        final_star_photo_list = []

        # for loop through the star transect dataframe (df)
        for index, row in df_filter.iterrows():

            # call the date_time_fn function to extract date and time information.
            date_time_list, photo_date = date_time_fn(row)

            # call the recorder_fn function to extract the recorder information.
            obs_recorder = recorder_fn(row)

            # call the estimator_fn function to extract the estimator information.
            obs_estimator = estimator_fn(row)

            # call the location_fn function to extract the district, property and site information.
            location_list = location_fn(row)

            # call the gps_points_fn function to extract the longitude and latitude information.
            lat_lon_list = gps_points_fn(row)

            # call the meta_date_fn function to extract the unique identifier information for each form record.
            meta_data_list = meta_data_fn(row)

            # create a list of variables to create a cleaned dataframe.

            # extract the site variable from the location list
            site = location_list[6:][0]
            print(site)
            site_code = location_list[5:6][0]

            # create a clean list and append/extend output lists and variables
            clean_list = [site]
            clean_list.extend(date_time_list)
            clean_list.extend([obs_recorder, obs_estimator])
            clean_list.extend(location_list[:6])
            clean_list.extend(lat_lon_list)

            #print('step2_1_star_transect_processing_workflow.py COMPLETED')

            # call the step2_2_star_transect_basics.py script.
            import step2_2_star_transect_basics
            clean_list = step2_2_star_transect_basics.main_routine(clean_list, row, site_code, string_clean_capital_fn)

            # call the step2_3_star_transect_botanical.py script.
            import step2_3_star_transect_botanical
            clean_list, veg_list = step2_3_star_transect_botanical.main_routine(
                clean_list, row, string_clean_capital_fn, veg_list_excel)

            # call the step2_4_photo_url_csv.py script.
            import step2_4_photo_url_csv
            photo_url_list = step2_4_photo_url_csv.main_routine(row, site_code, photo_date)

            clean_list.extend(photo_url_list[2:])
            # add metadata variables
            clean_list.extend(meta_data_list)

            # Replace clean list values (forb separation amendments to cover fractions if the veg_list is not empty
            if veg_list:

                # amend representative veg (rep_veg)
                clean_list[102] = veg_list[0]

                # amend adjusted perennial grass (adj_pg)
                clean_list[104] = veg_list[1]
                # amend final perennial grass (final_pg)

                # amend adjusted annual grass (adj_ag)
                clean_list[107] = veg_list[2]
                # amend final annual grass (final_ag)

                # amend adjusted perennial forb (final_ag)
                clean_list[110] = veg_list[3]
                # amend final perennial forb (final_ag)
                clean_list[111] = veg_list[3]

                # amend field annual forb (adj_ag)
                clean_list[112] = veg_list[4]
                # amend adjusted annual forb (final_ag)
                clean_list[113] = veg_list[5]
                # amend final annual forb(final_ag)
                clean_list[114] = veg_list[6]

                # amend field veg total(adj_veg_total)
                clean_list[115] = veg_list[7]
                # amend adjusted veg total(adj_veg_total)
                clean_list[116] = veg_list[8]
                # amend final veg total(final_veg_total)
                clean_list[117] = veg_list[9]

            final_star_list.append(clean_list)
            final_star_photo_list.append(photo_url_list)

        #print('-'*50)
        #print('The following outputs have been created:')

        # create offset geoDataFrame and export a shapefile lon lat set to center points.
        star_transect_df = pd.DataFrame(final_star_list)
        star_transect_df.columns = (
            'site_orig', 'date', 'date_time', 'recorder', 'estimator', 'district', 'prop', 'unlist_prop', 'final_prop',
            'establish', 'site',

            'datum', 'gps', 'c_lat', 'c_lon', 'c_acc', 'off_direct', 'o_lat', 'o_lon', 'o_acc', 'transect1',

            't1_bare', 't1_gravel', 't1_rock', 't1_ash', 't1_litter', 't1_crypto', 't1_dead_pg', 't1_green_pg',
            't1_dead_ag', 't1_green_ag',

            't1_dead_fb', 't1_green_fb', 't1_abv_green', 't1_abv_dead', 't1_abv_brown',
            't1_abv_ic', 't1_abv_nic', 't1_blw_green', 't1_blw_dead', 't1_blw_brown',

            't1_blw_none', 'transect2', 't2_bare', 't2_gravel', 't2_rock', 't2_ash', 't2_litter', 't2_crypto', 't2_dead_pg',
            't2_green_pg',

            't2_dead_ag', 't2_green_ag', 't2_dead_fb', 't2_green_fb', 't2_abv_green', 't2_abv_dead', 't2_abv_brown',
            't2_abv_ic', 't2_abv_nic', 't2_blw_green',

            't2_blw_dead', 't2_blw_brown', 't2_blw_none', 'transect3', 't3_bare', 't3_gravel', 't3_rock', 't3_ash',
            't3_litter', 't3_crypto',

            't3_dead_pg', 't3_green_pg', 't3_dead_ag', 't3_green_ag', 't3_dead_fb', 't3_green_fb', 't3_abv_green',
            't3_abv_dead', 't3_abv_brown', 't3_abv_ic',

            't3_abv_nic', 't3_blw_green', 't3_blw_dead', 't3_blw_brown', 't3_blw_none', 'tran1_url', 'tran2_url',
            'tran3_url',

            'rep_cover', 'field_litter', 'adj_litter', 'final_litter', 'field_exposed', 'adj_exposed', 'final_exposed',
            'field_veg', 'adj_veg', 'final_veg',

            'field_site_total', 'adj_site_total', 'final_site_total',

            'rep_veg', 'field_pg',
            'adj_pg', 'final_pg', 'field_ag', 'adj_ag', 'final_ag', 'field_pf', 'adj_pf', 'final_pf', 'field_af', 'adj_af',
            'final_af', 'field_veg_total', 'adj_veg_total', 'final_veg_total', 'height_tree', 'height_shrub',

            'bot_3p_1', 'bot_3p_2', 'bot_3p_3', 'bot_3p_4', 'bot_3p_5', 'bot_3p_6', 'bot_3p_7', 'bot_3p_8', 'bot_3p_9',
            'bot_3p_10', 'cover_3p_1', 'cover_3p_2', 'cover_3p_3', 'cover_3p_4', 'cover_3p_5', 'cover_3p_6', 'cover_3p_7',
            'cover_3p_8', 'cover_3p_9', 'cover_3p_10',

            'bot_pg_1', 'bot_pg_2', 'bot_pg_3', 'bot_pg_4', 'bot_pg_5', 'bot_pg_6', 'bot_pg_7',
            'bot_pg_8', 'bot_pg_9', 'bot_pg_10', 'cover_pg_1', 'cover_pg_2', 'cover_pg_3', 'cover_pg_4', 'cover_pg_5',
            'cover_pg_6', 'cover_pg_7', 'cover_pg_8', 'cover_pg_9', 'cover_pg_10',

            'bot_ag_1', 'bot_ag_2', 'bot_ag_3', 'bot_ag_4', 'bot_ag_5', 'bot_ag_6', 'bot_ag_7', 'bot_ag_8', 'bot_ag_9',
            'bot_ag_10', 'cover_ag_1', 'cover_ag_2', 'cover_ag_3', 'cover_ag_4', 'cover_ag_5', 'cover_ag_6', 'cover_ag_7',
            'cover_ag_8', 'cover_ag_9', 'cover_ag_10',

            'bot_pf_1', 'bot_pf_2', 'bot_pf_3', 'bot_pf_4', 'bot_pf_5', 'bot_pf_6', 'bot_pf_7', 'bot_pf_8', 'bot_pf_9',
            'bot_pf_10', 'cover_pf_1', 'cover_pf_2', 'cover_pf_3', 'cover_pf_4', 'cover_pf_5', 'cover_pf_6', 'cover_pf_7',
            'cover_pf_8', 'cover_pf_9', 'cover_pf_10',

            'bot_af_1', 'bot_af_2', 'bot_af_3', 'bot_af_4', 'bot_af_5', 'bot_af_6', 'bot_af_7', 'bot_af_8', 'bot_af_9',
            'bot_af_10', 'cover_af_1', 'cover_af_2', 'cover_af_3', 'cover_af_4', 'cover_af_5', 'cover_af_6', 'cover_af_7',
            'cover_af_8', 'cover_af_9', 'cover_af_10',

            'photo_off', 'photo_c', 'photo_n', 'photo_ne', 'photo_se', 'photo_s', 'photo_sw', 'photo_nw',
            'meta_key', 'clean_meta_key', 'form',)

        cols = ['c_acc', 'o_acc', 'field_litter', 'adj_litter', 'final_litter', 'field_exposed', 'adj_exposed',
                'final_exposed', 'field_veg',
                'adj_veg', 'final_veg', 'field_site_total', 'adj_site_total', 'final_site_total', 'rep_veg', 'field_pg',
                'adj_pg', 'final_pg', 'field_ag', 'adj_ag', 'final_ag', 'field_pf', 'adj_pf', 'final_pf', 'field_af',
                'adj_af', 'final_af', 'field_veg_total', 'adj_veg_total', 'final_veg_total', 'height_tree', 'height_shrub',

                'cover_3p_1', 'cover_3p_2', 'cover_3p_3', 'cover_3p_4', 'cover_3p_5', 'cover_3p_6', 'cover_3p_7',
                'cover_3p_8', 'cover_3p_9', 'cover_3p_10',

                'cover_pg_1', 'cover_pg_2', 'cover_pg_3', 'cover_pg_4', 'cover_pg_5', 'cover_pg_6', 'cover_pg_7',
                'cover_pg_8', 'cover_pg_9', 'cover_pg_10',

                'cover_ag_1', 'cover_ag_2', 'cover_ag_3', 'cover_ag_4', 'cover_ag_5', 'cover_ag_6', 'cover_ag_7',
                'cover_ag_8', 'cover_ag_9', 'cover_ag_10',

                'cover_pf_1', 'cover_pf_2', 'cover_pf_3', 'cover_pf_4', 'cover_pf_5', 'cover_pf_6', 'cover_pf_7',
                'cover_pf_8', 'cover_pf_9', 'cover_pf_10',

                'cover_af_1', 'cover_af_2', 'cover_af_3', 'cover_af_4', 'cover_af_5', 'cover_af_6',
                'cover_af_7', 'cover_af_8', 'cover_af_9', 'cover_af_10']

        # replace all int and float missing variables with a 0 value
        star_transect_df[cols] = star_transect_df[cols].fillna(0)
        star_transect_df2 = star_transect_df.replace('Nan', 'nan')
        star_transect_df3 = star_transect_df2.fillna('nan')
        csv_output = (odk_complete_dir + '\\clean_star_transect.csv')
        star_transect_df3.to_csv(csv_output)
        #print('-', csv_output)

        # ----------------------------------------- project and export shapefiles ------------------------------------------

        # filter dataframe based on datum
        wgs84_df = star_transect_df3[star_transect_df3["datum"] == "wgs84"]
        gda94_df = star_transect_df3[star_transect_df3["datum"] == "gda94"]

        if len(gda94_df) >= 1:
            # create offset geoDataFrame and export a shapefile lon lat set to center points.
            gda94_gdf = gpd.GeoDataFrame(
                gda94_df, geometry=gpd.points_from_xy(gda94_df.c_lon, gda94_df.c_lat), crs="EPSG:4283")
            gda94_from_wgs84_df['lon_gda'] = gda94_from_wgs84_df['geometry'].x
            gda94_from_wgs84_df['lat_gda'] = gda94_from_wgs84_df['geometry'].y

        if len(wgs84_df.index) >= 1:
            # create offset geoDataFrame and export a shapefile lon lat set to center points.
            wgs84_gdf = gpd.GeoDataFrame(
                wgs84_df, geometry=gpd.points_from_xy(wgs84_df.c_lon, wgs84_df.c_lat), crs="EPSG:4326")

            gda94_from_wgs84_df = wgs84_gdf.to_crs(4283)
            #gda94_from_wgs84_df['datum_gda94'] = 'gda94'
            gda94_from_wgs84_df['lon_gda'] = gda94_from_wgs84_df['geometry'].x
            gda94_from_wgs84_df['lat_gda'] = gda94_from_wgs84_df['geometry'].y
            shp_output = (temp_dir + '\\clean_star_transect_gda94.shp')
            gda94_from_wgs84_df.to_file(shp_output, driver='ESRI Shapefile')
            #print('-', shp_output)

        # -------------------------------------------- export gda shapefile --------------------------------------------

        if len(gda94_df.index) >= 1 and len(wgs84_df.index.index) >= 1:

            complete_gda94_df = gda94_from_wgs84_df.append(gda94_df)
            complete_gda94_df.crs
            shp_output = (temp_dir + '\\clean_star_transect_gda94.shp')
            complete_gda94_df.to_file(shp_output, driver='ESRI Shapefile')
            #print('-', shp_output)
            gda94_gdf = complete_gda94_df

        else:
            gda94_from_wgs84_df
            shp_output = (temp_dir + '\\clean_star_transect_gda94.shp')
            gda94_from_wgs84_df.to_file(shp_output, driver='ESRI Shapefile')
            #print('-', shp_output)
            gda94_gdf = gda94_from_wgs84_df

        # create a geoDataFrame and export as a shapefile lon lat set to offset points.
        off_set_star_df = gda94_gdf[['site', 'final_prop', 'district', 'date', 'date_time', 'recorder', 'estimator',
                                             'datum', 'off_direct', 'o_acc', 'o_lat', 'o_lon', 'meta_key',
                                             'meta_key', 'form']]
        off_set_star_gdf = gpd.GeoDataFrame(
            off_set_star_df, geometry=gpd.points_from_xy(off_set_star_df.o_lon, off_set_star_df.o_lat), crs="EPSG:4283")
        shp_output = (temp_dir + '\\clean_offset_star_transect_gda94.shp')
        # off_set_star_gdf.to_file(shp_output, driver='ESRI Shapefile')
        #print('-', shp_output)

        # create a dataFrame and export as a csv containing the photo_url_extraction_fn urls.
        star_photo_list_df = pd.DataFrame(final_star_photo_list)
        star_photo_list_df.columns = ['site', 'date', 'photo_off', 'photo_c', 'photo_n', 'photo_ne', 'photo_se', 'photo_s',
                                      'photo_sw', 'photo_nw']
        csv_output = (temp_dir + '\\photo_star_url.csv')
        star_photo_list_df.to_csv(csv_output)
        #print('-', csv_output)

        #print('The Star transect ODK Aggregate csv file has been processed.........')


if __name__ == '__main__':
    main_routine()
