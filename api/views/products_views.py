from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status, serializers
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
# from ..models.mango import Mango
# from ..serializers import MangoSerializer
from ..serializers import ProductSerializer, NoTokenViewsSerializer
from ..models.product import Product

# Create your views here.
class Products(generics.ListCreateAPIView):
  def get(self, request):
        """Index request"""
        # Get all the products:
        print(request)
        products = Product.objects.all()
        data = ProductSerializer(products, many=True).data
        return Response(data)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    def get(self, request, pk):
        """Show request"""
        # Locate the product to show
        product = get_object_or_404(Product, pk=pk)
        # Want to show details of product only log in USER
        if request.user != product.user:
            raise PermissionDenied('Unauthorized, please log in')

class NoTokenViews(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request):
     """Index request"""
     p = Product.objects.all()[:6]
     data = NoTokenViewsSerializer(p, many=True).data
     return Response(data)


#user create order add to cart
#user see one page product detail
#user see all products
#user edit cart
#user delete cart
