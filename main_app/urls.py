from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('albums/', views.albums_index, name='index'),
    path('albums/<int:album_id>/', views.albums_detail, name='detail'),
    path('albums/create/', views.AlbumCreate.as_view(), name='albums_create'),
    path('albums/<int:pk>/update/', views.AlbumUpdate.as_view(), name='albums_update'),
    path('albums/<int:pk>/delete/', views.AlbumDelete.as_view(), name='albums_delete'),
    path('albums/<int:album_id>/add_listening/', views.add_listening, name='add_listening'),
    path('albums/<int:album_id>/assoc_device/<int:device_id>/', views.assoc_device, name='assoc_device'),
    path('devices/', views.devices_index, name='devices_index'),
    path('devices/<int:device_id>/', views.devices_detail, name='devices_detail'),
    path('devices/create/', views.DeviceCreate.as_view(), name='devices_create'),
    path('devices/<int:pk>/update/', views.DeviceUpdate.as_view(), name='devices_update'),
    path('devices/<int:pk>/delete/', views.DeviceDelete.as_view(), name='devices_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]