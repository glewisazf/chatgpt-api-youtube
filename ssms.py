import pyodbc

cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=172.16.0.43:1433;"
                      "Database=AF_Live;"
                      #"Port=1433;"
                      "Trusted_Connection=yes;"
                      "User ID=sap_sa;"
                      "Password=visi0nEE;"
                      )#provider=SQLNCLI11.1;initial catalog=AF_LIVE;data source=sap-sql

cursor = cnxn.cursor()
cursor.execute('SELECT * FROM OHEM')

for row in cursor:
    print('row = %r' % (row,))
