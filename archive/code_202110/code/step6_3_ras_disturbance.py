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


def disturb_comment(row, string_clean_capital_fn):
    """ Extract the cyclone and dieback comments.

    :param row: pandas dataframe row value object.
    :param string_clean_capital_fn: function to remove whitespaces and clean strings.
    :return: dist_comment_list: list object containing two string variables:
    cyclone and dieback.
    """

    cyc_comment = string_clean_capital_fn(str(row['DIST_COMMENTS:CYCLONE_COMMENT']))
    dieback_comment = string_clean_capital_fn(str(row['DIST_COMMENTS:DIEBACK_COMMENT']))

    dist_comment_list = [cyc_comment, dieback_comment]

    return dist_comment_list


def pres_abs_disturbance_fn(dist_class_list):
    """ Assign present or absent to the respective disturbance features.

    :param dist_class_list: ordered list object that was matched from ordered_list variables within the
    photo_list of three variables, created by the clearing_cyclone_dieback_fn function.
    :return: dist_pa_list ordered list object derived from dist_class_object with matched variables
    (match -> str(Present)),  (no match - str(Absent)).
    """

    dist_pa_list = []

    for i in dist_class_list:
        if i != 'nan':
            dist = 'Present'
        else:
            dist = 'Absent'
        dist_pa_list.append(dist)

    return dist_pa_list


def feral_extraction_fn(row, string_clean_capital_fn):
    """ Extract the feral animal and feral evidence information.

    :param row: pandas dataframe row value object.
    :param string_clean_capital_fn: function to remove whitespaces and clean strings.
    :return: feral_list: list object storing feral animal type variables.
    :return: feral_evid_list: list object storing feral animal evidence variables.
    """

    feral_list = []
    feral_evid_list = []
    for i in range(6):
        str(i + 1)
        feral = string_clean_capital_fn(str(row['GROUP_FERAL:FERAL' + str(i + 1)]))
        feral_list.append(feral)
        feral_evid = string_clean_capital_fn(str(row['GROUP_FERAL:FERAL' + str(i + 1) + '_EVID']))
        feral_evid_list.append(feral_evid)

    return feral_list, feral_evid_list


def feral_other_extraction_fn(row, string_clean_capital_fn):
    """ Extract the other feral animal and other feral evidence information.

    :param row: pandas dataframe row value object.
    :param string_clean_capital_fn: function to remove whitespaces and clean strings.
    :return feral_other: feral_list: list object storing feral animal type variables not included in odk
    dropdown.
    :return feral_evid_other: list object storing feral animal evidence variables not included in odk
    dropdown.
    """

    # Extract other feral variables.
    feral_other = string_clean_capital_fn(str(row['GROUP_FERAL:FERAL_OTHER']))
    # clean string
    feral_other = string_clean_capital_fn(feral_other)
    feral_evid_other = string_clean_capital_fn(str(row['GROUP_FERAL:FERAL_OTHER_EVID']))

    return feral_other, feral_evid_other


def get_element_number_fn(a_list, search_term):
    """ Return the index value of a matching list variable, function utilised within evidence_comment_fn function.

    :param a_list: list object to be searched through for a matching variable (search_term).
    :param search_term: string object variable .
    :return: index: list index integer object when a match has been located.
    :return: 'not match: string object in match not located.
    """

    for index, value in enumerate(a_list):
        if search_term in value:
            return index
    return 'not match'


def sort_feral_list_fn(feral_list, required_list, final_list):
    """ Sort the feral animals recorded into the required order for the ras sheet.

    :param feral_list: list object storing feral animal type variables created in feral_extraction_fn function.
    :param required_list: ordered list object created in main_routine: seven feral animal categories as sting
    variables.
    :param final_list: list object created in main_routine: seven list items of np.nan variables.
    :return: final_list ordered list object where matched variables replace (np.nan -> str(variable))
     no match (np.nan -> str(nan)).
     """
    n = 0
    # loop through required list
    for i in required_list:
        # search for a required_list variable in the feral_list
        if i in feral_list:
            # append value to final_list in the ordered position
            final_list[n] = i

        else:
            # append str(nan) to final_list in the ordered position
            final_list[n] = 'nan'  # string ensures looping capability if no ferals recorded

        n += 1

    return final_list


