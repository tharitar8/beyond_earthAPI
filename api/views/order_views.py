from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status, serializers
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


from ..serializers import OrderSerializer
from ..models.order import Order


class OrderViews(APIView):
  def get(self, request):
    print('get')
    orders = Order.objects.all()
    data = OrderSerializer(orders, many=True).data
    return Response(data)

  def post(self, request):
    """Post Request"""
    print('text', request.data)
    data = request.data.copy()
    data['owner'] = request.user.id
    orders = OrderSerializer(data=data)
    print('orders', orders)
    if orders.is_valid():
      orders.save()
      return Response(orders.data)
    else:
      return Response(orders.errors)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

# cart nav link
    def get(self, request, pk):
        """Show request"""
        # Locate the order to show
        order = get_object_or_404(Order, pk=pk)
        print(request, pk)
        # Only want to show owned order?
        if request.user != order.owner:
            raise PermissionDenied('Unauthorized, you do not own this')
        # Run the data through the serializer so it's formatted
        data = OrderSerializer(order).data
        return Response({'order': data})
# checkout button
    def delete(self, request, pk):
      """Delete request"""
      # Locate order to delete
      order = get_object_or_404(Order, pk=pk)
      # Check the order's owner against the user making this request
      if request.user != order.owner:
          raise PermissionDenied('Unauthorized, you do not own this mango')
      # Only delete if the user owns the  order
      order.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
