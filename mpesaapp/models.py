from django.db import models


class Transaction(models.Model):
    merchant_request_id = models.CharField(max_length=255)
    checkout_request_id = models.CharField(max_length=255)
    result_code = models.IntegerField()
    result_desc = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=255)
    user_phone_number = models.CharField(max_length=15)

    # Add any additional fields or methods as needed

    def __str__(self):
        return f"{self.transaction_id} - {self.user_phone_number}"
