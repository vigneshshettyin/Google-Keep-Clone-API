from django.contrib import admin

# Register your models here.
from .models import CheckList, CheckListItem

admin.site.register(CheckList)
admin.site.register(CheckListItem)

