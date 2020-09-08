import unittest

from main import camper_age_input

# this piece of code still does not have a use woah the things that can happen
class FunctionTestCase (unittest.TestCase):
    def test_something (self):
        self.assertEqual(72, camper_age_input.convert_to_months(6))


if __name__ == '__main__':
    unittest.main()

