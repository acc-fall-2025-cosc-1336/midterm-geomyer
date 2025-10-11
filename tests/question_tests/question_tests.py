#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_c.question_c import get_assessment_value, get_tax_assessed    

class Test_Config(unittest.TestCase):

    def test_get_assessment_value_10000(self):
        self.assertEqual(get_assessment_value(10000), 6000) # 10000 * 0.6 = 6000
    def test_get_assessment_value_20000(self):
        self.assertEqual(get_assessment_value(20000), 12000) # 20000 * 0.6 = 12000

    def test_get_tax_assessed_6000(self):
        self.assertEqual(round(get_tax_assessed(6000), 2), 43.20) # 6000 * 0.0072 = 43.20
    def test_get_tax_assessed_10000(self):
        self.assertEqual(round(get_tax_assessed(10000), 2), 72.00) # 10000 * 0.0072 = 72.00



