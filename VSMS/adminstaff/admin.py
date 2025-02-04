from django.contrib import admin

# Register your models here.

from .models import Students,Stdinfo

class Edit(admin.ModelAdmin):
    list_display = ['stdno','StdName','qualification','email','DOJ','batch','image']
    list_editable = ['StdName','qualification','email','DOJ','batch','image']



admin.site.register(Students,Edit)
admin.site.register(Stdinfo,Edit)