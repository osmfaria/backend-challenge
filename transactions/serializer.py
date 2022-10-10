import ipdb
from rest_framework import serializers
from stores.serializers import StoreSerializer

from .functions import currency_formater
from .models import Transaction, Transactions_type


class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions_type
        fields = "__all__"

class TransactionSerializer(serializers.ModelSerializer):
    store = StoreSerializer(read_only=True)
    type = TransactionTypeSerializer(read_only=True)
    date_time = serializers.SerializerMethodField()
    currency = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = "__all__"


    def get_date_time(self, obj):
        return obj.date.strftime("%d/%m/%Y %H:%M:%S")


    def get_currency(self, obj):
        return currency_formater(obj.amount)
