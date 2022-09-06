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


# import modules
# nothing to import


# I have rearranged the order of this sheet. If there are errors it could be due to this.


def create_worksheet_fn(workbook, worksheet_name):
    """ Create worksheet and set row height.

            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet_name: string object containing worksheet name."""

    # Set up Site Establishment worksheet #
    worksheet = workbook.add_worksheet(worksheet_name)

    # Set row height
    worksheet.set_default_row(56.25)

    return workbook, worksheet


def insert_sheet_headings_fn(workbook, worksheet, heading2, heading3, heading4, heading6, color_fill):
    """ Add item headings to cells as strings.

            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading2: workbook style derived  from define heading2_fn.
            :param heading3: workbook style derived  from define heading3_fn.
            :param heading4: workbook style derived  from define heading4_fn.
            :param heading6: workbook style derived  from define heading6_fn.
            :param color_fill: workbook style derived  from define colour_fill_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.write_string('B3', 'LITTER', heading2)
    worksheet.write_string('C3', 'BARE GROUND', heading2)
    worksheet.write_string('D3', 'TOTAL VEG', heading2)
    worksheet.write_string('A4', 'Transect figure', heading2)
    worksheet.write_string('A5', 'Adjusted est', heading2)
    worksheet.write_string('B7', 'Perennial grasses', heading4)
    worksheet.write_string('C7', 'Annual grasses', heading4)
    worksheet.write_string('D7', 'Perennial forbs', heading4)
    worksheet.write_string('E7', 'Annual forbs', heading4)
    worksheet.write_string('F7', 'Unspecified plants', heading4)
    worksheet.write_string('A8', 'Transect figure', heading3)
    worksheet.write_string('A9', 'Adjusted figure', heading3)
    worksheet.write_string('A10', 'Estimate total', heading3)
    worksheet.write_string('C14', 'Confirmed species name', heading4)
    worksheet.write_string('D14', 'Field name', heading4)
    worksheet.write_string('E14', 'Cover estimate', heading4)
    worksheet.write_string('C25', 'Other species', heading6)
    worksheet.write_string('D25', 'Other species', heading6)
    worksheet.write_string('C27', 'Confirmed species name', heading4)
    worksheet.write_string('D27', 'Field name', heading4)
    worksheet.write_string('E27', 'Cover estimate', heading4)
    worksheet.write_string('C32', 'Other species', heading6)
    worksheet.write_string('D32', 'Other species', heading6)
    worksheet.write_string('C34', 'Confirmed species name', heading4)
    worksheet.write_string('D34', 'Field name', heading4)
    worksheet.write_string('E34', 'Cover estimate', heading4)
    worksheet.write_string('C39', 'Other species', heading6)
    worksheet.write_string('D39', 'Other species', heading6)
    worksheet.write_string('C41', 'Confirmed species name', heading4)
    worksheet.write_string('D41', 'Field name', heading4)
    worksheet.write_string('E41', 'Cover estimate', heading4)
    worksheet.write_string('C46', 'Other species', heading6)
    worksheet.write_string('D46', 'Other species', heading6)
    worksheet.write_string('C48', 'Confirmed species name', heading4)
    worksheet.write_string('D48', 'Field name', heading4)
    worksheet.write_string('E48', 'Cover estimate', heading4)
    worksheet.write_string('C53', 'Other species', heading6)
    worksheet.write_string('D53', 'Other species', heading6)

    worksheet.write('A3', None, color_fill)
    worksheet.write('A7', None, color_fill)

    return workbook, worksheet


def insert_blank_formatted_cells_fn(workbook, worksheet, heading7):
    """ Add blank formatted cells to worksheet.

            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading7: workbook style derived  from define heading7_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.write_blank('B4', None, heading7)
    worksheet.write_blank('C4', None, heading7)
    worksheet.write_blank('D4', None, heading7)
    worksheet.write_blank('B8', None, heading7)
    worksheet.write_blank('C8', None, heading7)
    worksheet.write_blank('D8', None, heading7)
    worksheet.write_blank('E8', None, heading7)
    worksheet.write_blank('F8', None, heading7)
    worksheet.write_blank('C16', None, heading7)
    worksheet.write_blank('D16', None, heading7)
    worksheet.write_blank('E16', None, heading7)
    worksheet.write_blank('C17', None, heading7)
    worksheet.write_blank('D17', None, heading7)
    worksheet.write_blank('E17', None, heading7)
    worksheet.write_blank('C18', None, heading7)
    worksheet.write_blank('D18', None, heading7)
    worksheet.write_blank('E18', None, heading7)
    worksheet.write_blank('C19', None, heading7)
    worksheet.write_blank('D19', None, heading7)
    worksheet.write_blank('E19', None, heading7)
    worksheet.write_blank('C21', None, heading7)
    worksheet.write_blank('D21', None, heading7)
    worksheet.write_blank('E21', None, heading7)
    worksheet.write_blank('C22', None, heading7)
    worksheet.write_blank('D22', None, heading7)
    worksheet.write_blank('E22', None, heading7)
    worksheet.write_blank('C23', None, heading7)
    worksheet.write_blank('D23', None, heading7)
    worksheet.write_blank('E23', None, heading7)
    worksheet.write_blank('C24', None, heading7)
    worksheet.write_blank('D24', None, heading7)
    worksheet.write_blank('E24', None, heading7)
    worksheet.write_blank('C28', None, heading7)
    worksheet.write_blank('D28', None, heading7)
    worksheet.write_blank('E28', None, heading7)
    worksheet.write_blank('C29', None, heading7)
    worksheet.write_blank('D29', None, heading7)
    worksheet.write_blank('E29', None, heading7)
    worksheet.write_blank('C30', None, heading7)
    worksheet.write_blank('D30', None, heading7)
    worksheet.write_blank('E30', None, heading7)
    worksheet.write_blank('C31', None, heading7)
    worksheet.write_blank('D31', None, heading7)
    worksheet.write_blank('E31', None, heading7)
    worksheet.write_blank('C35', None, heading7)
    worksheet.write_blank('D35', None, heading7)
    worksheet.write_blank('E35', None, heading7)
    worksheet.write_blank('C36', None, heading7)
    worksheet.write_blank('D36', None, heading7)
    worksheet.write_blank('E36', None, heading7)
    worksheet.write_blank('C37', None, heading7)
    worksheet.write_blank('D37', None, heading7)
    worksheet.write_blank('E37', None, heading7)
    worksheet.write_blank('C38', None, heading7)
    worksheet.write_blank('D38', None, heading7)
    worksheet.write_blank('E38', None, heading7)
    worksheet.write_blank('C42', None, heading7)
    worksheet.write_blank('D42', None, heading7)
    worksheet.write_blank('E42', None, heading7)
    worksheet.write_blank('C43', None, heading7)
    worksheet.write_blank('D43', None, heading7)
    worksheet.write_blank('E43', None, heading7)
    worksheet.write_blank('C44', None, heading7)
    worksheet.write_blank('D44', None, heading7)
    worksheet.write_blank('E44', None, heading7)
    worksheet.write_blank('C45', None, heading7)
    worksheet.write_blank('D45', None, heading7)
    worksheet.write_blank('E45', None, heading7)
    worksheet.write_blank('C49', None, heading7)
    worksheet.write_blank('D49', None, heading7)
    worksheet.write_blank('E49', None, heading7)
    worksheet.write_blank('C50', None, heading7)
    worksheet.write_blank('D50', None, heading7)
    worksheet.write_blank('E50', None, heading7)
    worksheet.write_blank('C51', None, heading7)
    worksheet.write_blank('D51', None, heading7)
    worksheet.write_blank('E51', None, heading7)
    worksheet.write_blank('C52', None, heading7)
    worksheet.write_blank('D52', None, heading7)
    worksheet.write_blank('E52', None, heading7)
    worksheet.write_blank('E25', None, heading7)
    worksheet.write_blank('E32', None, heading7)
    worksheet.write_blank('E39', None, heading7)
    worksheet.write_blank('E46', None, heading7)
    worksheet.write_blank('E53', None, heading7)

    return workbook, worksheet


