from django.test import TestCase, Client  # client allows to make fake requests to views
from django.utils import timezone
from posts.models import Post
from django.db.utils import IntegrityError

class PostModelTestCase(TestCase):
    def test_title_should_be_less_than_100(self):
        # Arrange
        # Create sample data for post
        title = "X" * 200
        created_at = timezone.now()
        content = "whatever"

        # Act
        post = Post.objects.create(title=title,created_at=created_at,content=content)

        # Create post
        # Assert
        # assert it failed
        self.assertNotEqual(post.title,title)

    def test_created_at_is_a_required_field(self):
        title = "Sample Post"
        content = "Sample Content"

        try:
            post = Post.objects.create(title=title,content=content)
        except IntegrityError as error:
            self.assertIsInstance(error, IntegrityError)

        with self.assertRaises():
            post = Post.objects.create(title=title, content=content)

class PostListViewTestCase(TestCase):
    pass
