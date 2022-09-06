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


def create_worksheet_fn(workbook, worksheet_name):
    """ Create worksheet and set row height.

            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet_name: string object containing worksheet name.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet = workbook.add_worksheet(worksheet_name)

    # Set row height
    worksheet.set_default_row(56.25)

    return workbook, worksheet


def insert_sheet_headings_fn(workbook, worksheet, heading3, heading4, heading6, color_fill):
    """ Add item headings to cells as strings.

            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading3: workbook style derived  from define heading3_fn.
            :param heading4: workbook style derived  from define heading4_fn.
            :param heading6: workbook style derived  from define heading6_fn.
            :param color_fill: workbook style derived  from define colour_fill_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.write_string('A3', 'STATION', heading3)
    worksheet.write_string('D3', 'SITE NUMBER', heading3)
    worksheet.write_string('F3', 'DATE & TIME:', heading3)
    worksheet.write_string('A4', 'Monitoring Officers', heading3)
    worksheet.write_string('A5', 'Location', heading3)
    worksheet.write_string('B5', 'LAT:', heading3)
    worksheet.write_string('D5', 'LON:', heading3)
    worksheet.write_string('F5', 'Paddock:', heading3)
    worksheet.write_string('A6', 'NEAREST WATER: Name', heading3)
    worksheet.write_string('C6', 'Type', heading3)
    worksheet.write_string('E6', 'Distance (km)', heading3)
    worksheet.write_string('G6', 'Direction', heading3)
    worksheet.write_string('A7', 'LAND TYPE:', heading3)
    worksheet.write_string('A8', 'Estimated bare soil', heading3)
    worksheet.write_string('A10', 'Category', heading3)
    worksheet.write_string('B10', '3P Grasses', heading4)
    worksheet.write_string('C10', 'Other perennial grasses', heading4)
    worksheet.write_string('D10', 'Annual grasses', heading4)
    worksheet.write_string('E10', 'Forbs', heading4)
    worksheet.write_string('G10', 'Max total', heading6)
    worksheet.write_string('H10', 'Min total', heading6)
    worksheet.write_string('A11', 'Cover', heading3)
    worksheet.write_string('A12', 'Species 1', heading3)
    worksheet.write_string('A13', 'Species 2', heading3)
    worksheet.write_string('A14', 'Species 3', heading3)
    worksheet.write_string('A15', 'Species 4', heading3)
    worksheet.write_string('A17', 'Basal area (m2/ha)', heading3)
    worksheet.write_string('A18', 'Category', heading3)
    worksheet.write_string('A19', 'Juvenile density (Stems/ha)', heading3)
    worksheet.write_string('A20', 'Species 1', heading3)
    worksheet.write_string('A21', 'Species 2', heading3)
    worksheet.write_string('A22', 'Species 3', heading3)
    worksheet.write_string('A23', 'Species 4', heading3)
    worksheet.write_string('A24', 'Species 5', heading3)
    worksheet.write_string('A25', 'Species 6', heading3)
    worksheet.write_string('A28', 'IS THIS AN ERODIBLE SOIL?', heading3)
    worksheet.write_string('B29', 'Severity', heading4)
    worksheet.write_string('C29', 'Stability', heading4)
    worksheet.write_string('A30', 'SCALDING - wind or water', heading3)
    worksheet.write_string('A31', 'WINDSHEETING', heading3)
    worksheet.write_string('A32', 'WATERSHEETING', heading3)
    worksheet.write_string('A33', 'RILLING', heading3)
    worksheet.write_string('A34', 'GULLYING', heading3)
    worksheet.write_string('A35', 'PASTURE UTILISATION:', heading3)
    worksheet.write_string('A36', 'WEEDS:', heading3)
    worksheet.write_string('A37', 'WILD ANIMAL ACTIVITY:', heading3)
    worksheet.write_string('B37', 'Camel', heading4)
    worksheet.write_string('C37', 'Rabbit', heading4)
    worksheet.write_string('D37', 'Donkey', heading4)
    worksheet.write_string('E37', 'Horse', heading4)
    worksheet.write_string('F37', 'Pig', heading4)
    worksheet.write_string('G37', 'Buffalo', heading4)
    worksheet.write_string('H37', 'Native herbivore', heading4)
    worksheet.write_string('A38', 'ACTIVE', heading3)
    worksheet.write_string('A39', 'EVIDENCE AND DESCRIPTION:', heading3)
    worksheet.write_string('A42', 'FIRE FREQUENCY:', heading3)
    worksheet.write_string('A43', 'FIRE INTENSITY:', heading3)
    worksheet.write_string('A45', 'LAND CONDITION SCORE:', heading3)

    worksheet.write('A29', None, color_fill)
    worksheet.write('A40', None, color_fill)
    worksheet.write('A41', None, color_fill)
    worksheet.write('A44', None, color_fill)
    worksheet.write('A46', None, color_fill)

    return workbook, worksheet


