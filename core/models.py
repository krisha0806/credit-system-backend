from django.db import models
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    monthly_income = models.FloatField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='loans')
    loan_amount = models.FloatField()
    interest_rate = models.FloatField()
    tenure_months = models.IntegerField()
    emi = models.FloatField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def __str__(self):
        return f"Loan #{self.id} for {self.customer.first_name}"

class LoanHistory(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='history')
    status = models.CharField(max_length=20)  # e.g., Approved, Rejected, Paid, Defaulted
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"History for Loan #{self.loan.id} - {self.status}"
