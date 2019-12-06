from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(casa, departameto)

class ViewAdmin(admin.ModelAdmin):
	pass