def insert_blank_formatted_cells_fn(workbook, worksheet, heading7):
    """ Add blank formatted cells to worksheet.

            :param workbook: open workbook object derived from create_workbook_fn function.
            :param worksheet: worksheet object current worksheet derived from create_worksheet_fn.
            :param heading7: workbook style derived  from define heading7_fn.
            :return: workbook: updated workbook object.
            :return worksheet: updated worksheet object."""

    worksheet.write_blank('B3', None, heading7)
    worksheet.write_blank('E3', None, heading7)
    worksheet.write_blank('G3', None, heading7)
    worksheet.write_blank('B4', None, heading7)
    worksheet.write_blank('D4', None, heading7)
    worksheet.write_blank('F4', None, heading7)
    worksheet.write_blank('C5', None, heading7)
    worksheet.write_blank('E5', None, heading7)
    worksheet.write_blank('G5', None, heading7)
    worksheet.write_blank('B6', None, heading7)
    worksheet.write_blank('D6', None, heading7)
    worksheet.write_blank('F6', None, heading7)
    worksheet.write_blank('H6', None, heading7)
    worksheet.write_blank('B7', None, heading7)
    worksheet.write_blank('F7', None, heading7)
    worksheet.write_blank('B8', None, heading7)
    worksheet.write_blank('B11', None, heading7)
    worksheet.write_blank('B12', None, heading7)
    worksheet.write_blank('B13', None, heading7)
    worksheet.write_blank('B14', None, heading7)
    worksheet.write_blank('B15', None, heading7)
    worksheet.write_blank('C11', None, heading7)
    worksheet.write_blank('C12', None, heading7)
    worksheet.write_blank('C13', None, heading7)
    worksheet.write_blank('C14', None, heading7)
    worksheet.write_blank('C15', None, heading7)
    worksheet.write_blank('D11', None, heading7)
    worksheet.write_blank('D12', None, heading7)
    worksheet.write_blank('D13', None, heading7)
    worksheet.write_blank('D14', None, heading7)
    worksheet.write_blank('D15', None, heading7)
    worksheet.write_blank('E11', None, heading7)
    worksheet.write_blank('E12', None, heading7)
    worksheet.write_blank('E13', None, heading7)
    worksheet.write_blank('E14', None, heading7)
    worksheet.write_blank('E15', None, heading7)
    worksheet.write_blank('G11', None, heading7)
    worksheet.write_blank('H11', None, heading7)
    worksheet.write_blank('B17', None, heading7)
    worksheet.write_blank('B19', None, heading7)
    worksheet.write_blank('B20', None, heading7)
    worksheet.write_blank('B21', None, heading7)
    worksheet.write_blank('B22', None, heading7)
    worksheet.write_blank('B23', None, heading7)
    worksheet.write_blank('B24', None, heading7)
    worksheet.write_blank('B25', None, heading7)
    worksheet.write_blank('E19', None, heading7)
    worksheet.write_blank('E20', None, heading7)
    worksheet.write_blank('E21', None, heading7)
    worksheet.write_blank('E22', None, heading7)
    worksheet.write_blank('E23', None, heading7)
    worksheet.write_blank('E24', None, heading7)
    worksheet.write_blank('E25', None, heading7)
    worksheet.write_blank('B28', None, heading7)
    worksheet.write_blank('B30', None, heading7)
    worksheet.write_blank('B31', None, heading7)
    worksheet.write_blank('B32', None, heading7)
    worksheet.write_blank('B33', None, heading7)
    worksheet.write_blank('B34', None, heading7)
    worksheet.write_blank('C30', None, heading7)
    worksheet.write_blank('C31', None, heading7)
    worksheet.write_blank('C32', None, heading7)
    worksheet.write_blank('C33', None, heading7)
    worksheet.write_blank('C34', None, heading7)
    worksheet.write_blank('B35', None, heading7)
    worksheet.write_blank('B36', None, heading7)
    worksheet.write_blank('B38', None, heading7)
    worksheet.write_blank('C38', None, heading7)
    worksheet.write_blank('D38', None, heading7)
    worksheet.write_blank('E38', None, heading7)
    worksheet.write_blank('F38', None, heading7)
    worksheet.write_blank('G38', None, heading7)
    worksheet.write_blank('H38', None, heading7)
    worksheet.write_blank('B39', None, heading7)
    worksheet.write_blank('B42', None, heading7)
    worksheet.write_blank('B43', None, heading7)
    worksheet.write_blank('E42', None, heading7)
    worksheet.write_blank('E43', None, heading7)
    worksheet.write_blank('B46', None, heading7)
    worksheet.write_blank('E46', None, heading7)
    worksheet.write_blank('B47', None, heading7)

    return workbook, worksheet


