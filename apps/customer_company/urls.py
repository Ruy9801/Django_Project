from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerCompanyViewSet

router = DefaultRouter()
router.register(r'customer_companies', CustomerCompanyViewSet, basename='customer_company')

urlpatterns = [
    path('api/', include(router.urls)),
]