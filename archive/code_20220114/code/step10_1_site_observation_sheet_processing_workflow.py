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
import glob
import warnings

warnings.filterwarnings("ignore")


def search_html_files_fn(site_dir):
    """ Search for all html files within a directory.

    :param site_dir: string object containing the path to the current site directory.
    :return html_list: list of string objects containing the path to all located transect.html files.
    """

    # create an empty list
    html_list = []

    for file in glob.glob(site_dir + '//*.html'):
        # append file paths to list
        html_list.append(file)

    return html_list


def table_clean_up_fn(html_list, remote_desktop):
    """ Filter the dataframe and rename feature headings.

    :param remote_desktop: string object variable used to define the workflow (command argument.
    :param html_list: list of string objects containing the path to all located transect.html files.
    :return clean_df_list: list object containing open pandas dataframe elements produced by the transect.html files.
    """

    clean_df_list = []

    for htmlTablePath in html_list:

        html_table_list = pd.read_html(htmlTablePath)
        if remote_desktop == 'remote':
            # print(remote_desktop)
            html_table = html_table_list[0]
        else:
            # print('local or offline')
            html_table = html_table_list[-1]
        df = html_table.iloc[:, 2:5]
        df.columns = ['ground', 'below', 'above']

        # call the variable_renaming_fn function
        df = variable_renaming_fn(df)

        clean_df_list.append(df)

    return clean_df_list


def variable_renaming_fn(df):
    """ Rename the feature variables for observational sheet insertion.

    :param df: pandas data frame object.
    :return df: pandas data frame that has had its values changed using the included dictionaries.
    """

    # Change values in columns to required values for workbook
    ground_values = {'bare': 'BARE GROUND', 'gravel': 'GRAVEL', 'rock': 'ROCK', 'ash': 'ASH', 'litter': 'LITTER',
                     'cryptogram': 'CRYPTOGRAM',
                     'dead_annual_grass': 'DEAD ANNUAL GRASS', 'dead_perennial_grass': 'DEAD PERENNIAL GRASS',
                     'dead_annual_forb':
                         'DEAD ANNUAL FORB / HERB', 'dead_forb': 'DEAD PERENNIAL FORB / HERB',
                     'green_annual_grass': 'GREEN ANNUAL GRASS',
                     'green_perennial_grass': 'GREEN PERENNIAL GRASS', 'green_annual_forb': 'GREEN ANNUAL FORB / HERB',
                     'green_forb':
                         'GREEN PERENNIAL FORB / HERB', 'green_plant': 'GREEN PLANT', 'dead_plant': 'DEAD PLANT'}

    below_values = {'below_green': 'BELOW - GREEN', 'below_brown': 'BELOW - BROWN', 'below_dead': 'BELOW - DEAD',
                    'subshrub': 'SUBSHRUB - GREY', 'none': 'BLANK'}

    above_values = {'above_green': 'ABOVE - GREEN', 'above_brown': 'ABOVE - BROWN', 'above_dead': 'ABOVE - DEAD',
                    'above_in_crown':
                        'ABOVE - IN CROWN', 'not_in_crown': 'BLANK'}

    df['ground'] = df['ground'].replace(ground_values)
    df['below'] = df['below'].replace(below_values)
    df['above'] = df['above'].replace(above_values)

    return df


