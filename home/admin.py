from django.contrib import admin
from .models import listItem
from .models import About
# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'price', 'amount',)
    search_fields = ['name']
    list_fields = ['name', 'price', 'amount']

admin.site.register( listItem,DepartmentAdmin)

admin.site.register( About)
