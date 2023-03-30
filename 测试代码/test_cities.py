import unittest
from city_function import get_string
class CityTestCase(unittest.TestCase):
    def test_city(self):
        string = get_string('Santiago','Chile')
        self.assertEqual(string,'Santiago,Chile')
    def test_city_population(self):
        string = get_string('santiago','chile',50000)
        self.assertEqual(string,'Santiago,Chile - Population 50000')
if __name__ == '_main_':
    unittest.main()