# !/usr/bin/env python

"""
Copyright 2021 Robert McGregor

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Import modules
from __future__ import print_function, division
import os
from datetime import datetime
import argparse
import shutil
import sys
import pandas as pd
import warnings
from glob import glob

warnings.filterwarnings("ignore")


def cmd_args_fn():
    p = argparse.ArgumentParser(
        description="""Process raw RMB odk outputs -> csv, shapefiles observational sheets, and Ras sheets.""")

    p.add_argument("-d", "--directory_odk", help="The directory containing ODK csv files.", default="raw_odk")

    p.add_argument("-x", "--export_dir", help="Directory path for outputs.",
                   default="Z:\\Scratch\\Zonal_Stats_Pipeline\\rmb_aggregate_processing\\outputs")

    p.add_argument("-c", "--chrome_driver", help="File path for the chrome extension driver.",
                   default="E:\\DENR\\code\\rangeland_monitoring\\rmb_aggregate_processing\\assets\\chrome_driver\\chrome_driver_v89_0_4389_23\\chromedriver.exe")

    p.add_argument("-r", "--remote_desktop", help="Working on the remote_desktop? - Enter remote_auto, remote, "
                                                  "local or offline.", default="remote")
    p.add_argument("-v", "--assets_veg_list_dir", help="Directory containing veg lists",
                   default="E:\\DENR\code\\rangeland_monitoring\\rmb_aggregate_processing\\assets\\veg_list")

    p.add_argument("-s", "--assets_shapefiles_dir", help="Directory containing shapefiles",
                   default="E:\\DENR\\code\\rangeland_monitoring\\rmb_aggregate_processing\\assets\\shapefiles")

    p.add_argument("-t", "--time_sleep", help="Time between odk aggregate actions -if lagging increase integer",
                   default=20)

    p.add_argument("-ht", "--html_dir", help="Directory containing html transect files (local or offline mode only",
                   default=r"E:\DENR\code\rangeland_monitoring\rmb_aggregate_processing\html_transect")

    p.add_argument("-ver", "--version", help="ODK version being processed (eg. v1, v2 etc.)",
                   default="v1")

    p.add_argument("-p", "--property_enquire",
                   help="Enter the name of of a single property you wish to process. (eg. Property Name)",
                   default=None)

    p.add_argument("-pd", "--pastoral_districts_directory",
                   help="Enter path to the Pastoral_Districts directory in the Spatial/Working drive)",
                   default='U:\\Pastoral_Districts')

    cmd_args = p.parse_args()

    if cmd_args.directory_odk is None:
        p.print_help()

        sys.exit()

    return cmd_args


def temporary_dir_fn(export_dir):
    """ Create a temporary directory 'user_date_time'.
    :param export_dir: string object path to an existing directory where an output folder will be created.
    """
    # extract user name
    home_dir = os.path.expanduser("~")
    _, user = home_dir.rsplit('\\', 1)
    final_user = user[3:]

    # create file name based on date and time.
    date_time_replace = str(datetime.now()).replace('-', '')
    date_time_list = date_time_replace.split(' ')
    date_time_list_split = date_time_list[1].split(':')
    '''
    temp_dir = export_dir + '\\' + final_user + '_' + str(date_time_list[0]) + '_' \
               + str(date_time_list_split[0]) + str(date_time_list_split[1])
    '''
    folder = '{0}_{1}_{2}_{3}'.format(final_user, str(date_time_list[0]),
                                      str(date_time_list_split[0]), str(date_time_list_split[1]))
    temp_dir = os.path.join(export_dir, folder)
    print('export_dir: ', export_dir)
    print('temp_dir: ', temp_dir)

    # check if the folder already exists - if False = create directory, if True = return error message zzzz.

    try:
        shutil.rmtree(temp_dir)

    except:
        print('The following directory did not exist line 105: ', temp_dir)

    # create folder a temporary folder titled (titled 'tempFolder)'
    os.makedirs(temp_dir)
    # print('temp dir created: ', temp_dir)

    prop_output_dir = '{0}\\{1}'.format(temp_dir, 'prop_output')
    prop_output_dir = os.path.join(temp_dir, 'prop_output')
    if not os.path.exists(prop_output_dir):
        os.mkdir(prop_output_dir)

    return temp_dir


def raw_odk_output_workflow_fn(file_path, results_csv, odk_results_list, temp_dir, veg_list_excel, pastoral_estate,
                               odk_complete_dir, property_enquire):
    """ Defines the script pathway depending on what raw ODK files are contained in the directory.

            :param property_enquire: string object containing a pastoral property name to be processed.
            :param odk_complete_dir: string object containing the path to a directory within temp_dir.
            :param odk_results_list: list object containing file paths to the odk results csv files.
            :param results_csv: string object (results file path), sliced from the odk_results_list
            :param file_path: string object containing the dir_path concatenated with search_criteria.
            :param temp_dir: string object path to the created output directory (date_time).
            :param veg_list_excel: string object path to the odk veg-list excel file (botanical and common names).
            :param pastoral_estate: string object containing the file path to the pastoral estate shapefile.
            :return None: """

    print('temp_dir 130 1: ', temp_dir)
    if results_csv == odk_results_list[0]:

        # call the step2_1_star_transect_processing_workflow.py script.
        import step2_1_star_transect_processing_workflow
        step2_1_star_transect_processing_workflow.main_routine(file_path, temp_dir, veg_list_excel, odk_complete_dir,
                                                               property_enquire)

    elif results_csv == odk_results_list[1]:

        # call the step3_1_integrated_processing_workflow.py script.
        import step3_1_integrated_processing_workflow
        step3_1_integrated_processing_workflow.main_routine(file_path, temp_dir, odk_complete_dir, property_enquire)

    elif results_csv == odk_results_list[2]:

        # call the step4_1_basal_processing_workflow.py script.
        import step4_1_basal_processing_workflow
        step4_1_basal_processing_workflow.main_routine(file_path, temp_dir, odk_complete_dir, property_enquire)

    elif results_csv == odk_results_list[3]:

        # call the step5_1_woody_processing_workflow.py script.
        import step5_1_woody_processing_workflow
        step5_1_woody_processing_workflow.main_routine(file_path, temp_dir, odk_complete_dir, property_enquire)

    elif results_csv == odk_results_list[4]:

        # call the step6_1_ras_processing_workflow.py script.
        import step6_1_ras_processing_workflow
        step6_1_ras_processing_workflow.main_routine(file_path, temp_dir, veg_list_excel, pastoral_estate,
                                                     odk_complete_dir, property_enquire)


def raw_odk_output_workflow_remote_auto_fn(file_path, temp_dir, veg_list_excel,
                                           pastoral_estate, odk_complete_dir, property_enquire, version):
    """ Defines the script pathway depending on what raw ODK files are contained in the directory, and calls the
    appropriate script based on the results csv located.

    :param version: string object containing the ODK form version.
    :param property_enquire: string object containing the property name being processed or None (None = ALL properties)
    :param odk_complete_dir: string object containing the path to a directory within temp_dir.
    :param file_path: string object containing the dir_path concatenated with search_criteria.
    :param temp_dir: string object path to the created output directory (date_time).
    :param veg_list_excel: string object path to the odk veg-list excel file (botanical and common names).
    :param pastoral_estate: string object containing the file path to the pastoral estate shapefile.
    """

    _, file_ = file_path.rsplit('\\', 1)

    if file_ == 'RMB_Star_Transect_' + version + '_results.csv':

        # call the step2_1_star_transect_processing_workflow.py script.
        import step2_1_star_transect_processing_workflow
        step2_1_star_transect_processing_workflow.main_routine(file_path, temp_dir, veg_list_excel, odk_complete_dir,
                                                               property_enquire)

    elif file_ == 'RMB_Integrated_' + version + '_results.csv':

        # call the step3_1_integrated_processing_workflow.py script.
        import step3_1_integrated_processing_workflow
        step3_1_integrated_processing_workflow.main_routine(file_path, temp_dir, odk_complete_dir, property_enquire)

    elif file_ == 'RMB_Basal_Sweep_' + version + '_results.csv':

        # call the step4_1_basal_processing_workflow.py script.
        import step4_1_basal_processing_workflow
        step4_1_basal_processing_workflow.main_routine(file_path, temp_dir, odk_complete_dir, property_enquire)

    elif file_ == 'RMB_Woody_Thickening_' + version + '_results.csv':

        # call the step5_1_woody_processing_workflow.py script.
        import step5_1_woody_processing_workflow
        step5_1_woody_processing_workflow.main_routine(file_path, temp_dir, odk_complete_dir, property_enquire)

    elif file_ == 'RMB_Rapid_Assessment_RAS_' + version + '_results.csv':

        # call the step6_1_ras_processing_workflow.py script.
        import step6_1_ras_processing_workflow
        step6_1_ras_processing_workflow.main_routine(file_path, temp_dir, veg_list_excel, pastoral_estate,
                                                     odk_complete_dir, property_enquire)


def assets_search_fn(search_criteria, folder):
    """ Using the search_criteria object search the asses sub-directory for a specific file.

    :param search_criteria: string object containing the name of a file including the file extension.
    :param folder: string object containing the name of a sub-directory located within the asset directory.
    :return: string object containing the located file name.
    """

    path_parent = os.path.dirname(os.getcwd())
    assets_dir = (path_parent + '\\' + folder)
    assets_dir = os.path.join(path_parent, folder)

    files = ""
    file_path = (assets_dir + '\\' + search_criteria)
    file_path = os.path.join(assets_dir, search_criteria)
    for files in glob(file_path):
        print(search_criteria, 'located.')

    return files


def odk_export_csv_checker_fn(directory_odk, located_list, results_csv, odk_results_list, temp_dir,
                              veg_list_excel, pastoral_estate, remote_desktop, odk_complete_dir, property_enquire,
                              version):
    """ Manage the initial workflow, separating remote_atu versus remote, local and offline.
    Calling either raw_odk_output_workflow_remote_auto_fn or raw_odk_output_workflow_fn respectively.

    :param version: string object containing the version number of the ODK forms being processed.
    :param property_enquire: string object containing the single pastoral property to be processed
    (i.e. data filtered by this name).
    :param directory_odk: string object containing the path to the directory housing all of the required ODK result
    csv's.
    :param odk_complete_dir: string object containing the path to a directory within temp_dir.
    :param remote_desktop: string object containing the computer networking capacity  being used (directs workflow).
    :param odk_results_list: list object containing file paths to the odk results csv files.
    :param located_list: list object containing Boolean objects if a specified results csv is located.
    :param results_csv: string object containing the raw odk file name and type.
    :param temp_dir: string object path to the created output directory (date_time).
    :param veg_list_excel: string object path to the odk veg-list excel file
    (containing botanical and common names).
    :param pastoral_estate: string object containing the file path to the pastoral estate shapefile.
    """

    if remote_desktop == 'remote_auto':
        path_parent = os.path.dirname(os.getcwd())
        #raw_odk_dir = (path_parent + '\\raw_odk')
        raw_odk_dir = os.path.join(path_parent, 'raw_odk')
        print('-' * 50)
        print('remote_auto results_csv: ', results_csv)
        file_path = results_csv

    else:
        raw_odk_dir = directory_odk

        #file_path = (raw_odk_dir + '\\' + results_csv)
        file_path = os.path.join(raw_odk_dir, results_csv)

    print('-' * 50)
    if not os.path.exists(file_path):
        located = False
        print(' - NOT LOCATED: ', results_csv)
        print(' - in directory: ', raw_odk_dir)
        print('-' * 50)
    else:

        if remote_desktop == 'remote_auto':

            # call the import_script_fn function.
            raw_odk_output_workflow_remote_auto_fn(file_path, temp_dir, veg_list_excel,
                                                   pastoral_estate,
                                                   odk_complete_dir, property_enquire, version)
        else:
            # call the import_script_fn function.
            raw_odk_output_workflow_fn(file_path, results_csv, odk_results_list, temp_dir, veg_list_excel,
                                       pastoral_estate,
                                       odk_complete_dir, property_enquire)

        located = True
    located_list.append(located)

    return file_path, remote_desktop, located_list


def main_routine():
    # todo update pipeline purpose
    """ This pipeline searches through a directory for the Rangelands Monitoring Branch raw odk outputs.
            :return observation spreadsheet (one per site)
            :return ras spreadsheet (one per site)
            :return

            inputs must include raw odk csv with the name unchanged from the aggregate download.
            Additional inputs are required if running the pipeline outside of the remote desktop (PG-BAS14) and
            processing included integrated data.
            Additional inputs:
     - 3 x .html outputs named of the star transect tables (3 per site)
        naming convention applies (i.e. 'BKE23A_Transect1_.html')

    If running from the remote desktop all downloads are automated.

    """
    # print('createFormatObservationXlsx.py INITIATED.')

    # read in the command arguments
    cmd_args = cmd_args_fn()
    directory_odk = cmd_args.directory_odk
    export_dir = cmd_args.export_dir
    chrome_driver_path = cmd_args.chrome_driver
    remote_desktop = cmd_args.remote_desktop
    time_sleep = int(cmd_args.time_sleep)
    html_dir = cmd_args.html_dir
    version = cmd_args.version
    prop_enquire = cmd_args.property_enquire
    pastoral_districts_path = cmd_args.pastoral_districts_directory

    if prop_enquire:
        property_enquire = prop_enquire.replace(' ', '_').title()
        print('=' * 50)
        print('Processing property: ', property_enquire)
        print('=' * 50)
    else:
        property_enquire = None
        print('=' * 50)
        print('Processing ALL properties..... This will take some time...')
        print('=' * 50)

    veg_list_excel = assets_search_fn("veg_list.xlsx", os.path.join("assets", "veg_list"))
    pastoral_estate = assets_search_fn("NT_Pastoral_Estate.shp", os.path.join("assets", "shapefiles"))
    previous_visits = assets_search_fn("NT_StarTransect_20200713.shp", os.path.join("assets", "shapefiles"))

    # list of the odk files required for the observation and RAS sheets to complete.
    odk_form_list = ["RMB_Star_Transect_" + version, "RMB_Integrated_" + version, "RMB_Basal_Sweep_" + version,
                     "RMB_Woody_Thickening_" + version, "RMB_Rapid_Assessment_RAS_" + version]

    if remote_desktop == "remote_auto":
        # extract user name
        home_dir = os.path.expanduser("~")
        _, user = home_dir.rsplit('\\', 1)

        # remove all old result files from the Downloads directory from the PGB-BAS server.
        #download_folder_path = "C:\\Users" + "\\" + user + "\\Downloads"
        download_folder_path = os.path.join("C:", "Users", user, "Downloads")
        #files = glob(download_folder_path + '\\*results*.csv')
        files = glob(os.path.join(download_folder_path, '*results*.csv'))
        # remove existing results files
        for f in files:
            os.remove(f)
            print('Located and removed: ', files, 'from', download_folder_path)

        # extract odk results csv files from aggregate.
        import step1_2_aggregate_collect_raw_data_remote_desktop
        odk_results_list = step1_2_aggregate_collect_raw_data_remote_desktop.main_routine(
            chrome_driver_path, odk_form_list, time_sleep)

        # purge result csv with 0 observations
        path_parent = os.path.dirname(os.getcwd())
        raw_odk_dir = (path_parent + '\\raw_odk')
        files = glob(raw_odk_dir + '\\*')
        for f in files:
            df = pd.read_csv(f)
            total_rows = len(df.index)
            if total_rows < 1:
                os.remove(f)
                print('Located and removed: ', files, 'from', raw_odk_dir)

        files = glob(download_folder_path + '\\*results.csv')
        # remove existing results files
        odk_results_list = []
        for f in files:
            df = pd.read_csv(f)
            total_rows = len(df.index)
            if total_rows > 1:
                _, file_ = f.rsplit('\\', 1)
                file_output = raw_odk_dir + '\\' + file_
                shutil.move(f, file_output)
                print('-' * 50)
                print('file_output: ', file_output)
                odk_results_list.append(file_output)
                print(file_, 'have been moved to ', raw_odk_dir)

    else:
        # All other workflows that are not remote_auto.
        odk_results_list = []
        for i in odk_form_list:
            file = i + '_results.csv'
            odk_results_list.append(file)
    # create an empty list for located result csv files for processing.
    located_list = []

    # call the temporary_dir_fn function to create a temporary directory located in cmd argument (-x) 'user_date_time'.
    temp_dir = temporary_dir_fn(export_dir)

    # create a directory to store csv files required for fractional cover analysis
    odk_complete_dir = os.path.join(temp_dir, "odk_complete")
    #odk_complete_dir = temp_dir + "\\odk_complete"
    os.mkdir(odk_complete_dir)
    # print('='*50)
    # print('odk results list: ', odk_results_list)
    for results_csv in odk_results_list:
        print('- located: ', results_csv)
        print('- in directory: ', directory_odk)

        # call the odk_export_csv_checker_fn function - search for star transect outputs
        file_path, remote_desktop, located_list = odk_export_csv_checker_fn(
            directory_odk, located_list, results_csv, odk_results_list, temp_dir,
            veg_list_excel, pastoral_estate, remote_desktop, odk_complete_dir,
            property_enquire, version)

    # Verify if an odk file was created and call step18_completeOdkOutputs2.
    print('!' * 50)
    print('located_list: ', located_list)
    if True in located_list:

        # call the step7_site_processing_workflow.py script.
        import step7_site_processing_workflow
        export_site_dir = step7_site_processing_workflow.main_routine(directory_odk, file_path, remote_desktop,
                                                                      temp_dir, veg_list_excel, previous_visits,
                                                                      chrome_driver_path, html_dir, pastoral_estate,
                                                                      odk_complete_dir)

        if remote_desktop != "offline":
            import step12_1_site_outputs_to_working_drive
            step12_1_site_outputs_to_working_drive.main_routine(export_site_dir, pastoral_estate,
                                                                pastoral_districts_path, temp_dir)
        else:
            print('You are offline; as such, site outputs have not been filed to the pastoral district directory')

    else:
        pass

    if remote_desktop != "offline":
        import step12_2_property_outputs_to_working_drive
        step12_2_property_outputs_to_working_drive.main_routine(temp_dir, pastoral_estate, pastoral_districts_path)
    else:
        print('You are offline; as such, property outputs have not been filed to the pastoral district directory')


if __name__ == '__main__':
    main_routine()
