from django.contrib import admin
from .models import Comments, Files, Friends
# Register your models here.
admin.site.register(Comments)
admin.site.register(Files)
admin.site.register(Friends)