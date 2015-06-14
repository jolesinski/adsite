from requests import models
from django.db import models
from django.utils import timezone
# Create your models here.


class Advert(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=4095)
    pub_date = models.DateTimeField('date published')
    expire_date = models.DateTimeField('expiration date')
    location = models.CharField(max_length=64)

    def has_expired(self):
        return timezone.now() >= self.expire_date

    def __str__(self):
        return self.title