from django.db import models

# Create your models here

    


class Post(models.Model):
    name = models.CharField(max_length=250)
    CATEGORY_CHOICES = (
        ('EVENTS', 'EVENTS'),
        ('STUDIO', 'STUDIO'),
        ('STREET PHOTOGRAPHY', 'STREET PHOTOGRAPGY'),
    )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    image = models.FileField(blank=True)
    


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'pics/')


