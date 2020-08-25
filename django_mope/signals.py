import django.dispatch

payment_requested_created = django.dispatch.Signal()
payment_request_complete = django.dispatch.Signal()
