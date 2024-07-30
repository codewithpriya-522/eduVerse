# import typing_extensions as typing
# import os
# import requests
# from langchain.llms import BaseLLM
# import google.generativeai as genai
# # pip install langchain google-cloud google-cloud-language

# # Set up the Google API key
# GOOGLE_API_KEY = ""

# # Define a function to use Google Generative AI (e.g., NLP analysis) via API key


# def analyze_text(text):
#     url = f"https://language.googleapis.com/v1/documents:analyzeEntities?key={GOOGLE_API_KEY}"
#     headers = {
#         "Content-Type": "application/json"
#     }
#     data = {
#         "document": {
#             "type": "PLAIN_TEXT",
#             "content": text
#         }
#     }
#     response = requests.post(url, headers=headers, json=data)
#     return response.json()

# # Integrate with LangChain (you might need to extend or modify BaseLLM)


# class GoogleCloudLLM(BaseLLM):
#     def __init__(self, api_key):
#         self.api_key = api_key

#     def generate(self, prompt):
#         result = analyze_text(prompt)
#         # Process result to extract desired information (this is a placeholder)
#         response_text = result
#         return response_text


# def generative_text_response(prompt):
#     # Example usage of LangChain with Google Generative AI
#     llm = GoogleCloudLLM(api_key=GOOGLE_API_KEY)

#     # Example prompt
#     # prompt = "Explain the benefits of using Google Generative AI with LangChain."

#     # Generate a response
#     response = llm.generate(prompt)
#     print(response)


# # Define your schema

# class Product(typing.TypedDict):


#     title: str
#     description: str
#     category: str
#     subcategory: str
#     estimatedPrice: str


# # Call the API
#     model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

#     result = model.generate_content(
#     "List 5 office supplies for my e-commerce website",
#     generation_config=genai.GenerationConfig(response_mime_type="application/json",
#                                              response_schema=list[Product]))

#     print(result.text)
