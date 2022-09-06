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


def transect_table_url_fn(row):
    """ Extract the html transect table url.

    :param row: pandas dataframe row value object.
    :return tran1_url: string object containing the transect1 name variable.
    :return tran2_url: string object containing the transect2 name variable.
    :return tran3_url: string object containing the transect1 name variable.
    """

    tran1_url = str(row['REPEAT_points_1'])
    tran2_url = str(row['REPEAT_points_2'])
    tran3_url = str(row['REPEAT_points_3'])

    tran_name_list = [tran1_url, tran2_url, tran3_url]
    return tran_name_list


def transect_variables_fn(row, n):
    """ Extract the transect variable counts.

    :param row: pandas dataframe row value object.
    :param n: string object containing the transect number (1,2 or 3).
    :return tran_count: list object containing 21 float variables.
    """

    bare = float(row['BAREG_COUNT' + n])
    gravel = float(row['GRAV_COUNT' + n])
    rock = float(row['RCK_COUNT' + n])
    ash = float(row['ASHH_COUNT' + n])
    litter = float(row['LIT_COUNT' + n])
    crypto = float(row['CRYP_COUNT' + n])
    dead_pg = float(row['DPG_COUNT' + n])
    green_pg = float(row['GPG_COUNT' + n])
    dead_ag = float(row['DAG_COUNT' + n])
    green_ag = float(row['GAG_COUNT' + n])
    dead_fb = float(row['DF_COUNT' + n])
    green_fb = float(row['GF_COUNT' + n])

    abv_green = float(row['ABOVEG_COUNT' + n])
    abv_dead = float(row['ABOVED_COUNT' + n])
    abv_brown = float(row['ABOVEB_COUNT' + n])
    abv_ic = float(row['ABOVEIC_COUNT' + n])
    abv_nic = float(row['ABOVENIC_COUNT' + n])

    blw_green = float(row['BELOWG_COUNT' + n])
    blw_dead = float(row['BELOWD_COUNT' + n])
    blw_brown = float(row['BELOWB_COUNT' + n])
    blw_none = float(row['BELOWN_COUNT' + n])

    tran_count = [bare, gravel, rock, ash, litter, crypto, dead_pg, green_pg, dead_ag, green_ag,
                  dead_fb, green_fb, abv_green, abv_dead, abv_brown, abv_ic, abv_nic, blw_green, blw_dead, blw_brown,
                  blw_none]

    return tran_count


def field_adjusted_fn(field, adjusted, represent):
    """ Extract the final site and vegetation values.

    :param field: string object containing the field variable.
    :param adjusted: string object containing the adjusted name variable.
    :param represent: string object containing the represent variable.
    """

    if represent == 'representative':
        final = field

    else:
        final = adjusted

    return field, adjusted, final


def coerce_to_zero(input_list):
    """ Loop through a list and convert Nan values to int(0).

    :param input_list: list object containing numeric values.
    :return output_list: processed list with null values converted to int(0).
    """

    input_list = [0 if x != x else x for x in input_list]

    return input_list


def site_cover_fn(row):
    """ Extract the site cover values.

     :param row: pandas dataframe row value object.
     :return site_cover_list: list object containing 13 string and float site cover fraction variables.
     """

    rep_cover = str(row['SITE_COVER_FRACTIONS:SITE_COVER_ADJ'])

    # append litter cover information
    field = float(row['LIT_SUM'])
    adjusted = float(row['SITE_COVER_FRACTIONS:LITTER_ADJUSTED'])
    # call the field_adjusted_fn function
    field_litter, adj_litter, final_litter = field_adjusted_fn(field, adjusted, rep_cover)

    # append exposed cover information
    field = float(row['EXPOSED_GROUND_SUM'])
    adjusted = float(row['SITE_COVER_FRACTIONS:EXPOSED_GROUND_ADJUSTED'])
    # call the field_adjusted_fn function
    field_exposed, adj_exposed, final_exposed = field_adjusted_fn(field, adjusted, rep_cover)

    # append veg cover information
    field = float(row['VEG_SUM'])
    adjusted = float(row['SITE_COVER_FRACTIONS:TOTAL_VEG_ADJUSTED'])
    # call the field_adjusted_fn function
    field_veg, adj_veg, final_veg = field_adjusted_fn(field, adjusted, rep_cover)

    # append veg cover information
    field = float(row['SITE_COVER_FRACTIONS:TOTAL_COVER'])
    adjusted = float(row['SITE_COVER_FRACTIONS:SITE_ADJ'])
    # call the field_adjusted_fn function
    field_site_total, adj_site_total, final_site_veg = field_adjusted_fn(field, adjusted, rep_cover)

    site_cover_list = [rep_cover, field_litter, adj_litter, final_litter, field_exposed, adj_exposed, final_exposed,
                       field_veg, adj_veg, final_veg, field_site_total, adj_site_total, final_site_veg]

    # call the coerce_to_zero function to convert null vales to 0
    final_cover_list = coerce_to_zero(site_cover_list)

    return final_cover_list


