from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from e_commerce import serializers
from e_commerce import models
from e_commerce import permissions


class RegisterViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.Register_Serializer
    queryset = models.User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ModelViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet)

class Product_ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Product_serializer
    queryset = models.Product.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    
    


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