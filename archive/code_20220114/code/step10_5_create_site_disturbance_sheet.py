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
import os


def create_worksheet_fn(workbook, worksheet_name):
    """ Create worksheet and set row height.

            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet_name: string object containing worksheet name.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    # Set up Site Establishment worksheet
    worksheet = workbook.add_worksheet(worksheet_name)

    # Set row height
    worksheet.set_default_row(57.00)

    return workbook, worksheet


def insert_sheet_headings(workbook, worksheet, heading2, heading3, heading4, heading5, color_fill):
    """ Add item headings to cells as strings.

            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading2: workbook style derived  from define heading2_fn.
            :param heading3: workbook style derived  from define heading3_fn.
            :param heading4: workbook style derived  from define heading4_fn.
            :param heading5: workbook style derived  from define heading5_fn.
            :param color_fill: workbook style derived  from define colour_fill_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.write_string('A2', 'ITEM', heading2)
    worksheet.write_string('A3', 'CLEARING:', heading3)
    worksheet.write_string('A5', 'CYCLONE/STORM:', heading3)
    worksheet.write_string('A7', 'DIEBACK', heading3)
    worksheet.write_string('A9', 'ADJACENT INFRASTRUCTURE:', heading3)
    worksheet.write_string('A10', 'COMMENTS:', heading3)
    worksheet.write_string('A11', 'DISTANCE TO INFRASTRUCTURE:', heading3)
    worksheet.write_string('A12', 'WILD ANIMAL ACTIVITY:', heading3)
    worksheet.write_string('B12', 'Camel', heading5)
    worksheet.write_string('C12', 'Rabbit', heading5)
    worksheet.write_string('D12', 'Donkey', heading5)
    worksheet.write_string('E12', 'Horse', heading5)
    worksheet.write_string('F12', 'Pig', heading5)
    worksheet.write_string('G12', 'Buffalo', heading5)
    worksheet.write_string('H12', 'Native herbivore', heading5)
    worksheet.write_string('I12', 'Other', heading5)
    worksheet.write_string('A13', 'ACTIVE', heading3)
    worksheet.write_string('A14', 'EVIDENCE AND DESCRIPTION:', heading3)
    worksheet.write_string('A17', 'FREQUENCY', heading3)
    worksheet.write_string('A18', 'INTENSITY', heading3)
    worksheet.write_string('A20', 'CATTLE ACTIVITY:', heading3)
    worksheet.write_string('A22', 'IS THIS AN ERODIBLE SOIL?', heading3)
    worksheet.write_string('B23', 'Severity', heading4)
    worksheet.write_string('A24', 'SCALDING - wind or water', heading3)
    worksheet.write_string('A25', 'WINDSHEETING', heading3)
    worksheet.write_string('A26', 'WATERSHEETING', heading3)
    worksheet.write_string('A27', 'RILLING', heading3)
    worksheet.write_string('A28', 'GULLYING', heading3)
    worksheet.write_string('A29', 'EROSION COMMENTS AND PHOTO NUMBERS', heading3)
    worksheet.write_string('A30', 'WEEDS', heading3)
    worksheet.write_string('A31', 'OTHER DISTURBANCE COMMENTS', heading3)

    worksheet.write('A4', None, color_fill)
    worksheet.write('A8', None, color_fill)
    worksheet.write('A16', None, color_fill)
    worksheet.write('A19', None, color_fill)
    worksheet.write('A23', None, color_fill)

    return workbook, worksheet


