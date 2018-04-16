from django.db import models


class Documento(models.Model):
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')