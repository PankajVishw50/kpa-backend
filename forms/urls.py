from django.urls import path

from forms.views import WheelSpecsView


urlpatterns = [
    path("wheel-specifications", WheelSpecsView.as_view(), name="wheel-specifications"),
]
