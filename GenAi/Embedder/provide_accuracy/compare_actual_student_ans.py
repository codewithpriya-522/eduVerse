import os
import google.generativeai as genai
import json
import pyodbc


def generate_response(prompt):
    os.environ['GOOGLE_API_KEY'] = ""
    genai.configure(api_key="")
    # genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    print(response.parts[0].text)
    return (response.parts[0].text)

# store


def strore_stu_per(response):
    server = 'LAPTOP-L8FRP4VT\SQLEXPRESS'
    database = 'rockyproject'
    username = 'LAPTOP-L8FRP4VT\arnab'
    Trusted_Connection = 'yes'

    # Create a connection string
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={Trusted_Connection}'

    # Connect to the SQL Server
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    # stdent performs detailed store

    cursor.execute('''insert into student_persentage (message,percentage)
                       values (?, ?)''', (response.get("message", ""), response.get("percentage", "")))

    conn.commit()

    # Close the connection
    cursor.close()
    conn.close()


stdent = " In a small clearing near the brook, wildflowers bloomed in an explosion of colors. Their petals, vibrant shades of violet, yellow, and crimson, created a stark contrast against the lush green backdrop."
question = "What is the significance of the brook in the forest?"
actual_answer = "The brook is a life-giving force that sustains the flora and fauna along its banks."

prompt = '''you act as a examiner and you will provide the percentage that how accurate is the student answer with actual answer  for the question
given below student answer ,actual answer and question 
response will be in simple json object format.
Here are the keys for the list of JSON objects, Below given the sample response - 
["message":"student answer is correct","percentage":"80%"]

stdent_answer:{stdent_answer},
actual_answer:{actual_answer},
question:{question}
'''
prompt = prompt.format(stdent_answer=stdent,
                       actual_answer=actual_answer, question=question)
data = generate_response(prompt)

response = json.loads(data)

# print(response.get("message", ""))
# print(response.get("percentage", ""))
print(response.get("message", ""))
strore_stu_per(response)
