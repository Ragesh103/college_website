from django.db import models

# Create your models here.
class students(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    middlename = models.CharField(max_length = 255)
    housename = models.CharField(max_length = 255,)
    fathername = models.CharField(max_length = 255)
    mobile = models.IntegerField()
    depart = models.CharField(max_length=255)


class teachers(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    middlename = models.CharField(max_length =255)
    emailid = models.EmailField()
    mobile = models.IntegerField()
    dep = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='teacher_photos/',blank=True,null=True)
    designation = models.CharField(max_length=255)

class departments(models.Model):
    depname = models.CharField(max_length = 255)
    depcode = models.CharField(max_length = 255)

