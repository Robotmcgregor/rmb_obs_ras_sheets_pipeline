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
import os
import warnings

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


def site_visit_vertical_list_fn(inter):
    """ Extract and observational workbook, visit worksheet variables as lists for workbook insertion.

             :param inter: pandas dataframe object (integrated).
             :return visit_vert_list2: list of variables for vertical insertion, including atmospheric conditions,
             soil colour and site description. """

    print('='*50)
    print(inter.atm_cond[0])
    if inter.atm_cond[0] == 'Heavy cloud 40 - 70% of the sky':
        atm = 'Heavy cloud 40 - 70% of sky'

    elif inter.atm_cond[0] == 'Some cloud 1- 5 % of sky':
        atm = 'Some cloud 1 - 5 % of sky'

    else:
        atm = inter.atm_cond[0]
    print(atm)
    visit_vert_list2 = [inter.season_cond[0], atm, inter.soil_cracks[0],
                        inter.soil_moist[0], inter.desc[0]]

    return visit_vert_list2


def site_establishment_vertical_fn(inter):
    """ Extract and observational workbook, establishment worksheet variables as lists for workbook insertion variables
        are dependent on whether this is a new or existing site.

             :param inter: pandas dataframe object (integrated).
             :return establish_list2456: list object containing list elements with establishment variables for ordered
             vertical insertion, including paddock name land system, water points and track information. """

    if inter.establish[0] == 'new':
        #print('new_site')

        estab_ver_list2 = [inter.paddock[0]]
        estab_ver_list4 = [inter.landscape[0], inter.soil_colour[0], inter.desc[0], inter.reason[0],
                           inter.land_system[0], inter.ls_consist[0], 'BLANK',
                           inter.water_name[0], inter.water_dist[0], inter.est_track_dist[0],
                           inter.est_inf_oth[0]]
        estab_ver_list5 = [inter.ls_source[0], inter.ls_alt[0]]
        #todo check if waterpoint dictonary is required

        estab_ver_list6 = [inter.water_point[0], inter.water_dir[0], inter.est_track_dir[0]]
        establish_list2456 = [estab_ver_list2, estab_ver_list4, estab_ver_list5, estab_ver_list6]
    else:
        estab_ver_list2 = [inter.paddock[0]]
        estab_ver_list4 = ['BLANK', 'BLANK', 'BLANK', 'BLANK',
                           'BLANK', 'BLANK', 'BLANK',
                           'BLANK', 'BLANK', 'BLANK', 'BLANK']
        estab_ver_list5 = ['BLANK', 'BLANK']
        estab_ver_list6 = ['BLANK', 'BLANK', 'BLANK']
        establish_list2456 = [estab_ver_list2, estab_ver_list4, estab_ver_list5, estab_ver_list6]

    return establish_list2456


def clearing_comment_fn(inter):
    """ Create a clearing comment based on multiple variables.

            :param inter: pandas dataframe object (integrated).
            :return clear_comm_final: string object containing a clearing comment derived from multiple fields."""

    if inter.clearing[0] != 'Absent':

        if inter.clear_pdk[0] == 'BLANK' and inter.land_use[0] == 'BLANK':
            clear_comm = str(inter.clear_age[0]) + ' clearing (' + str(inter.clear_type[0]) + ') may have ' \
                                                                                              'occurred. '

        elif inter.clear_pdk[0] != 'BLANK' and inter.land_use[0] == 'BLANK':
            clear_comm = str(inter.clear_age[0]) + ' clearing (' + str(
                inter.clear_type[0]) + ') may have occurred on ' + str(inter.clear_pdk[0]) + ' paddock.'

        elif inter.land_use[0] != 'BLANK' and inter.clear_pdk[0] == 'BLANK':
            clear_comm = str(inter.clear_age[0]) + ' clearing (' + str(
                inter.clear_type[0]) + ') may have occurred for the purposes of  ' + str(
                inter.land_use[0]) + '.'

        elif inter.land_use[0] != 'BLANK' and inter.clear_pdk[0] != 'BLANK':
            clear_comm = str(inter.clear_age[0]) + ' clearing (' + str(
                inter.clear_type[0]) + ') may have occurred on ' + str(
                inter.clear_pdk[0]) + ' paddock for the purposes of  ' + str(inter.land_use[0]) + '.'
        else:
            clear_comm = 'Scripting ERROR.'

        clear_comm_final = clear_comm.capitalize()

    else:
        clear_comm_final = 'BLANK'

    return clear_comm_final


