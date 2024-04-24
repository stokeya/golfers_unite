from django.test import TestCase

class ModelTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data")
        pass

    