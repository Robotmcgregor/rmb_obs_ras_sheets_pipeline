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
    """ Extract the erosion type and severity information using a dictionary to replace erosion values.

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


def condition_fn(row, string_clean_capital_fn):
    """ Extract the condition score and visit note information.

    :param row: pandas dataframe row value object.
    :param string_clean_capital_fn: function to remove whitespaces and clean strings.
    :return: output_list: list object containing three variables: condition, cond_note, dev_note.
    """

    condition = string_clean_capital_fn(
        str(row['CONDITION:CONDITION_SCORE']))
    cond_note = string_clean_capital_fn(str(row['CONDITION:VISIT_NOTES']))
    dev_note = string_clean_capital_fn(str(row['CONDITION:DEV_NOTE']))

    condition_list = [condition, cond_note, dev_note]
    return condition_list


def main_routine(clean_list, row, string_clean_capital_fn):
    """ Extract and process the disturbance variables from the raw RMB ras odk form result csv.

    :param clean_list: ordered list object that contains the processed integrated odk form result
    variables.
    :param row: pandas dataframe row value object.
    :param string_clean_capital_fn: function that processes string objects (dirty_string -> clean_string)
    :return: clean_list: ordered list object that contains the processed integrated odk form result
    variables variables processed within this script extend the list.
    """

    # call the erosion_fn function to extract the erosion type and severity information using a dictionary
    # to replace erosion values.
    erosion_list, erosion_comment = erosion_fn(row, string_clean_capital_fn)

    # call the condition_fn function to extract the condition score and visit note information.
    condition_list = condition_fn(row, string_clean_capital_fn)

    # extend clean_list with results
    clean_list.extend(erosion_list)
    clean_list.extend([erosion_comment])
    clean_list.extend(condition_list)

    return clean_list


if __name__ == '__main__':
    main_routine()
