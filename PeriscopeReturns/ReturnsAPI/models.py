# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Returnspredictionfeaturesmonthly(models.Model):
    item_id = models.BigIntegerField(primary_key=True)
    location = models.TextField(blank=True, null=True)
    region_1 = models.TextField(blank=True, null=True)
    item = models.TextField(blank=True, null=True)
    business_unit = models.TextField(blank=True, null=True)
    product_type = models.TextField(blank=True, null=True)
    fiscal_date = models.DateTimeField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    quarter = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    day_of_month = models.BigIntegerField(blank=True, null=True)
    peak_month = models.FloatField(blank=True, null=True)
    frequency_of_returns_in_previous_3_months = models.FloatField(blank=True, null=True)
    returned = models.FloatField(blank=True, null=True)
    returns_weekly_lag1 = models.FloatField(blank=True, null=True)
    returns_weekly_lag2 = models.FloatField(blank=True, null=True)
    returns_weekly_lag3 = models.FloatField(blank=True, null=True)
    returns_weekly_lag4 = models.FloatField(blank=True, null=True)
    returns_weekly_lag5 = models.FloatField(blank=True, null=True)
    standard_price = models.FloatField(blank=True, null=True)
    product_classification_category_by_company = models.TextField(blank=True, null=True)
    deposit_value = models.FloatField(blank=True, null=True)
    govt_regulations = models.FloatField(blank=True, null=True)
    weather_precipitation_level = models.FloatField(blank=True, null=True)
    weather_rain = models.FloatField(blank=True, null=True)
    weather_snow = models.FloatField(blank=True, null=True)
    weather_storm = models.FloatField(blank=True, null=True)
    is_container_unique_shape = models.FloatField(blank=True, null=True)
    container_shape = models.TextField(blank=True, null=True)
    container_size = models.TextField(blank=True, null=True)
    container_color = models.TextField(blank=True, null=True)
    container_lid_type = models.TextField(blank=True, null=True)
    customer_balances_qty = models.FloatField(blank=True, null=True)
    customer_stock_qty = models.FloatField(blank=True, null=True)
    returns_from_3rd_party_qty = models.FloatField(blank=True, null=True)
    transfer_to_other_zones_qty = models.FloatField(blank=True, null=True)
    no_of_one_way_trip_qty = models.FloatField(blank=True, null=True)
    in_transit_dc_to_brewery_qty = models.FloatField(db_column='in_transit_DC_to_brewery_qty', blank=True, null=True)  # Field name made lowercase.
    dist_between_collection_filling_depots = models.FloatField(blank=True, null=True)
    on_road_dist = models.FloatField(blank=True, null=True)
    sales_channels = models.TextField(blank=True, null=True)
    returns_channels = models.TextField(blank=True, null=True)
    forecasted_qty_fg = models.FloatField(db_column='forecasted_qty_FG', blank=True, null=True)  # Field name made lowercase.
    seasonal_index = models.FloatField(blank=True, null=True)
    time_in_market = models.FloatField(blank=True, null=True)
    percentage_float = models.FloatField(blank=True, null=True)
    is_promotion = models.FloatField(blank=True, null=True)
    promotion_type = models.TextField(blank=True, null=True)
    no_of_holidays_in_week = models.FloatField(blank=True, null=True)
    holiday_day_in_week = models.TextField(blank=True, null=True)
    ma = models.FloatField(blank=True, null=True)
    ema = models.FloatField(blank=True, null=True)
    macd = models.FloatField(blank=True, null=True)
    momentum = models.FloatField(blank=True, null=True)
    bollinger_low = models.FloatField(blank=True, null=True)
    bollinger_high = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ReturnsPredictionFeaturesMonthly'

