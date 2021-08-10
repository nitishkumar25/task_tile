from django.db import models

# Create your models here.
class Tile(models.Model):
    
    launchdate = models.DateTimeField(auto_now_add=True, null=True)
    status = models.TextField()
    def __str__(self):
        return self.status

class Task(models.Model):
    title = models.CharField(max_length=100)
    order = models.CharField(max_length=100)
    desc = models.CharField(max_length=5000)
    type = models.CharField(max_length=100)
    assg_user = models.CharField(max_length=100)
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE)
