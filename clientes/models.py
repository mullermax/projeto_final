from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=7,  decimal_places=4)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photo', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
