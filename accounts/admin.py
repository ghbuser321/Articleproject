from django.contrib import admin
from .models import CustomUser

class CutomUserAdimn(admin.ModelAdmin):
    list_display = ('id', 'username')
    list_display_links = ('id', 'username')

admin.site.register(CustomUser, CutomUserAdimn)
