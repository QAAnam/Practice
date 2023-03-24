import pyodbc

# create a connection string
conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=192.168.247.249;'
    r'DATABASE=SDMEGUAT;'
    r'UID="cognizant";'
    r'PWD="cgnznt$";'
)

# create a connection object
conn = pyodbc.connect(conn_str)

# create a cursor object
cursor = conn.cursor()

# execute a SQL query
query = "SELECT * FROM your_table_name"
cursor.execute(query)

# retrieve the results
results = cursor.fetchall()

# process the results
for row in results:
    print(row)

# close the cursor and connection
cursor.close()
conn.close()
