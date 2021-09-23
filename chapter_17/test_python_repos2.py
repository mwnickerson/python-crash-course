# a test for python repos 2

import unittest

import python_repos2 as pr

class PythonReposTestCase(unittest.TestCase):
    """tests for python_repos2.py"""

    def setUp(self):
        """call all the functions here and test individually"""
        self.r = pr.get_response()
        self.repo_dicts = pr.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.repo_links, self.stars, self.labels =\
            pr.get_project_data(self.repo_dicts)

    def test_get_response(self):
        """test for a valid response"""
        self.assertEqual(self.r.status_code, 200)

    def test_repo_dicts(self):
        """test that we are getting the correct data"""
        # expected result is 30 repos
        self.assertEqual(len(self.repo_dicts), 30)
        # repos should have required keys
        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())

if __name__ == '__main__':
    unittest.main()
