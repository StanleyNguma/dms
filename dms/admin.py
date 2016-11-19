from django.contrib import admin
from .models import UserGroups
from .models import Users

# Register your models here.
admin.site.register(UserGroups)
admin.site.register(Users)
