from django.test import TestCase

# Create your tests here.

from django.test import TestCase, Client

# Create your tests here.
class TestURL(TestCase):
    def test_url_menu(self):
        response = Client().get("/mywatchlist/")
        self.assertEqual(response.status_code, 200)

    def test_url_html(self):
        response = Client().get("/mywatchlist/html/")
        self.assertEqual(response.status_code, 200)

    def test_url_xml(self):
        response = Client().get("/mywatchlist/xml/")
        self.assertEqual(response.status_code, 200)

    def test_url_json(self):
        response = Client().get("/mywatchlist/json/")
        self.assertEqual(response.status_code, 200)