from django.contrib import admin
from .models import Customer
from .models import Project
from .models import Tracking

# Register your models here.
admin.site.register(Customer)
admin.site.register(Project)
admin.site.register(Tracking)