def veg_fractions_fn(row):
    """ Extract the site vegetation fraction values.

     :param row: pandas dataframe row value object.
     :return veg_fraction_list: list object containing 16 string and float site cover fraction variables
     3 np.nan placeholders have been included for annual forbs.
     """

    rep_veg = str(row['SITE_VEG_FRACTIONS:VEG_COVER_ADJUST'])

    # perennial grass
    field = float(row['PG_SUM_PROP'])
    adjusted = float(row['SITE_VEG_FRACTIONS:PG_TOTAL_ADJUSTED'])
    # call the fieldAdjusted feature
    field_perennial, adj_perennial, final_perennial = field_adjusted_fn(field, adjusted, rep_veg)

    # annual grass
    field = float(row['AG_SUM_PROP'])
    adjusted = float(row['SITE_VEG_FRACTIONS:AG_TOTAL_ADJUSTED'])
    # call the fieldAdjusted feature
    field_annual, adj_annual, final_annual = field_adjusted_fn(field, adjusted, rep_veg)

    # forbs
    field = float(row['F_SUM_PROP'])
    adjusted = float(row['SITE_VEG_FRACTIONS:F_TOTAL_ADJUSTED'])
    # call the fieldAdjusted feature
    field_forb, adj_forb, final_forb = field_adjusted_fn(field, adjusted, rep_veg)

    # totals
    field = float(row['SITE_VEG_FRACTIONS:TOTAL_VEG_FRACTION'])
    adjusted = float(row['SITE_VEG_FRACTIONS:VEG_ADJ'])
    # call the fieldAdjusted feature
    field_veg_total, adj_veg_total, final_veg_total = field_adjusted_fn(field, adjusted, rep_veg)

    # Append values to a list, three np.nan included to fill when forbs are split into perennial/annual
    veg_fraction_list = [rep_veg, field_perennial, adj_perennial, final_perennial, field_annual, adj_annual,
                         final_annual, field_forb, adj_forb, final_forb, np.nan, np.nan, np.nan, field_veg_total,
                         adj_veg_total, final_veg_total]

    # call the coerce_to_zero function to convert null vales to 0
    final_veg_fraction_list = coerce_to_zero(veg_fraction_list)

    return final_veg_fraction_list


def height_estimates_fn(row):
    """ Extract the tree and shrub height estimate values.

    :param row: pandas dataframe row value object.
    :return height_list: list object containing 2 float variables.
    """

    height_tree = str(row['HEIGHT_ESTIMATE:GRASS_HEIGHT'])
    height_shrub = str(row['HEIGHT_ESTIMATE:TREE_HEIGHT'])

    height_list = [height_tree, height_shrub]

    return height_list


def main_routine(clean_list, row, string_clean_capital_fn):
    """ Extract and clean transect data from the star transect odk raw output.

    :param string_clean_capital_fn: function object that cleans and reformats a string.
    :param clean_list: list object created under step2_1_star_transect_processing_workflow.py - new variables
    are extended or appended to the end.
    :param row: pandas dataframe row value object.
    :return clean_list: list object with additional variables extended or appended to the end.
    """

    # call the string_clean_capital_fn function ofn each transect.
    transect1 = string_clean_capital_fn(str(row['TRAN1']))
    transect2 = string_clean_capital_fn(str(row['TRAN2']))
    transect3 = string_clean_capital_fn(str(row['TRAN3']))

    # call the transect_table_url_fn function to extract the html transect table url.
    tran_name_list = transect_table_url_fn(row)

    # call the transect_count_function to extract the transect variable counts.
    transect1_count = transect_variables_fn(row, '1')
    transect2_count = transect_variables_fn(row, '2')
    transect3_count = transect_variables_fn(row, '3')

    # call the site cover function
    final_site_cover_list = site_cover_fn(row)

    # call the veg fractions function
    species_list = veg_fractions_fn(row)

    # call the height estimate function
    height_list = height_estimates_fn(row)

    # extend clean_list with the return variables.
    clean_list.extend([transect1])
    clean_list.extend(transect1_count)
    clean_list.extend([transect2])
    clean_list.extend(transect2_count)
    clean_list.extend([transect3])
    clean_list.extend(transect3_count)
    clean_list.extend(tran_name_list)
    clean_list.extend(final_site_cover_list)
    clean_list.extend(species_list)
    clean_list.extend(height_list)

    return clean_list


if __name__ == '__main__':
    main_routine()
