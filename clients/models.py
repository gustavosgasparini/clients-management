from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email =  models.EmailField(unique=True)
    age = models.IntegerField()
    bio = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='client_photos', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"