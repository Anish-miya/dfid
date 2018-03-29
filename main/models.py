from __future__ import unicode_literals
from django.db import models
from django.urls import reverse


class Provinces(models.Model):
    province_name = models.CharField(max_length=100)
    minister_name = models.CharField(max_length=50)
    capital = models.CharField(max_length=50)
    districts = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('index', kwargs={'pk': self.pk})

    def __str__(self):
        return self.province_name + '_' + self.minister_name + '_' + self.capital + '_' + self.districts


