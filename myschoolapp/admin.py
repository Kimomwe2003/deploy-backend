from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Subjects)
admin.site.register(Grade)
admin.site.register(Teacher)