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


def insert_sheet_headings_fn(workbook, worksheet, heading2, heading3, color_fill):
    """ Add item headings to cells as strings.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading2: workbook style derived  from define heading2_fn.
            :param heading3: workbook style derived  from define heading3_fn.
            :param color_fill: workbook style derived  from define colour_fill_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.write_string('A2', 'ITEM', heading2)
    worksheet.write_string('A3', 'GREENESS:', heading3)
    worksheet.write_string('A4', "Comments", heading3)
    worksheet.write_string('A5', 'ABUNDANCE:', heading3)
    worksheet.write_string('A6', 'Comments', heading3)
    worksheet.write_string('A7', 'UTILISATION:', heading3)
    worksheet.write_string('A8', 'Comments', heading3)
    worksheet.write_string('A9', 'LAND CONDITION SCORE:', heading3)
    worksheet.write('A10', None, color_fill)

    return workbook, worksheet


def merge_cells_fn(workbook, worksheet, heading1, heading2, heading3, heading4, heading7, color_fill):
    """ Add item headings to cells and merge.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading1: workbook style derived  from define heading1_fn.
            :param heading2: workbook style derived  from define heading2_fn.
            :param heading3: workbook style derived  from define heading3_fn.
            :param heading4: workbook style derived  from define heading4_fn.
            :param heading7: workbook style derived  from define heading7_fn.
            :param color_fill: workbook style derived  from define colour_fill_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.merge_range('A1:L1', 'STEP 8 - SITE CONDITION CHARACTERISTICS', heading1)
    worksheet.merge_range('A11:A12', 'VISIT ASSESSMENT NOTES:', heading3)
    worksheet.merge_range('B2:L2', 'INPUT', heading2)
    worksheet.merge_range('B3:L3', '', heading7)
    worksheet.merge_range('B4:L4', '', heading7)
    worksheet.merge_range('B5:L5', '', heading7)
    worksheet.merge_range('B6:L6', '', heading7)
    worksheet.merge_range('B7:L7', '', heading7)
    worksheet.merge_range('B8:L8', '', heading7)
    worksheet.merge_range('G9:L9', 'ASSESSMENT SCORE (good,fair, poor)', heading4)
    worksheet.merge_range('B9:F9', 'LAND COND GUIDE (A, B, C, D)', heading4)
    worksheet.merge_range('B10:F10', '', heading7)
    worksheet.merge_range('G10:L10', '', heading7)
    worksheet.merge_range('B11:L12', '', heading7)
    worksheet.merge_range('A13:L13', '', color_fill)
    worksheet.merge_range('B14:L14', '', heading7)
    worksheet.merge_range('B15:L15', '', heading7)
    worksheet.merge_range('B16:L16', '', heading7)
    worksheet.merge_range('B17:L17', '', heading7)
    worksheet.merge_range('B18:L18', '', heading7)

    return workbook, worksheet


def define_column_widths_fn(workbook, worksheet):
    """ Define and set column widths.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.set_column('A:A', 37.82)
    worksheet.set_column('B:B', 9.09)
    worksheet.set_column('C:C', 8.45)
    worksheet.set_column('D:D', 10.91)
    worksheet.set_column('E:E', 6.27)
    worksheet.set_column('F:F', 8.00)
    worksheet.set_column('G:G', 8.36)
    worksheet.set_column('H:H', 10.18)
    worksheet.set_column('I:I', 8.18)
    worksheet.set_column('J:J', 0.61)
    worksheet.set_column('K:K', 0.61)
    worksheet.set_column('L:L', 0.61)

    return workbook, worksheet


def main_routine(color_fill, heading1, heading2, heading3, heading4, heading7, workbook, obs_data_list, site,
                 insert_vertical_data_fn, insert_horizontal_data_fn):
    """

    :param color_fill:
    :param heading1:
    :param heading2:
    :param heading3:
    :param heading4:
    :param heading7:
    :param workbook:
    :param obs_data_list:
    :param site:
    :param insert_vertical_data_fn:
    :param insert_horizontal_data_fn:
    """
    worksheet_name = 'Step 8 - Site Condition'

    # call the create_worksheet_fn function.
    workbook, worksheet = create_worksheet_fn(workbook, worksheet_name)

    # call the insert_sheet_headings_fn function.
    workbook, worksheet = insert_sheet_headings_fn(workbook, worksheet, heading2, heading3, color_fill)

    # call the merge_cells_fn function.
    workbook, worksheet = merge_cells_fn(workbook, worksheet, heading1, heading2, heading3, heading4, heading7,
                                         color_fill)

    # call the define_column_widths_fn function
    workbook, worksheet = define_column_widths_fn(workbook, worksheet)

    condition_data_list = obs_data_list[8]

    if condition_data_list[0]:
        # call the insertDataFN function
        insert_vertical_data_fn(worksheet, 2, 1, condition_data_list[0], heading7, 1)

    if condition_data_list[1]:
        # call the insertDataFN function
        insert_horizontal_data_fn(worksheet, 9, 1, condition_data_list[1], heading7, 1)

        if condition_data_list[1][0] == 'A':
            score = 'EXCELLENT'
        elif condition_data_list[1][0] == 'B':
            score = 'GOOD'
        elif condition_data_list[1][0] == 'C':
            score = ' FAIR'
        elif condition_data_list[1][0] == 'D':
            score = 'POOR'
        else:
            score = 'ERROR'

        # call the insertDataFN function
        insert_vertical_data_fn(worksheet, 9, 6, [score], heading7, 1)

    if condition_data_list[2]:
        # call the insertDataFN function
        insert_vertical_data_fn(worksheet, 10, 1, condition_data_list[2], heading7, 1)

    workbook.close()
    #('step10_11_create_condition_sheet.py COMPLETE.')
    #print(site, ' workbook complete!!!!!!')


if __name__ == '__main__':
    main_routine()
