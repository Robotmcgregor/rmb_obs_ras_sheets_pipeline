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
import geopandas as gpd


warnings.filterwarnings("ignore")


def string_clean_upper_fn(dirty_string):
    """ Remove whitespaces and clean strings.

            :param dirty_string: string object.
            :return clean_string: processed string object. """

    str1 = dirty_string.replace('_', ' ')
    str2 = str1.replace('-', ' ')
    str3 = str2.upper()
    clean_string = str3.strip()
    return clean_string


def string_clean_capital_fn(dirty_string):
    """ Remove whitespaces and clean strings.

            :param dirty_string: string object.
            :return clean_string: processed string object. """

    str1 = dirty_string.replace('_', ' ')
    str2 = str1.replace('-', ' ')
    str3 = str2.capitalize()
    clean_string = str3.strip()
    return clean_string


def string_clean_title_fn(dirty_string):
    """ Remove whitespaces and clean strings.

            :param dirty_string: string object.
            :return clean_string: processed string object. """

    str1 = dirty_string.replace('_', ' ')
    str2 = str1.replace('-', ' ')
    str3 = str2.title()
    clean_string = str3.strip()
    return clean_string


def site_visit_variable_list_fn(star):
    """ Extract and observational workbook, establishment worksheet variables as lists for workbook insertion.

              :param star: pandas dataframe object (star transect).
              :return visit_vert_list1: list of variables for vertical insertion, including recorder, site and date time
              information."""

    visit_vert_list1 = [star.recorder[0], star.estimator[0], star.site_orig[0], star.date_time[0], 'BLANK']

    return visit_vert_list1


def site_establishment_fn(star):
    """ Extract and observational workbook, establishment worksheet variables as lists for workbook insertion.

             :param star: pandas dataframe object (star transect).
             :return estab_vert_list13: list of variables for vertical insertion, including property name,
             officers and lat lon information."""

    if star.establish.iloc[0] == 'new':
        estab_ver_list1 = [star.recorder[0], star.estimator[0], 'BLANK', star.prop[0], star.unlist_prop[0],
                           star.site_orig[0]]

        datum = string_clean_upper_fn(str(star.datum[0]))

        estab_ver_list3 = [star.date_time[0], star.off_direct[0], datum, star.o_lat[0], star.o_lon[0], star.c_lat[0],
                           star.c_lon[0]]
    else:
        estab_ver_list1 = [star.recorder[0], star.estimator[0], 'BLANK', star.prop[0], star.unlist_prop[0],
                           star.site_orig[0]]

        # todo establishment sheet new or existing - should these areas be blank or keep numbers
        estab_ver_list3 = ['BLANK', 'BLANK', 'BLANK', 'BLANK', 'BLANK', 'BLANK',
                           'BLANK']
        # I have added this to see
        """datum = string_clean_upper_fn(str(star.datum[0]))
        estab_ver_list3 = [star.date_time[0], star.off_direct[0], datum, star.o_lat[0], star.o_lon[0], star.c_lat[0],
                           star.c_lon[0]]"""

    estab_vert_list13 = [estab_ver_list1, estab_ver_list3]

    return estab_vert_list13


def ground_composition_ver_list_fn(star):
    """ Collect the ground layer composite data and preform fractional cover calculations.

     :param star: pandas data frame object.
     :return ground_vert_list12345: list object containing list elements of ground cover fractions ready for observation
      sheet insertion. """

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
            adjusted and total cover fractions. """

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
            :return botanical_list: list object containing ten botanical names."""

    botanical_list = []

    for i in range(10):
        species = df['bot_' + n + '_' + str(i + 1)][0]
        botanical_list.extend([species])
    return botanical_list


def cover_list_fn(df, n):
    """ create a list from the required (n) cover fields from the DataFrame (df), loops through ten
        times(number of variables).

            :param df: pandas data frame object.
            :param n: string object passed into the function (i.e. 'PG', 'AG').
            :return cover_list: list object containing ten cover values names."""

    cover_list = []

    for i in range(10):
        cover = df['cover_' + n + '_' + str(i + 1)][0]
        cover_list.extend([cover])

    return cover_list


def remove_list_values_fn(list1, search_criteria):
    """ Remove all values within a list containing the search_criteria.

             :param list1: input list object.
             :param search_criteria: string object passed into the function.
             :return list1: processed list object. """
    while search_criteria in list1: list1.remove(search_criteria)

    return list1


