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
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Import modules
from __future__ import print_function, division
import pandas as pd
import warnings

warnings.filterwarnings("ignore")


def string_clean_upper_fn(dirty_string):
    """ Remove whitespaces and clean strings.

    :param dirty_string: string object.
    :return clean_string: processed string object.
    """

    str1 = dirty_string.replace('_', ' ')
    str2 = str1.replace('-', ' ')
    str3 = str2.upper()
    clean_string = str3.strip()
    return clean_string


def string_clean_capital_fn(dirty_string):
    """ Remove whitespaces and clean strings.

    :param dirty_string: string object.
    :return clean_string: processed string object.
    """

    str1 = dirty_string.replace('_', ' ')
    str2 = str1.replace('-', ' ')
    str3 = str2.capitalize()
    clean_string = str3.strip()
    return clean_string


def string_clean_title_fn(dirty_string):
    """ Remove whitespaces and clean strings.

    :param dirty_string: string object.
    :return clean_string: processed string object.
    """

    str1 = dirty_string.replace('_', ' ')
    str2 = str1.replace('-', ' ')
    str3 = str2.title()
    clean_string = str3.strip()
    return clean_string


def site_visit_variable_list_fn(star):
    """ Extract and observational workbook, establishment worksheet variables as lists for workbook insertion.

    :param star: pandas dataframe object (star transect).
    :return visit_vert_list1: list of variables for vertical insertion, including recorder, site and date time
    information.
    """

    visit_vert_list1 = [star.recorder[0], star.estimator[0], star.site_orig[0], star.date_time[0], 'BLANK']

    print('visit_vert_list1: ', visit_vert_list1)
    return visit_vert_list1


def site_establishment_fn(star):
    """ Extract and observational workbook, establishment worksheet variables as lists for workbook insertion.

     :param star: pandas dataframe object (star transect).
     :return estab_vert_list13: list of variables for vertical insertion, including property name,
     officers and lat lon information.
     """

    if star.establish.iloc[0] == 'new':
        estab_ver_list1 = [star.recorder[0], star.estimator[0], 'BLANK', star.prop[0], star.unlist_prop[0],
                           star.site_orig[0]]

        estab_ver_list3 = [star.date_time[0], star.off_direct[0], 'GDA94', star.gda_o_lat[0], star.gda_o_lon[0],
                           star.gda_c_lat[0], star.gda_c_lon[0]]
    else:
        estab_ver_list1 = [star.recorder[0], star.estimator[0], 'BLANK', star.prop[0], star.unlist_prop[0],
                           star.site_orig[0]]

        estab_ver_list3 = [star.date_time[0], star.off_direct[0], 'GDA94', star.gda_o_lat[0], star.gda_o_lon[0],
                           star.gda_c_lat[0], star.gda_c_lon[0]]

    estab_vert_list13 = [estab_ver_list1, estab_ver_list3]

    return estab_vert_list13


def ground_composition_ver_list_fn(star):
    """ Collect the ground layer composite data and preform fractional cover calculations.

     :param star: pandas data frame object.
     :return ground_vert_list12345: list object containing list elements of ground cover fractions ready for observation
      sheet insertion.
      """

    if star.rep_cover[0] == 'representative' and star.rep_veg[0] == 'representative':

        ground_layer_ver_list1 = ['Yes']
    else:
        ground_layer_ver_list1 = ['No']

    ground_layer_ver_list2 = [(round(float(star.field_pg[0])) * (float(star.final_veg[0]) / 100)),
                              (round(float(star.field_ag[0])) * (float(star.final_veg[0]) / 100)),
                              (round(float(star.field_pf[0])) * (float(star.final_veg[0]) / 100)),
                              (round(float(star.field_af[0])) * (float(star.final_veg[0]) / 100)),
                              0,
                              (round(float(star.field_veg[0]))),
                              (round(float(star.field_litter[0]))),
                              (round(float(star.field_exposed[0])))]
    ground_layer_ver_list3 = [round(star.field_pg[0]), round(star.field_ag[0]), round(star.field_pf[0]),
                              round(star.field_af[0]), 0]
    ground_layer_ver_list4 = [(round(float(star.final_pg[0]) * float(star.final_veg[0]) / 100)),
                              (round(float(star.final_ag[0]) * float(star.final_veg[0]) / 100)),
                              (round(float(star.final_pf[0]) * float(star.final_veg[0]) / 100)),
                              (round(float(star.final_af[0]) * float(star.final_veg[0]) / 100)), 0,
                              round(star.final_veg[0]), round(star.final_litter[0]), round(star.final_exposed[0])]
    ground_layer_ver_list5 = [round(star.final_pg[0]), round(star.final_ag[0]), round(star.final_pf[0]),
                              round(star.final_af[0]), 0]

    ground_vert_list12345 = [ground_layer_ver_list1, ground_layer_ver_list2, ground_layer_ver_list3,
                             ground_layer_ver_list4, ground_layer_ver_list5]

    return ground_vert_list12345


