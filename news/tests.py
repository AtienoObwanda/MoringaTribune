from django.test import TestCase
from . models import Editor, Article, tags
# Create your tests here.

class EditorTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.atieno=Editor(firstName='Atieno', lastName='Obwanda',email='atienoobwanda@gmail.com',phone_number='0743068355')


# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.atieno,Editor))

    def test_save_method(self):
        self.atieno.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)