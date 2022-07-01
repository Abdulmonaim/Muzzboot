# from django.shortcuts import get_object_or_404
# from rest_framework.decorators import action
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django_filters.rest_framework import DjangoFilterBackend


from e_commerce import serializers
from e_commerce import models
from e_commerce import permissions


class RegisterViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.Register_Serializer
    queryset = models.User.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

    def get_permissions(self):

        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'list':
            permission_classes = [IsAdminUser]
        else:
                permission_classes = [permissions.UpdateOwnProfile]
        return [permission() for permission in permission_classes]




class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        response = super(UserLoginApiView, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'id': token.user_id, 'token': token.key})


class Product_ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Product_serializer
    queryset = models.Product.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['Product_title']
    filterset_fields = ['Product_price', 'Product_brand', 'Product_category', 'product_color', 'product_size']
    ordering_fields = ['Product_price']

    def get_permissions(self):

        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    
    
    # def get_queryset(self):
    #     if not bool(self.request.GET):
    #         return Entry.objects.none()

    #     return Entry.objects.all()



class Review_ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Review_serializer
    queryset = models.Review.objects.all()
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnProfile,)


class Category_ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Category_serializer
    queryset = models.Category.objects.all()


class Cart_ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Cart_serializer
    queryset = models.Cart.objects.all()
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnProfile,)



class Cart_item_ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Cart_item_serializer
    queryset = models.Cart_item.objects.all()
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnProfile,)



class Images_ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Images_serializer
    queryset = models.Images.objects.all()


class Color_ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Color_serializer
    queryset = models.Color.objects.all()


class Size_ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Size_serializer
    queryset = models.Size.objects.all()
