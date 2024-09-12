from django.contrib import admin
from todoapp.models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display=['id','user','title','priority','completed','create_date']
admin.site.register(Task,TaskAdmin)