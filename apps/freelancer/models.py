from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Freelancer(models.Model):

    phone_number = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    profession = models.CharField(max_length=90)
    what_i_can = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    work_time = models.TimeField(validators=[MinValueValidator(0), MaxValueValidator(99)], default='00:30')
    city = models.CharField(max_length=150)

    def clean(self):
        if self.birth_date:
            age = timezone.now().date().year - self.birth_date.year
            if age < 18:
                raise ValidationError({'birth_date': "Пользователь должен быть старже 18 лет."})
            
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} --> {self.profession}'
    
    