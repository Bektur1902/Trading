from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Company)
admin.site.register(Product)
admin.site.register(Price)
admin.site.register(PaymentAccount)
admin.site.register(ProductPrice)
admin.site.register(Purchases)
admin.site.register(Sales)


