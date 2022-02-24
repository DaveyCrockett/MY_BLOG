from urllib import response
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class Pages(SimpleTestCase):

    def test_home_page_view_is_up(self):
        response = self.client.get("/dash/home/")
        self.assertEqual(response.status_code, 200)

    def test_about_page_view_is_up(self):
        response = self.client.get("/dash/about/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_view_uses_correct_template(self):
        response = self.client.get("/dash/home/")
        self.assertTemplateUsed(response, "pages/home.html")
        self.assertTemplateUsed(response, "base.html")

    def test_about_page_view_uses_correct_template(self):
        response = self.client.get("/dash/about/")
        self.assertTemplateUsed(response, "pages/about.html")
        self.assertTemplateUsed(response, "base.html")
    
    def test_home_page_view_uses_correct_content(self):
        response = self.client.get("/dash/home/")
        self.assertContains(response, "HOME PAGE")

    def test__page_view_uses_correct_content(self):
        response = self.client.get("/dash/about/")
        self.assertContains(response, "ABOUT PAGE")

    def test_home_page_reverse_lookup(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_reverse_lookup(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