def merge_cells_fn(workbook, worksheet, heading1, heading2, heading4, heading7, color_fill):
    """ Add item headings to cells and merge.

            :param color_fill: workbook style derived  from define colour_fill_fn.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading1: workbook style derived  from define heading1_fn.
            :param heading2: workbook style derived  from define heading2_fn.
            :param heading4: workbook style derived  from define heading4_fn.
            :param heading7: workbook style derived  from define heading7_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.merge_range('A1:F1', 'STEP 7 - COVER ESTIMATES', heading1)
    worksheet.merge_range('A2:F2', 'SITE COVER FRACTIONS', heading1)
    worksheet.merge_range('E3:F3', 'SUM', heading2)
    worksheet.merge_range('E4:F4', '', heading7)
    worksheet.merge_range('E5:F5', '', heading7)
    worksheet.merge_range('A6:F6', 'VEGETATION COVER', heading1)
    worksheet.merge_range('B10:F10', '', heading7)
    worksheet.merge_range('A11:F11', '')
    worksheet.merge_range('A12:F12', 'VEGETATION', heading1)
    worksheet.merge_range('A13:E13', 'Perennial grasses', heading1)
    worksheet.merge_range('A14:B14', 'PROPORTION OF VEG COVER', heading4)
    worksheet.merge_range('C15:E15', '3P grasses', heading1)
    worksheet.merge_range('C20:E20', 'Other perennial grasses', heading1)
    worksheet.merge_range('A15:B24', '', heading7)
    worksheet.merge_range('A25:B25', '', color_fill)
    worksheet.merge_range('A26:E26', 'Annual grasses', heading1)
    worksheet.merge_range('A27:B27', 'PROPORTION OF VEG COVER', heading4)
    worksheet.merge_range('A28:B31', '', heading7)
    worksheet.merge_range('A32:B32', '', color_fill)
    worksheet.merge_range('A33:E33', 'Perennial forbs', heading1)
    worksheet.merge_range('A34:B34', 'PROPORTION OF VEG COVER', heading4)
    worksheet.merge_range('A35:B38', '', heading7)
    worksheet.merge_range('A39:B39', '', color_fill)
    worksheet.merge_range('A40:E40', 'Annual forbs', heading1)
    worksheet.merge_range('A41:B41', 'PROPORTION OF VEG COVER', heading4)
    worksheet.merge_range('A42:B45', '', heading7)
    worksheet.merge_range('A46:B46', '', color_fill)
    worksheet.merge_range('A47:E47', 'Unspecified plants', heading1)
    worksheet.merge_range('A48:B48', 'PROPORTION OF VEG COVER', heading4)
    worksheet.merge_range('A49:B52', '', heading7)
    worksheet.merge_range('A53:B53', '', color_fill)

    return workbook, worksheet


def define_column_widths_fn(workbook, worksheet):
    """ define and set column widths.

            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.set_column('A:A', 31.27)
    worksheet.set_column('B:B', 34.91)
    worksheet.set_column('C:C', 34.91)
    worksheet.set_column('D:D', 30.55)
    worksheet.set_column('E:E', 25.82)
    worksheet.set_column('F:F', 24.55)

    return workbook, worksheet


