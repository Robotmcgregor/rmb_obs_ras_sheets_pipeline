
[Back to Remote Sensing Wiki](https://github.com/Robotmcgregor/ntg_wiki/wiki)
# RMB Observation and RAS Sheet Pipeline

**Description**: This pipeline comprises of 49 scripts which access ODK Aggregate and produce RAS and Observational sheets
which are RLM database compliant. This pipeline produces cleaned csv file outputs and shapefies for each data point
located within the property bounds. The property level start transect csv is in the required format to run:
 - RMB Fractional Cover Zonal Stats Pipeline.
 Additionally, the pipeline collates and labels all photographs to be database compliant.
 
All outputs are filed in their respective property directory located on the Darwin Working drive.

**Note**: Due to the IT infrastructure of the remote desktop, the data extraction from ODK Aggregate is known to fail due to 
a stale element error. Command prompt --time_sleep can be adjusted range should be between 5 and 20.

## Outputs
### ODK Aggregate cleaned results
- **Output 1**: star_transect.csv
- **Output 2**: integrated.csv
- **Output 3**: basal.csv
- **Output 4**: woody_thickening.csv
- **Output 5**: ras.csv

### General
- **Output 6**: point data shapefile for each csv (above)
- **Output 7**: Point data shapefile for north offset ( used for pastoral infrastructure)
- **Output 8**: Observation excel sheet for each integrated site - RLM database compliant
- **Output 9**: Ras excel sheet for each RAS or Tier 1 site
- **Output 10**: Rename and download all photos for the property

**Note**: All outputs are filed to relevant property directory within th working drive when using **remote_auto**, 
**remote** or **local** workflows. If using **offline** outputs remain in the **output_dir** location.


Command arguments:
------------------

 - **tile_grid**
    - String object containing the path to the Landsat tile grid shapefile.


 - **directory_odk**:
    - String object containing the directory where odk aggregate from outputs will be saved or where they have 
      already been saved dependent on the command argument **remote_auto**.
      

 - **export_dir**:
    - String object containing the path to a directory. An export directory tree will be created here, with all outputs 
exported here.
      

 - **mosaic_dir**:
    - String object containing the path to the Landsat seasonal mosaic directory (default value is r'Z:\Landsat\mosaic').
   Note: deviation from this structure fill cause the pipeline to fail; however, path changes can be easily made on 
   step1_1_initiate_fractional_cover_zonal_stats_pipeline.py
      

- **chrome_driver**:
  - String object containing the directory where the chrome driver extension is located:
    Default location: r"E:\\DEPWS\\code\\rangeland_monitoring\\rmb_aggregate_processing\\assets\\chrome_driver\\chrome_driver_v89_0_4389_23\\chromedriver.exe"


 - **remote_desktop**:
   - String object controlling the workflow based on the computer you are running the pipeline from, and the 
     consequential restraints in the automation process __remote_auto__ is the recommended workflow.
     

        -remote_auto: Run on the Remote Desktop - Entire process is automated - only the property name is required and a command argument
       

        - remote: Run on the Remote Desktop - Data processing and filing of outputs is automated
          1. you are required to download ODK form result csv from ODK Aggregate prior to running this pipeline
          2. ODK Aggregate csv results MUST be located the directory defined by command argument **odk_dir**. 
          
            **Note**: Speeds up process by reducing interaction with the ODK Aggregate front end.
        

        - local: Run from your NTG online computer (006 WIFI) - Data processing and filing of outputs is automated
          1. you are required to download ODK form result csv from ODK Aggregate prior to running this pipeline
          2. ODK Aggregate csv results MUST be located the directory defined by command argument **odk_dir**. 
          3. You are also required to download Star Transect HTML tables ODK form result csv from ODK Aggregate prior to running this pipeline
          2. ODK Aggregate csv results MUST be located the directory defined by command argument **odk_dir**. 


        - offline: Run from any computer not associated with NTG systems - rmb_zonal python environment recommended.
          1. you are required to download ODK form result csv from ODK Aggregate prior to running this pipeline
          2. ODK Aggregate csv results MUST be located the directory defined by command argument **odk_dir**. 
          3. You are also required to download Star Transect HTML tables ODK form result csv from ODK Aggregate prior to running this pipeline
          2. ODK Aggregate csv results MUST be located the directory defined by command argument **odk_dir**. 
    **Note**: Outputs will not be filed beyond the **output_dir** command argument location.


- **assets_shapefiles_dir**:
  - String object containing the directory where the required shapefiles are located.
    Default location: r"E:\\DEPWS\\code\\rangeland_monitoring\\rmb_aggregate_processing\\assets\\shapefiles"


- **time_sleep**:
  - integer object identifying the length of time in seconds the Windows system will sleep between actions when 
    interacting with the front end of ODK Aggregate.
     Default time: 20


- **html_dir**:
  - String object containing the directory where the required star transect html tables will be located.
    Default location: r"E:\\DEPWS\code\\rangeland_monitoring\\rmb_aggregate_processing\\html_transect"
    **Note**: When working in **remote_auto** and **remote** the pipeline will take care of this action. 
    Whereas, when working in **offline** or **local** you need to save these files here.

 - **ver**:
  - String object identifying the ODK form version (i.e. v1 or v2)
     Default version: v2
    
 - **property_enquire**:
  - String object identifying the property you are wishing to process(eg. PROPERTY_NAME)", 
    Default string: None - will run all data contained within ODK Aggregate


 - **pastoral_districts_directory**:
  - String object containing the directory where the required Pastoral_Districts directory is located 
    (i.e. Spatial/Working drive), 
    Default string: r'U:\\Pastoral_Districts'

