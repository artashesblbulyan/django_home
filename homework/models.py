from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

STATUS_CHOICE = (
    (0, "Yes"),
    (1, "No"),
)




class Homework(models.Model):
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    is_active = models.IntegerField(choices=STATUS_CHOICE, default=0)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}"





