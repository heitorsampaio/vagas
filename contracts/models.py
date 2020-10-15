from datetime import datetime
from decimal import Decimal

from django.utils import timezone
from django.db import models
from users.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid


class Contract(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)
    client = models.ForeignKey(User,
                               related_name='contracts',
                               on_delete=models.CASCADE,
                               help_text='Contract User')
    bank = models.TextField(verbose_name='Contract Bank',
                            help_text='Information about bank')
    amount = models.DecimalField(default=0.00,
                                 max_digits=10,
                                 decimal_places=2,
                                 help_text='Contract Price',
                                 validators=[MinValueValidator(limit_value=1)])
    interest_rate = models.DecimalField(default=0.000,
                                        max_digits=6,
                                        decimal_places=3,
                                        help_text='Interest Rate',
                                        validators=[MinValueValidator(
                                            limit_value=0), MaxValueValidator(limit_value=1)]
                                        )
    submission_date = models.DateField(
        auto_now_add=True,
        editable=False,
        help_text='Submission Date'
    )

    ip_address = models.GenericIPAddressField(
        verbose_name='Ip address', help_text='Ip Adress of submission')

    class Meta:
        ordering = ['id']

    def __str__(self):
        """
        Formatar valor
        """
        return f'R$ {self.amout}, {self.bank}'

    def get_time(self):
        """
        Return contract time
        """
        today = datetime.datetime.now(tz=timezone.utc)
        contract_date = self.submission_date

        return (today - contract_date).days

    @property
    def balance(self):
        """
        Return balance of the contract
        """
        return round(self.amount + self.iof - self.paid_value, 2)

    @property
    def amout(self):
        """
        Calculate the total amount
        """
        value = round(self.interest_rate / 30, 3)
        time = self.get_time()

        return self.amount + ((1 + value) ** time)

    @property
    def iof(self):
        """
        Calculate IOF
        """
        aliquota = self.amount * Decimal(0.38 / 100.0)
        aliquota_per_day = self.get_time() * Decimal(0.0082 / 100.0) * self.amount

        return round(aliquota + aliquota_per_day, 2)

    @property
    def paid(self):
        """
        Return paid value
        """
        return self.payments.aggregate(sum('amount')).get('amount__sum') or Decimal(0.00)