def merge_cells_fn(workbook, worksheet, heading1, heading2, heading3, heading4):
    """ Merge and format required cells.

    :param workbook: workbook object created in the create_workbook_fn function.
    :param worksheet: excel sheet created with the create_worksheet_fn function.
    :param heading1: heading styles
    :param heading2: heading style
    :param heading3: heading style
    :param heading4: heading style
    :return: formatted worksheet."""

    worksheet.merge_range('A2:H2', 'RANGELAND ASSESSMENT SITE', heading1)
    worksheet.merge_range('D7:E7', 'LAND SYSTEM', heading3)
    worksheet.merge_range('A9:H9', 'PASTURE SPECIES COMPOSITION', heading2)
    worksheet.merge_range('A16:H16', 'WOODY SPECIES', heading2)
    worksheet.merge_range('B18:D18', 'Shrubs (adults <2m)', heading4)
    worksheet.merge_range('E18:H18', 'Trees', heading4)
    worksheet.merge_range('A26:H26', 'Disturbance', heading2)
    worksheet.merge_range('A27:H27', 'Erosion', heading2)
    worksheet.merge_range('D29:H29', 'Severity description', heading4)
    worksheet.merge_range('B40:H40', 'Fire', heading2)
    worksheet.merge_range('B41:D41', 'NORTH REGION', heading4)
    worksheet.merge_range('E41:H41', 'SOUTH REGION', heading4)
    worksheet.merge_range('B45:D45', 'LAND COND GUIDE (a, b,c, d)', heading4)
    worksheet.merge_range('E45:H45', 'ASSESSMENT SCORE (good,fair, poor)', heading4)
    worksheet.merge_range('A47:A49', 'OTHER COMMENTS:', heading3)
    worksheet.merge_range('D30:H30', '')
    worksheet.merge_range('D31:H31', '')
    worksheet.merge_range('D32:H32', '')
    worksheet.merge_range('D33:H33', '')
    worksheet.merge_range('D34:H34', '')
    worksheet.merge_range('B8:H8', '')
    worksheet.merge_range('B7:C7', '')
    worksheet.merge_range('F7:H7', '')
    worksheet.merge_range('C28:H28', '')
    worksheet.merge_range('B35:H35', '')
    worksheet.merge_range('B36:H36', '')
    worksheet.merge_range('B19:D19', '')
    worksheet.merge_range('B20:D20', '')
    worksheet.merge_range('B21:D21', '')
    worksheet.merge_range('B22:D22', '')
    worksheet.merge_range('B23:D23', '')
    worksheet.merge_range('B24:D24', '')
    worksheet.merge_range('B25:D25', '')
    worksheet.merge_range('E19:H19', '')
    worksheet.merge_range('E20:H20', '')
    worksheet.merge_range('E21:H21', '')
    worksheet.merge_range('E22:H22', '')
    worksheet.merge_range('E23:H23', '')
    worksheet.merge_range('E24:H24', '')
    worksheet.merge_range('E25:H25', '')
    worksheet.merge_range('B3:C3', '')
    worksheet.merge_range('G3:H3', '')
    worksheet.merge_range('B4:C4', '')
    worksheet.merge_range('D4:E4', '')
    worksheet.merge_range('F4:H4', '')
    worksheet.merge_range('G5:H5', '')
    worksheet.merge_range('B17:H17', '')
    worksheet.merge_range('B42:D42', '')
    worksheet.merge_range('B43:D43', '')
    worksheet.merge_range('E42:H42', '')
    worksheet.merge_range('E43:H43', '')
    worksheet.merge_range('B46:D46', '')
    worksheet.merge_range('E46:H46', '')
    worksheet.merge_range('B47:H49', '')
    worksheet.merge_range('B39:H39', '')
    worksheet.merge_range('B44:H44', '')

    return workbook, worksheet


