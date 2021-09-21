from django.urls import path
from .views.products_views import AddToCartView, NoTokenViews, ProductDetail
from .views.order_views import OrderDetail, OrderViews
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('orders/', OrderViews.as_view(), name='cart'),
    path('order/<int:pk>/', OrderDetail.as_view(), name='cart'),
    path('order/<int:orderpk>/product/<int:productpk>/', AddToCartView.as_view(), name='cart'),
    path('products/', NoTokenViews.as_view(), name='products'),
    path('product/<int:pk>', ProductDetail.as_view(), name='product'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
