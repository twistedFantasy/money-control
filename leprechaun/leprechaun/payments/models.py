from django.db import models
from model_utils import Choices

from leprechaun.users.models import User
from leprechaun.core.models import BaseModel

CURRENCIES = Choices(("usd", "USD"), ("eur", "EUR"))


class Payment(BaseModel):
    amount = models.DecimalField("Amount", max_digits=11, decimal_places=2)
    currency = models.CharField("Currency", max_length=3, choices=CURRENCIES, default=CURRENCIES.eur)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
