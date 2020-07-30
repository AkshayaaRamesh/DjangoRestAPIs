from django.contrib.auth.models import User
import django_filters
from .models import Returnspredictionfeaturesmonthly

class PlantAssetFilter(django_filters.FilterSet):
    class Meta:
        model = Returnspredictionfeaturesmonthly
        fields = {
                   'item' :['icontains'],
                   'location': ['icontains'],
                   'region_1':['icontains'],
                 }