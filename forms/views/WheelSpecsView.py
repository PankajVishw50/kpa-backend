from rest_framework.generics import ListCreateAPIView
from rest_framework.filters import OrderingFilter, SearchFilter
import django_filters.rest_framework as drf_filters

from forms.serializers import WheelSpecsSerializer
from forms.models import WheelSpecs
from forms.filters import WheelSpecsFilter


class WheelSpecsView(ListCreateAPIView):
    serializer_class = WheelSpecsSerializer
    queryset = WheelSpecs.objects.all()
    filter_backends = [
        OrderingFilter,
        SearchFilter,
        drf_filters.DjangoFilterBackend,
    ]
    ordering_fields = ["created_at", "submitted_date"]
    ordering = ["-created_at"]
    search_fields = [
        "form_number",
        "submitted_by__username",
    ]
    filterset_class = WheelSpecsFilter
