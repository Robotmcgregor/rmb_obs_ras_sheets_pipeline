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


def basal_factors_fn(row):
    """ Extract the basal factor.

    :param row: pandas dataframe row value object.
    :return factor: integer object containing the basal factor.
    """

    factor = float(row['LOCATION_FACTOR'])

    return factor


def basal_position_fn(row):
    """ Extract basal information for seven locations within each site.

    :param row: pandas dataframe row value object.
    :return basal_list: list object containing  five basal variables for each of the seven sites.
    """

    basal_list = []
    for i in range(7):
        str(i + 1)

        basal = str(row['Location_' + str(i + 1) + ':LOCATION' + str(i + 1) + '_LABEL'][:-4]).replace('-', ' ')
        dead_tree = float(row['Location_' + str(i + 1) + ':LOCATION' + str(i + 1) + '_TREE_DEAD'])
        live_tree = float(row['Location_' + str(i + 1) + ':LOCATION' + str(i + 1) + '_TREE_LIVE'])
        dead_shrub = float(row['Location_' + str(i + 1) + ':LOCATION' + str(i + 1) + '_SHRUB_DEAD'])
        live_shrub = float(row['Location_' + str(i + 1) + ':LOCATION' + str(i + 1) + '_SHRUB_LIVE'])
        list_a = [basal, dead_tree, live_tree, dead_shrub, live_shrub]
        basal_list.extend(list_a)

    return basal_list


def basal_calc_odk_fn(row):
    """ Extract basal totals round basal to 0.1.

    :param row: pandas dataframe row value object.
    :return basal_totals_list: list object containing three basal totals per site.
    """

    basal_tree = round(float(row['BA_ADULT_TREES']), 1)
    import numpy as np

    basal_shrub = round(float(row['BA_ADULT_SHRUBS']), 1)
    total_basal = round(float(basal_tree + basal_shrub), 1)

    basal_totals_list = [basal_tree, basal_shrub, total_basal]

    return basal_totals_list


def main_routine(clean_list, row):
    """ Extract the basal factor, counts and totals.

    :param clean_list: list object containing processed variables
    - new variables are extended to the end of the list.
    :param row: pandas dataframe row value object.
    :return clean_list: list object containing processed variables
    - new variables are extended to the end of the list.
    """

    # call the basal_factors_fn function to extract the basal factor.
    factor = basal_factors_fn(row)

    # call the basal_position_fn function to extract basal information for seven locations within each site.
    basal_list = basal_position_fn(row)

    # call the basal_calc_odk_fn function
    basal_totals_list = basal_calc_odk_fn(row)

    # extend outputs to clean_list
    clean_list.append(factor)
    clean_list.extend(basal_list)
    clean_list.extend(basal_totals_list)

    return clean_list


if __name__ == '__main__':
    main_routine()
