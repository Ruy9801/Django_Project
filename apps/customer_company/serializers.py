from rest_framework import serializers
from .models import CustomerCompany

class CustomerCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCompany
        fields = '__all__'
