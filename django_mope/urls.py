from django.urls import path

from django_mope import views

urlpatterns = [
    path('mope-webhook/', views.MopeWebhookView.as_view())
]
