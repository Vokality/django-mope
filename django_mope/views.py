import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from django_mope.models import MopePaymentRequest
from django_mope.utils import update_payment_request


class MopeWebhookView(generic.View):
    """
    Will be called by Mopé whenever the status of a
    payment request changes.
    """

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            data = json.loads(request.body)
            payment_request_id = data['id']

            exists = MopePaymentRequest.objects.filter(payment_request_id=payment_request_id).exists()
            if not exists:
                return JsonResponse(data={'status': 'not found'}, status=404)

            update_payment_request(payment_request_id)
            return JsonResponse(data={'status': 'ok'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse(data={'status': 'not ok'}, status=400)
