from django.contrib.auth import get_user_model
from django.test import TestCase

from django.urls import reverse

from .models import Post

# Create your tests here.


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username="Rvjonh", email="jonhvelasco3@gmail.com", password="secret"
        )

        cls.post = Post.objects.create(
            title="A good title", author=cls.user, body="Nice body content"
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.author.username, "Rvjonh")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(str(self.post), "A good title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A good title")
        self.assertContains(response, "Nice body content")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detailview(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get(reverse("post_detail", kwargs={"pk": "10000"}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "post_detail.html")
