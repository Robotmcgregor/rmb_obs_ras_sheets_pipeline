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
import pandas as pd
import warnings
import numpy as np

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


def pers_absent_fn(input_list):
    """ Convert 0 or values or np.nan values to 'Absent'.

    :param input_list: list object  containing unknown variables.
    :return output_list: list object containing processed variables.
    """

    output_list = []
    for i in input_list:

        if i == 0 or '0' or np.nan:
            output_value = 'Absent'
        else:
            i = np.nan
        output_list.extend([output_value])
    return output_list


def percentage_fn(input_list):
    """ Remove spaces and add a percentage sign.

    :param input_list: list object  containing unknown variables.
    :return output_list: list object containing processed variables.
    """

    output_list = []
    for i in input_list:
        space_free = str(i).replace(' ', '')
        final_variable = space_free + '%'
        output_list.extend([final_variable])

    return output_list


def pres_abs_to_true_false_fn(input_list):
    """ Assign true or false to present absent variables.
    :param input_list: list object containing Present/Absent string variables.
    :return output_list: list object containing processed string variables.
    """
    output_list = []
    for i in input_list:

        if i == 'Present':
            n = 'True'
        else:
            n = 'False'
        output_list.append(n)

    return output_list


def site_hor_list_variable_fn(ras):
    """ Extract rapid assessment survey (ras) sheet variables as a nested list of lists for horizontal insertion.

    :param ras: pandas dataframe object.
    :return ras_hort_list1234567891011121314: list object containing information to be inserted into the
    ras sheet horizontally, including site name, water points, basal density feral animals etc.
    """

    ras_hor_list1 = [ras.final_prop.iloc[0], ras.site_orig.iloc[0], ras.date_time.iloc[0]]
    ras_hor_list2 = [ras.recorder.iloc[0], 'BLANK', 'BLANK']
    ras_hor_list3 = [ras.gda_lat.iloc[0], ras.gda_lon.iloc[0], ras.paddock.iloc[0]]
    ras_hor_list4 = [ras.water_name.iloc[0], ras.water_point.iloc[0], ras.water_dist.iloc[0], ras.water_dir.iloc[0]]
    ras_hor_list5 = [ras.desc.iloc[0], ras.land_system.iloc[0]]
    ras_hor_list6 = [ras.bare_soil.iloc[0].replace('_', '-')]
    # call the percentage_fn function to remove spaces and add a '%' character.
    ras_hor_list6 = percentage_fn(ras_hor_list6)

    cover_list = [ras.cover_3p.iloc[0].replace('_', '-'), ras.cover_pg.iloc[0].replace('_', '-'),
                  ras.cover_ag.iloc[0].replace('_', '-'), ras.cover_pf.iloc[0].replace('_', '-')]
    # call the percentage_fn function to remove spaces and add a '%' character.
    cover_list = percentage_fn(cover_list)
    basal_list = [ras.basal.iloc[0]]
    density_list = [ras.tree_density.iloc[0], ras.shrub_density.iloc[0]]
    density_list = pers_absent_fn(density_list)
    erodible_soil = [ras.erod_soil.iloc[0]]
    pas_ulil_list = [ras.past_util.iloc[0]]
    weeds_comment_list = ['place filler']
    feral_list = [ras.camel.iloc[0], ras.rabbit.iloc[0], ras.donkey.iloc[0], ras.horse.iloc[0], ras.pig.iloc[0],
                  ras.buffalo.iloc[0], ras.nat_herb.iloc[0]]

    final_feral_list = pres_abs_to_true_false_fn(feral_list)

    condition_list = [ras.condition.iloc[0], ras.cond_note.iloc[0]]

    ras_hort_list1234567891011121314 = [
        ras_hor_list1, ras_hor_list2, ras_hor_list3, ras_hor_list4, ras_hor_list5, ras_hor_list6, cover_list,
        basal_list, density_list, erodible_soil, pas_ulil_list, weeds_comment_list, final_feral_list, condition_list]

    return ras_hort_list1234567891011121314


def erosion_comment_match_fn(erod_severity_list, erosion_comment_list):
    """ Create an ordered list of erosion comments based on the erosion severity value.

    :param erod_severity_list: ordered list object containing erosion severity variables.
    :param erosion_comment_list: list object containing the erosion comment.
    :return erosion_list: ordered list object with erosion comments matching erod_severity_list.
    """

    erosion_list = []
    for i in erod_severity_list:

        if i != 'BLANK':
            ero = erosion_comment_list[0]
            erosion_list.append(ero)
        else:
            ero = 'BLANK'
            erosion_list.append(ero)
    return erosion_list


