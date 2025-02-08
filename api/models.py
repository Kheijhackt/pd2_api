from django.db import models

# Create your models here.
# make a model here that has a string code for the primary key, and a single boolean field and an automated timestamp field for created and an automated modified timestamp field
class User(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    weevil_detected = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.code