from django.db import models

# Create your models here.
class Job(models.Model):
    companyName = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=500)

    def __str__(self):
        return self.companyName
