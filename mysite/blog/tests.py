from django.contrib.auth.models import User
from django.test import TestCase

from .models import Post


class PostModelTest(TestCase):

    def test_criar_post(self):
        usuario = User.objects.create_user(
            username="karol",
            password="123456"
        )

        post = Post.objects.create(
            title="Meu primeiro post",
            author=usuario
        )

        self.assertEqual(post.title, "Meu primeiro post")
        self.assertEqual(post.author, usuario)
        self.assertEqual(post.status, 0)

    def test_str_do_post(self):
        usuario = User.objects.create_user(
            username="karol",
            password="123456"
        )

        post = Post.objects.create(
            title="Teste do Post",
            author=usuario
        )

        self.assertEqual(str(post), "Teste do Post")