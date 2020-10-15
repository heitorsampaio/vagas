from django.db import models
from django.core.validators import MinValueValidator
from contracts.models import Contract
import uuid

class Payment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)
    contract = models.ForeignKey(Contract,
                                 related_name='payments',
                                 on_delete=models.CASCADE,
                                 help_text='Contract Payment')
    value = models.DecimalField(default=0.00, max_digits=10, decimal_places=2,
                                verbose_name='Payment value',
                                help_text='Payment Price',
                                validators=[MinValueValidator(limit_value=1)])
    date = models.DateTimeField(auto_now_add=True, editable=False,
                                help_text='Payment Date'
                                )