def site_cover_estimates_fn(star):
    """ Extract and observational workbook, site cover variables as lists for workbook insertion.

    :param star: pandas dataframe object (star transect).
    :return estimates_hor_list12345: list object containing list elements. List elements include field,
    adjusted and total cover fractions.
    """

    if star.rep_cover[0] == 'representative':

        estimates_hor_list1 = [star.field_litter[0], star.field_exposed[0], star.field_veg[0], star.field_site_total[0]]
        estimates_hor_list2 = [0.0, 0.0, 0.0, 0.0, 0.0]
        estimates_hor_list3 = [star.field_pg[0], star.field_ag[0], star.field_pf[0], star.field_af[0], 0]
        estimates_hor_list4 = [star.adj_pg[0], star.adj_ag[0], star.adj_pf[0], star.adj_af[0], 0]
        estimates_hor_list5 = [0.0]

    else:

        estimates_hor_list1 = [star.field_litter[0], star.field_exposed[0], star.field_veg[0], star.field_site_total[0]]
        estimates_hor_list2 = [star.adj_litter[0], star.adj_exposed[0], star.adj_veg[0], star.adj_site_total[0]]
        estimates_hor_list3 = [star.field_pg[0], star.field_ag[0], star.field_pf[0], star.field_af[0], 0]
        estimates_hor_list4 = [star.adj_pg[0], star.adj_ag[0], star.adj_pf[0], star.adj_af[0], 0]
        estimates_hor_list5 = [sum(estimates_hor_list4, 0)]

    estimates_hor_list12345 = [estimates_hor_list1, estimates_hor_list2, estimates_hor_list3, estimates_hor_list4,
                               estimates_hor_list5]

    # round nested list variables and convert to int.
    int_estimates_hor_list12345 = []
    for i in estimates_hor_list12345:

        nested_list = []
        for n in i:
            integer = int(round(n, 0))
            nested_list.append(integer)
        int_estimates_hor_list12345.append(nested_list)

    return int_estimates_hor_list12345


def species_list_fn(df, n):
    """ Create a list from the required (n) botanical name fields from the dataframe (df), loops through ten
    times(number of variables).

    :param df: pandas data frame object.
    :param n: string object passed into the function (i.e. 'PG', 'AG').
    :return botanical_list: list object containing ten botanical names.
    """

    botanical_list = []

    for i in range(10):
        species = df['bot_' + n + '_' + str(i + 1)][0]
        botanical_list.extend([species])
    return botanical_list


def cover_list_fn(df, n):
    """ Create a list from the required (n) cover fields from the DataFrame (df), loops through ten
    times(number of variables).

    :param df: pandas data frame object.
    :param n: string object passed into the function (i.e. 'PG', 'AG').
    :return cover_list: list object containing ten cover values names.
    """

    cover_list = []

    for i in range(10):
        cover = df['cover_' + n + '_' + str(i + 1)][0]
        cover_list.extend([cover])

    return cover_list


def remove_list_values_fn(list1, search_criteria):
    """ Remove all values within a list containing the search_criteria.

    :param list1: input list object.
    :param search_criteria: string object passed into the function.
    :return list1: processed list object.
    """
    while search_criteria in list1:
        list1.remove(search_criteria)

    return list1


def sort_two_lists_fn(list_a, list_b):
    """ Zip two lists and sort them base on list_a (cover values), and return an ordered botanical name list.

    :param list_a: list object containing string elements.
    :param list_b: list object containing float elements.
    :return sorted_list1: list of botanical names sorted by their representative cover values.
    """
    # zip the botanical and cover lists together
    zipped_list = zip(list_a, list_b)
    # sort the two lists together based on the cover values
    sorted_zipped_list = sorted(zipped_list)
    # extract the ordered botanical name list
    sorted_list1 = [elm for n, elm in sorted_zipped_list]

    return sorted_list1