def reverse_order_lists_and_clean_species_list_fn(species):
    """ Reverse the species list.

            :param species: list object containing species names and 'BLANK list elements.
            :return output_list: list object containing the elements of the species list in reverse order."""

    # call the remove_list_values_fn function on the species list
    species_list = remove_list_values_fn(species, 'BLANK')
    # reverse order list
    output_list = []

    for i in reversed(species_list):
        output_list.append(i)

    return output_list


def reverse_order_lists_and_clean_cover_list(cover):
    """ reverse the count list and convert to int.

            :param cover: list object containing cover value list elements.
            :return output_list: list object containing the elements of the cover list in reverse order."""

    cover_list = remove_list_values_fn(cover, 'BLANK')
    output_list = []
    # convert float to int in reverse order
    #todo these need to be kept as float not converted to integer.
    for i in reversed(cover_list):
        rounded_value = round(i, 1)

        n = int(rounded_value)
        output_list.append(n)

    return output_list


def split_list_fn(list1, n):
    """ split a list of string variables into maximum length (n).

            :param list1: input list object.
            :param n: integer object passed through the function defining the maximum values in the primary list.
            :return primary_list: list object containing the n number of variables form list1.
            :return secondary_list: list object containing all other variables from list1."""

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
            :return secondary_list: list object containing all other variables from list1."""

    # todo check this with multiple data values.
    no_zero_list = [i for i in list1 if i != 0]

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
            :return total: integer object containing the total value of summed values from the list1 object. """

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
            :return species_list: list object containing list elements of botanical and common named species. """

    species_list = []

    for botanical_name in target_list:
        botanical_name_list = botanical_series.Botanical_name.tolist()
        if botanical_name in botanical_name_list:

            common_name = botanical_series.loc[botanical_series['Botanical_name'] == botanical_name, 'Common_name'].iloc[
                0]

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
            :return secondary_species_list: list object containing the remainder of (n) list elements of  botanical and common named species"""

    print('='*50)
    print('species: ', species)
    print('cover: ', cover)
    # call the reverse_order_lists_and_clean_species_list_fn function
    descend_species_list = reverse_order_lists_and_clean_species_list_fn(species)
    print('descend_species_list: ', descend_species_list)

    # call the reverse_order_lists_and_clean_cover_list function
    descend_cover_list = reverse_order_lists_and_clean_cover_list(cover)
    print('descend_cover_list: ', descend_cover_list)

    # call the split_list_fn function
    primary_species_list, secondary_species_list = split_list_fn(descend_species_list, 4)
    print('primary_species_list: ', primary_species_list)
    print('secondary_species_list: ', secondary_species_list)

    # call the split_list_fn function
    primary_cover_list, secondary_cover_list = split_cover_list_fn(descend_cover_list, 4)
    print('primary_cover_list: ', primary_cover_list)
    print('secondary_cover_list: ', secondary_cover_list)

    # call the commonNameExtraction FN function
    final_species_list = common_name_extraction_fn(veg_series, primary_species_list)
    print('final_species_list: ', final_species_list)
    print('='*50)

    return primary_cover_list, secondary_cover_list, final_species_list, secondary_species_list


