from django.test import TestCase
from .models import Bug

# Create your tests here.
class ProductTest(TestCase):
    """
    Here we'll define the tests
    that we'll run against our Product models
    """

    def test_str(self):
        test_name = Bug(name='A product')
        self. assertEqual(str(test_name), 'A product')