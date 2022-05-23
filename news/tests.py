from django.test import TestCase
from . models import Editor, Article, tags
# Create your tests here.

class EditorTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.atieno=Editor(firstName='Atieno', lastName='Obwanda',email='atienoobwanda@gmail.com',phone_number='0743068355')
