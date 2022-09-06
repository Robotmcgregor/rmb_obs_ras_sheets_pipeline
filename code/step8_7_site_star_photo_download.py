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

warnings.filterwarnings("ignore")


def photos_fn(df):
    """ Extract the seven photograph urls.

    :param df: pandas dataframe object.
    :return photo_list: list of ODK Aggregate photo urls.
    """

    photo_off = df.photo_off.iloc[0]
    photo_c = df.photo_c.iloc[0]
    photo_n = df.photo_n.iloc[0]
    photo_ne = df.photo_ne.iloc[0]
    photo_se = df.photo_se.iloc[0]
    photo_s = df.photo_s.iloc[0]
    photo_sw = df.photo_sw.iloc[0]
    photo_nw = df.photo_nw.iloc[0]

    photo_list = [photo_off, photo_c, photo_n, photo_ne, photo_se, photo_s, photo_sw, photo_nw]

    return photo_list


def save_photo_fn(photos_list, site, site_dir, photo_date):
    """Download and save the seven transect photos_fn.

    :param photos_list: list of ODK Aggregate photo urls.
    :param site: string object containing the site name.
    :param site_dir: sting object containing the path to the site specific directory.
    :param photo_date: string object containing the date the photos were taken.
    """

    photo_dir_list = []

    for i in photos_list:
        tail = str(i[-20:]).split('3A')
        photo_name = tail[1].replace('PHOTO', '')
        _, site_name = site.rsplit('_', 1)
        output_str = (site_dir + '\\' + site_name + '_' + str(
            photo_date) + photo_name + '.jpg')
        photo_dir_list.append(output_str)
        urllib.request.urlretrieve(i, output_str)


def main_routine(photo_star_url_csv, site, site_dir):
    """ Read in the site_photo_integrated_url.csv file sort and download and name the relevant photographs.

    :param photo_star_url_csv: string object containing the path to the photo_star_url csv file.
    :param site: site: string object containing the site name.
    :param site_dir: string object containing the path to the site directory.
    :return photo_date: string object containing the date the photos were taken.
    """

    df = pd.read_csv(photo_star_url_csv)

    photo_date = df.date.iloc[0]

    # call photos_fn function to extract disturbance indicators, photo_url_extraction_fn urls and bearings.
    photos_list = photos_fn(df)

    # call save_photos_fn function to download and save the disturbance photographs captured in the integrated form.
    save_photo_fn(photos_list, site, site_dir, photo_date)

    return photo_date


if __name__ == '__main__':
    main_routine()