def evidence_comment_fn(evid_list, get_element_number_fn, required_list, sorted_list, final_list, feral_list):
    """ Create a list of animals and evidence observed for the ras sheet.

    :param evid_list: list object storing feral animal evidence variables (feral_evid_list) derived under the
     feral_extraction_fn function.
    :param get_element_number_fn: function that return the index value of a matching list variable.
    :param required_list: ordered list object created in main_routine: seven feral animal categories as sting
            variables.
    :param sorted_list: ordered list object where matched variables replace (np.nan -> str(variable))
             no match (np.nan -> str(nan)). derived under sort_feral_list_fn function (final_list).
    :param final_list: list object created in main_routine: seven list items of np.nan variables.
    :param feral_list: list object storing feral animal type variables derived from feral_extraction_fn function
    (excludes feral other variables)
    :return: feral_evid_comment_list: list object with string variables created by concatenating feral category
    and feral evidence variables (feral categories : evidence).
    """

    n = 0
    # create an empty list for feral comments
    feral_evid_comment_list = []

    for i in required_list:
        if i in sorted_list:
            # append value to final_list in the ordered position
            final_list[n] = i

            list_index = get_element_number_fn(feral_list, i)
            evidence = evid_list[list_index]
            feral_comment = str(i + ': ' + evidence)
            feral_evid_comment_list.append(feral_comment)
        else:
            pass

        n += 1
    return feral_evid_comment_list


def feral_other_fn(feral_evid_comment_list, sorted_list, feral_other, feral_evid_other):
    """ Append the other feral animal's records to the ends of the sorted_list, and feral_evid_comment_list.

    :param feral_evid_comment_list: list object with string variables created by concatenating feral category
    and feral evidence variables derived under evidence_comment_fn function.
    :param sorted_list: ordered list object where matched variables replace (np.nan -> str(variable))
    no match (np.nan -> str(nan)). derived under sort_feral_list_fn function (final_list).
    :param feral_other: feral_list: list object storing feral animal type variables not included in odk
    dropdown.
    :param feral_evid_other: list object storing feral animal evidence variables not included in odk
    dropdown.
    :return feral_evid_comment_list: list object with string variables created by concatenating feral category
    and feral evidence variables (feral categories : evidence) that has
    been extended with the feral other variable that has been extended with the feral other variable.
    :return: sorted_list: ordered list object where matched variables replace (np.nan -> str(variable))
    no match (np.nan -> str(nan)). derived under sort_feral_list_fn function (final_list) that has
    been extended with the feral other variable.
    """

    if str.lower(feral_other) != 'nan':
        # concat a comment string
        feral_evid_comment = str(feral_other + ': ' + feral_evid_other)
        # exted the string on to the end of the feral_evid_comment_list
        feral_evid_comment_list.extend([feral_evid_comment])
    else:
        feral_other = 'nan'

    # extend the feral ordered list.
    sorted_list.extend([feral_other])

    return feral_evid_comment_list, sorted_list


def fire_fn(row):
    """ Extract the fire information and amend string objects using relevant dictionaries.
    :param row: pandas dataframe row value object.
    :return: fire_list: list object containing four processed string variables:
    north_ff, north_fi, south_ff, south_fi.
    """

    north_ff_values = {'NFF_absent': 'Absent', 'since_last_growth_event': 'Since last growth event',
                       'before_last_growth_event': 'Before last growth event', 'nan': 'BLANK'}

    north_fi_values = {'NFI_absent': 'Absent', 'low_intensity_cool_fire': 'Low intensity/cool fire',
                       'low_moderate': 'Low/moderate', 'moderate': 'Moderate',
                       'moderate_high': 'Moderate/high', 'high': 'High', 'nan': 'BLANK'}

    south_ff_values = {'SFF_absent': 'Absent', '<1': '<12 months', '1_2': '1-2 years', '2_10': '2-10 years',
                       '>10': '>10 years', 'nan': 'BLANK'}

    south_fi_values = {'SFI_absent': 'Absent', 'cool': 'Cool fire', 'hot': 'Hot fire', 'nan': 'BLANK'}

    value = str(row['FIRE:NORTH_FF'])
    north_ff = (north_ff_values[value])

    value = str(row['FIRE:NORTH_FI'])
    north_fi = (north_fi_values[value])

    value = str(row['FIRE:SOUTH_FF'])
    south_ff = (south_ff_values[value])

    value = str(row['FIRE:SOUTH_FI'])
    south_fi = (south_fi_values[value])

    fire_list = [north_ff, north_fi, south_ff, south_fi]
    return fire_list


