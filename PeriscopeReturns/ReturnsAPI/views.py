from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Returnspredictionfeaturesmonthly
from .serializers import MonthlySerializer
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
from django.shortcuts import render
from .filters import PlantAssetFilter
from django.views import View
from django.views.generic import ListView, DetailView

# Create your views here.

# Display all details using function based view without pagination
# @api_view(['GET'])
# def display_all(request):
#     if request.method == 'GET':
#         display = Returnspredictionfeaturesmonthly.objects.all()
#         serializer = MonthlySerializer(display,many=True)
#         return Response(serializer.data)

# Display all details using function based view
@api_view(['GET'])
def display_all(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 10
        display = Returnspredictionfeaturesmonthly.objects.all()
        result_page = paginator.paginate_queryset(display, request)
        serializer = MonthlySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

# Display all details using class based view"
class show_all_view(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        show_all = Returnspredictionfeaturesmonthly.objects.all().order_by('-fiscal_date')
        result_page = paginator.paginate_queryset(show_all, request)
        serializer = MonthlySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

def search(request):
    plant_asset_list = Returnspredictionfeaturesmonthly.objects.all()
    plant_asset_filter = PlantAssetFilter(request.GET, queryset=plant_asset_list)
    return render(request,'filter.html',{'filter': plant_asset_filter})


def dropdownlist(request):
    result = Returnspredictionfeaturesmonthly.objects.all()
    return render(request,"dropdownlist.html",{"Returnspredictionfeaturesmonthly": result})

# class returns_filter_list_view(generics.ListAPIView):
#     queryset = Returnspredictionfeaturesmonthly.objects.all()
#     serializer_class = Returnspredictionfeaturesmonthly
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('item', 'location', 'region_1')


# class FilterListView(ListView):
#     model = Returnspredictionfeaturesmonthly
#     template_name = 'snippets/snippet_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter'] = PlantAssetFilter(self.request.GET, queryset=self.get_queryset())
#         return context

