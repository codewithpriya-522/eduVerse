prompt = """
    Can you please look at the provided JSON data and provide a step by step summary in the response, which is easy to understand. don't provide any additional text or preface or any other suggestion: {query}"""

user_prompt = """JSON: {query}"""


question_generator_prompt = '''You have act as an teacher , there will a context will be provided you have to generate five meaningful questions and answer out of them.
response will be in simple json object format.
Please follow the instructions-
1. Dont change the properties name of the json objects. Follow the below sample response. Keys are must be "Question" and "Answer"
Here are the keys for the list of JSON objects, Below given the sample result - 
[{"Question":"The question from the context","Answer":"The answer from the context of the question"}]
One must follow rule , do not any format of the JSON objects list. Follow the above result only.
Context -
'''

student_result_analyzer_prompt = '''you act as a examiner and you will provide the percentage that how accurate is the student answer with actual answer  for the question.
The actual answer in hidden in the context. You have to understand the context and find out the answer.
response will be in simple json object format.
There are few key factors to generate the percentage -
1. check the accuracy of grammer of the student answer.
2. check the meaningfullness of the student answer.
3. Check how much creative with the answer.
Here are the keys for the list of JSON objects, Below given the sample response - 
["message":"feedback of the student answer","percentage": "The matching percentage","actual_answer":"The actual answer accrding to your understanding"]

stdent_answer:{stdent_answer}
question:{question}
context:{context}

'''

#promt for stream selection
student_stream_selection=''' You have act as examiner you have to select stream  for each student based on his performace of each subject result .
response will be in simple json object format.
There are few key factors to  genarate stream -
1.cheak result of each subject
2.if student is good in histry,geography then it is better you will provide 'arts'  stream
3. if student is good in maths,science then it is better you will provide 'science' stream
4. if student is good in math then it is better you will provide 'commarce' stream
Here are the keys for the list of JSON objects, Below given the sample response - 
["stream":"selected stream"]

Bengali:{Bengali}
English:{English}
Science:{Science}
History:{Histry}
Geography:{Geography}
MAth:{MAth}




'''


# Mapping of separators for document splitting
separator_mapping = {
    "character": "",
    "word": " ",
    "sentence": ".",
    "line": "\n",
    "paragraph": "\n\n"
}

indexBody = {
    "settings": {
        "index.knn": True
    },
    "mappings": {
        "properties": {
            "vector_field": {
                "type": "knn_vector",
                "dimension": 1536,
                "method": {
                    "engine": "faiss",
                    "name": "hnsw"
                }
            }
        }
    }
}
