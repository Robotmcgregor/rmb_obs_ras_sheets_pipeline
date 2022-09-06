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

    return workbook, worksheet


def insert_sheet_headings_fn(workbook, worksheet, heading3, heading4, heading5, color_fill):
    """ Add item headings to cells as strings.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading3: workbook style derived  from define heading3_fn.
            :param heading4: workbook style derived  from define heading4_fn.
            :param heading5: workbook style derived  from define heading5_fn.
            :param color_fill: workbook style derived  from define colour_fill_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.write_string('A3', 'BELT WIDTH', heading3)
    worksheet.write_string('A4', 'Category', heading5)
    worksheet.write_string('B4', 'Transect 1', heading5)
    worksheet.write_string('C4', 'Transect 2', heading5)
    worksheet.write_string('D4', 'Transect 3', heading5)
    worksheet.write_string('E4', 'Transect 4', heading5)
    worksheet.write_string('F4', 'Transect 5', heading5)
    worksheet.write_string('A5', 'Juvenile shrubs (<0.5m)', heading4)
    worksheet.write_string('A10', 'Juvenile shrubs (<0.5m)', heading4)
    worksheet.write_string('B10', 'Total density (stems/ha)', heading4)
    worksheet.write_string('D10', 'Density class', heading4)
    worksheet.write_string('A6', 'Juvenile trees (<2m)', heading4)
    worksheet.write_string('A7', 'Total', heading4)
    worksheet.write_string('A11', 'Juvenile trees (<2m)', heading4)
    worksheet.write_string('B11', 'Total density (stem/ha)', heading4)
    worksheet.write_string('D11', 'Density class', heading4)
    worksheet.write_string('A12', 'Total', heading4)
    worksheet.write_string('B12', 'Total density (stems/ha)', heading4)
    worksheet.write_string('D12', 'Density class', heading4)
    worksheet.write_string('A14', "Confirmed Species Name", heading4)

    worksheet.write('F10', None, color_fill)
    worksheet.write('F11', None, color_fill)
    worksheet.write('F12', None, color_fill)
    worksheet.write('F14', None, color_fill)
    worksheet.write('F15', None, color_fill)
    worksheet.write('F16', None, color_fill)
    worksheet.write('F17', None, color_fill)
    worksheet.write('F18', None, color_fill)
    worksheet.write('F19', None, color_fill)
    worksheet.write('F20', None, color_fill)
    worksheet.write('F21', None, color_fill)
    worksheet.write('F22', None, color_fill)
    worksheet.write('F23', None, color_fill)
    worksheet.write('F24', None, color_fill)

    return workbook, worksheet


def insert_blank_formatted_cells_fn(workbook, worksheet, heading7):
    """ Add blank formatted cells to worksheet.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading7: workbook style derived  from define heading7_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.write_blank('A15', None, heading7)
    worksheet.write_blank('A16', None, heading7)
    worksheet.write_blank('A17', None, heading7)
    worksheet.write_blank('A18', None, heading7)
    worksheet.write_blank('A19', None, heading7)
    worksheet.write_blank('A20', None, heading7)
    worksheet.write_blank('A21', None, heading7)
    worksheet.write_blank('A22', None, heading7)
    worksheet.write_blank('A23', None, heading7)
    worksheet.write_blank('A24', None, heading7)

    return workbook, worksheet


