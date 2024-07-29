import re


def question_answer_formatted(long_string):
    # Regular expression pattern to match all questions and answers
    pattern = re.compile(
        r"'Question':\s*'([^']+?)'\s*,\s*'Answer':\s*'([^']+?)'", re.DOTALL)

    # Find all matches in the long string
    matches = pattern.findall(long_string)

    # Initialize the list of dictionaries
    qa_list = [{'Question': question, 'Answer': answer}
               for question, answer in matches]

    # Print the list of dictionaries
    print(qa_list)
