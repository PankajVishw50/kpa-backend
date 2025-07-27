from django.db import models, transaction
from django.contrib.auth import get_user_model
import secrets

from utils.base_models import TimeMonitorModel, UUIDPrimaryFieldModel

User = get_user_model()


class WheelSpecsManager(models.Manager):
    def mercy_create(self, form_number, submitted_by, submitted_date, **kwargs):
        """This method ignores if an user which does not exist is
        passed in `submitted_by`.
        It will create one user if not already exists, but would keep is not active.
        """

        with transaction.atomic():
            try:
                user = User.objects.get(username=submitted_by)
            except User.DoesNotExist:
                # Create New User
                user = User.objects.create_user(
                    username=submitted_by,
                    password=secrets.token_hex(),
                    is_active=False,
                )

            return self.create(
                form_number=form_number,
                submitted_by=user,
                submitted_date=submitted_date,
                **kwargs,
            )


class WheelSpecs(UUIDPrimaryFieldModel, TimeMonitorModel):
    form_number = models.CharField(
        max_length=32,
        unique=True,
    )

    submitted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    submitted_date = models.DateTimeField()

    # Fields
    axle_box_housing_bore_dia = models.CharField(max_length=100, blank=True, null=True)
    bearing_seat_diameter = models.CharField(max_length=32, blank=True, null=True)
    condemning_dia = models.CharField(max_length=32, blank=True, null=True)
    intermediate_wwp = models.CharField(max_length=32, blank=True, null=True)
    last_shop_issue_size = models.CharField(max_length=32, blank=True, null=True)
    roller_bearing_bore_dia = models.CharField(max_length=32, blank=True, null=True)
    roller_bearing_outer_dia = models.CharField(max_length=32, blank=True, null=True)
    roller_bearing_width = models.CharField(max_length=32, blank=True, null=True)
    tread_diameter_new = models.CharField(max_length=32, blank=True, null=True)
    variation_same_axle = models.CharField(max_length=32, blank=True, null=True)
    variation_same_bogie = models.CharField(max_length=32, blank=True, null=True)
    variation_same_coach = models.CharField(max_length=32, blank=True, null=True)
    wheel_disc_width = models.CharField(max_length=32, blank=True, null=True)
    wheel_gauge = models.CharField(max_length=32, blank=True, null=True)
    wheel_profile = models.CharField(max_length=100, blank=True, null=True)

    extras = models.JSONField(default=dict)

    objects = WheelSpecsManager()

    def __str__(self):
        return self.form_number
