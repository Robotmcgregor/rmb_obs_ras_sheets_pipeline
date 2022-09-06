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
from __future__ import print_function, division
import pandas as pd
import warnings
from datetime import datetime
import numpy as np
import geopandas as gpd
import os

warnings.filterwarnings("ignore")


def string_clean_upper_fn(dirty_string):
    """ Remove whitespaces and clean strings.

    :param dirty_string: string object.
    :return clean_string: processed string object.
    """

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
    :return clean_string: processed string object.
    """

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
    :return clean_string: processed string object.
    """

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

    :param row: pandas dataframe row value object
    :return date_time_list: list object containing two string variables: s_date2, obs_date_time.
    """

    s_date, s_time = row['START'].split('T')
    # date clean
    form_date = s_date[-2:] + '/' + s_date[-5:-3] + '/' + s_date[:4]
    s_date2 = s_date[-2:] + '/' + s_date[-5:-3] + '/' + s_date[2:4]
    photo_date = s_date.replace("-", "")

    # time clean
    s_hms, _ = s_time.split('.')
    s_hm = s_hms[:5]
    if s_hm[:1] == '0':
        s_hm2 = s_hm[1:5]
    else:
        s_hm2 = s_hm[:5]

    dirty_obs_time = datetime.strptime(s_hm2, '%H:%M')

    obs_time = dirty_obs_time.strftime("%I:%M %p")
    obs_date_time = form_date + ' ' + obs_time

    date_time_list = [form_date, obs_date_time]
    return date_time_list, photo_date


def recorder_fn(row):
    """ Extract recorder information.

    :param row: pandas dataframe row value object.
    :return obs_recorder: string object containing recorder name.
    """

    recorder = str(row['OFFICER_ONE:RECORDER'])
    # clean and incorporate recorder other
    if recorder == 'other':
        recorder = recorder.replace('other', str((row['OFFICER_ONE:OTHER_RECORDER'])))
    # clean variable, remove white space and possible typos
    recorder = string_clean_title_fn(recorder)
    first, second = recorder.split(' ')
    obs_recorder = second + ', ' + first

    if obs_recorder == "Gonzalez, Alvaro":
        final_obs_recorder = "Gonzalez Monge, Alvaro"
    else:
        final_obs_recorder = obs_recorder

    return final_obs_recorder


def estimator_fn(row):
    """ Extract estimator information.

    :param row: pandas dataframe row value object.
    :return obs_estimator: string object containing estimator name.
    """

    estimator = str(row['OFFICER_TWO:ESTIMATOR'])
    # clean variable, remove white space and possible typos
    if estimator == 'other':
        estimator = estimator.replace('other', str((row['OFFICER_TWO:OTHER_ESTIMATOR'])))
    estimator = string_clean_title_fn(estimator)
    first, second = estimator.split(' ')
    obs_estimator = second + ', ' + first

    if obs_estimator == "Gonzalez, Alvaro":
        final_obs_estimator = "Gonzalez Monge, Alvaro"
    else:
        final_obs_estimator = obs_estimator

    return final_obs_estimator


def location_fn(row):
    """ extract the district, property and site information.

    :param row: pandas dataframe row value object.
    :return location_list: list object containing five string variables:
    district, listed_property, unlisted_property, final_property and site.
    """

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

    # create a variable with property name and site to loop through.
    site_code = final_property.replace(' ', '_') + '_' + site

    location_list = [district, listed_property, unlisted_property, final_property, site_code, site]
    return location_list


def meta_data_fn(row):
    """ Extract and clean the form key information.

    :param row: pandas dataframe row value object.
    :return meta_key: string object containing the odk form identifier key.
    :return clean_meta_key: string object containing the cleaned odk form identifier key.
    :return form_name: string object containing the odk form identifier key.
    """
    meta_key = str(row['meta:instanceID'])
    clean_meta_key = meta_key[5:]
    form_name = str(row['meta:instanceName'])

    meta_data_list = [meta_key, clean_meta_key, form_name]
    return meta_data_list


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
    :return o_acc: float object containing the center point accuracy information.
    """

    datum = 'wgs84'
    gps = str(row['GPS_SELECT'])

    if gps == 'now_device':
        datum = 'wgs84'
        c_lat = float(row['GPS1:Latitude'])
        c_lon = float(row['GPS1:Longitude'])
        c_acc = float(row['GPS1:Accuracy'])

    elif gps == 'later_device':
        datum = 'wgs84'
        c_lat = float(row['SITE_GPS3:Latitude'])
        c_lon = float(row['SITE_GPS3:Longitude'])
        c_acc = float(row['SITE_GPS3:Accuracy'])

    elif gps == 'now_gps':
        datum = str(row['GPS2:DATUM1'])
        c_lat = float(row['GPS2:GPS2_LAT2'])
        c_lon = float(row['GPS2:GPS2_LONG2'])
        c_acc = np.nan

    else:
        datum = str(row['EXT_GPS_COORD4:DATUM2'])
        c_lat = float(row['EXT_GPS_COORD4:GPS_COORD_LAT4'])
        c_lon = float(row['EXT_GPS_COORD4:GPS_COORD_LONG4'])
        c_acc = np.nan

    lat_lon_list = [datum, gps, c_lat, c_lon, c_acc]
    return lat_lon_list


