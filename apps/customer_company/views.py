from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CustomerCompany
from .serializers import CustomerCompanySerializer

class CustomerCompanyViewSet(viewsets.ModelViewSet):
    queryset = CustomerCompany.objects.all()
    serializer_class = CustomerCompanySerializer

    @action(detail=False, methods=['GET'])
    def company_list(self, request):
        return self.list(request)

    @action(detail=True, methods=['GET'])
    def company_detail(self, request, pk=None):
        return self.retrieve(request, pk)

    @action(detail=False, methods=['POST'])
    def create_company(self, request):
        return self.create(request)

    @action(detail=True, methods=['PUT'])
    def edit_company(self, request, pk=None):
        return self.update(request, pk)

    @action(detail=True, methods=['DELETE'])
    def delete_company(self, request, pk=None):
        return self.destroy(request, pk)
