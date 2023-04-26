from django.test import SimpleTestCase

# Create your tests here.

class TestSimple(SimpleTestCase):
    def test_equation(self):
        self.assertEquals(1, 2)