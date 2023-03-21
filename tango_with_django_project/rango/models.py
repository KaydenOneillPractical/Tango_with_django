from django.db import models

class Category(models.Model):
    Title = models.CharField(max_length=128, unique=True)
    Author = models.CharField(max_length=128, unique=False)
    Date = models.CharField(max_length=128, unique=False)
    Text = models.CharField(max_length=128, unique=False)

    class Meta:
        verbose_name_plural = 'News'


    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title