import pyodbc


def marks_retrive(s_id):
    server = 'LAPTOP-I7B5FA0R\SQLEXPRESS'
    database = 'master'
    #username = 'LAPTOP-L8FRP4VT\arnab'
    Trusted_Connection = 'yes'

    # Create a connection string
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={Trusted_Connection}'

    # Connect to the SQL Server
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    query = "SELECT beng,eng,sci,hist,geo,math FROM  student_performance_detail where s_id=?"

    cursor.execute(query, s_id)

    row=cursor.fetchone()
    # print(type(row))

    # print(row)

    # print(row.beng)
    # print(type(row.eng))
    return row.beng,row.eng,row.sci,row.hist,row.geo,row.math

# Bengali,English,Science,Histry,Geography,MAth=marks_retrive(1)


# prompt=constants.student_stream_selection.format_promt(Bengali=Bengali,English=English,Science=Science,Histry=Histry,Geography=Geography,MAth=MAth)

# data = geminikey.generate_ai_response(prompt)

# print(data)








