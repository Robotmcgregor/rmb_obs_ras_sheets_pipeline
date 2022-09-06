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
import numpy as np

warnings.filterwarnings("ignore")


def extract_botanical_fn(row, string_clean_capital_fn, n):
    """ Extract woody thickening information (trees and shrubs) for the transect species lists within each site.
    The function also identifies any species listed as other and replaces it with the other information
    (i.e. manually entered botanical name)

     :param row: pandas dataframe row value object.
     :param string_clean_capital_fn: function (previously defined) to clean string objects returning capitalized
     string format.
     :param n: string object passed into the function (i.e str(TS), str(SB)).
     :return list_botanical: list object containing up to ten botanical names (other replaced)- ODK form inputs.
     within each site.
     """

    list_botanical = []

    for i in range(10):

        botanical = string_clean_capital_fn(str(row[n + '_SP:' + n + str(i + 1)]))
        if botanical == 'Other1':
            final_botanical = string_clean_capital_fn(str(row[n + '_SP:' + n + '_OTHER1']))
        elif botanical == 'Other2':
            final_botanical = string_clean_capital_fn(str(row[n + '_SP:' + n + '_OTHER2']))
        elif botanical == 'Other3':
            final_botanical = string_clean_capital_fn(str(row[n + '_SP:' + n + '_OTHER3']))
        elif botanical == 'Other4':
            final_botanical = string_clean_capital_fn(str(row[n + '_SP:' + n + '_OTHER4']))
        elif botanical == 'Other5':
            final_botanical = string_clean_capital_fn(str(row[n + '_SP:' + n + '_OTHER5']))
        else:
            final_botanical = botanical
        list_botanical.append(final_botanical)

    return list_botanical


def species_extraction_fn(row, string_clean_capital_fn, n):
    """ Loop through feature vegetation feature variables and extract the botanical names and cover fraction values
    (10 values per vegetation type).

    :param string_clean_capital_fn: function used to clean sing objects.
    :param row: pandas dataframe row value object.
    :param n: string object containing the species form code(i.e. 'PG' or 'AG').
    :return botanical_name_list: list object containing 10 botanical names variables.
    :return final_cover_list: list object containing 10 float variables (None -> 9999.0).
    """

    botanical_name_list = []
    cover_list = []
    # Extract botanical inputs and replace nn end varibles with str(Nan) and append them to a list.
    for i in range(10):
        value = string_clean_capital_fn(str(row[n + '_SP:' + n + str(i + 1) + '_NAME']))
        if value == "Pg end" or value == "Ag end" or value == "F end":
            botanical_name = "Nan"
        else:
            botanical_name = value
        botanical_name_list.append(botanical_name)

        # Extract species cover values and append to a list.
        cover = float(row[n + '_COVER:' + n + '_SP' + str(i + 1) + '_COVER'])
        cover_list.append(cover)

    # convert Nan values to 9999.0 in the species cover list.
    final_cover_list = [9999.0 if x != x else x for x in cover_list]

    return botanical_name_list, final_cover_list


