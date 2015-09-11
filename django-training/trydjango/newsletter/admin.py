from django.contrib import admin

# Register your models here.
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__str__", "timestamp"]
	list_filter = ['timestamp']

admin.site.register(SignUp, SignUpAdmin)