def merge_cells_fn(workbook, worksheet, heading1, heading2, heading4, heading7):
    """ Add item headings to cells and merge.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading1: workbook style derived  from define heading1_fn.
            :param heading2: workbook style derived  from define heading2_fn.
            :param heading4: workbook style derived  from define heading4_fn.
            :param heading7: workbook style derived  from define heading7_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.merge_range('A1:F1', 'STEP 6 - JUVENILE STEM COUNT', heading1)
    worksheet.merge_range('A2:E2', 'Does site show appreciable thickening?', heading2)
    worksheet.merge_range('B3:F3', '', heading7)
    worksheet.merge_range('A13:F13', 'MAJOR WOODY SPECIES', heading2)
    worksheet.merge_range('B14:C14', 'Field Name', heading4)
    worksheet.merge_range('B15:C15', '', heading7)
    worksheet.merge_range('D14:E14', 'Functional Type', heading4)
    worksheet.merge_range('D15:E15', '', heading7)
    worksheet.merge_range('B16:C16', '', heading7)
    worksheet.merge_range('D16:E16', '', heading7)
    worksheet.merge_range('B17:C17', '', heading7)
    worksheet.merge_range('D17:E17', '', heading7)
    worksheet.merge_range('B18:C18', '', heading7)
    worksheet.merge_range('D18:E18', '', heading7)
    worksheet.merge_range('B19:C19', '', heading7)
    worksheet.merge_range('D19:E19', '', heading7)
    worksheet.merge_range('B20:C20', '', heading7)
    worksheet.merge_range('D20:E20', '', heading7)
    worksheet.merge_range('B21:C21', '', heading7)
    worksheet.merge_range('D21:E21', '', heading7)
    worksheet.merge_range('B22:C22', '', heading7)
    worksheet.merge_range('D22:E22', '', heading7)
    worksheet.merge_range('B23:C23', '', heading7)
    worksheet.merge_range('D23:E23', '', heading7)
    worksheet.merge_range('B24:C24', '', heading7)
    worksheet.merge_range('D24:E24', '', heading7)

    return workbook, worksheet


def define_column_widths_fn(workbook, worksheet):
    """ Define and set column widths.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.set_column('A:A', 40.00)
    worksheet.set_column('B:B', 15.00)
    worksheet.set_column('C:C', 15.00)
    worksheet.set_column('D:D', 15.00)
    worksheet.set_column('E:E', 15.00)
    worksheet.set_column('F:F', 15.00)

    return workbook, worksheet


def define_column_heights_fn(workbook, worksheet):
    """ Define and set column heights.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.set_row(0, 47.25)
    worksheet.set_row(1, 47.25)
    worksheet.set_row(2, 47.25)
    worksheet.set_row(3, 33.75)
    worksheet.set_row(4, 56.25)
    worksheet.set_row(5, 56.25)
    worksheet.set_row(6, 56.25)
    worksheet.set_row(7, 3.00)
    worksheet.set_row(8, 3.00)
    worksheet.set_row(9, 65.00)
    worksheet.set_row(10, 65.00)
    worksheet.set_row(11, 65.00)
    worksheet.set_row(12, 65.00)
    worksheet.set_row(13, 65.00)
    worksheet.set_row(14, 65.00)
    worksheet.set_row(15, 65.00)
    worksheet.set_row(16, 65.00)
    worksheet.set_row(17, 65.00)
    worksheet.set_row(18, 65.00)
    worksheet.set_row(19, 65.00)
    worksheet.set_row(20, 65.00)
    worksheet.set_row(21, 65.00)
    worksheet.set_row(22, 65.00)
    worksheet.set_row(23, 65.00)

    return workbook, worksheet


def insert_default_values_fn(workbook, worksheet, heading7):
    """ Add default values and  format worksheet cells.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading7: workbook style derived  from define heading7_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.write_number('C10', 0, heading7)
    worksheet.write_number('C11', 0, heading7)
    worksheet.write_number('C12', 0, heading7)
    worksheet.write_string('E10', 'Not observed', heading7)
    worksheet.write_string('E11', 'Not observed', heading7)
    worksheet.write_string('E12', 'Not observed', heading7)
    worksheet.write_string('F2', 'No', heading7)
    worksheet.write_string('B3', 'BLANK', heading7)
    worksheet.write_number('B5', 0, heading7)
    worksheet.write_number('C5', 0, heading7)
    worksheet.write_number('D5', 0, heading7)
    worksheet.write_number('E5', 0, heading7)
    worksheet.write_number('F5', 0, heading7)
    worksheet.write_number('B6', 0, heading7)
    worksheet.write_number('C6', 0, heading7)
    worksheet.write_number('D6', 0, heading7)
    worksheet.write_number('E6', 0, heading7)
    worksheet.write_number('F6', 0, heading7)
    worksheet.write_number('B7', 0, heading7)
    worksheet.write_number('C7', 0, heading7)
    worksheet.write_number('D7', 0, heading7)
    worksheet.write_number('E7', 0, heading7)
    worksheet.write_number('F7', 0, heading7)

    worksheet.write_string('D15', 'BLANK', heading7)
    worksheet.write_string('D16', 'BLANK', heading7)
    worksheet.write_string('D17', 'BLANK', heading7)
    worksheet.write_string('D18', 'BLANK', heading7)
    worksheet.write_string('D19', 'BLANK', heading7)
    worksheet.write_string('D20', 'BLANK', heading7)
    worksheet.write_string('D21', 'BLANK', heading7)
    worksheet.write_string('D22', 'BLANK', heading7)
    worksheet.write_string('D23', 'BLANK', heading7)
    worksheet.write_string('D24', 'BLANK', heading7)

    return workbook, worksheet


