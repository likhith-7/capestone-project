from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product
from .serializers import ProductSerializer

@api_view(['POST'])
#class LatestProductsList(APIView):
def getLatestProductsFiltered(request):
        val = request.data['cat']
        products = Product.objects.filter(category=val)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)