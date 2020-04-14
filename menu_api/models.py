from django.db import models

# Create your models here.
class MenuResto(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name