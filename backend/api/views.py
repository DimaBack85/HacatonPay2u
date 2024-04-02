from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.http import JsonResponse

from pay2u.models import (
    Rate,
    Services,
    Subscription,
    Cashback,
    Payments,
    Notification,
    UserSubscription
)
from serializers import (
    Notification,
    CashbackSerializer,
    PaymentsSerializer,
    RateSerializer,
    ServicesSerializer,
    SubscriptionSerializer,
    UserSubscriptionSerializer
)


def user_subscription_list(request):
    subscriptions = UserSubscription.objects.all()
    data = {'subscriptions': list(subscriptions.values())}
    return JsonResponse(data)


def user_subscription_detail(request, subscription_id):
    subscription = UserSubscription.objects.get(id=subscription_id)
    data = {'subscription': {
        'id': subscription.id,
        'user_id': subscription.user_id.id,
        'date_start': subscription.date_start,
        'date_end': subscription.date_end,
        'status': subscription.status,
        'cashback_amount': subscription.cashback.amount,
        'payments_amount': subscription.payments.amount,
        'notification_text': subscription.notification.text
    }}
    return JsonResponse(data)


class NotificationViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet
):
    queryset = Notification.objects.all()

    permission_classes = (permissions.IsAuthenticated,)


class SubscriptionViewSet(mixins.ListModelMixin):
    queryset = Subscription.objects.all()
    permissions_classes  = ()
def get_subscription_list(request):
    subscriptions = Subscription.objects.all()
    subscription_list = []
    for subscription in subscriptions:
        subscription_list.append({
            'id': subscription.id,
            'name': subscription.name,
            'description': subscription.description
        })
    return JsonResponse({'subscriptions': subscription_list})


def get_subscription_details(request, subscription_id):
    try:
        subscription = Subscription.objects.get(id=subscription_id)
        return JsonResponse({
            'id': subscription.id,
            'name': subscription.name,
            'description': subscription.description
        })
    except Subscription.DoesNotExist:
        return JsonResponse({'error': 'Subscription not found'}, status=404)


def get_oversubscription_details(request, subscription_id):
    try:
        subscription = Subscription.objects.get(id=subscription_id)
        if subscription.is_oversubscription:
            return JsonResponse({
                'id': subscription.id,
                'name': subscription.name,
                'oversubscription_details': subscription.oversubscription_details
            })
        else:
            return JsonResponse({'error': 'Subscription is not an oversubscription'}, status=400)
    except Subscription.DoesNotExist:
        return JsonResponse({'error': 'Subscription not found'}, status=404)
