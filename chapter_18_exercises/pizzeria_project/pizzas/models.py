from django.db import models

class Pizza(models.Model):
    """a pizza that is on the menu"""
    name = models.CharField(max_length=50)

    def __str__(self):
        """return a string representation of the model"""
        return self.name

