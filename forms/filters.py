import django_filters
from django.db import models

from forms.models import WheelSpecs


class WheelSpecsFilter(django_filters.FilterSet):
    submitted_by = django_filters.CharFilter(
        field_name="submitted_by__username", lookup_expr="icontains"
    )

    class Meta:
        model = WheelSpecs
        fields = {
            "form_number",
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
        }
        filter_overrides = {
            models.CharField: {
                "filter_class": django_filters.CharFilter,
                "extra": lambda _: {
                    "lookup_expr": "icontains",
                },
            },
        }
