from django.urls import path

from forms.views import WheelSpecsView


urlpatterns = [
    path("wheelspecs", WheelSpecsView.as_view(), name="wheelspecs"),
]
