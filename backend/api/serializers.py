from rest_framework.serializers import ModelSerializer

from pay2u.models import (
    Cashback,
    Notification,
    Payments,
    Rate,
    Services,
    Subscription,
    UserSubscription,
)


class CashbackSerializer(ModelSerializer):
    class Meta:
        model = Cashback
        fields = ('amount', 'status',)


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ('text', 'date',)


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = ('amount', 'datetime',)


class RateSerializer(ModelSerializer):
    class Meta:
        model = Rate
        fields = ('title', 'price')


class ServicesSerializer(ModelSerializer):

    class Meta:
        model = Services
        fields = ('name', 'description', 'url',)


class SubscriptionSerializer(ModelSerializer):
    service = ServicesSerializer(Many=True)
    rate = RateSerializer(many=True)

    class Meta:
        model = Subscription
        fields = ('service', 'rate', 'name', 'description', 'refund',)


class UserSubscriptionSerializer(ModelSerializer):

    class Meta:
        model = UserSubscription
        fields = (
            'subscription',
            'user_id',
            'date_start',
            'date_end',
            'status',
            'cashback',
            'payments',
            'notification',
        )
