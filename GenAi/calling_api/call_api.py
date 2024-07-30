import requests

def call_embedding():
    # Define the URL and payload
    url = 'http://192.168.111.63:5000/api/embedding'
    payload = {
        'pdf_path': 'C:\\Users\\91700\\OneDrive\\Desktop\\GenAi\\pdf'
    }

    # Make the POST request
    response = requests.post(url, json=payload)

    # Check the status code
    if response.status_code == 200:
        try:
            # Store the response in a variable
            response_data = response.json()  # if the response is in JSON format
            # Print the response data
            print(response_data)
            return response_data
        except requests.exceptions.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            print(f"Response text: {response.text}")
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(f"Response text: {response.text}")

    return None


def call_summarization():
    # Define the URL and payload
    url = 'http://192.168.111.63:5000/api/summarization'
    payload = {
        'pdf_path': 'C:\\Users\\91700\\OneDrive\\Desktop\\GenAi\\pdf\\unseen.pdf'
    }

    # Make the POST request
    response = requests.post(url, json=payload)

    # Check the status code
    if response.status_code == 200:
        try:
            # Store the response in a variable
            response_data = response.json()  # if the response is in JSON format
            # Print the response data
            print(response_data)
            return response_data
        except requests.exceptions.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            print(f"Response text: {response.text}")
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(f"Response text: {response.text}")

    return None


def call_question_generation(context):
    # Define the URL and payload
    url = 'http://192.168.111.63:5000/api/questiongeneration'
    payload = {
        'context': context
    }

    # Make the POST request
    response = requests.post(url, json=payload)

    # Check the status code
    # if response.status_code == 200:
    #     try:
    #         Store the response in a variable
    #         response_data = response.json()  # if the response is in JSON format
    #         Print the response data
    #         print(response_data)
    #         return response_data
    #     except requests.exceptions.JSONDecodeError as e:
    #         print(f"Error decoding JSON: {e}")
    #         print(f"Response text: {response.text}")
    # else:
    #     print(f"Request failed with status code: {response.status_code}")
    #     print(f"Response text: {response.text}")

    # return None
       # Make the POST request
    #response = requests.post(url, json=payload)

    # Store the response in a variable
    response_data = response.json()  # if the response is in JSON format

    # Print the response data
    print(response_data)
    return response_data


def call_store_context(question_id):
    # Define the URL and payload
    url = 'http://192.168.111.63:5000/api/storecontext'
    payload = {
        'question_id': question_id
    }

    # Make the POST request
    response = requests.post(url, json=payload)

    # Check the status code
    if response.status_code == 200:
        try:
            # Store the response in a variable
            response_data = response.json()  # if the response is in JSON format
            # Print the response data
            print(response_data)
        except requests.exceptions.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            print(f"Response text: {response.text}")
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(f"Response text: {response.text}")


def call_store_accuracy(question_id):
    url = 'http://192.168.111.63:5000/api/accurecytest'
    payload = {
        'question_id': question_id
    }

    # Make the POST request
    response = requests.post(url, json=payload)

    # Check the status code
    if response.status_code == 200:
        try:
            # Store the response in a variable
            response_data = response.json()  # if the response is in JSON format
            # Print the response data
            print(response_data)
        except requests.exceptions.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            print(f"Response text: {response.text}")
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(f"Response text: {response.text}")


def call_stram_selection(s_id):
    url = 'http://192.168.111.63:5000/api/streamselection'
    payload = {
        's_id': s_id
    }

    # Make the POST request
    response = requests.post(url, json=payload)

    # Check the status code
    if response.status_code == 200:
        try:
            # Store the response in a variable
            response_data = response.json()  # if the response is in JSON format
            # Print the response data
            print(response_data)
        except requests.exceptions.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            print(f"Response text: {response.text}")
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(f"Response text: {response.text}")



# # Example usage
# ##r=call_embedding()
# context = call_summarization()
# if context and "context" in context:
#     print(context["context"])
#     question_ids = call_question_generation(context["context"])
# #question_ids=[1,2,3,4,5]
# if question_ids:
#     for i in question_ids:
#         call_store_context(i)
#     for i in question_ids:
#         call_store_accuracy(i)
response =call_stram_selection(2)
print(response)