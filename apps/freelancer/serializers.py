from rest_framework import serializers 
from django.contrib.auth import get_user_model 


User = get_user_model()

# first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     birth_date = models.DateField(default=date(1990, 1, 1))
#     avatar = models.ImageField(upload_to='avatars/', blank=True)


#     profession = models.CharField(max_length=90)
#     what_i_can = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2, default=2.00)
#     work_time = models.TimeField(validators=[MinValueValidator(0), MaxValueValidator(99)], default='00:30')
#     city = models.CharField(max_length=150)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)
    password_confirm = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)
    phone_number = serializers.CharField(required=True)
    
    class Meta:
        model = User 
        fields = ('birth_date','what_i_can', 'price', 'work_time', 'city', 'email', 'password', 'password_confirm', 'last_name', 'first_name', 'avatar', 'phone_number')


    def validate(self, attrs):
        password = attrs['password']
        password_confirm = attrs.pop('password_confirm')

        if password != password_confirm:
            raise  serializers.ValidationError(
                'Passwords didnt match!'
            )
        if password.isdigit() or password.isalpha():
            raise serializers.ValidationError(
                'Password feild must contain alpha and numeric symbols'
            )
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        exclude = ('password', )