def insert_default_values_fn(workbook, worksheet, heading7):
    """ Add default values and  format worksheet cells.

            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading7: workbook style derived  from define heading7_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.write_number('A15', 0, heading7)
    worksheet.write_number('A28', 0, heading7)
    worksheet.write_number('A35', 0, heading7)
    worksheet.write_number('A42', 0, heading7)
    worksheet.write_number('A49', 0, heading7)
    worksheet.write_number('B5', 0, heading7)
    worksheet.write_number('C5', 0, heading7)
    worksheet.write_number('D5', 0, heading7)
    worksheet.write_number('B9', 0, heading7)
    worksheet.write_number('C9', 0, heading7)
    worksheet.write_number('D9', 0, heading7)
    worksheet.write_number('E9', 0, heading7)
    worksheet.write_number('F9', 0, heading7)
    worksheet.write_number('C11', 0, heading7)
    worksheet.write_number('E5', 0, heading7)
    worksheet.write_number('E16', 0, heading7)
    worksheet.write_number('E17', 0, heading7)
    worksheet.write_number('E18', 0, heading7)
    worksheet.write_number('E19', 0, heading7)
    worksheet.write_number('E21', 0, heading7)
    worksheet.write_number('E22', 0, heading7)
    worksheet.write_number('E23', 0, heading7)
    worksheet.write_number('E24', 0, heading7)
    worksheet.write_number('E25', 0, heading7)
    worksheet.write_number('E28', 0, heading7)
    worksheet.write_number('E29', 0, heading7)
    worksheet.write_number('E30', 0, heading7)
    worksheet.write_number('E31', 0, heading7)
    worksheet.write_number('E32', 0, heading7)
    worksheet.write_number('E35', 0, heading7)
    worksheet.write_number('E36', 0, heading7)
    worksheet.write_number('E37', 0, heading7)
    worksheet.write_number('E38', 0, heading7)
    worksheet.write_number('E39', 0, heading7)
    worksheet.write_number('E42', 0, heading7)
    worksheet.write_number('E43', 0, heading7)
    worksheet.write_number('E44', 0, heading7)
    worksheet.write_number('E45', 0, heading7)
    worksheet.write_number('E46', 0, heading7)
    worksheet.write_number('E49', 0, heading7)
    worksheet.write_number('E50', 0, heading7)
    worksheet.write_number('E51', 0, heading7)
    worksheet.write_number('E52', 0, heading7)
    worksheet.write_number('E53', 0, heading7)
    worksheet.write_number('F8', 0, heading7)

    return workbook, worksheet


def insert_botanical_common_names_fn(item, row, col, insert_horizontal_data_fn, worksheet, heading7):
    """ loop through the botanical and common name lists and insert into the workbook.

            :param item: list object containing the input data.
            :param row: integer object containing the starting row value for data insertion.
            :param col: integer object containing the starting column value for data insertion.
            :param insert_horizontal_data_fn: function controlling horizontal data insertion.
            :param worksheet: current worksheet of the workbook (cover estimates).
            :param heading7: workbook heading style. """

    if item:

        # ---------------------------------------- Woody species ----------------------------------------------

        row = row
        col = col
        for i in item:
            # call the insert_vertical_data_fn function
            insert_horizontal_data_fn(worksheet, row, col, i, heading7, 1)

            row += 1


def main_routine(color_fill, heading1, heading2, heading3, heading4, heading6, heading7, workbook, obs_data_list,
                 insert_vertical_data_fn, insert_horizontal_data_fn, insert_horizontal_not_required_data_fn):
    """ Create the Cover estimates worksheet within the Rangeland Monitoring observation excel workbook.

            :param color_fill: workbook style derived  from define colour_fill_fn.
            :param heading1: workbook style derived  from define heading1_fn.
            :param heading2: workbook style derived  from define heading2_fn.
            :param heading3: workbook style derived  from define heading3_fn.
            :param heading4: workbook style derived  from define heading4_fn.
            :param heading6: workbook style derived  from define heading6_fn.
            :param heading7: workbook style derived  from define heading7_fn.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param obs_data_list: list object with list elements containing input data for the entire workbook.
            :param insert_vertical_data_fn: function controlling a vertical data insertion loop.
            :param insert_horizontal_data_fn: function controlling a horizontal data insertion loop. """

    #print('step10_10_create_site_cover_estimates.py INITIATED')

    work_sheet_name = 'Step 7 - Cover estimates  - Tab'

    # call the create_worksheet_fn function.
    workbook, worksheet = create_worksheet_fn(workbook, work_sheet_name)

    # call the insert_sheet_headings_fn function.
    workbook, worksheet = insert_sheet_headings_fn(workbook, worksheet, heading2, heading3, heading4, heading6,
                                                   color_fill)

    # call the insert_blank_formatted_cells_fn function.
    workbook, worksheet = insert_blank_formatted_cells_fn(workbook, worksheet, heading7)

    # call the merge_cells_fn function.
    workbook, worksheet = merge_cells_fn(workbook, worksheet, heading1, heading2, heading4, heading7, color_fill)

    # call the define_column_widths_fn function
    workbook, worksheet = define_column_widths_fn(workbook, worksheet)

    # call the insert_default_values_fn function
    workbook, worksheet = insert_default_values_fn(workbook, worksheet, heading7)

    if obs_data_list[6]:
        cover_estim_hor_list = obs_data_list[6]
        #print('obs_data_list[6]: ', obs_data_list[6])

    # call the insert_horizontal_not_required_data_fn function to insert the site cover transect values.
    if cover_estim_hor_list[0]:
        #print('cover_estim_hor_list[0]: ', cover_estim_hor_list[0])
        insert_horizontal_not_required_data_fn(worksheet, 3, 1, cover_estim_hor_list[0], heading7, 1)
    # call the insert_horizontal_not_required_data_fn function to insert the site cover adjusted est values.
    if cover_estim_hor_list[1]:
        insert_horizontal_not_required_data_fn(worksheet, 4, 1, cover_estim_hor_list[1], heading7, 1)
    # call the insert_horizontal_not_required_data_fn function to insert the vegetation cover adjusted est values.
    if cover_estim_hor_list[2]:
        insert_horizontal_not_required_data_fn(worksheet, 7, 1, cover_estim_hor_list[2], heading7, 1)
    # call the insert_horizontal_not_required_data_fn function to insert the vegetation cover adjusted est values.
    if cover_estim_hor_list[3]:
        insert_horizontal_not_required_data_fn(worksheet, 8, 1, cover_estim_hor_list[3], heading7, 1)
    # call the insert_horizontal_data_fn function to insert the vegetation cover estimates total values.
    if cover_estim_hor_list[4]:
        insert_horizontal_data_fn(worksheet, 9, 1, cover_estim_hor_list[4], heading7, 1)

    # create a nested list of blank values.
    blank_list = [['BLANK', 'BLANK'], ['BLANK', 'BLANK'], ['BLANK', 'BLANK'], ['BLANK', 'BLANK']]
    # call the insert_botanical_common_names_fn function and insert the nested blank list.
    insert_botanical_common_names_fn(blank_list, 15, 2, insert_horizontal_data_fn, worksheet,
                                     heading7)
    # call the insert_botanical_common_names_fn function and insert the nested blank list.
    insert_botanical_common_names_fn(blank_list, 20, 2, insert_horizontal_data_fn, worksheet,
                                     heading7)
    # call the insert_botanical_common_names_fn function and insert the nested blank list.
    insert_botanical_common_names_fn(blank_list, 27, 2, insert_horizontal_data_fn, worksheet,
                                     heading7)
    # call the insert_botanical_common_names_fn function and insert the nested blank list.
    insert_botanical_common_names_fn(blank_list, 34, 2, insert_horizontal_data_fn, worksheet,
                                     heading7)

    # call the insert_botanical_common_names_fn function and insert the nested blank list.
    insert_botanical_common_names_fn(blank_list, 41, 2, insert_horizontal_data_fn, worksheet,
                                     heading7)

    # call the insert_botanical_common_names_fn function and insert the nested blank list.
    insert_botanical_common_names_fn(blank_list, 48, 2, insert_horizontal_data_fn, worksheet,
                                     heading7)
    if obs_data_list[7]:
        #print('obs_data_list[7]: ', obs_data_list[7])
        estimates_veg_data_list = obs_data_list[7]
        #print('estimates_veg_data_list: ', estimates_veg_data_list)

        if estimates_veg_data_list[0]:
            #print('estimates_veg_data_list[0] : ', estimates_veg_data_list[0])

            # call the insert_botanical_common_names_fn function
            insert_botanical_common_names_fn(estimates_veg_data_list[0], 15, 2, insert_horizontal_data_fn, worksheet,
                                             heading7)

            #print('estimates_veg_data_list[1]: ', estimates_veg_data_list[1])
            insert_vertical_data_fn(worksheet, 15, 4, estimates_veg_data_list[1], heading7, 1)

        if estimates_veg_data_list[2]:
            #print('estimates_veg_data_list[2] : ', estimates_veg_data_list[2])

            # call the insert_botanical_common_names_fn function
            insert_botanical_common_names_fn(estimates_veg_data_list[2], 20, 2, insert_horizontal_data_fn, worksheet,
                                             heading7)

            #print('estimates_veg_data_list[3]: ', estimates_veg_data_list[3])
            insert_vertical_data_fn(worksheet, 20, 4, estimates_veg_data_list[3], heading7, 1)

        if estimates_veg_data_list[4]:

            #print('estimates_veg_data_list[4] : ', estimates_veg_data_list[4])
            # call the insert_botanical_common_names_fn function
            insert_botanical_common_names_fn(estimates_veg_data_list[4], 27, 2, insert_horizontal_data_fn, worksheet,
                                             heading7)

            #print('estimates_veg_data_list[5]: ', estimates_veg_data_list[5])
            insert_vertical_data_fn(worksheet, 27, 4, estimates_veg_data_list[5], heading7, 1)

        if estimates_veg_data_list[6]:

            #print('estimates_veg_data_list[6] : ', estimates_veg_data_list[6])
            # call the insert_botanical_common_names_fn function
            insert_botanical_common_names_fn(estimates_veg_data_list[6], 34, 2, insert_horizontal_data_fn, worksheet,
                                             heading7)

            #print('estimates_veg_data_list[7]: ', estimates_veg_data_list[7])
            insert_vertical_data_fn(worksheet, 34, 4, estimates_veg_data_list[7], heading7, 1)

        if estimates_veg_data_list[8]:
            #print('estimates_veg_data_list[8] : ', estimates_veg_data_list[8])
            # call the insert_botanical_common_names_fn function
            insert_botanical_common_names_fn(estimates_veg_data_list[8], 41, 2, insert_horizontal_data_fn, worksheet,
                                             heading7)

            #print('estimates_veg_data_list[9]: ', estimates_veg_data_list[9])
            insert_vertical_data_fn(worksheet, 41, 4, estimates_veg_data_list[9], heading7, 1)

            #veg_totals = estimates_veg_data_list[8]

    if estimates_veg_data_list[10]:

        insert_horizontal_data_fn(worksheet, 14, 0, estimates_veg_data_list[10][:1], heading7, 1)
        insert_horizontal_data_fn(worksheet, 27, 0, estimates_veg_data_list[10][1:2], heading7, 1)
        insert_horizontal_data_fn(worksheet, 34, 0, estimates_veg_data_list[10][2:3], heading7, 1)
        insert_horizontal_data_fn(worksheet, 41, 0, estimates_veg_data_list[10][3:4], heading7, 1)
        insert_horizontal_data_fn(worksheet, 48, 0, estimates_veg_data_list[10][4:5], heading7, 1)

    #print('step10_10_create_site_cover_estimates.py COMPLETE.')
    #print('SCRIPT 13: createSiteConditionSheetP.py initiating..........')


if __name__ == '__main__':
    main_routine()
