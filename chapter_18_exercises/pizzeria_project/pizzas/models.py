from django.db import models

class Pizza(models.Model):
    """a pizza that is on the menu"""
    name = models.CharField(max_length=50)

    def __str__(self):
        """return a string representation of the model"""
        return self.name

class Topping(models.Model):
    """toppings for the pizzas"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=30)

    def __str__(self):
        """return a string representation of the model"""
        return self.topping_name
