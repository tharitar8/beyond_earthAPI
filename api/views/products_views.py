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

#products homepage
class NoTokenViews(APIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    def get(self, request):
     """Index request"""
     p = Product.objects.all()
     data = NoTokenViewsSerializer(p, many=True).data
     return Response(data)

# update order
class AddToCartView(APIView):
  permission_classes = (IsAuthenticated,)
  """Update request"""
  def patch(self, request, orderpk, productpk):
    user = request.user
    data = request.data
    order = get_object_or_404(Order, pk=orderpk)
    order.productlist.add(productpk)
    order.save()
    # print(order.__dict__)
    serializer = OrderSerializer(order)
    return Response(serializer.data)



