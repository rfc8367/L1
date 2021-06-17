import unittest
from L6 import L6_Task_1
from L7 import L7_Task_2
from L11 import L11_Task_2
from L15 import L15_Task_2


class Testing6(unittest.TestCase):

    def currency_test(self):
        coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
        code = ('BTC', 'ETH', 'XRP', 'LTC')
        self.assertEqual(L6_Task_1.new_dictionary(coin, code),
                         {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'})



class Testing7(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(L7_Task_2.celsius_to_fahrenheit(40), 'Temperature. C to F: ')

    def test_celsius_to_kelvin(self):
        self.assertEqual(L7_Task_2.celsius_to_kelvin(23), 'Temperature. C to K: ')


    def test_fahrenheit_to_celsius(self):
        self.assertEqual(L7_Task_2.ahrenheit_to_celsius(65), 'Temperature. F to C: ')

    def test_fahrenheit_to_kelvin(self):
        self.assertEqual(L7_Task_2.fahrenheit_to_kelvin(83), 'Temperature. F to K: ')


    def test_kelvin_to_celsius(self):
        self.assertEqual(L7_Task_2.kelvin_to_celsius(11), 'Temperature. K to C: ')

    def  kelvin_to_fahrenheit(self):
        self.assertEqual(L7_Task_2.kelvin_to_fahrenheit(33), 'Temperature. K to F:  ')




class Testing11(unittest.TestCase):

    def email_test(self):
        self.assertEqual(L11_Task_2.mail_hider('what_is_the_name_of_half-life_speedrun@a_minute_of_silence.com'),
                         'wh**@**e.com')

class Testing15(unittest.TestCase):

    def phone_test(self):
        self.assertEqual((L15_Task_2.formatting('063-999-99-99'), '(+38) 063 999-99-99'),
        self.assertEqual((L15_Task_2.formatting('063 999-99-99'), '(+38) 063 999-99-99'),
        self.assertEqual((L15_Task_2.formatting('063-99999-99'), '(+38) 063 999-99-99'),
        self.assertEqual((L15_Task_2.formatting('+3806399999-99'), '(+38) 063 999-99-99'),
        self.assertEqual((L15_Task_2.formatting('380639999999'), '(+38) 063 999-99-99')

if __name__ == '__main__':
    unittest.main()

