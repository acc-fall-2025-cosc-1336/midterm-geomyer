#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import reverse_string    
from src.question_b.question_b import is_prime
from src.question_c.question_c import get_assessment_value, get_tax_assessed
from src.question_d.question_d import get_person_category

class Test_Config(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_is_prime(self):
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(11))

    def test_get_assessment_value_10000(self):
        self.assertEqual(get_assessment_value(10000), 6000) # 10000 * 0.6 = 6000
    def test_get_assessment_value_20000(self):
        self.assertEqual(get_assessment_value(20000), 12000) # 20000 * 0.6 = 12000

    def test_get_tax_assessed_6000(self):
        self.assertEqual(round(get_tax_assessed(6000), 2), 43.20) # 6000 * 0.0072 = 43.20
    def test_get_tax_assessed_10000(self):
        self.assertEqual(round(get_tax_assessed(10000), 2), 72.00) # 10000 * 0.0072 = 72.00

    def test_get_person_category(self):
        self.assertEqual(get_person_category(0), "Infant")
        self.assertEqual(get_person_category(1), "Infant")
        self.assertEqual(get_person_category(5), "Child")
        self.assertEqual(get_person_category(12), "Child")
        self.assertEqual(get_person_category(15), "Teenager")
        self.assertEqual(get_person_category(19), "Teenager")
        self.assertEqual(get_person_category(20), "Adult")
        self.assertEqual(get_person_category(70), "Adult")