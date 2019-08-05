from .serializers import ShipCharterSerializer, ShipSerializer, OwnerSerializer
from .models import ShipCharter,ShipOwner
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
from .models import Ship

# class Shiplist(ListView):
#     template_name ='ships/ship_list.html'
#     queryset = Ship.objects.all()


class ShipCarterList(APIView):
    def get(self, request):
        Carter_list = ShipCharter.objects.all()
        serializers = ShipCharterSerializer(Carter_list, many=True)
        print(serializers.data)
        return Response(serializers.data)


class ShipList(APIView):
    def get(self, request):
        Ship_list = Ship.objects.all()
        serializers = ShipSerializer(Ship_list, many=True)
        return Response(serializers.data)


class OwnerList(APIView):
    def get(self,requset):
        OwnerList = ShipOwner.objects.all()
        serializers = OwnerSerializer(OwnerList, many=True)
        return Response(serializers.data)

