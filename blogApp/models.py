# Create your models here.
from django.db import models
from django.db.models import CheckConstraint, Q
from accounts.models import CustomUser
import datetime
import pytz

class Offer(models.Model):
    OFFER = 'offer'
    DEMAND = 'demand'
    PAID = 'paid'
    UNPAID = 'unpaid'
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    TYPE_CHOICES = [
        (OFFER, 'Offre'),
        (DEMAND, 'Demande'),
    ]

    CATEGORY_CHOICES = [
        (UNPAID, 'Bénévole'),
        (PAID, 'Rémunéré'),
    ]

    GENDER_CHOICES = [
        (OTHER, 'Non-Binaire'),
        (FEMALE, 'Femme'),
        (MALE, 'Homme'),
    ]

    type = models.CharField(
        max_length=255,
        choices=TYPE_CHOICES,
        default=OFFER,
    )

    category = models.CharField(
        max_length=255,
        choices=CATEGORY_CHOICES,
        default=UNPAID,
    )

    title = models.CharField(max_length=50, null=False)
    summary = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=5000, blank=True)
    city = models.CharField(max_length=255, blank=True)
    min_age = models.PositiveIntegerField(null=True, blank=True)
    max_age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, default=None, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def recent(self):
        utc = pytz.UTC

        offer_date = self.created_on
        threshold = utc.localize(datetime.datetime.now() - datetime.timedelta(weeks=1))
        return offer_date > threshold
