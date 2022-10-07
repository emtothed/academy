from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ("courses",)

admin.site.register(User,UserAdmin)
admin.site.register(Course)
admin.site.register(Scores)
admin.site.register(quest)
