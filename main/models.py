from django.db import models

# Create your models here.


class Account(models.Model):
    email = models.CharField(max_length=200, verbose_name='Email')
    password = models.CharField(max_length=200, verbose_name='Password')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

