from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
   def test_home_page_status(self):
       context = self.client.get('/')
       self.assertEquals(context.status_code, 200)