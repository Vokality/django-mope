from django.conf import settings
from django.db import models


class MopePaymentRequestManager(models.Manager):
    pass


class MopePaymentRequest(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE)

    amount = models.IntegerField(default=0)
    currency = models.CharField(max_length=3)
    completed = models.BooleanField(default=False, db_index=True)
    payment_url = models.URLField()
    payment_request_id = models.CharField(max_length=64, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'mope payment request'
        verbose_name_plural = 'mope payment requests'
