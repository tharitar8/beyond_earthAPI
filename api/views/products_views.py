# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.exceptions import PermissionDenied
# from rest_framework import generics, status
# from django.shortcuts import get_object_or_404

# from ..models.mango import Mango
# from ..serializers import MangoSerializer


# def getRoutes(request):
#   routes = [
#     '/api/products/',
#     '/api/products/create/',

#     '/api/products/upload/',
#     '/api/products/<id>/reviews/',

#     '/api/products/top/',
#     '/api/products/<id>',

#     '/api/products/delete/<id>',
#     '/api/products/<update>/<id>',
#   ]

#   return JsonResponse(routes, safe=False)
