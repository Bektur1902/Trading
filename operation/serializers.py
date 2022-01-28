from rest_framework import serializers
from .models import *


class CompanySerializer(serializers.Serializer):

    title = serializers.CharField(max_length=100)
    manager_name = serializers.CharField(max_length=50)
    manager_second_name = serializers.CharField(max_length=50)
    manger_last_name = serializers.CharField(max_length=50)
    company_adress = serializers.CharField(max_length=100)

