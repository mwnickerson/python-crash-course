# Survey
# Chapter 11: testing a class
# A class to test

class AnonymousSurvey:
    """collect anonymous answers to a survey question."""

    def __init__(self, question):
        """store a quesion and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_questions(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """store a single response to the survey"""
        self.responses.append(new_response)

    def show_results(self):
        """show all responses that have been given"""
        print("Survey Results:")
        for response in self.responses:
            print(f"- {response.title()}")




