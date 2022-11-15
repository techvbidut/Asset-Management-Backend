from django.contrib import admin

# Register your models here.
from resources.models import *

admin.site.register(Resource)
admin.site.register(IssuedResource)