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


# I have rearranged the order of this sheet. If there are errors it could be due to this.


def create_worksheet_fn(workbook, worksheet_name):
    """ Create worksheet and set row height.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet_name: string object containing worksheet name."""

    # Set up Site Establishment worksheet
    worksheet = workbook.add_worksheet(worksheet_name)

    # Set row height
    worksheet.set_default_row(56.25)

    return workbook, worksheet


def insert_sheet_headings_fn(workbook, worksheet, heading4, color_fill):
    """ Add item headings to cells as strings.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading4: workbook style derived  from define heading4_fn.
            :param color_fill: workbook style derived  from define colour_fill_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.write_string('B5', 'Total site %', heading4)
    worksheet.write_string('C5', 'Vegetation cover %', heading4)
    worksheet.write_string('D5', 'Total site %', heading4)
    worksheet.write_string('E5', 'Vegetation cover %', heading4)
    worksheet.write_string('A6', 'Perennial grass', heading4)
    worksheet.write_string('A7', 'Annual grass', heading4)
    worksheet.write_string('A8', 'Perennial forb', heading4)
    worksheet.write_string('A9', 'Annual forb', heading4)
    worksheet.write_string('A10', 'Unspecified plant', heading4)
    worksheet.write_string('A11', 'Total veg', heading4)
    worksheet.write_string('A12', 'Litter', heading4)
    worksheet.write_string('A13', 'Bare Ground', heading4)
    worksheet.write('A4', None, color_fill)
    worksheet.write('A5', None, color_fill)
    worksheet.write('A2', None, color_fill)

    return workbook, worksheet


def insert_blank_formatted_cells_fn(workbook, worksheet, heading7):
    """ Add blank formatted cells to worksheet.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading7: workbook style derived  from define heading7_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.write_blank('C3', None, heading7)
    worksheet.write_blank('B6', None, heading7)
    worksheet.write_blank('B7', None, heading7)
    worksheet.write_blank('B8', None, heading7)
    worksheet.write_blank('B9', None, heading7)
    worksheet.write_blank('B10', None, heading7)
    worksheet.write_blank('B11', None, heading7)
    worksheet.write_blank('B12', None, heading7)
    worksheet.write_blank('B13', None, heading7)
    worksheet.write_blank('C6', None, heading7)
    worksheet.write_blank('C7', None, heading7)
    worksheet.write_blank('C8', None, heading7)
    worksheet.write_blank('C9', None, heading7)
    worksheet.write_blank('C10', None, heading7)
    worksheet.write_blank('D6', None, heading7)
    worksheet.write_blank('D7', None, heading7)
    worksheet.write_blank('D8', None, heading7)
    worksheet.write_blank('D9', None, heading7)
    worksheet.write_blank('D10', None, heading7)
    worksheet.write_blank('D11', None, heading7)
    worksheet.write_blank('D12', None, heading7)
    worksheet.write_blank('D13', None, heading7)
    worksheet.write_blank('E6', None, heading7)
    worksheet.write_blank('E7', None, heading7)
    worksheet.write_blank('E8', None, heading7)
    worksheet.write_blank('E9', None, heading7)
    worksheet.write_blank('E10', None, heading7)

    worksheet.write_number('B6', 0, heading7)
    worksheet.write_number('B7', 0, heading7)
    worksheet.write_number('B8', 0, heading7)
    worksheet.write_number('B9', 0, heading7)
    worksheet.write_number('B10', 0, heading7)
    worksheet.write_number('B11', 0, heading7)
    worksheet.write_number('B12', 0, heading7)
    worksheet.write_number('B13', 0, heading7)

    worksheet.write_number('C6', 0, heading7)
    worksheet.write_number('C7', 0, heading7)
    worksheet.write_number('C8', 0, heading7)
    worksheet.write_number('C9', 0, heading7)
    worksheet.write_number('C10', 0, heading7)

    worksheet.write_number('D6', 0, heading7)
    worksheet.write_number('D7', 0, heading7)
    worksheet.write_number('D8', 0, heading7)
    worksheet.write_number('D9', 0, heading7)
    worksheet.write_number('D10', 0, heading7)
    worksheet.write_number('D11', 0, heading7)
    worksheet.write_number('D12', 0, heading7)
    worksheet.write_number('D13', 0, heading7)

    worksheet.write_number('E6', 0, heading7)
    worksheet.write_number('E7', 0, heading7)
    worksheet.write_number('E8', 0, heading7)
    worksheet.write_number('E9', 0, heading7)
    worksheet.write_number('E10', 0, heading7)

    return workbook, worksheet


