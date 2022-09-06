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


def erosion_fn(row, string_clean_capital_fn):
    """ Extract the erosion information using an erosion dictionary and concatenate variables to create an erosion comment.

    :param row: pandas dataframe row value object.
    :param string_clean_capital_fn: function to remove whitespaces and clean strings.
    :return: establish_list: list object containing three variables: paddock, desc and reason.
    """

    erosion_values = {'active': 'Active', 'stable': 'Stable (historical)', 'nan': 'BLANK',
                      'sev_absent': 'Absent', 'natural': 'Natural', 'slight': 'Slight',
                      'moderate': 'Moderate', 'severe': 'Severe'}

    erosion_list = ['SCALDING', 'WINDSHEETING', 'WATERSHEETING', 'RILLING', 'GULLYING']

    output_list = []

    for i in erosion_list:
        sev = str(row['DISTURBANCE_EROSION:GROUP_SCALDING:' + i + '_SEVERITY'])
        stab = str(row['DISTURBANCE_EROSION:GROUP_SCALDING:' + i + '_STABILITY'])

        severity = (erosion_values[sev])
        stability = (erosion_values[stab])
        output_list.append(severity)
        output_list.append(stability)

    erosion_comment = string_clean_capital_fn(str(row['DISTURBANCE_EROSION:GROUP_SCALDING:EROSION_COMMENTS']))

    return output_list, erosion_comment


def cattle_pads_fn(row, string_clean_capital_fn):
    """ Extract the cattle pad information.

    :param row: pandas dataframe row value object.
    :param string_clean_capital_fn: function to remove whitespaces and clean strings.
    :return: cattle_list: list object containing two variables: cattle_pad, cattle_tramp.
    """

    cattle_pad = string_clean_capital_fn(str(row['CATTLE:CATTLE_PAD']))
    cattle_tramp = string_clean_capital_fn(str(row['CATTLE:CATTLE_TRAMP']))

    cattle_list = [cattle_pad, cattle_tramp]
    return cattle_list


def pasture_fn(row, string_clean_capital_fn):
    """ Extract the pasture information, using a pasture dictionary and concatenate variables to create a pasture comment.

    :param row: pandas dataframe row value object.
    :param string_clean_capital_fn: function to remove whitespaces and clean strings.
    :return: output_list: list object containing six variables: greenness, abundance and pasture utilisation
    information.
    """

    value_dict = {'green': 'GREEN', 'drying_off_greening_up': 'DRYING OFF/GREENING UP', 'dry': 'DRY',
                  'abundant': 'Abundant', 'moderately_abundant': 'Moderately abundant', 'sparse': 'Sparse',
                  'nan': 'BLANK',
                  'no_grazing': 'NO GRAZING', '<10%': '<10%', '11_25%': '11%-25%', '26_50%': '26%-50%',
                  '51_75%': '51%-75%', '76_90%': '76%-90%', '>90%': '>90%'}

    pasture_list = ['GREENESS', 'ABUNDANCE', 'PAST_UTIL']
    value_list = ['GREENESS', 'ABUNDANCE', 'PAST_UTIL_PROP']
    output_list = []

    # zip dependent lists and for loop through.
    for i, n in zip(pasture_list, value_list):
        value = str(row['GROUP_CONTITION:' + n])
        # extract from dictionary
        classification = (value_dict[value])
        comment = string_clean_capital_fn(str(row['GROUP_CONTITION:' + i + '_COMMENT']))
        output_list.append(classification)  # extend([classification])
        output_list.append(comment)  # extend([comment])

        # todo delete extend comments

    return output_list


def capitalise_fn(free_text):
    """ Clean a sentence string and produce a sentence structured string object.

    :param free_text: string object created from free text 255 characters.
    :return clean_text: processed string object.
    """
    sent_list = free_text.split('. ')
    clean_text = (". ".join((i.capitalize() for i in sent_list)))

    return clean_text


def condition_fn(row, string_clean_capital_fn):
    """ Extract the condition score information and clean the notes sentence variable.

    :param row: pandas dataframe row value object.
    :param string_clean_capital_fn: function to remove whitespaces and clean strings.
    :return: output_list: list object containing three variables: condition, cond_note, dev_note.
    """

    condition = string_clean_capital_fn(
        str(row['CONDITION:CONDITION_SCORE']))
    cond_note = string_clean_capital_fn(str(row['CONDITION:VISIT_NOTES']))
    cond_note2 = capitalise_fn(cond_note)
    # clean the string sentence.
    '. '.join(x.strip().capitalize() for x in cond_note.split('.'))  # todo use this for all free text
    dev_note = string_clean_capital_fn(str(row['CONDITION:DEV_NOTE']))

    condition_list = [condition, cond_note2, dev_note]

    return condition_list


def main_routine(clean_list, row, string_clean_capital_fn):
    """ Extract and process the disturbance variables from the raw RMB integrated odk form result csv.

    :param clean_list: ordered list object that contains the processed integrated odk form result
    variables.
    :param row: pandas dataframe row value object.
    :param string_clean_capital_fn: function that processes string objects (dirty_string -> clean_string)
    :return: clean_list: ordered list object that contains the processed integrated odk form result
    variables variables processed within this script extend the list.
    """

    # call the erosion_fn function to extract the erosion information.
    erosion_list, erosion_comment = erosion_fn(row, string_clean_capital_fn)

    # call the cattle_pads_fn function to extract the cattle pad information.
    cattle_list = cattle_pads_fn(row, string_clean_capital_fn)

    # call the pasture_fn function to extract the pasture information.
    pasture_list = pasture_fn(row, string_clean_capital_fn)

    # call the condition_fn function
    condition_list = condition_fn(row, string_clean_capital_fn)

    # extend clean list with results
    clean_list.extend(erosion_list)
    clean_list.extend([erosion_comment])
    clean_list.extend(cattle_list)
    clean_list.extend(pasture_list)
    clean_list.extend(condition_list)

    return clean_list


if __name__ == '__main__':
    main_routine()
