from django.contrib import admin
from .models import students,teachers,departments

# Register your models here.
admin.site.register(students)
admin.site.register(teachers)
admin.site.register(departments)
