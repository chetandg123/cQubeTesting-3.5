
# cQube Release-3.5

###  Prerequisites:
 - Open the Terminal
 - Google Chrome need to be installed in the server.
 - Steps to install the google chrome
 ```
   wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
   sudo apt install ./google-chrome-stable_current_amd64.deb
   Check chrome brower version using command -> google-chrome -version
  ```
 - Navigate to the directory where cQubeTesting-3.5 has been downloaded or cloned 
```
  cd cQube_Workflow/tests/cQubeTesting-3.5/
  ```
 - Chrome driver need to be downloaded and placed in the cQubeTesting-3.5/Driver/ folder.
 - Steps to Download the chrome driver 

 	Note: Based on the chrome browser version need to download chrome driver ```https://sites.google.com/chromium.org/driver/```
   
 - AWS S3 Configuration
```
  sudo apt-get install awscli
  aws configure
  AWS Access Key ID : #Fill the AWS Access key provided in the config.yml
  AWS Secret Access Key : #Fill the AWS Secret Access Key provided in the config.yml
  Default region name [None]: #Fill the Default region (Not manadatory to fill)
  Default output format [None]: #Fill the Default output format (Not manadatory to fill)
  ```
  
 
# Steps to execute the test script

    
     cd cQubeTesting/
     sudo apt update
     sudo apt install python3-pip
    
 - Execute the Requirement.txt in the terminal (Requirement.txt file is present in the cQubeTesting-3.5 Folder) [mandatory]
 ```
  sudo pip3 install -r Requirement.txt
 ```
 - Fill the config.ini file (config.ini file present in the cQubeTesting-3.5 Folder).
 
# Mandatory fields for installation and upgradation of backend configuration testing
### Note: Nifi Port must be opened(ie: 8096)
```		
[config]
domain= #Fill the domain name provided in the config.yml file ex: https://domain_name
username= #Fill the username for cQube login
password= #Fill the password for cQube login
basedirpath= #Fill the installation directory provided in the config.yml file ex:/opt
host=localhost
port=5432
database= #Fill the db name which is provided in the config.yml file
user= #Fill the db user which is provided in the config.yml file
db_password= #Fill the db user which is provided in the config.yml file                  
```                  
# Execution of automation testscripts for both installation and upgradation of backend configuration

 ``` 
 python3 -m unittest TestSuites/cQubeBackendConfiguration/run_configuration.py 
 ```
 
 
# Mandatory fields for installation and upgradation of Data Processing

```
[config]
domain= #Fill the domain name provided in the config.yml file ex: https://domain_name

[datasource]
#Implemented customized suite running - Enable or disable data source while running scripts [true or false]
nifi_static= true
nifi_crc= true
nifi_attendance= true
nifi_infra= true
nifi_diksha= true
nifi_telemetry= true
nifi_udise= true
nifi_pat= true
nifi_composite= true
nifi_progresscard= true
nifi_teacher_attendance= true
nifi_data_replay= true
nifi_sat= true

storage_type= #Fill the storage type which is specified in the config.yml while installation ex: s3 or local
bucket_name= #Fill the emission bucket_name which is specified in the config.yml while installation ex: cqube-test-emission Note: if your using storage_type as 'local' then no need to fill the bucket_name
emission_directory= #Fill the emission_directory which is specified in the config.yml while installation ex: /home/ubuntu/emission/ Note: if your using storage_type as 's3' then no need to fill the emission_directory

[filepath]
#Fill the absolute path ex: /home/ubuntu/district_mst.zip
district_master=
block_master=
cluster_master=
school_master=
school_management=

inspection_master=
user_location_master=

infra_trans=

student_attendance=
teacher_attendance=

udise=

periodic_exam_grade_details=
periodic_exam_subject_details=
periodic_exam_master=
periodic_exam_qst_master=
periodic_exam_result_trans=

semester_exam_grade_details=
semester_exam_subject_details=
semester_exam_master=
semester_exam_qst_master=
semester_exam_result_trans=
```             
# Execution of automation testscripts for both installation and upgradation of Data Processing

 ``` python3 -m unittest TestSuites/cQubeBackendConfiguration/run_workflow.py ```
 
# Mandatory fields for cQube UI application                    
### Before running Regression and System test suites please fill the data_source.ini file to run customized suite run
```
[data_source]		
#Implemented customized suite running - Enable or disable data source while running scripts [True or False] -
student=True
teacher=True
crc=True
composite=True
pat=True
sat=True
udise=True
telemetry=True
infrastructure=True
Diksha_ETB=True
Diksha_TPD=True						
		
[config]
domain= #Enter the url of the cqube application ex: https://<domain_name>/ or http://<ip>:4200
username= #Enter the username of report viewer
password= #Enter the password of report viewer
admin_username = #Enter the admin user name
admin_password = #Enter the admin password
createadmin= #for creating new admin user provide name of admin
adminpassword= # Enter password for new admin
createviewer= #for creating new admin user provide name of reportviewer
viewerpassword= # Enter password for new viewer
createemission= #for creating new admin user provide name of emission user
emissionpassword= # Enter password for new emission user
```

# Navigate to cQubeTesting-3.5 Directory in the terminal (ex cd /home/ubuntu/cQubeTesting-3.5)
### Note : To Test admin console test suite. Need to connected with vpn 

- For Regression:
```
python3 -m unittest TestSuites/Regression_suite/regression_map_reports.py
python3 -m unittest TestSuites/Regression_suite/regression_chart_table_reports.py
python3 -m unittest TestSuites/Regression_suite/regression_diksha_tpd_reports.py
python3 -m unittest TestSuites/Regression_suite/regression_exception_reports.py
python3 -m unittest Admin_console/admin_console_regression_testing.py
```
            
- For System Testing:
```
python3 -m unittest TestSuites/System_testing_suite/system_testing_suite.py
python3 -m unittest TestSuites/System_testing_suite/system_suite_2.py
python3 -m unittest Admin_console/admin_console_system_testing.py
```           
- For Smoke Testing:
```
python3 -m unittest TestSuites/SmokeTestSuite/smoke_test_map_reports.py
python3 -m unittest TestSuites/SmokeTestSuite/smoke_test_chart_table_reports.py
python3 -m unittest TestSuites/SmokeTestSuite/smoke_test_exception_reports.py
python3 -m unittest Admin_console/Admin_smoke_testsuit.py
```		

 ### Note : After execution of scripts,the report will be generated and present in the Reports folder