def sort_float_list_fn(list_c):
    """ Sort a list of float elements in ascending order.

    :param list_c: list object containing float elements.
    :return sorted_list2: ordered list object containing float elements.
    """
    # sort list of floats in ascending order
    sorted_list2 = sorted(list_c, key=float)

    return sorted_list2


def reverse_list_fn(list_d):
    """ Loop through an ordered list of float elements in reversed order (descending order) and append to a new list.

    :param list_d: list object containing float elements.
    :return reversed_list: list object containing float elements in revers order.
    """
    reversed_list = []
    # lop through list in reverser order
    for x in reversed(list_d):
        # append value to new list
        reversed_list.append(x)

    return reversed_list


def split_list_fn(list1, n):
    """ Split a list of string variables into maximum length (n).

    :param list1: input list object.
    :param n: integer object passed through the function defining the maximum values in the primary list.
    :return primary_list: list object containing the n number of variables form list1.
    :return secondary_list: list object containing all other variables from list1.
    """

    if len(list1) > n:

        output = [list1[i:i + n] for i in range(0, len(list1), n)]

        primary_list = output[0]
        secondary_list = output[1]
    else:
        primary_list = list1
        secondary_list = []

    return primary_list, secondary_list


def split_cover_list_fn(list1, n):
    """ split cover list into maximum length (n) once 0 values have been removed.

    :param list1: input list object.
    :param n: integer object passed through the function defining the maximum values in the primary list.
    :return primary_list: list object containing the n number of variables form list1.
    :return secondary_list: list object containing all other variables from list1.
    """

    no_zero_list = [i for i in list1 if i != 0.0]

    if len(no_zero_list) > n:

        output = [no_zero_list[i:i + n] for i in range(0, len(no_zero_list), n)]

        primary_list = output[0]
        secondary_list = output[1]
    else:
        primary_list = no_zero_list
        secondary_list = []
    return primary_list, secondary_list


def sum_list_fn(list1):
    """ Calculate the sum of list elements.

    :param list1:" input list of numeric variables.
    :return total: integer object containing the total value of summed values from the list1 object.
    """

    total = 0

    # Iterate each element in list
    # and add them in variable total
    for ele in range(0, len(list1)):
        total = total + list1[ele]

    return total


def common_name_extraction_fn(botanical_series, target_list):
    """ Extract the common name from the botanical_common_series excel document, if there is no match the botanical name
     will be listed as the common name as well as the botanical.

    :param botanical_series: series object containing botanical and common names.
    :param target_list: list object of botanical names.
    :return species_list: list object containing list elements of botanical and common named species.
    """

    species_list = []

    for botanical_name in target_list:
        botanical_name_list = botanical_series.Botanical_name.tolist()
        if botanical_name in botanical_name_list:

            common_name = botanical_series.loc[
                botanical_series['Botanical_name'] == botanical_name, 'Common_name'].iloc[0]

        else:
            common_name = botanical_name

        species_list.append([botanical_name, common_name])

    return species_list


def cover_vegetation_extraction_fn(veg_series, species, cover):
    """ Controls the sorting and common name extraction of the input lists species and cover.

    :param veg_series: series object containing botanical and common species names.
    :param species: list object containing botanical species names.
    :param cover: list object containing species count values.
    :return primary_cover_list: list object containing the (n) number of list elements.
    :return secondary_cover_list: list object containing the remainder of (n) elements.
    :return final_species_list: list object containing (n) list elements of botanical and common named species.
    :return secondary_species_list: list object containing the remainder of (n) list elements of  botanical and common
    named species"""

    # call the remove_list_values_fn function to remove 'BLANK' values.
    species_list = remove_list_values_fn(species, 'BLANK')
    cover_list = remove_list_values_fn(cover, 0.0)

    # call the sort_two_lists_fn function to sort two lists based on the cover values, extracting the botanical names.
    sorted_bot_list = sort_two_lists_fn(cover_list, species_list)

    # call the sort_float_list_fn function to sort the cover list (floats separately).
    sort_cover_list = sort_float_list_fn(cover_list)

    # call the reverse_list_fn to revers the sorted lists
    reverse_sort_bot_list = reverse_list_fn(sorted_bot_list)
    reverse_sort_cover_list = reverse_list_fn(sort_cover_list)

    # call the split_list_fn function to separate the reversed ordered species list into two lists based on n value.
    primary_species_list, secondary_species_list = split_list_fn(reverse_sort_bot_list, 4)

    # call the split_list_fn function to separate the reversed ordered species list into two lists based on n value.
    primary_cover_list, secondary_cover_list = split_cover_list_fn(reverse_sort_cover_list, 4)

    # call the common_name_extraction_fn function to extract the common names for the botanical names.
    final_species_list = common_name_extraction_fn(veg_series, primary_species_list)

    return primary_cover_list, secondary_cover_list, final_species_list, secondary_species_list


