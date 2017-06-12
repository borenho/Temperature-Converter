import unittest
from temp_converter import convert_celsius_to_fahrenheit

class TempConverterTest(unittest.TestCase):
    # convert temperature from celsius to F
    # test data type input

    def test_celsius_is_converted_to_fahrenheit(self):
        """
            F = C * 9/5 +32
        """
        actual = convert_celsius_to_fahrenheit(10)
        expected = 50
        self.assertEqual(actual, expected, 'Celsius should convert to crrect Fahrenheit value')
        self.assertEqual(convert_celsius_to_fahrenheit(20), 68, 'Celsius should convert to crrect Fahrenheit value')