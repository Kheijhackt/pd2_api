from django.db import models

# Create your models here.
# make a model here that has a string code for the primary key, and a single boolean field and an automated timestamp field for created and an automated modified timestamp field
class Device(models.Model):
    STATUS_CHOICES = [
        (0, 'Standby'),
        (1, 'Weevils found'),
        (2, 'Weevils attracted'),
        (3, 'Weevils eliminated'),
        (4, 'Weevils not found')
    ]

    id = models.CharField(max_length=10, primary_key=True)
    operating = models.BooleanField(default=False)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.id