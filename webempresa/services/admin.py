from django.contrib import admin
from .models import Service
# Register your models here.
#para mostrar las horas en solo texto
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Service, ServiceAdmin)




