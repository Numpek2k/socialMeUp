from django.db import models
from django.contrib.auth.models import User


# Create your models here.


def get_path(instance, filename):
    return '{0}/{1}'.format(instance.author.username, filename)


class Files(models.Model):
    postedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_path, blank=True)
    title = models.CharField(max_length=100, default='')
    description = models.TextField(blank=True)

    def image_path(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class Comments(models.Model):
    postedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ForeignKey(Files, on_delete=models.CASCADE)
    content = models.TextField()


class Friends(models.Model):
    idWho = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person')
    idWhom = models.ForeignKey(User, on_delete=models.CASCADE)
