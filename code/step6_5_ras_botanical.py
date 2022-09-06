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
import numpy as np

warnings.filterwarnings("ignore")


def extract_botanical_fn(row, string_clean_capital_fn, n):
    """ Extract botanical names for the four ODK data entry options.

     :param row: pandas dataframe row value object.
     :param string_clean_capital_fn: function to clean string objects returning capitalized format.
     :param n: string object passed into the function (i.e str(TS), str(SB)).
     :return list_botanical: list object containing the five botanical names for the input species form.
     within each site.
     """

    list_botanical = []

    for i in range(4):

        botanical = string_clean_capital_fn(str(row[n + '_SP:' + n + str(i + 1)]))
        if botanical == 'Other1':
            final_botanical = string_clean_capital_fn(str(row[n + '_SP:' + n + '_OTHER1']))
        elif botanical == 'Other2':
            final_botanical = string_clean_capital_fn(str(row[n + '_SP:' + n + '_OTHER2']))
        elif botanical == 'Other3':
            final_botanical = string_clean_capital_fn(str(row[n + '_SP:' + n + '_OTHER3']))
        elif botanical == 'Other4':
            final_botanical = string_clean_capital_fn(str(row[n + '_SP:' + n + '_OTHER4']))
        else:
            final_botanical = botanical
        list_botanical.append(final_botanical)

    return list_botanical


def basal_density_fn(row):
    """ Extract the basal area, tree and shrub density variables.
    
    :param row: pandas dataframe row value object.
    :return basal_density_list: list object containing three variables: 
    basal, tree_density, shrub_density.
    """

    basal = float(row['BASAL_AREA'])
    tree_density = str(row['WOODY_THICKENING:TREE_COVER'])
    shrub_density = str(row['WOODY_THICKENING:SHRUB_COVER'])

    basal_density_list = [basal, tree_density, shrub_density]
    return basal_density_list


def grass_cover_fn(row, n):
    """ Extract the min and max cover variables.

    :param row: pandas dataframe row value object.
    :param n: string object passed into the function ( i.e. PG, AG). 
    :return value:  string object created by concatenating min and max  values."""

    min_cover = str(row['GROUP_GROUND_COVER:MIN_' + n + '_COVER_TOTAL'])
    if min_cover != np.nan:
        min_cover = min_cover
    else:
        min_cover = '0'

    max_cover = str(row['GROUP_GROUND_COVER:MAX_' + n + '_COVER_TOTAL'])
    if max_cover != np.nan:
        max_cover = max_cover
    else:
        max_cover = '0'

    value = min_cover + '-' + max_cover

    if value == '0 - 0':
        value = '0'

    return value


def grass_cover_min_max_fn(row):
    """ Extract the total min and max cover values.

    :param row: pandas dataframe row value object.
    :return min_cover: total minimum vegetation cover value.
    :return max_cover: total maximum vegetation  cover value.
    """

    min_cover = int(row['GROUP_GROUND_COVER:MIN_TOTAL'])
    max_cover = int(row['GROUP_GROUND_COVER:MAX_TOTAL'])

    min_max_list = [min_cover, max_cover]
    return min_cover, max_cover


def main_routine(clean_list, row, string_clean_capital_fn):
    """ Extract the ras botanical names.

    :param clean_list: list object containing processed variables.
    - new variables are extended to the end of the list.
    :param row: pandas dataframe row value object.
    :param string_clean_capital_fn: function to clean string objects returning capitalized format.
    :return clean_list: list object containing processed variables
    - new variables are extended to the end of the list.
    """

    variable_list = ['PPP', 'PG', 'AG', 'FB', 'TS', 'SB']
    list_grass_botanical = []
    for i in variable_list:
        # call the extract_botanical_fn function to extract botanical names for the four ODK data entry options.
        botanical1, botanical2, botanical3, botanical4 = extract_botanical_fn(
            row, string_clean_capital_fn, i)

        # extend the final list of grass species
        list_grass_botanical.extend([botanical1, botanical2, botanical3, botanical4])

    variable_list = ['PPP', 'PG', 'AG', 'FB']
    cover_grass_list = []
    grass_cover_string_list = []
    for i in variable_list:
        value = grass_cover_fn(row, str(i))
        grass_cover_string_list.extend([value])

    # extend clean_list with results
    clean_list.extend(list_grass_botanical)
    clean_list.extend(grass_cover_string_list)

    # call the basal_density_fn function to extract the basal area, tree density and shrub density information.
    basal_density_list = basal_density_fn(row)

    # call the grass_cover_min_max_fn function to extract the grass min and max values.
    min_max_list = grass_cover_min_max_fn(row)

    # extend outputs to clean list
    clean_list.extend(min_max_list)
    clean_list.extend(basal_density_list)

    return clean_list


if __name__ == '__main__':
    main_routine()
