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


def belt_width_fn(row):
    """ Extract the woody thickening belt width.

    :param row: pandas dataframe row value object.
    :return factor: integer object containing the woody transect width.
    """

    transect_dict = {'500': '1 metre', '1000': '2 metres', '2000': '4 metres'}

    width = str(row['BELT_WIDTH'])
    belt_width = (transect_dict[width])

    return belt_width


def wood_thick_counts_fn(row):
    """ Extract woody thickening information for the five transects within each site.

    :param row: pandas dataframe row value object.
    :return woody_list: list object containing three woody thickening variables for each of the five transects
    within each site.
    """

    woody_list = []
    for i in range(5):
        woody = str(row['TRANSECT_' + str(i + 1) + ':TRAN' + str(i + 1)]).replace('-', ' ')
        tree = (row['TRANSECT_' + str(i + 1) + ':T' + str(i + 1) + '_JUV_TREE'])
        shrub = float(row['TRANSECT_' + str(i + 1) + ':T' + str(i + 1) + '_JUV_SHRUB'])
        list_a = [woody, tree, shrub]
        woody_list.extend(list_a)

    return woody_list


def woody_density_fn(row):
    """ Extract woody density totals.

    :param row: pandas dataframe row value object.
    :return woody_density_list: list object containing four density totals per site.
    """

    juv_tree_count = float(row['GROUP_VEG_LIST:STEM_COUNT_TOTAL_TREE'])
    juv_shrub_count = float(row['GROUP_VEG_LIST:STEM_COUNT_TOTAL_SHRUB'])

    juv_tree_density = float(row['GROUP_VEG_LIST:STEM_DENSITY_TREE_CALC'])
    juv_shrub_density = float(row['GROUP_VEG_LIST:STEM_DENSITY_SHRUB_CALC'])

    woody_density_list = [juv_tree_count, juv_shrub_count, juv_tree_density, juv_shrub_density]

    return woody_density_list


def main_routine(clean_list, row):
    """ Extract the woody thickening transect width, form counts and density totals.

    :param clean_list: list object containing processed variables
    - new variables are extended to the end of the list.
    :param row: pandas dataframe row value object.
    :return clean_list: list object containing processed variables
    - new variables are extended to the end of the list.
    """

    # call the belt_width_fn function to extract the woody thickening belt width.
    belt_width = belt_width_fn(row)

    # call the wood_thick_counts_fn function to extract woody thickening information for the five transects within
    # each site.
    woody_list = wood_thick_counts_fn(row)

    # call the woody_density_fn function to extract woody density totals.
    woody_density_list = woody_density_fn(row)

    # extend outputs to clean_list
    clean_list.extend([belt_width])
    clean_list.extend(woody_list)
    clean_list.extend(woody_density_list)

    return clean_list


if __name__ == '__main__':
    main_routine()
