from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status, serializers
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes

# from ..models.mango import Mango
# from ..serializers import MangoSerializer
from ..serializers import ProductSerializer, NoTokenViewsSerializer, OrderSerializer
from ..models.product import Product
from ..models.order import Order

# showProductPage
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    def get(self, request, pk):
        """Show one product request"""
        # Locate the product to show
        product = get_object_or_404(Product, pk=pk)
        # Want to show details of product only log in USER
        data = ProductSerializer(product).data
        return Response(data)

#Show all Products on homepage with non sing-in user
class NoTokenViews(APIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    def get(self, request):
     """Index request"""
     p = Product.objects.all()
     data = NoTokenViewsSerializer(p, many=True).data
     return Response(data)
