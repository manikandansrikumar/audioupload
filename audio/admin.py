from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Song)
admin.site.register(Podcast)
admin.site.register(AudioBook)