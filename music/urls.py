
from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [

    path('showdata/', views.Test_File, name='showdata'),

    # path('', views.LoginFormView.as_view(), name='login'),
    path('', views.lgin, name='login'),

    path('check_user/', views.check_user, name='check_user'),

    path('index/', views.IndexView.as_view(), name='index'),

    path('register/', views.UserFormView.as_view(), name='register'),

    path('test/', views.TestFormView.as_view(), name='test'),

    path('<pk>/', views.DetailsView.as_view(), name='detail'),

    # music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

    path('album/<pk>/', views.AlbumUpdate.as_view(), name='album-update'),

    path('album/<pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),

    # music/song/add/
    path('song/add/', views.SongCreate.as_view(), name='song-add'),

    path('song/all/', views.SongList.as_view(), name='song-list'),

    path('logout/', views.LogOut, name='logout'),



]

