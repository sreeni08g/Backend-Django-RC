from django.contrib import admin

# Register your models here.
from scrapper import models

admin.site.register(models.QueryHistory)