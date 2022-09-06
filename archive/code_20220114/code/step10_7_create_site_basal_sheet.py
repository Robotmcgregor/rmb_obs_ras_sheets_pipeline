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


def create_worksheet(workbook, worksheet_name):
    """ Create establishment worksheet and set row height.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet_name: string object containing worksheet name."""

    # Set up Site Establishment worksheet #
    worksheet = workbook.add_worksheet(worksheet_name)

    return workbook, worksheet


def insert_sheet_headings_fn(workbook, worksheet, heading4, heading5, color_fill):
    """ Add item headings to cells as strings.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading4: workbook style derived  from define heading4_fn.
            :param heading5: workbook style derived  from define heading5_fn.
            :param color_fill: workbook style derived  from define colour_fill_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.write_string('A3', 'Location', heading5)
    worksheet.write_string('A4', 'Basal factor', heading5)
    worksheet.write_string('B5', 'Live', heading5)
    worksheet.write_string('C5', 'Dead', heading5)
    worksheet.write_string('D5', 'Live', heading5)
    worksheet.write_string('E5', 'Dead', heading5)
    worksheet.write_string('F5', 'Live', heading5)
    worksheet.write_string('G5', 'Dead', heading5)
    worksheet.write_string('H5', 'Live', heading5)
    worksheet.write_string('I5', 'Dead', heading5)
    worksheet.write_string('J5', 'Live', heading5)
    worksheet.write_string('K5', 'Dead', heading5)
    worksheet.write_string('L5', 'Live', heading5)
    worksheet.write_string('M5', 'Dead', heading5)
    worksheet.write_string('N5', 'Live', heading5)
    worksheet.write_string('O5', 'Dead', heading5)
    worksheet.write_string('A7', 'TREES', heading4)
    worksheet.write_string('A8', 'SHRUBS', heading4)
    worksheet.write_string('A17', 'ADULT TREES (>2m)', heading4)
    worksheet.write_string('A18', 'ADULT SHRUBS (>2m)', heading4)
    worksheet.write_string('A19', 'TOTAL', heading4)
    worksheet.write('A5', None, color_fill)
    worksheet.write('A6', None, color_fill)
    worksheet.write('A16', None, color_fill)

    return workbook, worksheet


def insert_blank_formatted_cells_fn(workbook, worksheet, heading7):
    """ Add blank formatted cells to worksheet.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading7: workbook style derived  from define heading7_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.write_blank('B7', None, heading7)
    worksheet.write_blank('C7', None, heading7)
    worksheet.write_blank('D7', None, heading7)
    worksheet.write_blank('E7', None, heading7)
    worksheet.write_blank('F7', None, heading7)
    worksheet.write_blank('G7', None, heading7)
    worksheet.write_blank('H7', None, heading7)
    worksheet.write_blank('I7', None, heading7)
    worksheet.write_blank('J7', None, heading7)
    worksheet.write_blank('K7', None, heading7)
    worksheet.write_blank('L7', None, heading7)
    worksheet.write_blank('M7', None, heading7)
    worksheet.write_blank('N7', None, heading7)
    worksheet.write_blank('O7', None, heading7)
    worksheet.write_blank('B8', None, heading7)
    worksheet.write_blank('C8', None, heading7)
    worksheet.write_blank('D8', None, heading7)
    worksheet.write_blank('E8', None, heading7)
    worksheet.write_blank('F8', None, heading7)
    worksheet.write_blank('G8', None, heading7)
    worksheet.write_blank('H8', None, heading7)
    worksheet.write_blank('I8', None, heading7)
    worksheet.write_blank('J8', None, heading7)
    worksheet.write_blank('K8', None, heading7)
    worksheet.write_blank('L8', None, heading7)
    worksheet.write_blank('M8', None, heading7)
    worksheet.write_blank('N8', None, heading7)
    worksheet.write_blank('O8', None, heading7)

    return workbook, worksheet


