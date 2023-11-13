from django.db import models


class CustomerCompany(models.Model):

    company_name = models.CharField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, unique=True)
    