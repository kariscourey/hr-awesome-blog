from django.db import models

# One
class Post(models.Model):  # inheriting built-in model class that ships with django
    # unique_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.title}"

# Many
class Comment(models.Model):
    # Fields/Columns
    author = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, null=True)
    content = models.TextField(max_length=100)
    # sets up a one-to-many relationship; think OnetoManyField
    post = models.ForeignKey(
        "Post", related_name="coments", on_delete=models.CASCADE
    )  # cascade will delete all comments if you delete the post!

    def __str__(self):
        return ("Comment By {self.author} on {self.post.title}")

# Many
class Keyword(models.Model):
    word = models.CharField(max_length=20)
    posts = models.ManyToManyField("Post", related_name="keywords")

    def __str__(self):
        return self.word
