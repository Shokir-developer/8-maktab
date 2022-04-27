from django.db import models

class News(models.Model):
	title = models.CharField(null=True, max_length=100)
	body = models.TextField()
	image = models.ImageField(upload_to='news')
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
