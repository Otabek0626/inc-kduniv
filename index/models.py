from django.db import models
from datetime import datetime
# Create your models here.

def upload_location(instance, filename):
    filebase, extension = filename.split('.')
    return 'static/assets/images/%s.%s' % (f'{instance.email}_{instance.first_name}', extension)



class Profile(models.Model):
    first_name = models.CharField(max_length = 50)
    middle_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = upload_location)
    country = models.CharField(max_length = 50)
    nationality = models.CharField(max_length = 50)
    passport_number = models.CharField(max_length = 50)
    home_address = models.CharField(max_length = 150)
    current_address = models.CharField(max_length = 150)
    tel_number_home = models.CharField(max_length = 50)
    tel_number_mobile = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 100)
    name_of_institution = models.CharField(max_length = 50)
    address_of_institution = models.CharField(max_length = 150)
    degree = models.CharField(max_length = 50)
    department = models.CharField(max_length = 150)
    major = models.CharField(max_length = 150)
    tem_number_of_institution = models.CharField(max_length = 50)
    email_of_institution = models.EmailField(max_length = 100)
    english = models.CharField(max_length = 50)
    korean = models.CharField(max_length = 50)
    statement_of_interest = models.TextField()
    applied_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return f"{self.first_name}, {self.gender}, {self.country}, {self.email}, {self.email}, {self.applied_at}"