def merge_cells_fn(workbook, worksheet, heading1, heading2, heading4, heading5, heading7, heading8, color_fill):
    """ Add item headings to cells and merge.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading1: workbook style derived  from define heading1_fn.
            :param heading2: workbook style derived  from define heading2_fn.
            :param heading4: workbook style derived  from define heading4_fn.
            :param heading5: workbook style derived  from define heading5_fn.
            :param heading7: workbook style derived  from define heading7_fn.
            :param heading8: workbook style derived  from define heading8_fn.
            :param color_fill: workbook style derived  from define colour_fill_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.merge_range('A1:K1', 'STEP 5 - BASAL SWEEPS', heading1)
    worksheet.merge_range('L2:O2', '', heading7)
    worksheet.merge_range('A2:K2', 'Does site have recordable basal area?', heading4)
    worksheet.merge_range('B3:C3', 'North', heading5)
    worksheet.merge_range('D3:E3', 'Centre', heading5)
    worksheet.merge_range('F3:G3', 'South', heading5)
    worksheet.merge_range('H3:I3', 'South East', heading5)
    worksheet.merge_range('J3:K3', 'North West', heading5)
    worksheet.merge_range('L3:M3', 'North East', heading5)
    worksheet.merge_range('N3:O3', 'South West', heading5)
    worksheet.merge_range('B4:C4', '', heading7)
    worksheet.merge_range('D4:E4', '', heading7)
    worksheet.merge_range('F4:G4', '', heading7)
    worksheet.merge_range('H4:I4', '', heading7)
    worksheet.merge_range('J4:K4', '', heading7)
    worksheet.merge_range('L4:M4', '', heading7)
    worksheet.merge_range('N4:O4', '', heading7)
    worksheet.merge_range('B16:E16', 'BASAL AREA (m2/ha)', heading4)
    worksheet.merge_range('B17:E17', '', heading7)
    worksheet.merge_range('B18:E18', '', heading7)
    worksheet.merge_range('B19:E19', '', heading7)
    worksheet.merge_range('A20:O20', '', color_fill)
    worksheet.merge_range('A21:O21', 'Major woody species', heading2)
    worksheet.merge_range('A22:E22', 'Confirmed Species name', heading4)
    worksheet.merge_range('F22:K22', 'Field name', heading4)
    worksheet.merge_range('L22:O22', 'Functional type', heading4)
    worksheet.merge_range('A23:E23', '', heading8)
    worksheet.merge_range('A24:E24', '', heading8)
    worksheet.merge_range('A25:E25', '', heading8)
    worksheet.merge_range('A26:E26', '', heading8)
    worksheet.merge_range('A27:E27', '', heading8)
    worksheet.merge_range('A28:E28', '', heading8)
    worksheet.merge_range('A29:E29', '', heading8)
    worksheet.merge_range('A30:E30', '', heading8)
    worksheet.merge_range('A31:E31', '', heading8)
    worksheet.merge_range('A32:E32', '', heading8)
    worksheet.merge_range('F16:O16', '', color_fill)
    worksheet.merge_range('F23:K23', '', heading7)
    worksheet.merge_range('F24:K24', '', heading7)
    worksheet.merge_range('F25:K25', '', heading7)
    worksheet.merge_range('F26:K26', '', heading7)
    worksheet.merge_range('F27:K27', '', heading7)
    worksheet.merge_range('F28:K28', '', heading7)
    worksheet.merge_range('F29:K29', '', heading7)
    worksheet.merge_range('F30:K30', '', heading7)
    worksheet.merge_range('F31:K31', '', heading7)
    worksheet.merge_range('F32:K32', '', heading7)
    worksheet.merge_range('L23:O23', '', heading7)
    worksheet.merge_range('L24:O24', '', heading7)
    worksheet.merge_range('L25:O25', '', heading7)
    worksheet.merge_range('L26:O26', '', heading7)
    worksheet.merge_range('L27:O27', '', heading7)
    worksheet.merge_range('L28:O28', '', heading7)
    worksheet.merge_range('L29:O29', '', heading7)
    worksheet.merge_range('L30:O30', '', heading7)
    worksheet.merge_range('L31:O31', '', heading7)
    worksheet.merge_range('L32:O32', '', heading7)

    return workbook, worksheet


def define_column_widths_fn(workbook, worksheet):
    """ define and set column widths.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.set_column('A:A', 31.00)
    worksheet.set_column('B:B', 13.50)
    worksheet.set_column('C:C', 13.50)
    worksheet.set_column('D:D', 13.50)
    worksheet.set_column('E:E', 13.50)
    worksheet.set_column('F:F', 13.50)
    worksheet.set_column('G:G', 13.50)
    worksheet.set_column('H:H', 13.50)
    worksheet.set_column('I:I', 13.50)
    worksheet.set_column('J:J', 13.50)
    worksheet.set_column('K:K', 13.50)
    worksheet.set_column('L:L', 13.50)
    worksheet.set_column('M:M', 13.50)
    worksheet.set_column('N:N', 13.50)
    worksheet.set_column('O:O', 13.50)

    return workbook, worksheet


