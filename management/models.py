from django.db import models

class SeasonalFlavor(models.Model):
    flavor_name = models.CharField(max_length=100)
    available_until = models.DateField()

    def __str__(self):
        return self.flavor_name


class IngredientInventory(models.Model):
    ingredient_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.ingredient_name


class CustomerFeedback(models.Model):
    customer_name = models.CharField(max_length=100)
    suggestion = models.TextField()
    allergy_concern = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Feedback from {self.customer_name}"

