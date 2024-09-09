from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    tags = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title