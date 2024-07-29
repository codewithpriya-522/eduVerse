
import pyodbc


def stream_stroe(s_id,stream_sub):
    server = 'LAPTOP-I7B5FA0R\SQLEXPRESS'
    database = 'master'
    #username = 'LAPTOP-L8FRP4VT\arnab'
    Trusted_Connection = 'yes'

    # Create a connection string
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={Trusted_Connection}'

    # Connect to the SQL Server
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    query = "insert into stream_select (s_id,stream_sub) values (?,?)"

    cursor.execute(query, (s_id, stream_sub))
    conn.commit()  # commit the transaction to the database
    cursor.close()
    conn.close()
    
