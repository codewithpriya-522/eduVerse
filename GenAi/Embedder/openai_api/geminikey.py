import os
import google.generativeai as genai


def generate_ai_response(prompt):
    os.environ['GOOGLE_API_KEY'] = ""
    genai.configure(api_key="")
    # genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response


# def check_accuracy_provide_percentage(prompt):
#     os.environ['GOOGLE_API_KEY'] = ""
#     genai.configure(api_key="")
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content(prompt)
