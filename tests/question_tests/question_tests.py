#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_b.question_b import is_prime

class Test_Config(unittest.TestCase):

    def test_is_prime(self):
        self.assertEqual(True, is_prime(5))
        self.assertEqual(False, is_prime(4))
        self.assertEqual(True, is_prime(11))
        