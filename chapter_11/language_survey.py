# Language survey
# Chapter 11: Testing a class
# The program for the function

from survey import AnonymousSurvey

# Define a question and make a survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question and store the responses to the question
my_survey.show_questions()
print("Enter 'q' to quit at anytime")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results
print("\nThank you for the responses")
my_survey.show_results()