from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self): #Python 2 is __unicode__
		return self.email
