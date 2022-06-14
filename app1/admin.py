from django.contrib import admin

from app1.models import Document, Users

# Register your models here.
admin.site.register(Users)
admin.site.register(Document)