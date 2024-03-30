from rest_framework import serializers

from pay2u.models import (
    Cashback,
    Notification,
    Payments,
    Rate,
    Services,
    Subscription,
    UserSubscription,
)


class NotificationSeriaizers(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['text', 'date']


class CashbackSeriaizers(serializers.ModelSerializer):
    class Meta:
        model = Cashback
        fields = ['amount', 'status']


class PaymentsSeriaizers(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ['amount', 'datetime']


class RateSeriaizers(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['titel', 'price']


class ServicesSeriaizers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['name', 'description', 'url']


class SubscriptionSeriaizers(serializers.ModelSerializer):
    servise = ServicesSeriaizers(many=True)
    rate = RateSeriaizers(many=True)

    class Meta:
        model = Subscription
        fields = ['rate', 'servise', 'name', 'description', 'refund']


class UserSubscriptionSeriaizers(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = [
            'subscription',
            'user',
            'date_beginning',
            'date_ending',
            'status',
            'cashback',
            'payments',
            'notification'
        ]
