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
import xlsxwriter


def create_workbook_fn(property_name, site_dir, site):
    """Create an empty excel workbook.

            :param site_dir: sting object containing the path to the working site folder.
            :param site: string object containing the site name.
            :return: workbook: empty workbook object created in the site_dir directory ready for data insertion."""

    workbook = xlsxwriter.Workbook(site_dir + '//'+ property_name + '_' + site + '.xlsx')

    return workbook


def define_heading1(workbook):
    """ Define heading1 formatting.

            :param workbook: workbook object created in the create_workbook_fn function.
            :return heading1: workbook heading style."""

    heading1 = workbook.add_format()
    heading1.set_font_name('Calibri')
    heading1.set_font_size(32)
    heading1.set_bold()
    heading1.set_align('center')
    heading1.set_align('vcenter')
    heading1.set_text_wrap()
    heading1.set_bg_color('#fcbd00')
    heading1.set_border()
    heading1.set_border_color('#C0C0C0')

    return workbook, heading1


def define_heading2(workbook):
    """ Define heading2 formatting.

            :param workbook: workbook object created in the create_workbook_fn function.
            :return heading2: workbook heading style."""

    heading2 = workbook.add_format()
    heading2.set_font_name('Calibri')
    heading2.set_font_size(20)
    heading2.set_bold()
    heading2.set_align('center')
    heading2.set_align('vcenter')
    heading2.set_text_wrap()
    heading2.set_bg_color('#fcbd00')
    heading2.set_border()
    heading2.set_border_color('#C0C0C0')

    return workbook, heading2


def define_heading3(workbook):
    """ Define heading3 formatting.

            :param workbook: workbook object created in the create_workbook_fn function.
            :return heading3: workbook heading style."""

    heading3 = workbook.add_format()
    heading3.set_font_name('Calibri')
    heading3.set_font_size(16)
    heading3.set_bold()
    heading3.set_align('right')
    heading3.set_align('vcenter')
    heading3.set_text_wrap()
    heading3.set_bg_color('#fcbd00')
    heading3.set_border()
    heading3.set_border_color('#C0C0C0')

    return workbook, heading3


def define_heading4(workbook):
    """ Define heading4 formatting.

            :param workbook: workbook object created in the create_workbook_fn function.
            :return heading4: workbook heading style."""

    heading4 = workbook.add_format()
    heading4.set_font_name('Calibri')
    heading4.set_font_size(16)
    heading4.set_bold()
    heading4.set_align('center')
    heading4.set_align('vcenter')
    heading4.set_text_wrap()
    heading4.set_bg_color('#fcbd00')
    heading4.set_border()
    heading4.set_border_color('#C0C0C0')

    return workbook, heading4


def define_heading5(workbook):
    """ Define heading5 formatting.

            :param workbook: workbook object created in the create_workbook_fn function.
            :return heading5: workbook heading style."""

    heading5 = workbook.add_format()
    heading5.set_font_name('Calibri')
    heading5.set_font_size(14)
    heading5.set_bold()
    heading5.set_align('center')
    heading5.set_align('vcenter')
    heading5.set_text_wrap()
    heading5.set_bg_color('#fedf98')
    heading5.set_border()
    heading5.set_border_color('#C0C0C0')

    return workbook, heading5


def define_heading6(workbook):
    """ Define heading6 formatting.

            :param workbook: workbook object created in the create_workbook_fn function.
            :return heading6: workbook heading style."""

    heading6 = workbook.add_format()
    heading6.set_font_name('Calibri')
    heading6.set_font_size(14)
    heading6.set_bold()
    heading6.set_align('center')
    heading6.set_align('vcenter')
    heading6.set_text_wrap()
    heading6.set_border()
    heading6.set_border_color('#C0C0C0')

    return workbook, heading6


def define_heading7(workbook):
    """ Define heading7 formatting.

            :param workbook: workbook object created in the create_workbook_fn function.
            :return heading7: workbook heading style."""

    heading7 = workbook.add_format()
    heading7.set_font_name('Calibri')
    heading7.set_font_size(14)
    heading7.set_align('center')
    heading7.set_align('vcenter')
    heading7.set_text_wrap()
    heading7.set_border()
    heading7.set_border_color('#C0C0C0')

    return workbook, heading7


def define_heading8(workbook):
    """ Define heading8 formatting.

            :param workbook: workbook object created in the create_workbook_fn function.
            :return heading8: workbook heading style."""

    heading8 = workbook.add_format()
    heading8.set_font_name('Calibri')
    heading8.set_font_size(14)
    heading8.set_italic()
    heading8.set_align('center')
    heading8.set_align('vcenter')
    heading8.set_text_wrap()
    heading8.set_border()
    heading8.set_border_color('#C0C0C0')

    return workbook, heading8


def define_color_fill(workbook):
    """ Define heading3 formatting.

            :param workbook: workbook object created in the create_workbook_fn function.
            :return colour_fill: workbook cell fill style."""

    color_fill = workbook.add_format()
    color_fill.set_bg_color('#fcbd00')
    color_fill.set_border()
    color_fill.set_border_color('#C0C0C0')

    return workbook, color_fill


def main_routine(property_name, site, site_dir):
    """Create a workbook and format cells for the Rangeland Monitoring observation excel workbook.

            :param property_name:
            :param site: string object containing the site name.
            :param site_dir: string object containing the path to the current site directory.
            :return color_fill: workbook style derived  from define colour_fill_fn.
            :return heading1: workbook style derived  from define heading1_fn.
            :return heading2: workbook style derived  from define heading2_fn.
            :return heading3: workbook style derived  from define heading3_fn.
            :return heading4: workbook style derived  from define heading4_fn.
            :return heading5: workbook style derived  from define heading5_fn.
            :return  heading6: workbook style derived  from define heading6_fn.
            :return  heading7: workbook style derived  from define heading7_fn.
            :return workbook: open workbook object derived from create_workbook_fn function.  """

    #print('step10_2_observation_sheet_formatting.py INITIATED.')

    # call the create_workbook_fn function.
    workbook = create_workbook_fn(property_name, site_dir, site)

    # call the define_heading1 function.
    workbook, heading1 = define_heading1(workbook)

    # call the define_heading2 function.
    workbook, heading2 = define_heading2(workbook)

    # call the define_heading3 function.
    workbook, heading3 = define_heading3(workbook)

    # call the define_heading4 function.
    workbook, heading4 = define_heading4(workbook)

    # call the define_heading5 function.
    workbook, heading5 = define_heading5(workbook)

    # call the define_heading6 function.
    workbook, heading6 = define_heading6(workbook)

    # call the define_heading7 function.
    workbook, heading7 = define_heading7(workbook)

    # call the define_heading8 function.
    workbook, heading8 = define_heading8(workbook)

    workbook, color_fill = define_color_fill(workbook)

    #print('step10_2_observational_sheet_formatting.py COMPLETE.')
    #print('step22_createSiteEstablishmentSheet3P.py initiating..........')

    return color_fill, heading1, heading2, heading3, heading4, heading5, heading6, heading7, heading8, workbook


if __name__ == '__main__':
    main_routine()
