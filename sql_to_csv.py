"""
Description: Python Code to query a SQL table and write the data into a CSV file.
Author: Aditya Hegde
"""
import pyodbc
import csv
import datetime

driver = '{ODBC Driver 17 for SQL Server}'
server = 'grm-dsc-db-dev.database.windows.net'
database = 'inventory_dev'
username = 'sqladmin'
password = 'Uvw@#4t5e$u9S8oy'

start_date = datetime.date(2019, 1, 1)
end_date = datetime.date(2019, 3, 31)

conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = conn.cursor()
###query = 'select * from dbo.chn_bsak_till_may where augdt between ''2019-01-01'' and ''2019-03-31'' '
###cursor.execute(query)
##cursor.execute("select * from dbo.chn_bsak_till_may where augdt >= %s  and augdt <= %s",start_date,end_date)
cursor.execute("select * from chn_nrp.src_bsik ")
##where augdt >= '2019-10-01
## and augdt <='2019-09-30'
with open("nrp_bsik.csv", "w", newline='', encoding="utf-8") as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(col[0] for col in cursor.description)
    for row in cursor:
        writer.writerow(row)