def main_routine(star_csv, veg_list_excel):
    """ This script extracts variables from the current site star dataframe and returns xxx ordered lists for
    observational workbook establishment sheet insertion.

    :param star_csv: sting object containing the file path to the current site star csv file.
    :param veg_list_excel: string object containing the path to an excel document containing botanical and
    common names.
    :return estab_vert_list13:  list of variables for vertical insertion, including property name,
    officers and lat lon information.
    :return visit_vert_list1: list of variables for vertical insertion, including recorder, site and date time
    information.
    :return ground_vert_list12345: list object containing list elements of ground cover fractions ready for
    observation sheet insertion.
    :return estimates_hor_list12345: list object containing list elements. List elements include field,
    adjusted and total cover fractions.
    :return estimates_veg_list: list object containing the final species and cover elements for insertion.
    """

    # import the site star transect csv
    star_tran = pd.read_csv(star_csv)

    cols = ['wgs_c_acc', 'wgs_o_acc', 'field_litter', 'adj_litter', 'final_litter', 'field_exposed', 'adj_exposed',
            'final_exposed', 'field_veg', 'adj_veg', 'final_veg', 'field_site_total', 'adj_site_total',
            'final_site_total', 'rep_veg', 'field_pg', 'adj_pg', 'final_pg', 'field_ag', 'adj_ag', 'final_ag',
            'field_pf', 'adj_pf', 'final_pf', 'field_af', 'adj_af', 'final_af', 'field_veg_total', 'adj_veg_total',
            'final_veg_total', 'height_tree', 'height_shrub', 'cover_3p_1', 'cover_3p_2', 'cover_3p_3', 'cover_3p_4',
            'cover_3p_5', 'cover_3p_6', 'cover_3p_7', 'cover_3p_8', 'cover_3p_9', 'cover_3p_10', 'cover_pg_1',
            'cover_pg_2', 'cover_pg_3', 'cover_pg_4', 'cover_pg_5', 'cover_pg_6', 'cover_pg_7', 'cover_pg_8',
            'cover_pg_9', 'cover_pg_10', 'cover_ag_1', 'cover_ag_2', 'cover_ag_3', 'cover_ag_4', 'cover_ag_5',
            'cover_ag_6', 'cover_ag_7', 'cover_ag_8', 'cover_ag_9', 'cover_ag_10', 'cover_pf_1', 'cover_pf_2',
            'cover_pf_3', 'cover_pf_4', 'cover_pf_5', 'cover_pf_6', 'cover_pf_7', 'cover_pf_8', 'cover_pf_9',
            'cover_pf_10', 'cover_af_1', 'cover_af_2', 'cover_af_3', 'cover_af_4', 'cover_af_5', 'cover_af_6',
            'cover_af_7', 'cover_af_8', 'cover_af_9', 'cover_af_10']

    # replace all int and float missing variables with a 0 value
    star_tran[cols] = star_tran[cols].fillna(float(0.0))
    star = star_tran.fillna('BLANK').replace('Nan', 'BLANK')

    # import the odk veg list and create a series
    veg_df = pd.read_excel(veg_list_excel, sheet_name='grass_forb_list')
    veg_series = veg_df[['Botanical_name', 'Common_name']]

    # clean property name
    property_name = star.final_prop[0].replace(' ', '_')

    # call the site_visit_vertical_list_fn function to extract basic visit information (e.g. recorder, date time)
    visit_vert_list1 = site_visit_variable_list_fn(star)

    # call the site_establishment_fn function to extract basic establishment information (e.g. recorder, land system)
    estab_vert_list13 = site_establishment_fn(star)

    # call the ground_composition_ver_list_fn function to extract and preform vegetation fractional cover calculations.
    ground_vert_list12345 = ground_composition_ver_list_fn(star)

    # call the ground_composition_ver_list_fn function to extract and preform site fractional cover calculations.
    estimates_hor_list12345 = site_cover_estimates_fn(star)

    # ------------------------------------------- 3P Perennial Grass ---------------------------------------------------

    # call the species_list_fn function to extract the botanical vegetation names for 3p grasses.
    species = species_list_fn(star, '3p')
    # call the cover_list_fn function to extract the botanical cover numbers per species.
    cover = cover_list_fn(star, '3p')

    # call the cover_vegetation_extraction_fn to control the sorting and splitting of vegetation lists.
    primary_cover_list3p, secondary_cover_list3p, final_species_list3p, secondary_species_list3p = \
        cover_vegetation_extraction_fn(veg_series, species, cover)

    # call the species_list_fn function to extract the botanical vegetation names for perennial grasses.
    species = species_list_fn(star, 'pg')

    # call the cover_list_fn function to extract the botanical cover numbers per species.
    cover = cover_list_fn(star, 'pg')

    if len(secondary_cover_list3p) > 0:
        species.extend(secondary_species_list3p)
        cover.extend(secondary_cover_list3p)

    # call the cover_vegetation_extraction_fn to control the sorting and splitting of vegetation lists.
    primary_cover_list_pg, secondary_cover_list_pg, final_species_list_pg, secondary_species_list_pg = \
        cover_vegetation_extraction_fn(veg_series, species, cover)

    # call the sum_list_fn function to calculate the sum of list elements.
    sum_total_p = sum_list_fn(primary_cover_list3p + primary_cover_list_pg)

    # ------------------------------------------------ Annual Grass ----------------------------------------------------

    # call the species_list_fn function to extract the botanical vegetation names for annual grasses.
    species = species_list_fn(star, 'ag')

    # call the cover_list_fn function to extract the botanical cover numbers per species.
    cover = cover_list_fn(star, 'ag')

    # call the cover_vegetation_extraction_fn to control the sorting and splitting of vegetation lists.
    primary_cover_list_ag, secondary_cover_list_ag, final_species_list_ag, secondary_species_list_ag = \
        cover_vegetation_extraction_fn(veg_series, species, cover)
    # print('ag:', primary_cover_list_ag, secondary_cover_list_ag, final_species_list_ag, secondary_species_list_ag)

    # call the sum_list_fn function to calculate the sum of list elements.
    sum_total_ag = sum_list_fn(primary_cover_list_ag)
    # print('ag sum: ', sum_total_ag)

    # ------------------------------------------------ Perennial Forb --------------------------------------------------

    # call the species_list_fn function to extract the botanical vegetation names for perennial forbs.
    species = species_list_fn(star, 'pf')
    # call the cover_list_fn function to extract the botanical cover numbers per species.
    cover = cover_list_fn(star, 'pf')

    # call the cover_vegetation_extraction_fn to control the sorting and splitting of vegetation lists.
    primary_cover_list_pf, secondary_cover_list_pf, final_species_list_pf, secondary_species_list_pf = \
        cover_vegetation_extraction_fn(veg_series, species, cover)

    # call the sum_list_fn function to calculate the sum of list elements.
    sum_total_pf = sum_list_fn(primary_cover_list_pf)

    # ------------------------------------------------- Annual Forb ----------------------------------------------------

    # call the species_list_fn function to extract the botanical vegetation names for annual forbs.
    species = species_list_fn(star, 'af')
    # call the cover_list_fn function to extract the botanical cover numbers per species.
    cover = cover_list_fn(star, 'af')

    # call the cover_vegetation_extraction_fn to control the sorting and splitting of vegetation lists.
    primary_cover_list_af, secondary_cover_list_af, final_species_list_af, secondary_species_list_af = \
        cover_vegetation_extraction_fn(veg_series, species, cover)

    # call the sum_list_fn function to calculate the sum of list elements.
    sum_total_af = sum_list_fn(primary_cover_list_af)

    total_cover_list = [sum_total_p, sum_total_ag, sum_total_pf, sum_total_af, 0]
    estimates_veg_list = [final_species_list3p, primary_cover_list3p, final_species_list_pg, primary_cover_list_pg,
                          final_species_list_ag, primary_cover_list_ag,
                          final_species_list_pf, primary_cover_list_pf, final_species_list_af, primary_cover_list_af,
                          total_cover_list]

    return property_name, estab_vert_list13, visit_vert_list1, ground_vert_list12345, estimates_hor_list12345, \
           estimates_veg_list


if __name__ == '__main__':
    main_routine()
