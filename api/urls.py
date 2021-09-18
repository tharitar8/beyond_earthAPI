from django.urls import path
from .views.products_views import NoTokenViews, ProductDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing

    path('products/', NoTokenViews.as_view(), name='products'),
    path('products/<int:pk>', ProductDetail.as_view(), name='product'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
