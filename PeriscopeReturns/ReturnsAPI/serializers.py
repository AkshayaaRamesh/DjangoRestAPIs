from rest_framework import serializers
from .models import Returnspredictionfeaturesmonthly

class MonthlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Returnspredictionfeaturesmonthly
        fields = ('item_id','location','region_1','item','product_type','fiscal_date','returned')