def weed_fn(row, string_clean_capital_fn, n):
    """ Extract the weed name, density size and comment information.

    :param row: pandas dataframe row value object.
    :param string_clean_capital_fn: function to remove whitespaces and clean strings.
    :param n: string object: passed when calling the function (1, 2 or 3)
    :return: weed_list: list object containing three string variables:
    weed, weed_size, weed_den, weed_com.
    """

    weed = str(row['WEEDS:GROUP_WEED' + n + ':WEED' + n])

    if weed == 'other_weed':
        weed = weed.replace('other_weed', str(row['WEEDS:GROUP_WEED' + n + ':WEED' + n + '_OTHER']))
    weed = string_clean_capital_fn(weed)

    weed_size = str(row['WEEDS:GROUP_WEED' + n + ':GROUP_WEEDS' + n + '_SIZE:SPECIES_SIZE' + n])
    weed_den = str(row['WEEDS:GROUP_WEED' + n + ':GROUP_WEEDS' + n + '_SIZE:SPECIES_DENSITY' + n])
    weed_com = str(row['WEEDS:GROUP_WEED' + n + ':GROUP_WEEDS' + n + '_SIZE:WEED' + n + '_COMMENT'])
    # clean weed comment
    weed_com = string_clean_capital_fn(weed_com)

    weed_list = [weed, weed_size, weed_den, weed_com]
    return weed_list


def main_routine(clean_list, row, string_clean_capital_fn):
    """ Extract and process the disturbance variables from the raw RMB ras odk form result csv.

    :param clean_list: ordered list object that contains the processed integrated odk form result
    variables.
    :param row: pandas dataframe row value object.
    :param string_clean_capital_fn: function that processes string objects (dirty_string -> clean_string)
    :return: clean_list: ordered list object that contains the processed integrated odk form result
    variables variables processed within this script extend the list.
    """

    # -------------------------------------------- Feral animals -------------------------------------------------------

    # call the feral_extraction_fn function to extract the feral animal and feral evidence information.
    feral_list, evid_list = feral_extraction_fn(row, string_clean_capital_fn)

    # call the feral_other_extraction_fn function to extract the other feral animal and other feral evidence
    # information.
    feral_other, feral_evid_other = feral_other_extraction_fn(row, string_clean_capital_fn)

    final_list = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
    required_list = ['Camel', 'Rabbit', 'Donkey', 'Horse', 'Pig', 'Buffalo', 'Natherb']

    # call the sort_feral_list_fn function to sort the feral animals recorded into the required order for the RAS
    # sheet using the previously defined lists.
    sorted_list = sort_feral_list_fn(feral_list, required_list, final_list)

    # call the evidence_comment_fn function to create a list of animals and evidence observed for the RAS sheet
    feral_evid_comment_list = evidence_comment_fn(evid_list, get_element_number_fn, required_list, sorted_list,
                                                  final_list, feral_list)

    # call the feral_other_fn function to append the other feral animal’s records to the ends of the sorted_list, 
    # and feral_evid_comment_list.
    feral_evid_comment_list, sorted_list = feral_other_fn(feral_evid_comment_list, sorted_list, feral_other,
                                                          feral_evid_other)

    # call the pres_abs_disturbance_fn function to assign present or absent to the respective disturbance features.
    sorted_feral_pa_list = pres_abs_disturbance_fn(sorted_list)

    # ---------------------------------------------------- Fire --------------------------------------------------------
    # call the fire_fn function to extract the fire information and amend string objects using relevant dictionaries.
    fire_list = fire_fn(row)

    # ----------------------------------------------------- Weeds ------------------------------------------------------

    # call the weed_fn function to extract the weed name, density size and comment information.
    weed_list1 = weed_fn(row, string_clean_capital_fn, '1')
    weed_list2 = weed_fn(row, string_clean_capital_fn, '2')
    weed_list3 = weed_fn(row, string_clean_capital_fn, '3')

    # ----------------------------------------------- Extend list ------------------------------------------------------
    # Extend add list to the end of clean_list
    clean_list.extend(sorted_feral_pa_list)
    # Extend add list to the end of clean_list
    final_feral_comment = ', '.join(feral_evid_comment_list)
    clean_list.extend([final_feral_comment])
    clean_list.extend(fire_list)
    clean_list.extend(weed_list1)
    clean_list.extend(weed_list2)
    clean_list.extend(weed_list3)

    return clean_list


if __name__ == '__main__':
    main_routine()
