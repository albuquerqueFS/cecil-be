from django.db import models
from django.utils.translation import gettext_lazy as _
from app.models import User


class Movement(models.Model):
    class Types(models.TextChoices):
        INCOME = "INCOME", _("Income")
        EXPENSE = "EXPENSE", _("Expense")

    value = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)
    is_recurrent = models.BooleanField(default=False)
    types = models.CharField(max_length=10, choices=Types.choices)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="movements")
