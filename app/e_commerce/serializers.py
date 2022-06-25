from pyexpat import model
from wsgiref import validate
from rest_framework import serializers
from e_commerce import models




class Register_Serializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'mobile', 'address')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
            mobile=validated_data['mobile'],
            address=validated_data['address']
        )

        return user



class Product_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'



class Review_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'


class Category_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'



class Cart_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'


class Cart_item_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart_item
        fields = '__all__'
        


class Images_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Images
        fields = '__all__'


class Color_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Color
        fields = '__all__'


class Size_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Size
        fields = '__all__'

