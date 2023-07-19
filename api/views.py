from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Devices
from .serializers import DevicesSerializer
from .utils import API_KEY


# Create your views here.
@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List': '/device-list/',
        'Add': '/add-device/',
        'Delete': '/delete-device/<str:pk>',
        'Check-Device-Name': '/check-device-name/<str:name>',
        'Check-Device-Mac': '/check-device-mac/<str:mac>'
    }
    return Response(api_urls)

@api_view(['GET'])
def deviceList(request):

    devices = Devices.objects.all()
    serializer = DevicesSerializer(devices, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addDevice(request):
    
    try:
        api_key = request.data['apiKey']
        if API_KEY != api_key:
            return Response({'error': 'Invalid API key.'}, status=401)
    except:
        return Response({'error': 'API key missing.'}, status=401)

    serializer = DevicesSerializer(data=request.data)
    name = request.data['name']
    mac = request.data['macAdd']

    try:
        query = Devices.objects.get(name=name)
        return Response({
            "error": True,
            "error_msg": "This Name aleady registered in the Database !!",
            })
    except:
        try:
            query = Devices.objects.get(macAdd=mac)
            return Response({
                "error": True,
                "error_msg": "This Device has already registered in system!!",
                })
        except:
            pass

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteDevice(request, pk):

    try:
        api_key = request.data['api_key']
        if API_KEY != api_key:
            return Response({'error': 'Invalid API key.'}, status=401)
    except:
        return Response({'error': 'API key missing.'}, status=401)

    try:
        devices = Devices.objects.get(id=pk)
        devices.delete()
    except:
        return(Response("There is no user under this id !!"))

    return Response("Successfully Deleted!!")

@api_view(['GET'])
def checkDeviceName(request, name):
    try:
        query = Devices.objects.get(name=name)
        return Response({
            "error": True,
            "error_msg": "This Name aleady registered in the Database !!",
            })
    except:
        return Response({
            "error": False,
            })

@api_view(['GET'])
def checkDeviceMac(request, mac):
    try:
        query = Devices.objects.get(macAdd=mac)
        return Response({
            "error": True,
            "error_msg": "This Device has already registered in system!!",
        })
    except:
        return Response({
            "error": False,
        })
