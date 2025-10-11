#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import reverse_string

class Test_Config(unittest.TestCase):

    def reverse_string(self):
        self.assertEqual(True, reverse_string())


