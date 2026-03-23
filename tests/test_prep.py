import unittest
from prep import strange_function


class MyTestCase(unittest.TestCase):

    # Here a == b and c < d, so the function should return behaviour 1
    def test_behaviour_1(self):
        self.assertEqual(strange_function(2, 2, 1, 5), 'behaviour 1')

    # Here a == b but c is not less than d, so it should return behaviour 2
    def test_behaviour_2(self):
        self.assertEqual(strange_function(3, 3, 7, 2), 'behaviour 2')

    # Here a != b, and a < c, so it should return behaviour 3
    def test_behaviour_3(self):
        self.assertEqual(strange_function(1, 2, 3, 4), 'behaviour 3')

    # Here a != b and a is not less than c, so the function goes to the last part
    # Then d < b is true, so it should return behaviour 4
    def test_behaviour_4(self):
        self.assertEqual(strange_function(5, 3, 2, 1), 'behaviour 4')

    # Here a != b and a is not less than c
    # Also d < b is false, but c < a is true, so it should return behaviour 5
    def test_behaviour_5(self):
        self.assertEqual(strange_function(5, 3, 2, 4), 'behaviour 5')

    # Here a != b and a is not less than c
    # Then d < b is false and c < a is also false, so it should return behaviour 6
    def test_behaviour_6(self):
        self.assertEqual(strange_function(5, 3, 5, 4), 'behaviour 6')

    """def test_strange_function1(self):
        self.assertEqual(
            first=strange_function(1, 2, 3, 4),
            second='behaviour 3'
        )"""

    #TODO: Can you write more test cases below to increase the test coverage of `strange_function`?