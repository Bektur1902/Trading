from django.urls import path
from .views import CompanyView

app_name = 'companys'

urlpatterns = [
    path('companys/', CompanyView.as_view()),
]
