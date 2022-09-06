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


def extract_botanical_fn(row, string_clean_capital_fn, n):
    """ Extract woody thickening information for the five transects within each site.

             :param row: pandas dataframe row value object.
             :param string_clean_capital_fn: function to clean string objects returning capitalized format.
             :param n: string object passed into the function (i.e str(TS), str(SB)).
             :return list_botanical: list object containing the five botanical names for the input species form.
             within each site."""

    list_botanical = []

    for i in range(5):

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


def main_routine(clean_list, row, string_clean_capital_fn):
    """ Extract the basal botanical names from the raw RMB ODK basal sweep results.

            :param clean_list: list object containing processed variables
            - new variables are extended to the end of the list.
            :param row: pandas dataframe row value object.
            :param string_clean_capital_fn: function to clean string objects returning capitalized format.
            :return clean_list: list object containing processed variables
            - new variables are extended to the end of the list."""

    # Call the extract_botanical_fn function to extract tree botanical names.
    tree_botanical_list = extract_botanical_fn(row, string_clean_capital_fn, 'TS')

    # Call the extract_botanical_fn function to extract shrub botanical names.
    shrub_botanical_list = extract_botanical_fn(row, string_clean_capital_fn, 'SB')

    clean_list.extend(tree_botanical_list)
    clean_list.extend(shrub_botanical_list)

    return clean_list


if __name__ == '__main__':
    main_routine()
