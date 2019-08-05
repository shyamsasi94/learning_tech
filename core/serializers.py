from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import ShipCharter, Ship, ShipOwner


class ShipCharterSerializer(serializers.ModelSerializer):
    email = SerializerMethodField(allow_null=True)

    class Meta:
        model = ShipCharter
        fields = ["name", "ship_owner", "email"]
        # fields='__all__'
        # for all data use fields='__all__'

    def get_email(self, obj):
        mail = f"{obj.name}@example.com"
        return mail


class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = "__all__"


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShipOwner
        depth = 1
        fields = "__all__"