def prop_code_extraction_fn(estate_series, property_name, site):
    """ Extract the common name from the botanical_common_series excel document.

    :param site: string object containing the site name.
    :param estate_series: geopandas series object containing property and property code variables.
    :param property_name: string object containing the property name passed into the function.
    :return prop_code: string object containing the property code.
    """

    property_name_list = estate_series.PROPERTY.tolist()
    prop_upper = string_clean_upper_fn(str(property_name))
    if prop_upper in property_name_list:
        prop_code = estate_series.loc[estate_series['PROPERTY'] == prop_upper, 'PROP_TAG'].iloc[0]
    else:
        prop_code = property_name

    prop_code.replace(" ", "_")
    code_site = prop_code + "_" + site

    return prop_code, code_site


def main_routine(file_path, temp_dir, veg_list, pastoral_estate, odk_complete_dir, property_enquire):
    """ Control the ras data extraction workflow producing two outputs.

    :param odk_complete_dir: string object containing the path to a directory within temp_dir.
    :param file_path: string object containing the dir_path concatenated with search_criteria.
    :param temp_dir: string object path to the created output directory (date_time).
    :param veg_list: string object containing the path to an excel document containing botanical and
    common names.
    :param pastoral_estate: string object containing the file path to the pastoral estate shapefile.
    :return clean_star_transect.csv: clean csv file output to the command argument export directory.
    :return clean_ras.csv.csv:  csv file containing photo url information to the command argument export
    directory.
    :return clean_ras.csv.shp: clean shapefile output to the command argument export directory
    - contains all information.
    """

    df = pd.read_csv(file_path)

    if property_enquire:
        df_filter = df[df['PROP:PROPERTY'] == property_enquire]
    else:
        df_filter = df
    length_df_filter = len(df_filter.index)

    if length_df_filter == 0:
        pass

    else:

        final_ras_list = []
        final_ras_photo_list = []

        # read in the estate shapefile and create series
        estate = gpd.read_file(pastoral_estate)
        estate_series = estate[['PROPERTY', 'PROP_TAG']]

        for index, row in df_filter.iterrows():
            # call the date_time_fn function to extract date and time information.
            date_time_list, photo_date = date_time_fn(row)

            # call the recorder_fn function to extract the recorder information.
            obs_recorder = recorder_fn(row)

            # call the location_fn function to extract the district, property and site information.
            location_list = location_fn(row)

            # call the gps_points_fn function to extract the longitude and latitude information.
            lat_lon_list = gps_points_fn(row)

            # call the meta_date_fn function to extract the unique identifier information for each form record.
            meta_data_list = meta_data_fn(row)

            # extract the site variable from the location list
            site = location_list[5:][0]
            site_code = location_list[4:5][0]

            # create a clean list and append/extend output lists and variables
            clean_list = [site]
            clean_list.extend(date_time_list)
            clean_list.append(obs_recorder)
            clean_list.extend(location_list[:5])
            clean_list.extend(lat_lon_list)

            # call the step6_2_ras_land_types.py script.
            import step6_2_ras_land_types
            clean_list = step6_2_ras_land_types.main_routine(
                clean_list, row, string_clean_capital_fn, string_clean_title_fn, string_clean_upper_fn)

            # call the step6_3_ras_disturbance.py script.
            import step6_3_ras_disturbance
            clean_list = step6_3_ras_disturbance.main_routine(
                clean_list, row, string_clean_capital_fn)

            # call the step6_4_ras_disturbance2.py script.
            import step6_4_ras_disturbance2
            clean_list = step6_4_ras_disturbance2.main_routine(
                clean_list, row, string_clean_capital_fn)

            # call the step6_5_ras_botanical.py script.
            import step6_5_ras_botanical
            ras_clean_list = step6_5_ras_botanical.main_routine(
                clean_list, row, string_clean_capital_fn)

            # call the step6_6_ras_photos.py script.
            import step6_6_ras_photos
            clean_list, ras_photo_list = step6_6_ras_photos.main_routine(
                clean_list, row, site_code, photo_date)

            # add metadata variables
            clean_list.extend(meta_data_list)
            final_ras_list.append(clean_list)
            final_ras_photo_list.append(ras_photo_list)

        # convert the final list to a DataFrame
        ras_df = pd.DataFrame(final_ras_list)

        ras_df.columns = [
            'site_orig', 'date', 'date_time', 'recorder', 'district', 'prop', 'unlist_prop', 'final_prop',
            'site', 'datum', 'gps', 'c_lat',
            'c_lon', 'c_acc', 'paddock', 'past_util', 'desc', 'erod_soil', 'bare_soil', 'land_system',
            'ls_consist',
            'ls_alt', 'ls_source', 'water_point', 'water_name', 'water_dir', 'water_dist', 'camel', 'rabbit',
            'donkey', 'horse', 'pig', 'buffalo', 'nat_herb', 'other_feral', 'feral_com', 'north_ff', 'north_fi',
            'south_ff', 'south_fi', 'weed1', 'weed_size1', 'weed_den1', 'weed_com1', 'weed2', 'weed_size2', 'weed_den2',
            'weed_com2', 'weed3', 'weed_size3', 'weed_den3', 'weed_com3', 'scald_sev', 'scald_stab', 'wind_sev',
            'wind_stab', 'water_sheet_sev', 'water_sheet_stab', 'rill_sev', 'rill_stab', 'gully_sev', 'gully_stab',
            'erosion_com', 'condition', 'cond_note', 'dev_note', 'bot_3p_1', 'bot_3p_2', 'bot_3p_3', 'bot_3p_4',
            'bot_pg_1',
            'bot_pg_2', 'bot_pg_3', 'bot_pg_4', 'bot_ag_1', 'bot_ag_2', 'bot_ag_3', 'bot_ag_4', 'bot_pf_1', 'bot_pf_2',
            'bot_pf_3', 'bot_pf_4', 'bot_ts_1', 'bot_ts_2', 'bot_ts_3', 'bot_ts_4', 'bot_sb_1', 'bot_sb_2', 'bot_sb_3',
            'bot_sb_4', 'cover_3p', 'cover_pg', 'cover_ag', 'cover_pf', 'min_cover', 'max_cover', 'basal',
            'tree_density',
            'shrub_density', 'site_photo1', 'photo_bear1', 'site_photo2',
            'photo_bear2', 'site_photo3', 'photo_bear3', 'eros_photo1', 'photo_bear1', 'eros_photo2', 'eros_bear2',
            'eros_photo3', 'eros_bear3', 'meta_key', 'clean_meta_key', 'form']

        cols = ['basal', 'tree_density', 'shrub_density']

        # replace all int and float missing variables with a 0 value
        ras_df[cols] = ras_df[cols].fillna(0)
        ras_df2 = ras_df.replace('Nan', 'nan')

        # ------------------------------------- project and export shapefiles ------------------------------------------

        # filter dataframe based on datum
        wgs84_df = ras_df2[ras_df2["datum"] == "wgs84"]
        gda94_df = ras_df2[ras_df2["datum"] == "gda94"]

        if len(gda94_df) >= 1:
            # create offset geoDataFrame and export a shapefile lon lat set to center points.
            gda94_gdf = gpd.GeoDataFrame(
                gda94_df, geometry=gpd.points_from_xy(gda94_df.c_lon, gda94_df.c_lat), crs="EPSG:4283")

            gda94_df.insert(14, 'gda_lon', gda94_gdf['geometry'].x)
            gda94_df.insert(15, 'gda_lat', gda94_gdf['geometry'].y)

        if len(wgs84_df.index) >= 1:
            # print('wgs84 action')
            # create offset geoDataFrame and export a shapefile lon lat set to center points.
            wgs84_gdf = gpd.GeoDataFrame(
                wgs84_df, geometry=gpd.points_from_xy(wgs84_df.c_lon, wgs84_df.c_lat), crs="EPSG:4326")
            gda94_from_wgs84_df = wgs84_gdf.to_crs(4283)
            gda94_from_wgs84_df.insert(14, 'gda_lon', gda94_from_wgs84_df['geometry'].x)
            gda94_from_wgs84_df.insert(15, 'gda_lat', gda94_from_wgs84_df['geometry'].y)

        # -------------------------------------------- export gda shapefile --------------------------------------------

        if len(gda94_df.index) >= 1 and len(wgs84_df.index) >= 1:

            complete_gda94_df = gda94_from_wgs84_df.append(gda94_df)
            gda94_gdf = complete_gda94_df

        else:
            gda94_from_wgs84_df
            gda94_gdf = gda94_from_wgs84_df

        df = pd.DataFrame(gda94_gdf)
        df['cover_3p'] = df['cover_3p'].str.replace('-', '_')
        df['cover_pg'] = df['cover_pg'].str.replace('-', '_')
        df['cover_ag'] = df['cover_ag'].str.replace('-', '_')
        df['cover_pf'] = df['cover_pf'].str.replace('-', '_')
        df['bare_soil'] = df['bare_soil'].str.replace('-', '_')
        df.drop(columns=['gps', 'geometry', 'prop', 'unlist_prop', 'datum'], inplace=True)
        df.rename(columns={"c_lat": "wgs_lat", "c_lon": "wgs_lon", "c_acc": "wgs_acc"}, errors="raise",
                  inplace=True)
        df1 = df.replace('BLANK', 'nan')
        df2 = df1.replace('nan', np.nan)



        gdf = gpd.GeoDataFrame(
            df1, geometry=gpd.points_from_xy(df1.gda_lon, df1.gda_lat, crs="EPSG:4283"))

        csv_output = (odk_complete_dir + '\\clean_ras.csv')
        df1.to_csv(csv_output, index=False)

        df_new = pd.read_csv(csv_output)

        gdf_new = gpd.GeoDataFrame(
            df_new, geometry=gpd.points_from_xy(df_new.gda_lon, df_new.gda_lat, crs="EPSG:4283"))

        shp_output = (temp_dir + '\\clean_ras_gda94.shp')
        gdf_new.to_file(shp_output, driver='ESRI Shapefile')

        unique_prop_list = gdf_new.final_prop.unique().tolist()
        for prop in unique_prop_list:

            prop_dir = '{0}\\{1}\\{2}'.format(temp_dir, 'prop_output', prop.replace(' ', '_'))
            if not os.path.exists(prop_dir):
                os.mkdir(prop_dir)

            prop_csv_dir = '{0}\\{1}'.format(prop_dir, 'Csv')
            if not os.path.exists(prop_csv_dir):
                os.mkdir(prop_csv_dir)

            prop_shp_dir = '{0}\\{1}'.format(prop_dir, 'Shp')
            if not os.path.exists(prop_shp_dir):
                os.mkdir(prop_shp_dir)

            prop_gdf = gdf_new[gdf_new['final_prop'] == prop]

            csv_output = '{0}\\{1}{2}'.format(prop_csv_dir, prop.replace(' ', '_'), '_ras.csv')
            prop_gdf.to_csv(csv_output, index=False)

            shp_output = '{0}\\{1}{2}'.format(prop_shp_dir, prop.replace(' ', '_'), '_ras_gda94.shp')
            prop_gdf.to_file(shp_output, driver='ESRI Shapefile')

        # create a dataFrame and export as a csv containing the photo_url_extraction_fn urls.
        ras_photo_list_df = pd.DataFrame(final_ras_photo_list)
        ras_photo_list_df.columns = ['site', 'date', 'site_photo1', 'bearing_photo1', 'site_photo2', 'bearing_photo2',
                                     'site_photo3', 'bearing_photo3',
                                     'erosion_photo1', 'bearing_erosion1', 'erosion_photo2', 'bearing_erosion2',
                                     'erosion_photo3', 'bearing_erosion3']
        csv_output = (temp_dir + '\\photo_ras_url.csv')
        ras_photo_list_df.to_csv(csv_output, index=False)


if __name__ == '__main__':
    main_routine()
