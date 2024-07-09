from django.test import TestCase
from django.urls import resolve, reverse
from lists.views import HomePageView

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func.__name__, HomePageView.as_view().__name__)

    def test_home_page_returns_correct_html(self):
        response = self.client.get(reverse('Home'))
        self.assertTemplateUsed(response, 'lists/home.html')
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith("<html>"))
        self.assertIn('<title>To-Do Lists</title>', html)
        self.assertTrue(html.strip().endswith("</html>"))