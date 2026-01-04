from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField(help_text="Write using Markdown")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
