from django.urls import path
from .views.products_views import NoTokenViews, ProductDetail
from .views.order_views import OrderDetail, OrderViews, AddToCartView
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('products/', NoTokenViews.as_view(), name='products'),
    # product detail on their own page
    path('product/<int:pk>', ProductDetail.as_view(), name='productdetail'),
    # get all orders from this link
    path('orders/', OrderViews.as_view(), name='order'),
    #click 'add to cart' patch the order place new item in there
    path('order/<int:orderpk>/product/<int:productpk>/',
         AddToCartView.as_view(), name='cart'),
    # get specific order show and delete
    path('order/<int:pk>/', OrderDetail.as_view(), name='cart'),
    
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
