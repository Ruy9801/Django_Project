from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password 
from django.contrib.auth.models import AbstractUser
from datetime import date

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        if not email:
            return ValueError('Email is required')
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.create_activation_code()
        user.password = make_password(password)
        user.save()
        return user
    
    def create_user(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)
    
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        return self._create_user(email, password, **kwargs)


class Freelancer(AbstractUser):

    phone_number = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(default=date(1990, 1, 1))
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    
    profession = models.CharField(max_length=90, default='self-taught')
    what_i_can = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=2.00)
    work_time = models.TimeField(validators=[MinValueValidator(0), MaxValueValidator(99)], default='00:30')
    city = models.CharField(max_length=150)
    username = None

    activation_code = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def clean(self):
        if self.birth_date:
            age = timezone.now().date().year - self.birth_date.year
            if age < 18:
                raise ValidationError({'birth_date': "Пользователь должен быть старже 18 лет."})
            
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} --> {self.profession}'
    
    def create_activation_code(self):
        import uuid 
        code = str(uuid.uuid4())
        self.activation_code = code