def define_column_heights_fn(workbook, worksheet):
    """ Define and set column heights.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.set_row(0, 80.25)
    worksheet.set_row(1, 56.25)
    worksheet.set_row(2, 33.75)
    worksheet.set_row(3, 27.75)
    worksheet.set_row(4, 27.75)
    worksheet.set_row(5, 5.00)
    worksheet.set_row(6, 56.25)
    worksheet.set_row(7, 56.25)
    worksheet.set_row(8, 3.00)
    worksheet.set_row(9, 3.00)
    worksheet.set_row(10, 3.00)
    worksheet.set_row(11, 3.00)
    worksheet.set_row(12, 3.00)
    worksheet.set_row(13, 3.00)
    worksheet.set_row(14, 3.00)
    worksheet.set_row(15, 56.25)
    worksheet.set_row(16, 56.25)
    worksheet.set_row(17, 56.25)
    worksheet.set_row(18, 56.25)
    worksheet.set_row(19, 56.25)
    worksheet.set_row(20, 56.25)
    worksheet.set_row(21, 56.25)
    worksheet.set_row(22, 56.25)
    worksheet.set_row(23, 56.25)
    worksheet.set_row(24, 56.25)
    worksheet.set_row(25, 56.25)
    worksheet.set_row(26, 56.25)
    worksheet.set_row(27, 56.25)
    worksheet.set_row(28, 56.25)
    worksheet.set_row(29, 56.25)
    worksheet.set_row(30, 56.25)
    worksheet.set_row(31, 56.25)

    return workbook, worksheet


def insert_default_values_fn(workbook, worksheet, heading7):
    """ Add default values and  format worksheet cells.
            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading7: workbook style derived  from define heading7_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.write_string('L2', 'No', heading7)
    worksheet.write_string('B3', 'BLANK', heading7)
    worksheet.write_string('D3', 'BLANK', heading7)
    worksheet.write_string('F3', 'BLANK', heading7)
    worksheet.write_string('H3', 'BLANK', heading7)
    worksheet.write_string('J3', 'BLANK', heading7)
    worksheet.write_string('L3', 'BLANK', heading7)
    worksheet.write_string('N3', 'BLANK', heading7)
    worksheet.write_string('B4', 'BLANK', heading7)
    worksheet.write_string('D4', 'BLANK', heading7)
    worksheet.write_string('F4', 'BLANK', heading7)
    worksheet.write_string('H4', 'BLANK', heading7)
    worksheet.write_string('J4', 'BLANK', heading7)
    worksheet.write_string('L4', 'BLANK', heading7)
    worksheet.write_string('N4', 'BLANK', heading7)

    worksheet.write_string('A23', 'BLANK', heading7)
    worksheet.write_string('A24', 'BLANK', heading7)
    worksheet.write_string('A25', 'BLANK', heading7)
    worksheet.write_string('A25', 'BLANK', heading7)
    worksheet.write_string('A26', 'BLANK', heading7)
    worksheet.write_string('A27', 'BLANK', heading7)
    worksheet.write_string('A28', 'BLANK', heading7)
    worksheet.write_string('A29', 'BLANK', heading7)
    worksheet.write_string('A30', 'BLANK', heading7)
    worksheet.write_string('A31', 'BLANK', heading7)
    worksheet.write_string('A32', 'BLANK', heading7)
    worksheet.write_string('F23', 'BLANK', heading7)
    worksheet.write_string('F24', 'BLANK', heading7)
    worksheet.write_string('F25', 'BLANK', heading7)
    worksheet.write_string('F25', 'BLANK', heading7)
    worksheet.write_string('F26', 'BLANK', heading7)
    worksheet.write_string('F27', 'BLANK', heading7)
    worksheet.write_string('F28', 'BLANK', heading7)
    worksheet.write_string('F29', 'BLANK', heading7)
    worksheet.write_string('F30', 'BLANK', heading7)
    worksheet.write_string('F31', 'BLANK', heading7)
    worksheet.write_string('F32', 'BLANK', heading7)
    worksheet.write_string('L23', 'BLANK', heading7)
    worksheet.write_string('L24', 'BLANK', heading7)
    worksheet.write_string('L25', 'BLANK', heading7)
    worksheet.write_string('L25', 'BLANK', heading7)
    worksheet.write_string('L26', 'BLANK', heading7)
    worksheet.write_string('L27', 'BLANK', heading7)
    worksheet.write_string('L28', 'BLANK', heading7)
    worksheet.write_string('L29', 'BLANK', heading7)
    worksheet.write_string('L30', 'BLANK', heading7)
    worksheet.write_string('L31', 'BLANK', heading7)
    worksheet.write_string('L32', 'BLANK', heading7)

    worksheet.write_number('B7', 0, heading7)
    worksheet.write_number('C7', 0, heading7)
    worksheet.write_number('D7', 0, heading7)
    worksheet.write_number('E7', 0, heading7)
    worksheet.write_number('F7', 0, heading7)
    worksheet.write_number('G7', 0, heading7)
    worksheet.write_number('H7', 0, heading7)
    worksheet.write_number('I7', 0, heading7)
    worksheet.write_number('J7', 0, heading7)
    worksheet.write_number('K7', 0, heading7)
    worksheet.write_number('L7', 0, heading7)
    worksheet.write_number('M7', 0, heading7)
    worksheet.write_number('N7', 0, heading7)
    worksheet.write_number('O7', 0, heading7)
    worksheet.write_number('B8', 0, heading7)
    worksheet.write_number('C8', 0, heading7)
    worksheet.write_number('D8', 0, heading7)
    worksheet.write_number('E8', 0, heading7)
    worksheet.write_number('F8', 0, heading7)
    worksheet.write_number('G8', 0, heading7)
    worksheet.write_number('H8', 0, heading7)
    worksheet.write_number('I8', 0, heading7)
    worksheet.write_number('J8', 0, heading7)
    worksheet.write_number('K8', 0, heading7)
    worksheet.write_number('L8', 0, heading7)
    worksheet.write_number('M8', 0, heading7)
    worksheet.write_number('N8', 0, heading7)
    worksheet.write_number('O8', 0, heading7)

    worksheet.write_number('B17', 0, heading7)
    worksheet.write_number('B18', 0, heading7)
    worksheet.write_number('B19', 0, heading7)

    return workbook, worksheet


