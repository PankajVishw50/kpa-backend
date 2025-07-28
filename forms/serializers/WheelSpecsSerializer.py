from rest_framework import serializers
import re
from django.conf import settings

from forms import models
from forms.models import WheelSpecs


class WheelSpecsFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecs
        fields = [
            "axle_box_housing_bore_dia",
            "bearing_seat_diameter",
            "condemning_dia",
            "intermediate_wwp",
            "last_shop_issue_size",
            "roller_bearing_bore_dia",
            "roller_bearing_outer_dia",
            "roller_bearing_width",
            "tread_diameter_new",
            "variation_same_axle",
            "variation_same_bogie",
            "variation_same_coach",
            "wheel_disc_width",
            "wheel_gauge",
            "wheel_profile",
            "extras",
        ]

    def validate(self, attrs):
        # Validate against Regex Patterns if provided
        for field, pattern in settings.REGEX_PATTERNS.items():
            if pattern and attrs.get(field) and not re.match(pattern, attrs.get(field)):
                raise serializers.ValidationError(
                    {field: f"Invalid format for {field.replace('_', ' ')}."}
                )

        return attrs


class WheelSpecsSerializer(serializers.ModelSerializer):
    fields = WheelSpecsFieldsSerializer()

    submitted_by = serializers.CharField()

    class Meta:
        model = WheelSpecs
        fields = [
            "id",
            "form_number",
            "submitted_by",
            "submitted_date",
            "created_at",
            "fields",
        ]

    def to_representation(self, instance):
        instance.fields = instance
        return super().to_representation(instance)

    def to_internal_value(self, data):
        base = super().to_internal_value(data)
        fields_data = base.pop("fields", {})
        return {
            **base,
            **fields_data,
        }

    def create(self, validated_data):
        wspec = WheelSpecs.objects.mercy_create(**validated_data)
        wspec.save()
        return wspec
