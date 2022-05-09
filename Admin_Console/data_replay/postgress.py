import csv

import psycopg2

'''Script performs the connection to postgres psql data base and verifying the total no of records in the trans tables
'''
connection = psycopg2.connect \
    (database="",  # provide db name
     user="",  # provide user name of postgres psql
     password="",  # provide the password of postgres psql
     host="",  # provide the host ip address
     port="")  # provide the port number

destination_file = "/home/ubuntu/Data_Retention_result.csv"
cursor = connection.cursor()
# Print PostgreSQL Connection properties
print(connection.get_dsn_parameters(), "\n")
before_crc = cursor.execute('select count(*) from crc_inspection_trans')
before_pat = cursor.execute('select count(*) from periodic_exam_result_trans')
before_sat = cursor.execute('select count(*) from semester_exam_result_trans')
before_diksha = cursor.execute('select count(*) from diksha_content_trans')

data_source = [before_crc, before_diksha, before_pat, before_sat]
heading = "Before Doing Locators retention"

after_crc = cursor.execute('select count(*) from crc_inspection_trans')
after_pat = cursor.execute('select count(*) from periodic_exam_result_trans')
after_sat = cursor.execute('select count(*) from semester_exam_result_trans')
after_diksha = cursor.execute('select count(*) from diksha_content_trans')

current_records = [after_crc, after_diksha, after_pat, after_sat]
with open(destination_file, 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(heading)
    writer.writerow(data_source)

# after data retention      # writer.writerow(current_records)
cursor.close()
connection.close()