def insert_horizontal_data_fn(worksheet, row, col, input_list, style, factor):
    """ Insert data (list of lists) horizontally.

            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param row: integer object containing the row start number for data insertion.
            :param col: integer object containing the column start number for data insertion.
            :param input_list: list of lists object containing data for insertion.
            :param style: style guide variable - heading style passed through function (i.e. (heading1-7).
            :param factor: integer object containing number of rows to skip/not skip."""

    if input_list[0]:
        # Iterate over the data and write it out row by row.
        for item in input_list:
            worksheet.write(row, col, item, style)
            col += factor


def insert_horizontal_may_start_with_zero_fn(worksheet, row, col, input_list, style, factor):
    """ Insert data (list of lists) horizontally.

            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param row: integer object containing the row start number for data insertion.
            :param col: integer object containing the column start number for data insertion.
            :param input_list: list of lists object containing data for insertion.
            :param style: style guide variable - heading style passed through function (i.e. (heading1-7).
            :param factor: integer object containing number of rows to skip/not skip."""

    # Iterate over the data and write it out row by row.
    for item in input_list:

        if item != 0.0:
            worksheet.write(row, col, item, style)
            col += factor
        else:
            col += factor


def insert_vertical_may_start_with_zero_fn(worksheet, row, col, input_list, style, factor):
    """ Insert data (list of lists) skipping BLANK data when responses are not required vertically.

            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param row: integer object containing the row start number for data insertion.
            :param col: integer object containing the column start number for data insertion.
            :param input_list: list of lists object containing data for insertion.
            :param style: style guide variable - heading style passed through function (i.e. (heading1-7).
            :param factor: integer object containing number of rows to skip/not skip."""

    # Iterate over the data and write it out row by row.
    for item in input_list:
        if item != 0.0:
            worksheet.write(row, col, item, style)
            row += factor
        else:
            row += factor