def merge_cells_fn(workbook, worksheet, heading1, heading4):
    """ Add item headings to cells and merge.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading1: workbook style derived  from define heading1_fn.
            :param heading4: workbook style derived  from define heading4_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.merge_range('A1:E1', 'GROUND LAYER COMPOSITION', heading1)
    worksheet.merge_range('A3:B3', 'DO THE TRANSECTS ACCURATELY REPRESENT THE SITE?', heading4)
    worksheet.merge_range('B4:C4', 'Transect data', heading4)
    worksheet.merge_range('D4:E4', 'Cover estimates', heading4)

    return workbook, worksheet


def define_column_widths_fn(workbook, worksheet):
    """ define and set column widths.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.set_column('A:A', 30.27)
    worksheet.set_column('B:B', 30.27)
    worksheet.set_column('C:C', 30.27)
    worksheet.set_column('D:D', 30.27)
    worksheet.set_column('E:E', 30.27)

    return workbook, worksheet


def main_routine(color_fill, heading1, heading4, heading7,
                 workbook, obs_data_list, insert_vertical_data_fn, insert_horizontal_may_start_with_zero_fn,
                 insert_vertical_may_start_with_zero_fn):
    """
    :param insert_vertical_may_start_with_zero_fn:
    :param insert_horizontal_may_start_with_zero_fn:
    :param color_fill:
    :param heading1:
    :param heading4:
    :param heading7:
    :param workbook:
    :param obs_data_list:
    :param insert_vertical_data_fn:
    """

    #print('step10_9_create_site_ground_layer.py INITIATED.')

    worksheet_name = 'Output 1 - Ground layer composi'

    # call the create_worksheet_fn function.
    workbook, worksheet = create_worksheet_fn(workbook, worksheet_name)

    # call the insert_sheet_headings_fn function.
    workbook, worksheet = insert_sheet_headings_fn(workbook, worksheet, heading4, color_fill)

    # call the insert_blank_formatted_cells_fn function.
    workbook, worksheet = insert_blank_formatted_cells_fn(workbook, worksheet, heading7)

    # call the merge_cells_fn function.
    workbook, worksheet = merge_cells_fn(workbook, worksheet, heading1, heading4)

    # call the define_column_widths_fn function
    workbook, worksheet = define_column_widths_fn(workbook, worksheet)

    cover_data_list = obs_data_list[5]

    if cover_data_list[0]:
        # call the insertDataFN function
        insert_vertical_may_start_with_zero_fn(worksheet, 2, 2, cover_data_list[0], heading7, 1)
    if cover_data_list[1]:
        # call the insertDataFN function
        insert_vertical_may_start_with_zero_fn(worksheet, 5, 1, cover_data_list[1], heading7, 1)
    if cover_data_list[2]:
        # call the insertDataFN function
        insert_vertical_may_start_with_zero_fn(worksheet, 5, 2, cover_data_list[2], heading7, 1)
    if cover_data_list[3]:
        # call the insertDataFN function
        insert_vertical_may_start_with_zero_fn(worksheet, 5, 3, cover_data_list[3], heading7, 1)
    if cover_data_list[4]:
        # call the insertDataFN function
        insert_vertical_may_start_with_zero_fn(worksheet, 5, 4, cover_data_list[4], heading7, 1)

    #print('step10_9_create_site_ground_layer.py COMPLETE.')
    #print('step10_10_create_site_cover_estimates.py initiating..........')


if __name__ == '__main__':
    main_routine()