def botanical_extraction_fn(string_clean_capitalize_fn, match_list, input_name_list, input_cover_list):
    """ Loop through two dependent lists - botanical name list and species cover list and match species names against
    a list
    (i.e. 3P grass and Annual Forbs).
    Matching botanical species list elements and their respective species cover are appended to two matching lists.
    Whereas, non-matching botanical species list elements and their respective species cover are appended to two
    non-matching lists.

    :param string_clean_capitalize_fn: remove whitespaces and clean strings (dirty_string -> clean_string)
    :param match_list: list object of botanical names used to match against input list elements (boanical name list).
    (i.e. input_name_list).
    :param input_name_list: list object containing n botanical names variables (species_extraction_fn)
    :param input_cover_list: list object containing n float variables (None -> 9999.0) (species_extraction_fn).
    :return list_botanical_match: list object of the same size as the input list (n).
    match (variable -> variable) or no match (variable -> str(Nan)).
    :return list_botanical_no_match: list object of the same size as the input list (n).
    match (variable -> variable) or no match (variable -> str(Nan)).
    :return list_cover_match: list object of the same size as the input list (n).
    match (variable -> variable) or no match (variable -> float(9999.0).
    :return list_cover_no_match: list object of the same size as the input list (n).
    match (variable -> variable) or no match (variable -> float(9999.0).
    """

    list_botanical_match = []
    list_botanical_no_match = []
    list_cover_match = []
    list_cover_no_match = []

    # Loop through two dependant lists (species name and species cover).
    for name, cover in zip(input_name_list, input_cover_list):

        # clean the species name
        clean_name = string_clean_capitalize_fn(name)

        if any(clean_name in x for x in match_list):
            list_botanical_match.append(clean_name)
            list_cover_match.append(cover)
            list_botanical_no_match.append('Nan')
            list_cover_no_match.append(9999.0)

        else:
            list_botanical_no_match.append(clean_name)
            list_cover_no_match.append(cover)
            list_botanical_match.append('Nan')
            list_cover_match.append(9999.0)

    return list_botanical_match, list_botanical_no_match, list_cover_match, list_cover_no_match


def sort_two_lists_fn(species_list, cover_list):
    """ Sort two dependent lists (species list and species cover) in descending order based on the cover values after
    the 9999.0 list elements have been converted to np.nan.

    :param species_list: list object containing 10 botanical names or "Nan" values.
    :param cover_list: list object containing 10 species cover values or 9999.0 - values are dependent with species list
    elements.
    :return list_cover_sorted_nan: list object (species_list_fn) that has been sorted in ascending order based on count
    values.
    :return list_species_sorted: list object (cover_list) that has been sorted in ascending order (9999.0 -> np.nan).
    """

    # zip two dependent lists soreted by cover values.
    tuple_cover_sorted, tuple_species_sorted = zip(*sorted(zip(cover_list, species_list)))

    # convert tuple to list
    list_cover_sorted = list(tuple_cover_sorted)
    list_species_sorted = list(tuple_species_sorted)

    # convert 9999.0 to np.nan values
    list_cover_sorted_nan = [np.nan if i == 9999.0 else i for i in list_cover_sorted]

    return list_cover_sorted_nan, list_species_sorted


def coerce_to_zero(input_list):
    """ Loop through a list and convert Nan values to int(0).

    :param input_list: list object containing numeric values.
    :return output_list: processed list with null values converted to int(0).
    """

    input_list = [0 if x != x else x for x in input_list]

    return input_list