#
# class Returnspredictionfeaturesweekly(models.Model):
#     item_id = models.BigIntegerField(blank=True, null=True)
#     location = models.TextField(blank=True, null=True)
#     region_1 = models.TextField(blank=True, null=True)
#     item = models.TextField(blank=True, null=True)
#     business_unit = models.TextField(blank=True, null=True)
#     product_type = models.TextField(blank=True, null=True)
#     fiscal_date = models.DateTimeField(blank=True, null=True)
#     year = models.IntegerField(blank=True, null=True)
#     quarter = models.IntegerField(blank=True, null=True)
#     month = models.IntegerField(blank=True, null=True)
#     week_of_year = models.IntegerField(blank=True, null=True)
#     week_of_month = models.BigIntegerField(blank=True, null=True)
#     last_week_of_month = models.BooleanField(blank=True, null=True)
#     day_of_year = models.IntegerField(blank=True, null=True)
#     day_of_month = models.BigIntegerField(blank=True, null=True)
#     weekend = models.BooleanField(blank=True, null=True)
#     mon = models.BooleanField(blank=True, null=True)
#     tue = models.BooleanField(blank=True, null=True)
#     wed = models.BooleanField(blank=True, null=True)
#     thu = models.BooleanField(blank=True, null=True)
#     fri = models.BooleanField(blank=True, null=True)
#     sat = models.BooleanField(blank=True, null=True)
#     sun = models.BooleanField(blank=True, null=True)
#     week_in_peak_month = models.FloatField(blank=True, null=True)
#     returned = models.FloatField(blank=True, null=True)
#     returns_weekly_lag1 = models.FloatField(blank=True, null=True)
#     returns_weekly_lag2 = models.FloatField(blank=True, null=True)
#     returns_weekly_lag3 = models.FloatField(blank=True, null=True)
#     returns_weekly_lag4 = models.FloatField(blank=True, null=True)
#     returns_weekly_lag5 = models.FloatField(blank=True, null=True)
#     standard_price = models.FloatField(blank=True, null=True)
#     product_classification_category_by_company = models.TextField(blank=True, null=True)
#     deposit_value = models.FloatField(blank=True, null=True)
#     govt_regulations = models.FloatField(blank=True, null=True)
#     weather_precipitation_level = models.FloatField(blank=True, null=True)
#     weather_rain = models.FloatField(blank=True, null=True)
#     weather_snow = models.FloatField(blank=True, null=True)
#     weather_storm = models.FloatField(blank=True, null=True)
#     is_container_unique_shape = models.FloatField(blank=True, null=True)
#     container_shape = models.TextField(blank=True, null=True)
#     container_size = models.TextField(blank=True, null=True)
#     container_color = models.TextField(blank=True, null=True)
#     container_lid_type = models.TextField(blank=True, null=True)
#     customer_balances_qty = models.FloatField(blank=True, null=True)
#     customer_stock_qty = models.FloatField(blank=True, null=True)
#     returns_from_3rd_party_qty = models.FloatField(blank=True, null=True)
#     transfer_to_other_zones_qty = models.FloatField(blank=True, null=True)
#     no_of_one_way_trip_qty = models.FloatField(blank=True, null=True)
#     in_transit_dc_to_brewery_qty = models.FloatField(db_column='in_transit_DC_to_brewery_qty', blank=True, null=True)  # Field name made lowercase.
#     dist_between_collection_filling_depots = models.FloatField(blank=True, null=True)
#     on_road_dist = models.FloatField(blank=True, null=True)
#     sales_channels = models.TextField(blank=True, null=True)
#     returns_channels = models.TextField(blank=True, null=True)
#     forecasted_qty_fg = models.FloatField(db_column='forecasted_qty_FG', blank=True, null=True)  # Field name made lowercase.
#     seasonal_index = models.FloatField(blank=True, null=True)
#     time_in_market = models.FloatField(blank=True, null=True)
#     percentage_float = models.FloatField(blank=True, null=True)
#     is_promotion = models.FloatField(blank=True, null=True)
#     promotion_type = models.TextField(blank=True, null=True)
#     no_of_holidays_in_week = models.FloatField(blank=True, null=True)
#     holiday_day_in_week = models.TextField(blank=True, null=True)
#     ma = models.FloatField(blank=True, null=True)
#     ema = models.FloatField(blank=True, null=True)
#     macd = models.FloatField(blank=True, null=True)
#     momentum = models.FloatField(blank=True, null=True)
#     bollinger_low = models.FloatField(blank=True, null=True)
#     bollinger_high = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ReturnsPredictionFeaturesWeekly'
