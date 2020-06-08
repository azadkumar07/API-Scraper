from django.db import models
class API(models.Model):
	API_Name = models.CharField(max_length=200)
	API_Link = models.CharField(max_length=200)
	API_Des = models.CharField(max_length=200)
	API_Auth = models.CharField(max_length=200)
	API_HTTPS = models.CharField(max_length=200)
	API_CORS = models.CharField(max_length=200)

	def __str__(self):
		return self.API_Name
