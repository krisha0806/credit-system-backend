from django.db import models
from django.contrib.auth.models import User

class CreditEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, default='General') 

    def __str__(self):
        return f"{self.user.username} - {self.amount} ({self.category})"

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=20)
    approved_limit = models.IntegerField()  # auto-calculated

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