def define_column_widths_fn(workbook, worksheet):
    """ Set column widths.

    :param workbook: workbook object created in the create_workbook_fn function.
    :param worksheet: excel sheet created with the create_worksheet_fn function.
    :return: formatted worksheet. """

    worksheet.set_column('A:A', 37.82)
    worksheet.set_column('B:B', 18.45)
    worksheet.set_column('C:C', 16.73)
    worksheet.set_column('D:D', 17.91)
    worksheet.set_column('E:E', 15.36)
    worksheet.set_column('F:F', 15.27)
    worksheet.set_column('G:G', 17.43)
    worksheet.set_column('H:H', 14.14)

    return workbook, worksheet


def insert_vertical_data_fn(worksheet, row, col, input_list, style, factor):
    """ Insert list of data vertically.

        :param worksheet: formatted excel sheet created with the create_worksheet_fn function.
        :param row: integer used to define which row to insert a list object.
        :param col: integer used to define which column to insert a list object.
        :param input_list: list object containing variables for worksheet insertion.
        :param style: text style (i.e. heading 1-7)
        :param factor: integer defines the cell/row increment for list insertion. """

    if input_list:
        # Iterate over the data and write it out row by row.
        for item in input_list:
            worksheet.write(row, col, item, style)
            row += factor


def insert_horizontal_data_fn(worksheet, row, col, input_list, style, factor):
    """ Insert list of data horizontally.

        :param worksheet: formatted excel sheet created with the create_worksheet_fn function.
        :param row: integer used to define which row to insert a list object.
        :param col: integer used to define which column to insert a list object.
        :param input_list: list object containing variables for worksheet insertion.
        :param style: text style (i.e. heading 1-7)
        :param factor: integer defines the cell/row increment for list insertion. """

    if input_list:
        # Iterate over the data and write it out row by row.
        for item in input_list:
            worksheet.write(row, col, item, style)
            col += factor


