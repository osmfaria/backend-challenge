import uuid

from django.db import models


class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=16)
    card = models.CharField(max_length=16)

    store = models.ForeignKey(
        "stores.Store", on_delete=models.CASCADE, related_name="transactions"
    )
    type = models.ForeignKey(
        "transactions.Transactions_type",
        on_delete=models.CASCADE,
        related_name="transactions",
    )


class Transactions_type(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    description = models.CharField(max_length=40)
    type = models.CharField(max_length=12)
