# Test Survey
# Chapter 11 : testing a class
# Tests the anonymous survey class

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """test for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    # adding a second test for multiple inputs
    def test_store_three_responses(self):
        """Test that multiple responses are stored properly"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Chinese']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()