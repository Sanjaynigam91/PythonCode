import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=LAPTOP-FD48K96U\\SQLEXPRESS;" # your_server_name
    "DATABASE=LISCare;" # your_database
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

#cursor.execute("SELECT name FROM sys.databases")

cursor.execute("select * from tbl_LIS_Users")



for row in cursor:
    print(row)



conn.close()