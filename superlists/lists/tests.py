from django.test import TestCase
from django.urls import resolve
from lists.views import HomePageView

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func.__name__, HomePageView.as_view().__name__)