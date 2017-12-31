from django.db import models

# Create your models here.
class photography(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    file = models.FileField(default=0)
    def __str__(self):
        return self.title
