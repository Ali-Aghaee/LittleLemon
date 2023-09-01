from django.test import TestCase
from ..models import Menu

class MenuViewTest(TestCase):
    item = Menu.objects.setup()
    