def main_routine(obs_data_list, property_name, site, site_dir, star, remote_desktop, photo_date):
    """ This script controls the workflow for the production and data insertion for the RMB observational sheets.
    The script calls the following 10 scripts to create one observational sheet:
    - step10_2_observation_sheet_formatting.py
    - step10_3_site_create_establishment_sheet.py
    - step10_4_create_site_visit_sheet.py
    - step10_5_create_site_disturbance_sheet.py
    - step10_6_create_site_transect_sheets.py
    - step10_7_create_site_basal_sheet.py
    - step10_8_create_site_juvenile_stem_sheet.py
    - step10_9_create_site_ground_layer_sheet.py
    - step10_10_create_site_cover_estimates.py
    - step10_11_create_site_condition_sheet.py

    :param photo_date: string object containing the photo date YYYYMMDD.
    :param remote_desktop: string object variable used to define the workflow (command argument)
    :param property_name: string object containing teh property name.
    :param obs_data_list: list object containing list elements containing observation data for
    (one list per worksheet) insertion.
    :param site: string object containing the site name.
    :param site_dir: string object containing the path to the current site directory.
    :param star: pandas data frame object.
    """

    print('_'*50)
    print(property_name)
    print(site)

    # call the search_html_files_fn function
    html_list = search_html_files_fn(site_dir)

    # call the table_clean_up_fn function
    clean_df_list = table_clean_up_fn(html_list, remote_desktop)

    # call the step10_2_observation_sheet_formatting.py script.
    import step10_2_observation_sheet_formatting
    color_fill, heading1, heading2, heading3, heading4, heading5, heading6, heading7, heading8, workbook = \
        step10_2_observation_sheet_formatting.main_routine(property_name, site, site_dir)

    # call the step10_3_site_create_establishment_sheet.py script.
    import step10_3_site_create_establishment_sheet
    insert_vertical_data_fn, insert_horizontal_data_fn, insert_vertical_not_required_data_fn, \
    insert_horizontal_not_required_data_fn = step10_3_site_create_establishment_sheet.main_routine(
        heading1, heading2, heading3, heading7, workbook, obs_data_list)

    # call the step10_4_create_site_visit_sheet.py script.
    import step10_4_create_site_visit_sheet
    step10_4_create_site_visit_sheet.main_routine(
        heading1, heading2, heading3, heading7, workbook, obs_data_list, insert_vertical_data_fn,
        insert_vertical_not_required_data_fn, site, site_dir)

    # call the step10_5_create_site_disturbance_sheet.py script.
    import step10_5_create_site_disturbance_sheet
    step10_5_create_site_disturbance_sheet.main_routine(
        color_fill, heading1, heading2, heading3, heading4, heading5, heading7, workbook, obs_data_list,
        site_dir, insert_vertical_data_fn, insert_horizontal_data_fn, insert_vertical_not_required_data_fn, photo_date)

    # call the step10_6_create_site_transect_sheets.py script.
    import step10_6_create_site_transect_sheets
    step10_6_create_site_transect_sheets.main_routine(
        clean_df_list, color_fill, heading1, heading2, heading4, heading7, workbook, star,
        insert_vertical_data_fn, remote_desktop)

    # call the step10_7_create_site_basal_sheet.py script.
    import step10_7_create_site_basal_sheet
    insert_horizontal_may_start_with_zero_fn, insert_vertical_may_start_with_zero_fn = step10_7_create_site_basal_sheet.main_routine(
        color_fill, heading1, heading2, heading4, heading5, heading7, heading8, workbook, obs_data_list,
        insert_vertical_data_fn, insert_horizontal_data_fn)

    # call the step10_8_create_site_juvenile_stem_sheet.py script.
    import step10_8_create_site_juvenile_stem_sheet
    step10_8_create_site_juvenile_stem_sheet.main_routine(
        color_fill, heading1, heading2, heading3, heading4, heading5, heading7, workbook, obs_data_list,
        insert_vertical_data_fn, insert_horizontal_data_fn, insert_horizontal_may_start_with_zero_fn, insert_vertical_may_start_with_zero_fn)

    # call the step10_9_create_site_ground_layer_sheet.py script.
    import step10_9_create_site_ground_layer_sheet
    step10_9_create_site_ground_layer_sheet.main_routine(
        color_fill, heading1, heading4, heading7, workbook, obs_data_list, insert_vertical_data_fn, insert_horizontal_may_start_with_zero_fn, insert_vertical_may_start_with_zero_fn)

    # call the step10_10_create_site_cover_estimates.py script.
    import step10_10_create_site_cover_estimates
    step10_10_create_site_cover_estimates.main_routine(
        color_fill, heading1, heading2, heading3, heading4, heading6, heading7, workbook, obs_data_list,
        insert_vertical_data_fn, insert_horizontal_data_fn, insert_horizontal_not_required_data_fn)

    # call the step10_11_create_site_condition_sheet.py script.
    import step10_11_create_site_condition_sheet
    step10_11_create_site_condition_sheet.main_routine(
        color_fill, heading1, heading2, heading3, heading4, heading7, workbook, obs_data_list, site,
        insert_vertical_data_fn, insert_horizontal_data_fn)

    print('Observation sheet complete.')

if __name__ == '__main__':
    main_routine()
