from django.urls import path
from .views import apiOverview, deviceList, addDevice, deleteDevice, checkDeviceMac, checkDeviceName

urlpatterns = [
    path('', apiOverview, name="api-overview"),
    path('device-list/', deviceList, name="device-list"),
    path('add-device/', addDevice, name="add-device"),
    path('delete-device/<str:pk>', deleteDevice, name="delete-device"),
    path('check-device-name/<str:name>', checkDeviceName, name="check-device-name"),
    path('check-device-mac/<str:mac>', checkDeviceMac, name="check-device-mac"),
]