def fire_fn(inter):
    """ Create a clearing comment based on multiple variables.

            :param inter: pandas dataframe object (integrated).
            :return north_fire_list: list object containing the northern fire frequency and intensity variables.
            :return south_fire_list: list object containing the northern fire frequency and intensity variables. """

    district = inter.district[0]

    if district == 'Darwin' or 'Gulf' or 'Katherine' or 'Sturt Plateau' or 'Roper':
        north_ff = inter.north_ff[0]
        north_fi = inter.north_fi[0]
        south_ff = 'BLANK'
        south_fi = 'BLANK'
        if north_ff == 'BLANK':
            north_ff = 'Absent'
        if north_fi == 'BLANK':
            north_fi = 'Absent'
    elif district == 'Northern Alice Springs' or 'Southern Alice Springs' or 'Tennant Creek' or 'Plenty':
        south_ff = inter.south_ff[0]
        south_fi = inter.south_fi[0]
        north_ff = 'BLANK'
        north_fi = 'BLANK'
        if south_ff == 'BLANK':
            south_ff = 'Absent'
        if south_fi == 'BLANK':
            south_fi = 'Absent'
    else:
        north_ff = inter.north_ff[0]
        north_fi = inter.north_fi[0]
        south_ff = inter.south_ff[0]
        south_fi = inter.south_fi[0]

    north_fire_list = [north_ff, north_fi]
    south_fire_list = [south_ff, south_fi]

    return north_fire_list, south_fire_list


def weeds_comment_fn(inter):
    """ Create a weed comment based on multiple variables.

            :param inter: pandas dataframe object (integrated).
            :return weed_comment_list: list object containing a weed comments derived from multiple fields."""



    # extract weed information.
    weed_list = [inter.weed1[0], inter.weed2[0], inter.weed3[0]]
    size_list = [inter.weed_size1[0], inter.weed_size2[0], inter.weed_size3[0]]
    den_list = [inter.weed_den1[0], inter.weed_den2[0], inter.weed_den3[0]]
    com_list = [inter.weed_comm1[0], inter.weed_comm2[0], inter.weed_comm3[0]]

    # create an empty list for weed comments
    weed_comment_list = []

    # loop through zipped lists and append comments.
    for weed, size, den in zip(weed_list, size_list, den_list):
        if weed != 'BLANK' and weed != 'End selection':
            den_value = {'absent': 'absent', 2: 'single plant <10%', 3: 'low 1-10%',
                         4: 'medium 10-50%', 5: 'high >50%'}
            density = (den_value[den])

            size_value = {5: '5m diameter', 20: '20m diameter', 50: '50m diameter', 100: '100m diameter',
                          200: '200m diameter'}
            size_ = (size_value[size])

            comment1 = weed + ': ' + 'density (' + str(density) + ') size (' + str(size_) + ')'
            weed_comment_list.append(comment1)

    if not weed_comment_list:

        weed_comment_list.append('BLANK')

    sent_string = ""
    for i in weed_comment_list:
        if i != 'BLANK':
            sent_string += str(i) + '. '

    return weed_comment_list, sent_string


def list_of_photos(site_dir, search_criteria):
    """ Create a list of file paths for matching search_criteria.

        :param site_dir: string path containing the site directory path.
        :param search_criteria: string object containing search wildcard information.
        :return: file name: string object containing either the matching search criteria or 'BLANK."""

    for root, dirs, files in os.walk(site_dir):

        if search_criteria in files:
            file_name = search_criteria
        else:
            file_name = 'BLANK'

    return file_name


def pres_abs_to_true_false_fn(input_list):
    """ #Asign true or false to present absent variables.

            :param input_list: list object containing Present/Absent string variables.
            :return output_list: list object containing processed string variables. """

    output_list = []
    for i in input_list:

        if i == 'Present':
            n = 'true'
        else:
            n = 'false'
        output_list.append(n)

    return output_list


def disturbance_ver_data_fn(inter, site_dir):
    """ Extract disturbance variables from the integrated data frame as list items for vertical insertion into a
    worksheet.

            :param inter: pandas  data frame object.
            :param site_dir: string object containing the path to the site directory.
            :return disturb_vert_list12345678: list object containing list elements ready for vertical insertion,
            including: clearing, photo file names and erosion information."""

    dist_ver_list1 = [inter.clearing[0], inter.cyclone[0], inter.dieback[0]]

    # call the list_of_photos_fn function to search for photo_url_extraction_fn names.
    clearing_photo = list_of_photos(site_dir, 'clearing')
    cyclone_photo = list_of_photos(site_dir, 'cyclone')
    dieback_photo = list_of_photos(site_dir, 'dieback')

    dist_ver_list2 = [clearing_photo, cyclone_photo, dieback_photo]
    # call the clearing_comment_fn function
    clearing_comment = clearing_comment_fn(inter)
    dist_ver_list3 = [clearing_comment, inter.cyc_comm[0], inter.die_comm[0]]

    # convert distance from float to int if distance was collected.
    if inter.rev_inf_dist[0] != 'BLANK':
        rev_inf_dist = int(inter.rev_inf_dist[0])
    else:
        rev_inf_dist = inter.rev_inf_dist[0]
    dist_ver_list4 = [inter.rev_inf[0], inter.rev_inf_comm[0], rev_inf_dist]

    dist_ver_list5 = [inter.erod_soil[0]]

    # Erodible severity
    dist_ver_list6 = [inter.scald_sev[0], inter.wind_sev[0], inter.water_sheet_sev[0],
                      inter.rill_sev[0], inter.gully_sev[0]]
    dist_ver_list6 = ['Absent' if i== 'BLANK' else i for i in dist_ver_list6]

    # erosion stability
    dist_ver_list7 = [inter.scald_stab[0], inter.wind_stab[0], inter.water_sheet_stab[0], inter.rill_stab[0],
                      inter.gully_stab[0]]

    # call the weeds_comment_fn function
    weeds_comment_list, sent_string = weeds_comment_fn(inter)

    weed_comment = weeds_comment_list[0]
    if weed_comment != 'BLANK':
        weeds = 'present'
    else:
        weeds = 'absent'

    dist_ver_list8 = [inter.erosion_comm[0], weeds, sent_string]

    disturb_vert_list12345678 = [dist_ver_list1, dist_ver_list2, dist_ver_list3, dist_ver_list4, dist_ver_list5,
                                 dist_ver_list6, dist_ver_list7, dist_ver_list8]
    return disturb_vert_list12345678


