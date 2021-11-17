
from django.urls import path
from . import views

app_name = 'myapp2'

urlpatterns = [
    path('', views.index, name='index'),

    path('display/<str:user_address>', views.display, name="display"),

    path('show/', views.show, name='show'),

    path('result/', views.result, name='result'),

    path('add_user/', views.add_user, name='add_user'),

    path('add_user_info/', views.add_user_info, name='add_user_information'),

    path('myview/', views.MyView.as_view(), name='myview'),

    path('myview2/', views.MyView2.as_view(), name='myview2'),

    path('ajax_page/', views.ajax_page, name='ajax_page'),

    path('ajax_sum/', views.ajax_sum, name='ajax_sum'),

    path('show_form/', views.TestForm.as_view(), name='show_form'),
]