def site_vert_list_variable_fn(ras):
    """ Extract rapid assessment survey (ras) sheet variables as a nested list of lists for vertical insertion.

    :param ras: pandas dataframe object.
    :return ras_vert_list123456789101112: list object containing information to be inserted into the
    ras sheet vertically, including botanical lists, fire and erosion variables etc.
    """

    ras_ver_list1 = [ras.bot_3p_1[0], ras.bot_3p_2[0], ras.bot_3p_3[0], ras.bot_3p_4[0]]
    ras_ver_list2 = [ras.bot_pg_1[0], ras.bot_pg_2[0], ras.bot_pg_3[0], ras.bot_pg_4[0]]
    ras_ver_list3 = [ras.bot_ag_1[0], ras.bot_ag_2[0], ras.bot_ag_3[0], ras.bot_ag_4[0]]
    ras_ver_list4 = [ras.bot_pf_1[0], ras.bot_pf_2[0], ras.bot_pf_3[0], ras.bot_pf_4[0]]
    min_max_list = [ras.max_cover[0], ras.min_cover[0]]

    ras_ver_list5 = [ras.bot_sb_1[0], ras.bot_sb_2[0], ras.bot_sb_3[0], ras.bot_sb_4[0]]
    ras_ver_list6 = [ras.bot_ts_1[0], ras.bot_ts_2[0], ras.bot_ts_3[0],
                     ras.bot_ts_4[0]]
    erod_severity_list = [ras.scald_sev[0], ras.wind_sev[0], ras.water_sheet_sev[0], ras.rill_sev[0], ras.gully_sev[0]]
    erod_stability_list = [ras.scald_stab[0], ras.wind_stab[0], ras.water_sheet_stab[0], ras.rill_stab[0],
                           ras.gully_stab[0]]

    erosion_comment_list = [ras.erosion_com[0]]
    erosion_list = erosion_comment_match_fn(erod_severity_list, erosion_comment_list)

    north_fire_list = [ras.north_ff[0], ras.north_fi[0]]
    south_fire_list = [ras.south_ff[0], ras.south_fi[0]]

    ras_vert_list123456789101112 = [
        ras_ver_list1, ras_ver_list2, ras_ver_list3, ras_ver_list4, min_max_list, ras_ver_list5, ras_ver_list6,
        erod_severity_list, erod_stability_list, erosion_list, north_fire_list, south_fire_list]

    return ras_vert_list123456789101112


def weeds_comment_fn(ras):
    """ Create a weed comment based on multiple variables.

    :param ras: pandas dataframe object (integrated).
    :return weed_comment_list: list object containing a weed comments derived from multiple fields.
    """

    # extract weed information.
    weed_list = [ras.weed1[0], ras.weed2[0], ras.weed3[0]]
    size_list = [ras.weed_size1[0], ras.weed_size2[0], ras.weed_size3[0]]
    den_list = [ras.weed_den1[0], ras.weed_den2[0], ras.weed_den3[0]]

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

    return weed_comment_list


def main_routine(ras_csv):
    # ras_csv, site, site_dir
    """ Extract the ras information add export data as a list for ras sheet insertion.

    :param ras_csv: pandas dataframe object.
    :return ras_hort_list1234567891011121314: list object containing nested lists for horizontal insertion.
    :return ras_vert_list123456789101112: list object containing nested lists for vertical insertion.
    """

    # import the site ras transect csv
    ras = pd.read_csv(ras_csv).fillna('BLANK').replace('Nan', 'BLANK')

    property_name = ras.final_prop[0].replace(' ', '_')
    # call the site_hor_list_variable_fn function to extract rapid assessment survey (ras) sheet variables as a nested
    # list of lists for horizontal insertion.
    ras_hort_list1234567891011121314 = site_hor_list_variable_fn(ras)

    # call the site_vert_list_variable_fn function to extract rapid assessment survey (ras) sheet variables as a nested
    # list of lists for vertical insertion.
    ras_vert_list123456789101112 = site_vert_list_variable_fn(ras)

    # call the weeds_comment_fn function to extract a list of weed comments.
    weeds_comment_list = weeds_comment_fn(ras)

    # join lists into a string
    weeds_comment = ', '.join(weeds_comment_list)
    # add a full stop to the end of the comment.
    sent_string = ""
    if weeds_comment != 'BLANK':
        sent_string += str(weeds_comment) + '. '

    # replace the weed comment with the final weed comment.
    ras_hort_list1234567891011121314[11] = [sent_string]

    return property_name, ras_hort_list1234567891011121314, ras_vert_list123456789101112


if __name__ == '__main__':
    main_routine()
