
from django.urls import path

from . import views

app_name = 'myapp'

# 127.0.0.1:8000/myapp/ this pattern is fixed for myapp
# after this below patterns start
# like '' means 127.0.0.1:8000/myapp/
# like 'show/<int:num>/' means 127.0.0.1:8000/myapp/show/num/ ,here num can be any integer number like 1,.. etc
# like 'display/' means 127.0.0.1:8000/myapp/display/

urlpatterns = [

    path('', views.index, name='index'),

    path('display/', views.display, name='display'),

    path('show/<int:num>/', views.show, name='show'),

    path('printt/<int:num1>/<int:num2>/', views.printt, name='printt'),

    path('animal/', views.animal, name='animal'),

    path('bird/', views.bird, name='bird'),

    path('fish/', views.fish, name='fish'),

    path('flower/', views.flower, name='flower'),

    path('fruit/', views.fruit, name='fruit'),

    path('tree/', views.tree, name='tree'),

    path('tname/', views.tname, name='tname'),

    path('add/', views.add, name='add'),

    path('empinfo/', views.empinfo, name='empinfo'),

    path('insert/', views.insert, name='insert'),

    path('insert_data/', views.insert_data, name='insert_data'),

    path('search/', views.search, name='search'),

    path('search_data/', views.search_data, name='search_data'),

    path('update/', views.update, name='update'),

    path('update_data/', views.update_data, name='update_data'),

    path('delete/', views.delete, name='delete'),

    path('delete_data/', views.delete_data, name='delete_data'),

    path('country/', views.CountryView.as_view(), name='country'),

]

