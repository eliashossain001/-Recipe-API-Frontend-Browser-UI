from django.db import models

class Recipe(models.Model):
    cuisine = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    rating = models.FloatField(null=True, blank=True)
    prep_time = models.IntegerField(null=True, blank=True)
    cook_time = models.IntegerField(null=True, blank=True)
    total_time = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    nutrients = models.JSONField()
    serves = models.CharField(max_length=100)

    def __str__(self):
        return self.title
