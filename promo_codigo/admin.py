from django.contrib import admin
from .models import PromoCodigo
# Register your models here.

class CodigoPromoAdmin(admin.ModelAdmin):
    exclude = ['codigo']

admin.site.register(PromoCodigo,CodigoPromoAdmin)

