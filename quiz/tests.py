from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from quiz.views import index
# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)


    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = index(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>quiz</title>', html)  
        self.assertTrue(html.strip().endswith('</html>'))
    
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, '/index.html')
