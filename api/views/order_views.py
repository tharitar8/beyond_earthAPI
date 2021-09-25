from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status, serializers
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


from ..serializers import OrderSerializer
from ..models.order import Order

# make a patch request order
class AddToCartView(APIView):
  permission_classes = (IsAuthenticated,)
  """Update request"""
  def patch(self, request, orderpk, productpk):
    user = request.user
    data = request.data
    order = get_object_or_404(Order, pk=orderpk)
    order.productlist.add(productpk)
    order.save()
    print(order.__dict__)
    serializer = OrderSerializer(order)
    return Response(serializer.data)

# see all orders
class OrderViews(APIView):
  def get(self, request):
    print('get')
    orders = Order.objects.all()
    data = OrderSerializer(orders, many=True).data
    return Response(data)

# post request to create an order when SignIn
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

# cart link on nav bar get to see that order
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

  # delete order
    def delete(self, request, pk):
      """Delete request"""
      # Locate order to delete
      order = get_object_or_404(Order, pk=pk)
      # Check the order's owner against the user making this request
      if request.user != order.owner:
          raise PermissionDenied('Unauthorized, you do not own this order')
      # Only delete if the user owns the  order
      order.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
# have to make patch route update when inside the cart
