from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status, serializers
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
# from ..models.mango import Mango
# from ..serializers import MangoSerializer
from ..serializers import ProductSerializer, NoTokenViewsSerializer, OrderSerializer
from ..models.product import Product, Order, OrderItem, ShippingAddress

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []
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
    permission_classes = []
    def get(self, request):
     """Index request"""
     p = Product.objects.all()[:6]
     data = NoTokenViewsSerializer(p, many=True).data
     return Response(data)

# create order
class AddToCartView(APIView):
  permission_classes = (IsAuthenticated,)
  """Create request"""
  def post(self, request):
    user = request.user
    data = request.data
    # request.data['product']['owner'] = request.user.id
    orderItems = ProductSerializer(data=request.data['product'])
    print(data)
    if orderItems and len(orderItems) == 0:
        return Response({'detail': 'No Order Items'}, status=status.HTTP_400_BAD_REQUEST)
    else:
      # create order
      order = Order.objects.create(
          user=user,
          paymentMethod=data['paymentMethod'],
          taxPrice=data['taxPrice'],
          shippingPrice=data['shippingPrice'],
          totalPrice=data['totalPrice']
      )
      # create shipping address
      shipping = ShippingAddress.objects.create(
          order=order,
          address=data['shippingAddress']['address'],
          city=data['shippingAddress']['city'],
          postalCode=data['shippingAddress']['postalCode'],
          country=data['shippingAddress']['country'],
      )
#  create order items and set order to orderItem relationship
      for i in orderItems:
            product = Product.objects.get(_id=i['product'])

            item = OrderItem.objects.create(
                product=product,
                order=order,
                name=product.name,
                qty=i['qty'],
                price=i['price'],
                image=product.image.url,
            )
            # Update stock
            product.countInStock -= item.qty
            product.save()
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the order to show
        order = get_object_or_404(Order, pk=pk)
        # Only want to show owned order?
        if request.user != order.owner:
            raise PermissionDenied('Unauthorized, you do not own this mango')
        # Run the data through the serializer so it's formatted
        data = OrderSerializer(order).data
        return Response({'order': data})

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

    def partial_update(self, request, pk):
      """Update Request"""
      # Locate Order
      # get_object_or_404 returns a object representation of our Order
      order= get_object_or_404(Order, pk=pk)
      # Check the order's owner against the user making this request
      if request.user != order.owner:
          raise PermissionDenied('Unauthorized, you do not own this order')

      # Ensure the owner field is set to the current user's ID
      request.data['order']['owner'] = request.user.id
      # Validate updates with serializer
      data = OrderSerializer(order, data=request.data['order'], partial=True)
      if data.is_valid():
          # Save & send a 204 no content
          data.save()
          return Response(status=status.HTTP_204_NO_CONTENT)
      # If the data is not valid, return a response with the errors
      return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
