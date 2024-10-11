from drf_multiple_model.views import FlatMultipleModelAPIView
from rest_framework import filters
from . models import Car, Ship, AirCraft
from . serializers import CarSerializer, ShipSerializer, AirCraftSerializer
class MultipleModelAPIView(FlatMultipleModelAPIView):
    add_model_type = False
    querylist = [
        {
            'queryset': Car.objects.all(),
            'serializer_class': CarSerializer,
        },
        {
            'queryset': AirCraft.objects.all(),
            'serializer_class': AirCraftSerializer,
        },
        
        {
            'queryset': Ship.objects.all(),
            'serializer_class': ShipSerializer,
        },
        
    ]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name',) 