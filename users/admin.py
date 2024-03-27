from django.contrib import admin
from .models import Profile, MentorProfile, Projects

admin.site.register(Profile)
admin.site.register(MentorProfile)
admin.site.register(Projects)