def main_routine(color_fill, heading1, heading2, heading4, heading5, heading7, heading8, workbook, obs_data_list,
                 insert_vertical_data_fn, insert_horizontal_data_fn):
    #print('script10_7_create_site_basal_sheet.py INITIATED.')

    worksheet_name = 'Step 5 - Basal Sweeps - Table 2'

    # call the create_worksheet_fn function.
    workbook, worksheet = create_worksheet(workbook, worksheet_name)

    # call the insert_sheet_headings_fn function.
    workbook, worksheet = insert_sheet_headings_fn(workbook, worksheet, heading4, heading5, color_fill)

    # call the insert_blank_formatted_cells_fn function.
    workbook, worksheet = insert_blank_formatted_cells_fn(workbook, worksheet, heading7)

    # call the merge_cells_fn function.
    workbook, worksheet = merge_cells_fn(workbook, worksheet, heading1, heading2, heading4, heading5, heading7,
                                         heading8, color_fill)

    # call the define_column_widths_fn function
    workbook, worksheet = define_column_widths_fn(workbook, worksheet)

    # call the define_column_heights_fn function
    workbook, worksheet = define_column_heights_fn(workbook, worksheet)

    # call the insert_default_values_fn function
    workbook, worksheet = insert_default_values_fn(workbook, worksheet, heading7)

    basal_data_list = obs_data_list[3]

    if basal_data_list[0]:
        #print('basal_data_list[0]: ', basal_data_list[0])
        # call the insert_horizontal_data_fn function
        insert_horizontal_data_fn(worksheet, 1, 11, ['Yes'], heading7, 2)

        # call the insert_horizontal_data_fn function
        insert_horizontal_data_fn(worksheet, 2, 1, basal_data_list[0], heading7, 2)

    if basal_data_list[1]:
        #print('basal_data_list[1]: ', basal_data_list[1])
        # call the insert_horizontal_data_fn function
        insert_horizontal_data_fn(worksheet, 3, 1, basal_data_list[1], heading7, 2)

        # if basal_data_list[2]:
        #print('basal_data_list[2]: ', basal_data_list[2])
        # call the insert_horizontal_data_fn function
        insert_horizontal_may_start_with_zero_fn(worksheet, 6, 1, basal_data_list[2], heading7, 1)

        # if basal_data_list[3]:
        #print('basal_data_list[3]: ', basal_data_list[3])
        # call the insert_horizontal_data_fn function
        insert_horizontal_may_start_with_zero_fn(worksheet, 7, 1, basal_data_list[3], heading7, 1)

    if basal_data_list[4]:
        #print('basal_data_list[4]: ', basal_data_list[4])
        # call the insert_vertical_data_fn function
        insert_vertical_may_start_with_zero_fn(worksheet, 16, 1, basal_data_list[4], heading7, 1)

    # ------------------------------------------- Woody species -------------------------------------------------------

    if basal_data_list[5]:
        #print('basal_data_list[5]: ', basal_data_list[5])
        row = 22
        col = 0
        for i in basal_data_list[5]:
            value_ = (i[:1])

            # call the insert_vertical_data_fn function
            insert_horizontal_data_fn(worksheet, row, col, value_, heading7, 1)

            row += 1

    if basal_data_list[5]:
        value_ = (i[1:])

        row = 22
        col = 5

        for i in basal_data_list[5]:
            value_ = (i[1:])
            # call the insert_vertical_data_fn function
            insert_horizontal_data_fn(worksheet, row, col, value_, heading7, 1)

            row += 1

    if basal_data_list[6]:
        #print('basal_data_list[6]: ', basal_data_list[6])
        insert_vertical_data_fn(worksheet, 22, 11, basal_data_list[6], heading7, 1)

    #print('script10_7_create_site_basal_sheet.py COMPLETE.')
    #print('SCRIPT 10_8: create_site_juvenile_stem_sheet.py initiating..........')

    return insert_horizontal_may_start_with_zero_fn, insert_vertical_may_start_with_zero_fn


if __name__ == '__main__':
    main_routine()
