from rest_framework import serializers
from .models import *

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            "id",
            "url",
            "title", 
            "icon",
        ]

class IntinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Intinerary
        fields = [
            "id",
            "url",
            "label",
            "level",
            "description",
            "activity",
        ]

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = [
            "id",
            "url",
            "name",
            "description",
        ]

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = [
            "id",
            "url",
            "area",
            "FAQ",
            "description",
        ]

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = [
            "id",
            "url",
            "country",
            "name",
            "position",
            "activities",
        ]

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = [
            "id",
            "url",
            "start_point",
            "end_point",
            "destination",
        ]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "url",
            "name",
            "phone_number",
            "address",
        ]