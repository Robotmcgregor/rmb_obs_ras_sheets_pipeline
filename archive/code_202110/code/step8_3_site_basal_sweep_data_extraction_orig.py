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

warnings.filterwarnings("ignore")


def species_list_fn(df, n, m):
    """ Create a list from the required (n) botanical name fields from the dataframe (df), loops through ten
        times(number of variables).
            :param df: pandas data frame object.
            :param n: string object passed into the function (i.e. 'tree_live', 'tree_dead').
            :param m: string object passed into the function (i.e. 'shrub_live', 'shrub_dead').
            :return botanical_list: list object containing ten botanical names."""

    botanical_list = []

    for i in range(7):
        species1 = df[n + str(i + 1)][0]
        species2 = df[m + str(i + 1)][0]

        botanical_list.append(species1)
        botanical_list.append(species2)

    return botanical_list


def basal_list_horizontal_fn(basal):
    """ Extract basal observation sheet variables as a list of lists.

            :param basal: pandas dataframe object.
            :return basal_hor_list1234: list object containing basal information to be inserted into the observation sheet
            horizontally, including factor, basal species and count information. """

    basal_hor_list1 = [basal.basal1[0], basal.basal2[0], basal.basal3[0], basal.basal4[0], basal.basal5[0],
                       basal.basal6[0], basal.basal7[0]]

    factor = basal.factor[0]

    basal_hor_list2 = [factor, factor, factor, factor, factor, factor, factor]

    basal_hor_list3 = species_list_fn(basal, 'live_tree', 'dead_tree')
    basal_hor_list4 = species_list_fn(basal, 'live_shrub', 'dead_shrub')

    basal_hor_list1234 = [basal_hor_list1, basal_hor_list2, basal_hor_list3, basal_hor_list4]
    #print('.'*60)
    #print('basal_hor_list1234: ', basal_hor_list1234)
    return basal_hor_list1234


def basal_list_vertical_fn(basal):
    """ Extract basal observation sheet variables as a list of lists.

            :param basal: pandas dataframe object.
            :return basal_vert_list123: list object containing basal information to be inserted into the observation
            sheet vertically, including species lists and basal species per ha values. """

    basal_ver_list1 = [round(float(basal.basal_tree[0]), 2), round(float(basal.basal_shrub[0]), 2),
                       round(float(basal.total_basal[0]),2)]
    #print('basal_ver_list1', basal_ver_list1)

    basal_ver_list2 = [basal.bot_ts1[0], basal.bot_ts2[0], basal.bot_ts3[0], basal.bot_ts4[0],
                       basal.bot_ts5[0]]
    basal_ver_list3 = [basal.bot_sb1[0], basal.bot_sb2[0], basal.bot_sb3[0], basal.bot_sb4[0],
                       basal.bot_sb5[0]]

    basal_vert_list123 = [basal_ver_list1, basal_ver_list2, basal_ver_list3]
    #print('.'*60)
    #print('basal_vert_list123', basal_vert_list123)
    return basal_vert_list123


def common_name_extraction_fn(botanical_series, target_list, form):
    """ Extract the common name from the botanical_common_series excel document.

            :param botanical_series: pandas series object containing common and botanical species names.
            :param target_list: List of botanical species defined under basal_list_vertical_fn.
            :param form: string object passed into the function (tree or shrub).
            :return species_list: list object containing list elements [botanical_name, common_name].
            :return form_list: list object containing the form identifier of each species. """

    species_list = []
    form_list = []

    for botanical_name in target_list:
        botanical_name_list = botanical_series.Botanical_name.tolist()

        if botanical_name != 'BLANK':

            if botanical_name in botanical_name_list:

                common_name = botanical_series.loc[botanical_series['Botanical_name'] == botanical_name, 'Common_name'].iloc[0]
                form_list.append(form) # added this 11/5/2021
            else:
                common_name = botanical_name

            form_list.append(form)

            species_list.append([botanical_name, common_name])

    return species_list, form_list


'''def sort_three_lists(list_a, list_b, listc):

    list_a, list_b, listc = zip(*sorted(zip(list_a, list_b, listc)))
    print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    print(list_a, list_b, listc)
    return list_a, list_b, listc'''


def main_routine(basal_csv, site, site_dir, shrub_list_excel):

    """ Extract variables from the current site basal data frame and return ordered lists for observational
    workbook insertion.

            :param basal_csv: sting object containing the file path to the current site basal csv file.
            :param site: string object containing the current site.
            :param site_dir: string object containing the path to the site directory.
            :param shrub_list_excel: string object containing the path to an excel document containing botanical and
                common names.
            :return basal_hor_list1234: list object containing basal information to be inserted into the observation
            sheet horizontally, including factor, basal species and count information.
            :return basal_vert_list123: list object containing basal information to be inserted into the observation
                sheet vertically, including species lists and basal species per ha values. """

    #print('step8_3_site_basal_sweep_data_extraction.py INITIATED.')

    basal = pd.read_csv(basal_csv).fillna('BLANK').replace('Nan', 'BLANK')

    veg_df = pd.read_excel(shrub_list_excel, sheet_name='tree_shrub_list')
    # filter out unwanted fields.
    veg_series = veg_df[['Botanical_name', 'Common_name']]

    # call the basal_list_horizontal_fn function
    basal_hor_list1234 = basal_list_horizontal_fn(basal)

    # call the basal_list_vertical_fn function
    basal_vert_list123 = basal_list_vertical_fn(basal)

    # call the commonNameExtraction FN function
    basal_species_list1, basal_ver_list4 = common_name_extraction_fn(veg_series, basal_vert_list123[1], 'Tree')

    # call the common_name_extraction_fn function
    basal_species_list2, basal_ver_list5 = common_name_extraction_fn(veg_series, basal_vert_list123[2], 'Shrub')

    # extend the basal_species_list1 containing all tree and shrub species and replace the list at basalVerList[1]
    basal_species_list1.extend(basal_species_list2)

    # replace list position 1 in the basalVerList list of lists.
    basal_vert_list123[1] = basal_species_list1

    # extend formList1 with formList2
    basal_ver_list4.extend(basal_ver_list5)

    # replace basalVerList[2] with formList1
    basal_vert_list123[2] = basal_ver_list4

    return basal_hor_list1234, basal_vert_list123

    #print('script8_3_site_basal_sweep_data_extraction.py COMPLETED')


if __name__ == '__main__':
    main_routine()
