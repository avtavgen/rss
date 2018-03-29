import os
from urllib import request
from django.core.files import File
from django.db import models


class RssFeed(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=250)
    link = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    img = models.ImageField(upload_to='images/')
    img_url = models.URLField(blank=True, null=True)
    date = models.CharField(max_length=50)

    def get_remote_image(self):
        if self.img_url and not self.img:
            result = request.urlretrieve(self.img_url)
            self.img.save(
                os.path.basename(self.img_url),
                File(open(result[0], 'rb'))
            )
            self.save()

    def __str__(self):
        return self.title
