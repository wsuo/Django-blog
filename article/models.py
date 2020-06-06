from django.db import models


# Create your models here.


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.TextField()
    abstract = models.TextField()
    content = models.TextField()

