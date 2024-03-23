from django.contrib import admin
from .models import *


# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'phone_number', 'email')
#     search_fields = ['full_name']


admin.site.register(TeacherModel)
admin.site.register(StudentModel)


class LevelAdmin(admin.ModelAdmin):
    list_display = ('level_name', 'price_level')
    search_fields = ['level_name', 'price_level']


admin.site.register(LevelModel, LevelAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('location_name', 'location_phone_number')
    search_fields = ['location_name']


admin.site.register(Address, AddressAdmin)


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('exercise_name', 'unit_name')
    search_fields = ['exercise_name']

