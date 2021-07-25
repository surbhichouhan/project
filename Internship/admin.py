from django.contrib import admin
from .models import Internship, UserProfile, Application, Education, Experience, UploadImage
from .models import Demouser,Demo
from django.db import models
# Register your models here.
admin.site.register(Internship)
admin.site.register(UserProfile)
admin.site.register(Application)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(UploadImage)
admin.site.register(Demouser)
# class DemoAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.DateTimeField: {'input_formats': ('%d/%m/%Y',)},
#     }
admin.site.register(Demo)
