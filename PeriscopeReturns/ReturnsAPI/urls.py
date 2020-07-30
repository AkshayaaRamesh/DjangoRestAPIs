from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'PeriscopeReturns'

urlpatterns = [
    # path('filter/', views.FilterListView.as_view(), name='list'),
    path('display/', views.display_all, name='display'),
    path('show_all/',views.show_all_view.as_view(), name= 'show'),
    path('filter/', views.search, name='search'),
    path('dropdown/', views.dropdownlist, name='dropdown')
]