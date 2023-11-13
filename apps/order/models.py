from django.db import models
from apps.customer.models import Customer
from apps.freelancer.models import Freelancer 


class Order(models.Model):

    freelancer = models.ForeignKey(Freelancer, related_name='orders', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.freelancer} -> {self.customer}'
    
    