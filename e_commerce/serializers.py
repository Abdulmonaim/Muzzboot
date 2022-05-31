from dataclasses import fields
from rest_framework import serializers
from .models import * 
from rest_framework.response import Response


class Product_serializer (serializers.ModelSerializer):
    class Meta : 
        model = Product
        fields = '__all__'


class Product_review_serializer (serializers.ModelSerializer):
    class Meta : 
        model = Product_review
        fields = '__all__'


class Product_type_serializer (serializers.ModelSerializer):
    class Meta : 
        model = Product_type
        fields = '__all__'


class User_serializer (serializers.ModelSerializer):
    class Meta : 
        model = User
        fields = ('id', 'name ', 'password')


class Register_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        my_incoming_data = validated_data

        # If you want to pop any field from the incoming data then you can like below.
        # popped_data = validated_data.pop('timeFrames')

        inserted_data = User.objects.create(**validated_data)
        return Response(inserted_data)  


# class account_serializer (serializers.ModelSerializer):
#     class Meta : 
#         model = account
#         fields = '__all__'


class Category_serializer (serializers.ModelSerializer):
    class Meta : 
        model = Category
        fields = '__all__'


class Order_serializer (serializers.ModelSerializer):
    class Meta : 
        model = Order
        fields = '__all__'


class Order_item_serializer (serializers.ModelSerializer):
    class Meta : 
        model = Order_item
        fields = '__all__'


class Transaction_serializer (serializers.ModelSerializer):
    class Meta : 
        model = Transaction
        fields = '__all__'


class Brand_serializer (serializers.ModelSerializer):
    class Meta : 
        model = Brand
        fields = '__all__'


class Color_serializer (serializers.ModelSerializer):
    class Meta : 
        model = Color
        fields = '__all__'

class Size_serializer (serializers.ModelSerializer):
    class Meta : 
        model = Size
        fields = '__all__'

















class Images_serializer (serializers.ModelSerializer):
    class Meta : 
        model = Images
        fields = '__all__'
