from django.db import models


class Customer(models.Model):

    phone_number = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} --> {self.balance}'
    
