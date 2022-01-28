from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Company


# Create your views here.


class CompanyView(APIView):

    def get(self, request):
        companys = Company.objects.all()
        return Response({"companys" : companys})


