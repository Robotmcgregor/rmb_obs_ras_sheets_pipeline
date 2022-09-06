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
import warnings

warnings.filterwarnings("ignore")


def site_desc_fn(row, string_clean_capital_fn):
    """ Extract the paddock name and pasture utilisation information.

    :param row: pandas dataframe row value object.
    :param string_clean_capital_fn: function to remove whitespaces and clean strings.
    :return: desc_list: list object containing three variables:
    paddock, desc and reason.
    """

    paddock = string_clean_capital_fn(str(row['GROUP_LT:PADDOCK_NAME']))
    utilisation = string_clean_capital_fn(str(row['GROUP_CONDITION:PASTURE_UTILISATION']))
    desc_list = [paddock, utilisation]

    return desc_list


def landscape_fn(row, string_clean_capital_fn, string_clean_upper_fn):
    """ Extract the landscape information: land type, erodible soil and bare soil.

    :param string_clean_upper_fn:
    :param row: pandas dataframe row value object.
    :param string_clean_capital_fn: function to remove whitespaces and clean strings.
    :return: soil_list: list object containing two variables: landscape, erodible_soil.
    """

    landscape = string_clean_capital_fn(str(row['GROUP_LT:LAND_TYPE']))
    if landscape == 'Other':
        landscape = string_clean_capital_fn(str(row['GROUP_LT:LAND_TYPE_OTHER']))

    erodible_soil = string_clean_capital_fn(str(row['GROUP_SOIL:ERODIBLE_SOIL']))

    bare_soil = string_clean_upper_fn(str(row['GROUP_SOIL:BARE_SOIL'])).replace(' ', ' - ')

    soil_list = [landscape, erodible_soil, bare_soil]
    return soil_list


def land_system_fn(row, string_clean_capital_fn):
    """ Extract land system and land system source information.

    :param row: pandas dataframe row value object.
    :param string_clean_capital_fn: function to remove whitespaces and clean strings.
    :return: land_system_list: list object containing four variables:
    land_system, ls_consistent, land_system_alt, ls_source.
    """

    ls_consistent = str(row['GROUP_LS:LAND_SYS_CONSIST'])
    land_system = string_clean_capital_fn(str(row['GROUP_LAND_SYSTEM:LAND_SYSTEM']))

    land_system_alt = string_clean_capital_fn(str(row['ALT_LAND_SYS']))

    if ls_consistent == 'ls_no':
        ls_source = string_clean_capital_fn(str(row['GROUP_ALT_LS:ALT_LS_SOURCE']))

    elif ls_consistent == 'ls_yes':
        ls_consistent = 'Yes'
        ls_source = string_clean_capital_fn(str(row['GROUP_LS:LS_SOURCE']))

    else:
        ls_consistent = 'Not assessed'
        ls_source = string_clean_capital_fn(str(row['GROUP_LS:LS_SOURCE']))

    land_system_list = [land_system, ls_consistent, land_system_alt, ls_source]
    return land_system_list


def water_point_fn(row, string_clean_capital_fn, string_clean_title_fn):
    """ Extract water type, water name and distance to water information.

    :param row: pandas dataframe row value object.
    :param string_clean_capital_fn: function to remove whitespaces and clean strings.
    :param string_clean_title_fn: function to remove whitespaces and clean strings.
    :return: water_point_list: list object containing four variables:
    water_point, water_point_name, water_dir and water_distance.
    """

    water_point = string_clean_capital_fn(str(row['GROUP_WATER:WATER_FINAL']))

    water_point_name = string_clean_title_fn(str(row['GROUP_WATER:GROUP_WATER_DIST:NEAR_WATER_NAME']))

    water_dir = string_clean_capital_fn(str(row['GROUP_WATER:GROUP_WATER_DIST:DIRECTION_WATER']))
    water_distance = float(row['GROUP_WATER:GROUP_WATER_DIST:DIST_NEAR_WATER'])

    water_point_list = [water_point, water_point_name, water_dir, water_distance]
    return water_point_list


def main_routine(clean_list, row, string_clean_capital_fn, string_clean_title_fn, string_clean_upper_fn):
    """Extract site visit variables from the ras odk output.

    :param string_clean_upper_fn: function used to clean and reformat string objects.
    :param clean_list: ordered list object that contains the processed integrated odk form result variables.
    :param row: pandas dataframe row value object.
    :param string_clean_capital_fn: function that processes string objects (dirty_string -> clean_string)
    :param string_clean_title_fn: function that processes string objects (dirty_string -> clean_string)
    :return: clean_list: ordered list object that contains the processed integrated odk form result
    variables variables processed within this script extend the list.
    """

    # call the site_desc_fn function
    disc_list = site_desc_fn(row, string_clean_capital_fn)

    # call the landscape_fn function
    soil_list = landscape_fn(row, string_clean_capital_fn, string_clean_upper_fn)

    # call the land_system_fn function
    land_system_list = land_system_fn(row, string_clean_capital_fn)

    # call the water_point_fn function
    water_point_list = water_point_fn(row, string_clean_capital_fn, string_clean_title_fn)

    # extend clean_list with the return variables.
    clean_list.extend(disc_list)
    clean_list.extend(soil_list)
    clean_list.extend(land_system_list)
    clean_list.extend(water_point_list)

    return clean_list


if __name__ == '__main__':
    main_routine()