def main_routine(clean_list, row, string_clean_capital_fn, veg_list_excel):
    """ Extract and clean botanical values and botanical count values from the star transect odk raw output.

    :param veg_list_excel: string object containing the path to an excel document containing the botanical and
    common names of vegetation species.
    :param string_clean_capital_fn: function created step2_1_star_transect_processing_workflow.py - used to
    clean and return capitalize case string variables.
    :param clean_list: list object created under step2_1_star_transect_processing_workflow.py - new variables
    are extended or appended to the end.
    :param row: pandas dataframe row value object.
    :return clean_list: list object with additional variables extended or appended to the end.
    :return veg_list_excel: list object containing extended variable to separate forms into annual and perennial.
    """

    # ------------------------------------------ Identify 3P grass from perennial --------------------------------------
    # read in 3p grass species excel
    # import the 3p list from the final species excel replace all nan values with 'BLANK'
    ppp = pd.read_excel(veg_list_excel, sheet_name='ppp_list').fillna('BLANK').replace('Nan', 'BLANK')

    # convert column 4 of the worksheet to a list
    ppp_list = ppp['PPP_list'].tolist()

    # remove all 'BLANK values from list
    cleaned3p_list = [x for x in ppp_list if str(x) != 'BLANK']

    # add white grass to the 3p list if selected by the field officer.
    white_grass = str(row['TO_DO_LIST:PER_3P'])
    if white_grass == 'ppp':
        cleaned3p_list.append('Sehima nervosum')

    # --------------------------------------------- Annual forb list ---------------------------------------------------
    # read in and annual forb species excel
    # import the annual forb list from the final species excel replace all nan values with 'BLANK'
    forb = pd.read_excel(veg_list_excel, sheet_name='annual_forb_list').fillna('BLANK').replace('Nan',
                                                                                                'BLANK')
    # convert to list
    af_list = forb['Botanical_Annual_Forb'].tolist()

    # remove all 'BLANK values from list
    cleaned_af_list = [x for x in af_list if str(x) != 'BLANK']

    # ------------------------------ Perennial and 3p grass processing and sorting -------------------------------------

    # call the species_extraction_fn to extract 10 species names and cover values.
    botanical_name_list, cover_list = species_extraction_fn(row, string_clean_capital_fn, 'PG')

    # call the botanical_extraction_fn function sperate perennial grass list and cover into 3p grass and cover
    # and perennial and cover lists.
    list_botanical3p, list_botanical_pg, list3p_cover, list_pg_cover = botanical_extraction_fn(
        string_clean_capital_fn, cleaned3p_list, botanical_name_list, cover_list)

    # call the sort_two_lists_fn function to sort dependent lists in species cover decending order.
    list3p_cover_sorted_nan, list3p_species_sorted = sort_two_lists_fn(list_botanical3p, list3p_cover)
    list_pg_cover_sorted_nan, list_pg_species_sorted = sort_two_lists_fn(list_botanical_pg, list_pg_cover)

    # append all values to the cleaned values to the list (clean_list)
    clean_list.extend(list3p_species_sorted)
    clean_list.extend(list3p_cover_sorted_nan)
    clean_list.extend(list_pg_species_sorted)
    clean_list.extend(list_pg_cover_sorted_nan)

    # ------------------------------------------- Annual grass processing ----------------------------------------------

    # call the species_extraction_fn to extract 10 species names and cover values.
    botanical_name_list, cover_list = species_extraction_fn(row, string_clean_capital_fn, 'AG')
    list_cover_sorted_nan = [np.nan if i == 9999.0 else i for i in cover_list]

    # append all values to the cleaned values to the list (clean_list)
    clean_list.extend(botanical_name_list)
    clean_list.extend(list_cover_sorted_nan)

    # --------------------------------------- Perennial and annual Forb processing -------------------------------------

    # call the species_extraction_fn to extract 10 species names and cover values.
    botanical_name_list, cover_list = species_extraction_fn(row, string_clean_capital_fn, 'F')

    # call the botanical_extraction_fn function sperate perennial grass list and cover into annual forb and cover
    # and perennial forb and cover lists.
    list_botanical_af, list_botanical_pf, list_af_cover, list_pf_cover = botanical_extraction_fn(
        string_clean_capital_fn, cleaned_af_list, botanical_name_list, cover_list)

    # call the sort_two_lists_fn function to sort dependent lists in species cover decending order.
    list_af_cover_sorted_nan, list_af_species_sorted = sort_two_lists_fn(list_botanical_af, list_af_cover)
    list_pf_cover_sorted_nan, list_pf_species_sorted = sort_two_lists_fn(list_botanical_pf, list_pf_cover)

    # append all values to the cleaned values to the list (clean_list)
    clean_list.extend(list_pf_species_sorted)
    clean_list.extend(list_pf_cover_sorted_nan)
    clean_list.extend(list_af_species_sorted)
    clean_list.extend(list_af_cover_sorted_nan)

    # ------------------------------------------ Amend Forb field and adjusted values ----------------------------------

    # Annual and perennial forbs are considered separate unlike perennial and 3P grasses, as such the total field and
    # adjusted values need to be overridden based on annual nd perennial forb assignments.
    veg_list = []

    represent_veg = str(
        row['SITE_VEG_FRACTIONS:VEG_COVER_ADJUST'])

    # Varify if any of the forb species identified were annual forbs are detected.
    if list_af_cover_sorted_nan.count(np.nan) < 10:

        while np.nan in list_af_cover_sorted_nan:
            list_af_cover_sorted_nan.remove(np.nan)

        total = float(0.0)

        # Iterate each element in list and add them in variable total
        for ele in range(0, len(list_af_cover_sorted_nan)):
            total = total + list_af_cover_sorted_nan[ele]

        represent_veg = str(row['SITE_VEG_FRACTIONS:VEG_COVER_ADJUST'])

        rep_veg = 'amended - annual forb'

        adj_perennial = float(row['PG_SUM_PROP'])
        adj_annual = float(row['AG_SUM_PROP'])
        adj_p_forb = (float(row['F_SUM_PROP']) - float(total))
        field_a_forb = float(0.0)
        adj_a_forb = float(total)
        final_a_forb = float(total)
        field_veg_total = round(float(row['SITE_VEG_FRACTIONS:TOTAL_VEG_FRACTION']), 0)
        adj_veg_total = round(float(row['SITE_COVER_FRACTIONS:TOTAL_COVER']), 0)
        final_veg_total = round(float(row['SITE_COVER_FRACTIONS:TOTAL_COVER']), 0)

        veg_list = [rep_veg, adj_perennial, adj_annual, adj_p_forb, field_a_forb, adj_a_forb,
                    final_a_forb, field_veg_total, adj_veg_total, final_veg_total]

    elif represent_veg == 'representative':

        rep_veg = represent_veg
        adj_perennial = float(row['SITE_VEG_FRACTIONS:PG_TOTAL_ADJUSTED'])
        adj_annual = float(row['SITE_VEG_FRACTIONS:AG_TOTAL_ADJUSTED'])
        adj_p_forb = float(row['SITE_VEG_FRACTIONS:F_TOTAL_ADJUSTED'])
        field_a_forb = float(0.0)
        adj_a_forb = float(0.0)
        final_a_forb = float(0.0)
        field_veg_total = round(float(row['SITE_VEG_FRACTIONS:TOTAL_VEG_FRACTION']), 0)
        adj_veg_total = round(float(row['SITE_VEG_FRACTIONS:VEG_ADJ']), 0)
        final_veg_total = round(float(row['SITE_COVER_FRACTIONS:TOTAL_COVER']), 0)

        veg_list = [rep_veg, adj_perennial, adj_annual, adj_p_forb, field_a_forb, adj_a_forb,
                    final_a_forb, field_veg_total, adj_veg_total, final_veg_total]

    else:

        total = float(0.0)
        rep_veg = represent_veg

        adj_perennial = float(row['SITE_VEG_FRACTIONS:PG_TOTAL_ADJUSTED'])
        adj_annual = float(row['SITE_VEG_FRACTIONS:AG_TOTAL_ADJUSTED'])
        adj_p_forb = float(row['SITE_VEG_FRACTIONS:F_TOTAL_ADJUSTED']) - float(total)
        field_a_forb = float(0.0)
        adj_a_forb = float(0.0)
        final_a_forb = float(0.0)
        field_veg_total = round(float(row['SITE_VEG_FRACTIONS:TOTAL_VEG_FRACTION']), 0)
        adj_veg_total = round(float(row['SITE_VEG_FRACTIONS:VEG_ADJ']), 0)
        final_veg_total = round(float(row['SITE_VEG_FRACTIONS:VEG_ADJ']), 0)

        veg_list = [rep_veg, adj_perennial, adj_annual, adj_p_forb, field_a_forb, adj_a_forb,
                    final_a_forb, field_veg_total, adj_veg_total, final_veg_total]

    cleaned_veg_list = coerce_to_zero(veg_list)

    return clean_list, cleaned_veg_list


if __name__ == '__main__':
    main_routine()
