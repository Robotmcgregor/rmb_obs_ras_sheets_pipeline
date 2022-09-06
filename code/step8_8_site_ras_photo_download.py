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
import urllib
import os

warnings.filterwarnings("ignore")


def photos_fn(ras):
    """ Extract ras photo url and bearings.

    :param ras: pandas data frame object.
    :return: photo_list: list object containing the photo url.
    :return bearing_list: list of photo bearings.
    """

    site_photo_list = [ras.site_photo1.iloc[0], ras.site_photo2.iloc[0], ras.site_photo3.iloc[0]]
    site_bearing_list = [ras.bearing_photo1.iloc[0], ras.bearing_photo2.iloc[0],
                         ras.bearing_photo3.iloc[0]]

    erosion_photo_list = [ras.erosion_photo1.iloc[0], ras.erosion_photo2.iloc[0], ras.erosion_photo3.iloc[0]]
    erosion_bearing_list = [ras.bearing_erosion1.iloc[0], ras.bearing_erosion2.iloc[0],
                            ras.bearing_erosion3.iloc[0]]

    return site_photo_list, site_bearing_list, erosion_photo_list, erosion_bearing_list


def save_photo_fn(photo_list, bearing_list, site, site_dir, photo_date):
    """ Download and save the ras photographs captured in th integrated form.

    :param photo_date: string object containing the date in YYYYMMDD.
    :param photo_list: list object containing the photo url.
    :param bearing_list: list object containing the photo bearing.
    :param site: string object containing the site name.
    :param site_dir: string object containing the path to the site directory.
    """

    photo_dir_list = []

    i = 1
    for photo, bear in zip(photo_list, bearing_list):

        if photo != 'BLANK':
            tail = str(photo[-20:]).split('3A')
            photo_name_ = tail[1].replace('_PHOTO1', '')
            photo_name = photo_name_ + str(i)
            # todo add bearing to metadata
            # bear2 = round(float(bear), 4)
            # bearing = str(bear2).replace('.', '-')
            _, site_name = site.rsplit('_', 1)
            #output_str = (site_dir + '\\' + site + '_' + str(photo_date) + '_' + photo_name + '.jpg')
            output_str = os.path.join(site_dir, "{0}_{1}_{2}{3}".format(site, str(photo_date), photo_name, '.jpg'))
            photo_dir_list.append(output_str)
            urllib.request.urlretrieve(photo, output_str)

        i += 1


def main_routine(photo_ras_url_csv, site, site_dir):
    """ Read in the site_photo_ras_url.csv file sort and download and name the relevant photographs.

    :param photo_ras_url_csv: string object containing the path to the site_photo_ras_url csv file.
    :param site: site: string object containing the site name.
    :param site_dir: string object containing the path to the site directory.
    """

    ras_photo = pd.read_csv(photo_ras_url_csv, index_col=0).fillna('BLANK').replace('Nan', 'BLANK')

    photo_date = ras_photo.date.iloc[0]

    # call photos_fn function to extract ras urls and bearings.
    site_photo_list, site_bearing_list, erosion_photo_list, erosion_bearing_list = photos_fn(ras_photo)

    # call save_photos_fn function to download and save the ras photographs captured in the ODK RAS form.
    save_photo_fn(site_photo_list, site_bearing_list, site, site_dir, photo_date)

    # call save_photos_fn function to download and save the erosion photographs captured in the ODK RAS form.
    save_photo_fn(erosion_photo_list, erosion_bearing_list, site, site_dir, photo_date)



if __name__ == '__main__':
    main_routine()
