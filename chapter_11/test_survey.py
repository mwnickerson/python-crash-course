# Test Survey
# Chapter 11 : testing a class
# Tests the anonymous survey class
# using setUp to shorten the code
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """test for the class AnonymousSurvey"""

    def setUp(self):
        """
        create a survey and a set of responses for use in all test methods
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Chinese']

    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    # adding a second test for multiple inputs
    def test_store_three_responses(self):
        """Test that multiple responses are stored properly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()