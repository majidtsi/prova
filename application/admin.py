from django.contrib import admin
from .models import Cliente,Category,Reservation,Piatti,Ordini

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Category)
admin.site.register(Reservation)
admin.site.register(Piatti)
admin.site.register(Ordini)