def main_routine(star_csv, site, site_dir, veg_list_excel, previous_visits):
    """ Extract variables from the current site star data frame and return ordered lists for observational
    workbook insertion.

            :param previous_visits:
            :param star_csv: sting object containing the file path to the current site star csv file.
            :param site: string object containing the current site.
            :param site_dir: string object containing the path to the site directory.
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
            :return estimates_veg_list: list object containing the final species and cover elements for insertion. """

    print('step_8_2_site_star_data_extraction.py INITIATED.')

    # import the site star transect csv
    star_tran = pd.read_csv(star_csv)

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
    star_tran[cols] = star_tran[cols].fillna(float(0.0))
    star = star_tran.fillna('BLANK').replace('Nan', 'BLANK')

    # import the odk veg list
    veg_df = pd.read_excel(veg_list_excel, sheet_name='grass_forb_list')

    veg_series = veg_df[['Botanical_name', 'Common_name']]

    property_name = star.final_prop[0].replace(' ', '_')

    # call the site_visit_vertical_list_fn function to extract basic visit information (e.g. recorder, date time)
    visit_vert_list1 = site_visit_variable_list_fn(star)

    # call the site_establishment_fn function to extract basic establishment information (e.g. recorder, land system)
    estab_vert_list13 = site_establishment_fn(star)

    # call the ground_composition_ver_list_fn function to extract and preform vegetation fractional cover calculations.
    ground_vert_list12345 = ground_composition_ver_list_fn(star)

    # call the ground_composition_ver_list_fn function to extract and preform site fractional cover calculations.
    estimates_hor_list12345 = site_cover_estimates_fn(star)

    # call the species_list_fn function to extract the botanical vegetation names for 3p grasses.
    species = species_list_fn(star, '3p')
    # call the cover_list_fn function to extract the botanical cover numbers per species.
    cover = cover_list_fn(star, '3p')

    # call the cover_vegetation_extraction_fn to control the sorting and splitting of vegetation lists.
    primary_cover_list3p, secondary_cover_list3p, final_species_list3p, secondary_species_list3p = \
        cover_vegetation_extraction_fn(veg_series, species, cover)

    # call the species_list_fn function
    species = species_list_fn(star, 'pg')
    print('pg species: ', species)
    # call the cover_list function
    cover = cover_list_fn(star, 'pg')
    print('pg cover: ', cover)

    if len(secondary_cover_list3p) > 0:
        species.extend(secondary_species_list3p)
        cover.extend(secondary_cover_list3p)

    # call the cover_vegetation_extraction_fn to control the sorting and splitting of vegetation lists.
    primary_cover_list_pg, secondary_cover_list_pg, final_species_list_pg, secondary_species_list_pg = \
        cover_vegetation_extraction_fn(veg_series, species, cover)
    print('pg: ', primary_cover_list_pg, secondary_cover_list_pg, final_species_list_pg, secondary_species_list_pg)
    # call the sum_list_fn function
    sum_total_p = sum_list_fn(primary_cover_list3p + primary_cover_list_pg)
    print('pg sum: ', sum_total_p)

    ''' --------------------------- Annual Grass -------------------------'''
    # call the species_list_fn function
    species = species_list_fn(star, 'ag')
    print('ag: ', species)
    # call the cover_list function
    cover = cover_list_fn(star, 'ag')
    print('ag cover: ', cover)

    # call the cover_vegetation_extraction_fn to control the sorting and splitting of vegetation lists.
    primary_cover_list_ag, secondary_cover_list_ag, final_species_list_ag, secondary_species_list_ag = \
        cover_vegetation_extraction_fn(veg_series, species, cover)
    print('ag:', primary_cover_list_ag, secondary_cover_list_ag, final_species_list_ag, secondary_species_list_ag)

    # call the sum_list_fn function
    sum_total_ag = sum_list_fn(primary_cover_list_ag)
    print('ag sum: ', sum_total_ag)

    ''' ------------------------ Perennial Forb -----------------------------'''
    # call the species_list_fn function
    species = species_list_fn(star, 'pf')
    # call the cover_list function
    cover = cover_list_fn(star, 'pf')

    # call the cover_vegetation_extraction_fn to control the sorting and splitting of vegetation lists.
    primary_cover_list_pf, secondary_cover_list_pf, final_species_list_pf, secondary_species_list_pf = \
        cover_vegetation_extraction_fn(veg_series, species, cover)

    # call the sum_list_fn function
    sum_total_pf = sum_list_fn(primary_cover_list_pf)

    '''---------------------------- Annual forb -------------------------------'''
    # call the species_list_fn function
    species = species_list_fn(star, 'af')
    # call the cover_list function
    cover = cover_list_fn(star, 'af')

    # call the cover_vegetation_extraction_fn to control the sorting and splitting of vegetation lists.
    primary_cover_list_af, secondary_cover_list_af, final_species_list_af, secondary_species_list_af = \
        cover_vegetation_extraction_fn(veg_series, species, cover)

    # call the sum_list_fn function
    sum_total_af = sum_list_fn(primary_cover_list_af)

    total_cover_list = [sum_total_p, sum_total_ag, sum_total_pf, sum_total_af, 0]
    estimates_veg_list = [final_species_list3p, primary_cover_list3p, final_species_list_pg, primary_cover_list_pg,
                          final_species_list_ag, primary_cover_list_ag,
                          final_species_list_pf, primary_cover_list_pf, final_species_list_af, primary_cover_list_af,
                          total_cover_list]

    print('step_8_2_site_star_data_extraction.py COMPLETE.')

    return property_name, estab_vert_list13, visit_vert_list1, ground_vert_list12345, estimates_hor_list12345, \
           estimates_veg_list


if __name__ == '__main__':
    main_routine()
