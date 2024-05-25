from django.db import models

# Create your models here

class SurveyResponse(models.Model):
    category = models.CharField(max_length=255)
    preference = models.CharField(max_length=255)
    
    def __str__(self):
        return self.category