def insert_blank_formatted_cells_fn(workbook, worksheet, heading7):
    """ Add blank formatted cells to worksheet.

            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading7: workbook style derived  from define heading7_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.write_blank('B13', None, heading7)
    worksheet.write_blank('C13', None, heading7)
    worksheet.write_blank('D13', None, heading7)
    worksheet.write_blank('E13', None, heading7)
    worksheet.write_blank('F13', None, heading7)
    worksheet.write_blank('G13', None, heading7)
    worksheet.write_blank('H13', None, heading7)
    worksheet.write_blank('I13', None, heading7)
    worksheet.write_blank('K20', None, heading7)
    worksheet.write_blank('B24', None, heading7)
    worksheet.write_blank('B25', None, heading7)
    worksheet.write_blank('B26', None, heading7)
    worksheet.write_blank('B27', None, heading7)
    worksheet.write_blank('B28', None, heading7)

    worksheet.write_string('B31', 'BLANK', heading7)

    return workbook, worksheet


def merge_cells_fn(workbook, worksheet, worksheet_name, heading1, heading2, heading4, heading7):
    """ Add item headings to cells and merge.

            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param worksheet_name: string object containing the worksheet name.
            :param heading1: workbook style derived  from define heading1_fn.
            :param heading2: workbook style derived  from define heading2_fn.
            :param heading4: workbook style derived  from define heading4_fn.
            :param heading7: workbook style derived  from define heading7_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.merge_range('A1:K1', worksheet_name, heading1)
    worksheet.merge_range('B2:K2', 'INPUT', heading2)
    worksheet.merge_range('B3:C3', '', heading7)
    worksheet.merge_range('D3:E3', 'Photo numbers', heading4)
    worksheet.merge_range('F3:K3', '', heading7)
    worksheet.merge_range('B4:C4', 'Comments', heading4)
    worksheet.merge_range('D4:K4', '', heading7)
    worksheet.merge_range('B5:C5', '', heading7)
    worksheet.merge_range('D5:E5', 'Photo numbers', heading4)
    worksheet.merge_range('F5:K5', '', heading7)
    worksheet.merge_range('B6:C6', 'Comments', heading4)
    worksheet.merge_range('D6:K6', '', heading7)
    worksheet.merge_range('B7:C7', '', heading7)
    worksheet.merge_range('D7:E7', 'Photo numbers', heading4)
    worksheet.merge_range('F7:K7', '', heading7)
    worksheet.merge_range('B8:C8', 'Comments', heading4)
    worksheet.merge_range('D8:K8', '', heading7)
    worksheet.merge_range('B9:K9', '', heading7)
    worksheet.merge_range('B10:K10', '', heading7)
    worksheet.merge_range('B11:K11', '', heading7)
    worksheet.merge_range('B14:K14', '', heading7)
    worksheet.merge_range('A15:K15', 'FIRE', heading2)
    worksheet.merge_range('B16:F16', 'NORTH REGION', heading4)
    worksheet.merge_range('B17:F17', '', heading7)
    worksheet.merge_range('G17:K17', '', heading7)
    worksheet.merge_range('B18:F18', '', heading7)
    worksheet.merge_range('G16:K16', 'SOUTH REGION', heading4)
    worksheet.merge_range('G18:K18', '', heading7)
    worksheet.merge_range('B19:K19', '')  # No formatting required
    worksheet.merge_range('B20:C20', 'CATTLE PADS', heading4)
    worksheet.merge_range('D20:F20', '', heading7)
    worksheet.merge_range('G20:J20', 'TRAMPLING', heading4)
    worksheet.merge_range('A21:K21', 'EROSION', heading2)
    worksheet.merge_range('B22:K22', '', heading7)
    worksheet.merge_range('C23:D23', 'Stability', heading4)
    worksheet.merge_range('E23:K23', '', heading7)
    worksheet.merge_range('C24:D24', '', heading7)
    worksheet.merge_range('E24:K24', '', heading7)
    worksheet.merge_range('C25:D25', '', heading7)
    worksheet.merge_range('E25:K25', '', heading7)
    worksheet.merge_range('C26:D26', '', heading7)
    worksheet.merge_range('E26:K26', '', heading7)
    worksheet.merge_range('C27:D27', '', heading7)
    worksheet.merge_range('E27:K27', '', heading7)
    worksheet.merge_range('C28:D28', '', heading7)
    worksheet.merge_range('E28:K28', '', heading7)
    worksheet.merge_range('B29:K29', '', heading7)
    worksheet.merge_range('B30:K30', '', heading7)
    worksheet.merge_range('B31:K31', '', heading7)

    return workbook, worksheet


