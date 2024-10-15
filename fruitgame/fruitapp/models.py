from django.db import models

class FruitSet(models.Model):
    fruit1 = models.CharField(max_length=100)
    fruit2 = models.CharField(max_length=100, blank=True)  # Kept empty for future use if needed
    result = models.CharField(max_length=100)  # The result for this set of fruits

    def __str__(self):
        return f"{self.fruit1} - Result: {self.result}"