def main_routine(color_fill, heading1, heading2, heading3, heading4, heading5, heading7, workbook, obs_data_list,
                 insert_vertical_data_fn, insert_horizontal_data_fn, insert_horizontal_may_start_with_zero_fn,
                 insert_vertical_may_start_with_zero_fn):
    """

    :param insert_vertical_may_start_with_zero_fn:
    :param insert_horizontal_may_start_with_zero_fn:
    :param color_fill:
    :param heading1:
    :param heading2:
    :param heading3:
    :param heading4:
    :param heading5:
    :param heading7:
    :param workbook:
    :param obs_data_list:
    :param insert_vertical_data_fn:
    :param insert_horizontal_data_fn:
    """
    #print('script10_8_create_site_juvenile_stem_sheet.py INITIATED.')

    workSheetName = 'STEP 6 - Juvenile stem count - '

    # call the create_worksheet_fn function.
    workbook, worksheet = create_worksheet_fn(workbook, workSheetName)

    # call the insert_sheet_headings_fn function.
    workbook, worksheet = insert_sheet_headings_fn(workbook, worksheet, heading3, heading4, heading5, color_fill)

    # call the insert_blank_formatted_cells_fn function.
    workbook, worksheet = insert_blank_formatted_cells_fn(workbook, worksheet, heading7)

    # call the merge_cells_fn function.
    workbook, worksheet = merge_cells_fn(workbook, worksheet, heading1, heading2, heading4, heading7)

    # call the define_column_widths_fn function
    workbook, worksheet = define_column_widths_fn(workbook, worksheet)

    # call the define_column_heights_fn function
    workbook, worksheet = define_column_heights_fn(workbook, worksheet)

    # call the insert_default_values_fn function
    workbook, worksheet = insert_default_values_fn(workbook, worksheet, heading7)

    woodyDataList = obs_data_list[4]

    if woodyDataList[0]:
        # call the insertDataFN function to insert Yes or No for does the site show thickening.
        insert_vertical_data_fn(worksheet, 1, 5, woodyDataList[0], heading7, 1)
    if woodyDataList[1]:
        # call the insertDataFN function to insert belt width.
        insert_vertical_data_fn(worksheet, 2, 1, woodyDataList[1], heading7, 1)
    if woodyDataList[2]:
        # -------------------------------------- Transect data ---------------------------------------------------------
        # call the insertDataFN function to insert transect 1 values.
        insert_vertical_may_start_with_zero_fn(worksheet, 4, 1, woodyDataList[2], heading7, 1)
    if woodyDataList[3]:
        # call the insertDataFN function to insert transect 2 values.
        insert_vertical_may_start_with_zero_fn(worksheet, 4, 2, woodyDataList[3], heading7, 1)
    if woodyDataList[4]:
        # call the insertDataFN function to insert transect 3 values.
        insert_vertical_may_start_with_zero_fn(worksheet, 4, 3, woodyDataList[4], heading7, 1)
    if woodyDataList[5]:
        # call the insertDataFN function to insert transect 4 values.
        insert_vertical_may_start_with_zero_fn(worksheet, 4, 4, woodyDataList[5], heading7, 1)
    if woodyDataList[6]:
        # call the insertDataFN function to insert transect 5 values.
        insert_vertical_may_start_with_zero_fn(worksheet, 4, 5, woodyDataList[6], heading7, 1)

    # ----------------------------------------------- Density ----------------------------------------------------------
    if woodyDataList[7]:
        # call the insertDataFN function to insert density values
        insert_vertical_may_start_with_zero_fn(worksheet, 9, 2, woodyDataList[7], heading7, 1)

    if woodyDataList[8]:
        # call the insertDataFN function to insert density values
        insert_vertical_data_fn(worksheet, 9, 4, woodyDataList[8], heading7, 1)

    # ----------------------------------------------  Woody species ----------------------------------------------------
    if woodyDataList[9]:

        row = 14
        col = 0
        for i in woodyDataList[9]:
            # call the insert_vertical_data_fn function
            insert_horizontal_data_fn(worksheet, row, col, i, heading7, 1)

            row += 1
        if woodyDataList[10]:
            insert_vertical_data_fn(worksheet, 14, 3, woodyDataList[10], heading7, 1)

    #print('script10_8_create_site_juvenile_stem_sheet.py COMPLETE.')
    #print('script10_9_create_site_ground_layer_sheet.py initiating..........')


if __name__ == '__main__':
    main_routine()