def define_column_widths_fn(workbook, worksheet):
    """ define and set column widths.

            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.set_column('A:A', 37.91)
    worksheet.set_column('B:B', 12.27)
    worksheet.set_column('C:C', 8.45)
    worksheet.set_column('D:D', 10.82)
    worksheet.set_column('E:E', 8.14)
    worksheet.set_column('F:F', 8.09)
    worksheet.set_column('G:G', 8.45)
    worksheet.set_column('H:H', 12.14)
    worksheet.set_column('I:I', 8.14)
    worksheet.set_column('J:J', 6.82)
    worksheet.set_column('K:K', 17.55)

    return workbook, worksheet


def list_of_photos_fn(site_dir, search_criteria, photo_date):
    """ Search a directory for a file (search criteria and return a filename variable.

            :param site_dir: string object containing the path to site directory.
            :param search_criteria: wildcard variable.
            :return: file_name string object containing the matching file name or None. """

    # split site_dir into path and site name
    _, site_name = site_dir.rsplit('_', 1)
    photo_list = []
    for root, dirs, files in os.walk(site_dir):
        # initiate a range loop - each variable may have up to three photographs.
        for i in range(3):
            # define the search criteria
            search = site_name + '_' + str(photo_date) + '_' + search_criteria + str(i + 1) + '.jpg'
            if search in files:
                file_name = search
                # if located append file name to list
                photo_list.append(file_name)

    if photo_list:
        # join lists into a string
        file_name = ', '.join(photo_list)

    else:
        file_name = 'BLANK'

    return file_name


def main_routine(color_fill, heading1, heading2, heading3, heading4, heading5, heading7, workbook, obs_data_list,
                 site_dir, insert_vertical_data_fn, insert_horizontal_data_fn, insert_vertical_not_required_data_fn,
                 photo_date):
    """This script creates the disturbance worksheet within the current workbook.

            :param insert_vertical_not_required_data_fn:
            :param photo_date: integer object containing the date the photo was taken.
            :param color_fill: workbook style derived  from define colour_fill_fn.
            :param heading1: workbook style derived  from define heading1_fn.
            :param heading2: workbook style derived  from define heading2_fn.
            :param heading3: workbook style derived  from define heading3_fn.
            :param heading4: workbook style derived  from define heading4_fn.
            :param heading5: workbook style derived  from define heading5_fn.
            :param heading7: workbook style derived  from define heading7_fn.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param obs_data_list: list object with list elements containing input data for the entire workbook.
            :param site_dir: string object containing the path to the current site directory.
            :param insert_vertical_data_fn: function controlling a vertical data insertion loop.
            :param insert_horizontal_data_fn: function controlling a horizontal data insertion loop. """


    worksheet_name = 'Step 3 - Disturbance Details'

    # call the create_worksheet_fn function.
    workbook, worksheet = create_worksheet_fn(workbook, worksheet_name)

    # call the insert_sheet_headings_fn function.
    workbook, worksheet = insert_sheet_headings(workbook, worksheet, heading2, heading3, heading4, heading5, color_fill)

    # call the insert_blank_formatted_cells_fn function.
    workbook, worksheet = insert_blank_formatted_cells_fn(workbook, worksheet, heading7)

    # call the merge_cells_fn function.
    workbook, worksheet = merge_cells_fn(workbook, worksheet, worksheet_name, heading1, heading2, heading4, heading7)

    # call the define_column_widths_fn function
    workbook, worksheet = define_column_widths_fn(workbook, worksheet)

    disturbance_data_list = obs_data_list[2]
    if disturbance_data_list[0]:
        # call the insertDataFN function and insert present or absent values for clearing cyclone and dieback
        insert_vertical_data_fn(worksheet, 2, 1, disturbance_data_list[0], heading7, 2)
    if disturbance_data_list[1]:
        # call the insertDataFN function to insert comments for clearing, cyclone and dieback.
        insert_vertical_data_fn(worksheet, 3, 3, disturbance_data_list[2], heading7, 2)
    if disturbance_data_list[2]:
        # call the insertDataFN function to insert photo numbers for clearing, cyclone and dieback.
        insert_vertical_not_required_data_fn(worksheet, 2, 5, disturbance_data_list[1], heading7, 2)

    if disturbance_data_list[3]:
        dist_list = disturbance_data_list[3]

        if dist_list[0] == 'BLANK':
            pass
            # call the insertDataFN function to insert adjacent infrastructure, comments and distance to infrastructure.
            #insert_vertical_data_fn(worksheet, 8, 1, [dist_list[0]], heading7, 1)

        if dist_list[1]== 'BLANK':
            # call the insertDataFN function to insert adjacent infrastructure, comments and distance to infrastructure.
            insert_vertical_data_fn(worksheet, 9, 1, [dist_list[1]], heading7, 1)

        if dist_list[2] == 'BLANK':
            pass
            # call the insertDataFN function to insert adjacent infrastructure, comments and distance to infrastructure.
            #insert_vertical_data_fn(worksheet, 8, 1, [dist_list[0]], heading7, 1)

    if disturbance_data_list[4]:
        # call the insertDataFN function to insert true or false inputs for feral activity.
        insert_horizontal_data_fn(worksheet, 12, 1, disturbance_data_list[4], heading7, 1)
    if disturbance_data_list[5]:
        # call the insertDataFN function to insert evidence and description for feral animals
        insert_horizontal_data_fn(worksheet, 13, 1, disturbance_data_list[5], heading7, 1)
    if disturbance_data_list[6]:
        # call the insertDataFN function to insert northern region fire.
        insert_vertical_data_fn(worksheet, 16, 1, disturbance_data_list[6], heading7, 1)
    if disturbance_data_list[7]:
        # call the insertDataFN function to insert southern region fire.
        insert_vertical_data_fn(worksheet, 16, 6, disturbance_data_list[7], heading7, 1)
    if disturbance_data_list[8]:
        # call the insertDataFN function to insert cattle activity Present or Absent.
        insert_horizontal_data_fn(worksheet, 19, 3, disturbance_data_list[8], heading7, 7)
    if disturbance_data_list[9]:
        # call the insertDataFN function to insert if the soil is erodible - Yes or No
        insert_vertical_data_fn(worksheet, 21, 1, disturbance_data_list[9], heading7, 1)
    if disturbance_data_list[10]:
        # call the insertDataFN function to insert erosion severity.
        insert_vertical_data_fn(worksheet, 23, 1, disturbance_data_list[10], heading7, 1)
    if disturbance_data_list[11]:
        # call the insertDataFN function to insert stability.
        insert_vertical_data_fn(worksheet, 23, 2, disturbance_data_list[11], heading7, 1)
    if disturbance_data_list[12]:
        # call the insertDataFN function to insert erosion comments and photo numbers, weeds present or absent and
        # other disturbance comments.
        insert_vertical_data_fn(worksheet, 28, 1, disturbance_data_list[12], heading7, 1)

    # ---------------------------- disturbance photo_url_extraction_fn numbers -----------------------------------------

    clearing_photo = list_of_photos_fn(site_dir, 'CLEARING', photo_date)
    if clearing_photo:
        # call the insert_vertical_not_required_data_fn function and insert clearing photo_url_extraction_fn file name
        insert_vertical_not_required_data_fn(worksheet, 2, 5, [clearing_photo], heading7, 1)

    cyclone_photo = list_of_photos_fn(site_dir, 'CYCLONE', photo_date)
    if cyclone_photo:
        # call the insert_vertical_not_required_data_fn function and insert clearing photo_url_extraction_fn file name
        insert_vertical_not_required_data_fn(worksheet, 4, 5, [clearing_photo], heading7, 1)

    dieback_photo = list_of_photos_fn(site_dir, 'DIEBACK', photo_date)
    if dieback_photo:
        # call the insert_vertical_not_required_data_fn function and insert clearing photo_url_extraction_fn file name
        insert_vertical_not_required_data_fn(worksheet, 6, 5, [dieback_photo], heading7, 1)

    if disturbance_data_list[12]:
        # todo check if erosion comment with photo works
        erosion_photo = list_of_photos_fn(site_dir, 'EROSION', photo_date)
        if disturbance_data_list[12][0] == 'BLANK':
            if erosion_photo:
                # call the insertDataFN function and insert clearing photo_url_extraction_fn file name
                insert_vertical_data_fn(worksheet, 28, 1, [erosion_photo], heading7, 1)
        else:
            if erosion_photo:
                erosion_comment = disturbance_data_list[12][0] + '. Photo numbers: '
                # call the insertDataFN function and insert clearing photo_url_extraction_fn file name
                insert_vertical_data_fn(worksheet, 28, 1, [erosion_comment], heading7, 1)
            else:
                pass

        if disturbance_data_list[12][1] == 'absent':
            insert_vertical_data_fn(worksheet, 29, 1, ['Absent'], heading7, 1)


        if disturbance_data_list[12][2] == '':
            insert_vertical_data_fn(worksheet, 30, 1, ['BLANK'], heading7, 1)

    else:
        pass




if __name__ == '__main__':
    main_routine()
