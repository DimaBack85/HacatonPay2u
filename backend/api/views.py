from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from pay2u.models import (
    Rate, 
    Services, 
    Subscription, 
    Cashback, 
    Payments, 
    Notification, 
    UserSubscription
)
from serializers import Notification


class NotificationViewSet(mixins.ListModelMixin, 
                          mixins.RetrieveModelMixin, 
                          viewsets.GenericViewSet
):
    queryset = Notification.objects.all()

    permission_classes = (permissions.IsAuthenticated,)
