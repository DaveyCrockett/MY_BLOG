from urllib import response
from django.test import TestCase
from .models import Post
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
class PostTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "Testuser",
            "test@test.com"
        )

        self.post = Post.objects.create(
            title = "My Post",
            author = self.user,
            body = "Test",
            image = "MEDIA/images/coffee_cup.jpg"
        )

    def test_post_model_string_represtentation(self):
        self.assertEqual(str(self.post), self.post.title)

    def test_post_model_content(self):
        self.assertEqual(f"{self.post.title}", self.post.title)
        self.assertEqual(f"{self.post.author}", f"{self.post.author}")
        self.assertEqual(f"{self.post.body}", self.post.body)
        self.assertEqual(f"{self.post.image}", self.post.image)

    def test_blog_post_list_view_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_blog_post_list_view_content(self):
        response = self.client.get(reverse("blog_post_list"))
        self.assertContains(response, "My Post")
        self.assertContains(response, "Test")
        self.assertContains(response, "Testuser")

    def test_post_detail_view_status_code(self):
        response = self.client.get("/blog_posts/1/")
        self.assertEqual(response.status_code, 200)

    def test_post_create_view_status_code(self):
        response = self.client.get("/new_blog_post/")
        self.assertEqual(response.status_code, 302)
    
    def test_post_delete_view_status_code(self):
        response = self.client.get("/posts/1/delete/")
        self.assertEqual(response.status_code, 302)

    def test_post_edit_view_status_code(self):
        response = self.client.get("/posts/1/edit/")
        self.assertEqual(response.status_code, 302)

    def test_blog_post_list_view_page_reverse_lookup(self):
        response = self.client.get(reverse("blog_post_list"))
        self.assertEqual(response.status_code, 200)