import unittest
from lecture import randomised_function

"""class MyTestCase(unittest.TestCase):

    def test_randomised_function(self):
        self.assertEqual('software', randomised_function())  # This will pass or fail randomly"""

from unittest.mock import patch
class MyTestCase(unittest.TestCase):

    # If randint returns a number smaller than 5,
    # is_small(a) becomes True, so the function should return 'software'
    @patch('random.randint', return_value=3)
    def test_randomised_function_returns_software(self, mock_randint):
        self.assertEqual('software', randomised_function())

    # If randint returns 5 or more,
    # is_small(a) becomes False, so the function should return 'engineering'
    @patch('random.randint', return_value=8)
    def test_randomised_function_returns_engineering(self, mock_randint):
        self.assertEqual('engineering', randomised_function())
        # TODO: Can we make this test deterministic? (HINT: Mock testing)
