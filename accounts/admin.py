from django.contrib import admin

# Register your models here.
from accounts.models import *

admin.site.register(EmployeeDetail)
admin.site.register(Team)