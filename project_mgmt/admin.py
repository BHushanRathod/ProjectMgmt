from django.contrib import admin

# Register your models here.
from project_mgmt.models import Projects, Task

admin.site.register(Projects)
admin.site.register(Task)