def main_routine(color_fill, heading1, heading2, heading3, heading4, heading6, heading7, ras_data_list,
                 site, workbook):
    """Create the Rangeland Monitoring rapid assessment survey (ras) excel workbook.

        :return colour_fill: workbook cell fill style.
        :param heading1: workbook heading style.
        :param heading2: workbook heading style.
        :param heading3: workbook heading style.
        :param heading4: workbook heading style.
        :param heading6: workbook heading style.
        :param heading7: workbook heading style.
        :param workbook: workbook object created in the create_workbook_fn function.
        :param ras_data_list: list object containing list elements of variable fro insertion.
        :param site: string object containing the site name. """

    #('step11_2_create_ras_sheet.py INITIATED.')

    worksheet_name = 'Rangeland Monitoring - RAS'

    # call the create_worksheet_fn function.
    workbook, worksheet = create_worksheet_fn(workbook, worksheet_name)

    # call the insert_sheet_headings_fn function.
    workbook, worksheet = insert_sheet_headings_fn(workbook, worksheet, heading3, heading4, heading6, color_fill)

    # call the insert_blank_formatted_cells_fn function.
    workbook, worksheet = insert_blank_formatted_cells_fn(workbook, worksheet, heading7)

    # call the merge_cells_fn function.
    workbook, worksheet = merge_cells_fn(workbook, worksheet, heading1, heading2, heading3, heading4)

    # call the define_column_widths_fn(workbook) function
    workbook, worksheet = define_column_widths_fn(workbook, worksheet)

    if ras_data_list[0]:

        # call the insert_horizontal_data_fn function and inset station name.
        insert_horizontal_data_fn(worksheet, 2, 1, ras_data_list[0][:1], heading7, 1)
        # call the insert_horizontal_data_fn function and inset site and datetime information.
        insert_horizontal_data_fn(worksheet, 2, 4, ras_data_list[0][1:], heading7, 2)

    if ras_data_list[1]:
        # call the insert_horizontal_data_fn function to insert monitoring officers information.
        insert_horizontal_data_fn(worksheet, 3, 1, ras_data_list[1], heading7, 2)

    if ras_data_list[2]:
        # call the insert_horizontal_data_fn function and insert location information.
        insert_horizontal_data_fn(worksheet, 4, 2, ras_data_list[2], heading7, 2)
    if ras_data_list[3]:
        # call the insert_horizontal_data_fn function and insert water information.
        insert_horizontal_data_fn(worksheet, 5, 1, ras_data_list[3], heading7, 2)
    if ras_data_list[4]:
        # call the insert_horizontal_data_fn function and insert landtype information.
        insert_horizontal_data_fn(worksheet, 6, 1, ras_data_list[4], heading7, 4)
    if ras_data_list[5]:
        # call the insert_horizontal_data_fn function and insert bare soil information.

        insert_horizontal_data_fn(worksheet, 7, 1, ras_data_list[5], heading7, 1)

    if ras_data_list[6]:
        # call the insert_horizontal_data_fn function and insert bare soil information.

        insert_horizontal_data_fn(worksheet, 10, 1, ras_data_list[6], heading7, 1)

    if ras_data_list[7]:
        # call the insert_vertical_data_fn function to insert the 3p grass information.

        insert_vertical_data_fn(worksheet, 11, 1, ras_data_list[7], heading7, 1)

    if ras_data_list[8]:
        # call the insert_vertical_data_fn function to insert the perennial grass information.

        insert_vertical_data_fn(worksheet, 11, 2, ras_data_list[8], heading7, 1)

    if ras_data_list[9]:
        # call the insert_vertical_data_fn function to insert the annual grass information.

        insert_vertical_data_fn(worksheet, 11, 3, ras_data_list[9], heading7, 1)

    if ras_data_list[10]:
        # call the insert_vertical_data_fn function to insert the forb information.

        insert_vertical_data_fn(worksheet, 11, 4, ras_data_list[10], heading7, 1)

    if ras_data_list[11]:
        # call the insert_horizontal_data_fn function to insert the max and min totals.

        insert_horizontal_data_fn(worksheet, 10, 6, ras_data_list[11], heading7, 1)

    if ras_data_list[12]:
        # call the insert_horizontal_data_fn function to insert the basal information.

        insert_horizontal_data_fn(worksheet, 16, 1, ras_data_list[12], heading7, 1)

    if ras_data_list[13]:
        # call the insert_horizontal_data_fn function to insert the juvenile density information.

        insert_horizontal_data_fn(worksheet, 18, 1, ras_data_list[13], heading7, 3)

    if ras_data_list[14]:
        # call the insert_vertical_data_fn function to insert the forb information.

        insert_vertical_data_fn(worksheet, 19, 1, ras_data_list[14], heading7, 1)

    if ras_data_list[15]:
        # call the insert_vertical_data_fn function to insert the forb information.

        insert_vertical_data_fn(worksheet, 19, 4, ras_data_list[15], heading7, 1)

    if ras_data_list[16]:
        # call the  insert_horizontal_data_fn function to insert the erodible soil information.

        insert_horizontal_data_fn(worksheet, 27, 1, ras_data_list[16], heading7, 1)

    if ras_data_list[17]:
        # call the insert_vertical_data_fn function to insert erosion severity information.

        insert_vertical_data_fn(worksheet, 29, 1, ras_data_list[17], heading7, 1)

    if ras_data_list[18]:
        # call the insert_vertical_data_fn function to insert erosion severity information.

        insert_vertical_data_fn(worksheet, 29, 2, ras_data_list[18], heading7, 1)

    if ras_data_list[19]:
        # call the insert_vertical_data_fn function to insert erosion severity information.

        insert_vertical_data_fn(worksheet, 29, 3, ras_data_list[19], heading7, 1)

    if ras_data_list[20]:
        # call the  insert_horizontal_data_fn function to insert pasture utilisation information.

        insert_horizontal_data_fn(worksheet, 34, 1, ras_data_list[20], heading7, 1)

    if ras_data_list[21]:
        # call the  insert_horizontal_data_fn function to insert weed comment.

        insert_horizontal_data_fn(worksheet, 35, 1, ras_data_list[21], heading7, 1)

    if ras_data_list[22]:
        # call the  insert_horizontal_data_fn function to insert feral animal true or false.

        insert_horizontal_data_fn(worksheet, 37, 1, ras_data_list[22], heading7, 1)

    if ras_data_list[23]:
        if ras_data_list[23] != 'BLANK, BLANK, BLANK':
            weed_comment = ras_data_list[23]
        else:
            weed_comment = 'BLANK'
            # call the  insert_horizontal_data_fn function to insert weed comment.

            insert_horizontal_data_fn(worksheet, 38, 1, [weed_comment], heading7, 1)

    if ras_data_list[24]:
        # call the insert_vertical_data_fn function to insert northern fire information.

        insert_vertical_data_fn(worksheet, 41, 1, ras_data_list[24], heading7, 1)

    if ras_data_list[25]:
        # call the insert_vertical_data_fn function to insert southern fire information.

        insert_vertical_data_fn(worksheet, 41, 4, ras_data_list[25], heading7, 1)

    if ras_data_list[26][:1]:
        # call the  insert_horizontal_data_fn function to insert land condition.

        insert_horizontal_data_fn(worksheet, 45, 1, ras_data_list[26][:1], heading7, 1)

        if ras_data_list[26][:1][0] == 'A':
            score = 'Excellent'
        elif ras_data_list[26][:1][0] == 'B':
            score = 'Good'
        elif ras_data_list[26][:1][0] == 'C':
            score = ' Fair'
        elif ras_data_list[26][:1][0] == 'D':
            score = 'Poor'
        else:
            score = 'ERROR'
    insert_horizontal_data_fn(worksheet, 45, 4, [score], heading7, 1)

    if ras_data_list[26][1:]:
        # call the  insert_horizontal_data_fn function to insert land condition.

        insert_horizontal_data_fn(worksheet, 46, 1, ras_data_list[26][1:], heading7, 1)

    # -------------------------- Remove if tree and shrub increase to 6 options ------------------

    insert_vertical_data_fn(worksheet, 23, 1, ['BLANK', 'BLANK'], heading7, 1)
    insert_vertical_data_fn(worksheet, 23, 4, ['BLANK', 'BLANK'], heading7, 1)

    workbook.close()
    #print('step11_2_create_ras_sheet.py COMPLETE.')
    #print(site, ' workbook complete!!!!!!')

    return site


if __name__ == '__main__':
    main_routine()
