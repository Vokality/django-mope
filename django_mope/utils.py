from django.conf import settings
from mope import Mope
from requests import HTTPError

from django_mope.models import MopePaymentRequest
from django_mope.signals import payment_request_complete, payment_requested_created

_mope = Mope(token=settings.MOPE_API_TOKEN)


def create_payment_request(amount, currency, order_id,
                           redirect_url, user_id=None, description=None):
    response = _mope.shop.create_payment_request(
        amount=amount,
        order_id=order_id,
        description=description,
        redirect_url=redirect_url,
    )

    request = MopePaymentRequest.objects.create(
        amount=amount,
        user_id=user_id,
        currency=currency,
        payment_url=response.url,
        payment_request_id=response.id,
    )

    payment_requested_created.send(sender=MopePaymentRequest, instance=request)
    return request


def update_payment_request(payment_request_id):
    try:
        response = _mope.shop.get_payment_request(
            payment_id=payment_request_id
        )

        if response.status != 'paid':
            return

        request = MopePaymentRequest.objects.get(
            payment_request_id=payment_request_id
        )

        request.completed = True
        request.save()
        payment_request_complete.send(sender=MopePaymentRequest, instance=request)
        return request
    except (MopePaymentRequest.DoesNotExist, HTTPError):
        return None