def disturbance_hor_data_fn(inter):
    """ Extract disturbance variables from the integrated data frame as list items for horizontal insertion into the
    observational workbook.

    :param inter: pandas  data frame object.
    :return dist_hor_list12345: list object containing list elements ready for horizontal insertion."""

    feral_list = [inter.camel[0], inter.rabbit[0], inter.donkey[0], inter.horse[0], inter.pig[0],
                  inter.buffalo[0], inter.nat_herb[0], inter.other_feral[0]]

    dist_hor_list1 = pres_abs_to_true_false_fn(feral_list)

    dist_hor_list2 = [inter.feral_comm[0]]

    # call the fire_fn function
    dist_hor_list3, dist_hor_list4 = fire_fn(inter)

    dist_hor_list5 = [inter.cattle_pad[0], inter.cattle_tramp[0]]

    dist_hor_list12345 = [dist_hor_list1, dist_hor_list2, dist_hor_list3, dist_hor_list4, dist_hor_list5]
    return dist_hor_list12345


def site_cond_variable_list_fn(inter):
    """ Extract site condition variables from the integrated data frame as list items for horizontal or
    vertical into a worksheet.
     :param inter: pandas  data frame object.
     :return cond_vert_list12: list object containing condition sheet vertical inserts,
     including: greeness, abundance, and pasture utilisation information.
     :return cond_hor_list1: list object containing condition sheet horizontal insert (condition note). """

    cond_values = {'no_grazing': 'NO GRAZING', '<10%': '<10%', '11_25%': '11%-25%', '26_50%': '26%-50%',
                     '51_75%': '51%-75%', '76_90%': '76%-90%', '>90%': '>90%', 'green': 'GREEN',
                     'drying_off_greening_up': 'DRYING OFF/GREENING UP', 'dry': 'DRY'}

    cond_ver_list1 = [inter.greenness[0], inter.green_comm[0], inter.abundance[0], inter.abund_comm[0],
                      inter.past_util[0], inter.past_util_comm[0]]
    cond_ver_list2 = [inter.cond_note[0]]
    cond_hor_list1 = [inter.condition[0]]

    cond_vert_list12 = [cond_ver_list1, cond_ver_list2]
    return cond_vert_list12, cond_hor_list1


def main_routine(integrated_csv, site_dir):
    """ Extract variables from the current site integrated data frame and return ordered lists for observational 
    workbook insertion.
            :param integrated_csv: sting object containing the file path to the current site integrated csv file.
            :param site_dir: string object containing the path to the site directory.
            :return establish_list2456: list object containing list elements with establishment variables for ordered
                vertical insertion.
            :return visit_vert_list2: list of variables for vertical insertion, including atmospheric conditions,
                soil colour and site description.
            :return disturb_vert_list12345678: list object containing list elements ready for vertical insertion,
                including: clearing, photo file names and erosion information.
            :return establish_list2456: list object containing list elements with establishment variables for ordered
                vertical insertion, including paddock name land system, water points and track information.
            :return north_fire_list: list object containing the northern fire frequency and intensity variables.
            :return south_fire_list: list object containing the northern fire frequency and intensity variables.
            :return cond_vert_list12: list object containing condition sheet vertical inserts,
                including: greeness, abundance, and pasture utilisation information.
            :return cond_hor_list1: list object containing condition sheet horizontal insert (condition note). """

    #print('step8_1_site_integrated_data_extraction.py INITIATED.')

    inter = pd.read_csv(integrated_csv).fillna('BLANK').replace('Nan', 'BLANK')

    property_name = inter.final_prop[0].replace(' ', '_')

    # call the site_visit_vertical_list_fn function
    visit_ver_list2 = site_visit_vertical_list_fn(inter)

    establish_list2456 = site_establishment_vertical_fn(inter)

    disturb_vert_list12345678 = disturbance_ver_data_fn(inter, site_dir)

    dist_hor_list12345 = disturbance_hor_data_fn(inter)

    cond_vert_list12, cond_hor_list1 = site_cond_variable_list_fn(inter)

    #print('step8_1_site_integrated_data_extraction.py COMPLETE.')

    return property_name, establish_list2456, visit_ver_list2, disturb_vert_list12345678, dist_hor_list12345, cond_vert_list12, \
           cond_hor_list1


if __name__ == '__main__':
    main_routine()
