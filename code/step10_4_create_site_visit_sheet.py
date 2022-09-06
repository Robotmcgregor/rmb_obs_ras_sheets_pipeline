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
from glob import glob
import os

def create_worksheet(workbook, worksheet_name):
    """ Create establishment worksheet and set row height.

            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet_name: string object containing worksheet name."""

    # Set up Site Establishment worksheet
    worksheet = workbook.add_worksheet(worksheet_name)

    # Set row height
    worksheet.set_default_row(56.25)

    return workbook, worksheet


def insert_sheet_headings(workbook, worksheet, heading2, heading3):
    """ Add item headings to cells as strings.

            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading2: workbook style derived  from define heading2_fn.
            :param heading3: workbook style derived  from define heading3_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.write_string('A2', 'ITEM', heading2)
    worksheet.write_string('B2', 'INPUT', heading2)
    worksheet.write_string('A3', 'RECORDER:', heading3)
    worksheet.write_string('A4', 'ESTIMATOR:', heading3)
    worksheet.write_string('A5', 'SITE ID:', heading3)
    worksheet.write_string('A6', 'DATE & TIME:', heading3)
    worksheet.write_string('A7', 'OFFSET PHOTO NUMBER:', heading3)
    worksheet.write_string('A8', 'SEASONAL CONDITIONS:', heading3)
    worksheet.write_string('A9', 'ATMOSPHERIC CONDITIONS:', heading3)
    worksheet.write_string('A10', 'SURFACE CRACKS:', heading3)
    worksheet.write_string('A11', 'SOIL MOISTURE:', heading3)
    worksheet.write_string('A12', 'BRIEF SITE DESCRIPTION:', heading3)

    return workbook, worksheet


def insert_blank_formatted_cells_fn(workbook, worksheet, heading7):
    """ Add blank formatted cells to worksheet.

            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading7: workbook style derived  from define heading7_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.write_blank('B3', None, heading7)
    worksheet.write_blank('B4', None, heading7)
    worksheet.write_blank('B5', None, heading7)
    worksheet.write_blank('B6', None, heading7)
    worksheet.write_blank('B7', None, heading7)
    worksheet.write_blank('B8', None, heading7)
    worksheet.write_blank('B9', None, heading7)
    worksheet.write_blank('B10', None, heading7)
    worksheet.write_blank('B11', None, heading7)
    worksheet.write_blank('B12', None, heading7)

    return workbook, worksheet


def merge_cells_fn(workbook, worksheet, worksheet_name, heading1):
    """ Add item headings to cells and merge.

            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param worksheet_name: string object containing the worksheet name.
            :param heading1: workbook style derived  from define heading1_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.merge_range('A1:B1', worksheet_name, heading1)

    return workbook, worksheet


def define_column_widths_fn(workbook, worksheet):
    """ define and set column widths.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.set_column('A:A', 45.73)
    worksheet.set_column('B:B', 71.09)

    return workbook, worksheet


def assets_search_fn(search_criteria, assets_dir):
    photo_name = 'BLANK'
    #file_path = (assets_dir + '\\' + search_criteria)
    file_path = os.path.join(assets_dir, search_criteria)
    for files in glob(file_path):
        _, photo_name = files.rsplit("\\", 1)

    return photo_name


def main_routine(heading1, heading2, heading3, heading7, workbook, obs_data_list, insert_vertical_data_fn,
                 insert_vertical_not_required_data_fn, site, site_dir):
    """ Create the site visit worksheet within the Rangeland Monitoring observation excel workbook.

            :param heading1: workbook style derived  from define heading1_fn.
            :param heading2: workbook style derived  from define heading2_fn.
            :param heading3: workbook style derived  from define heading3_fn.
            :param heading7: workbook style derived  from define heading7_fn.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param obs_data_list: list object with list elements containing input data for the entire workbook.
            :param insert_vertical_data_fn: function controlling a vertical data insertion loop.  """

    worksheet_name = 'Step 2 - Visit Details'

    # call the createEstablishmentWorksheet function.
    workbook, worksheet = create_worksheet(workbook, worksheet_name)

    # call the insert_sheet_headings_fn function.
    workbook, worksheet = insert_sheet_headings(workbook, worksheet, heading2, heading3)

    # call the insert_blank_formatted_cells_fn function.
    workbook, worksheet = insert_blank_formatted_cells_fn(workbook, worksheet, heading7)

    # call the merge_cells_fn function.
    workbook, worksheet = merge_cells_fn(workbook, worksheet, worksheet_name, heading1)

    # call the define_column_widths_fn(workbook) function
    workbook, worksheet = define_column_widths_fn(workbook, worksheet)

    # search for offset photo
    offset_photo = assets_search_fn('*OFF.jpg', site_dir)

    visit_data_list = obs_data_list[1]
    # call the insertDataFN function
    if visit_data_list[0]:
        visit_data_list[0][4] = offset_photo
        insert_vertical_not_required_data_fn(worksheet, 2, 1, visit_data_list[0], heading7, 1)
    if visit_data_list[1]:
        # call the insertDataFN function
        insert_vertical_not_required_data_fn(worksheet, 7, 1, visit_data_list[1], heading7, 1)

    #print('step10_4_create_site_visit.py COMPLETE.')
    #print('step10_5_create_site_disturbance_sheet.py initiating..........')




if __name__ == '__main__':
    main_routine()
