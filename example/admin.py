from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ResumeModel)
class ResumeAdmin(admin.ModelAdmin):
    list_display=['id','name','gender','state','mobile','email',
                  'image','file']
