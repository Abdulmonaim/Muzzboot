# from pyexpat import model
# from wsgiref import validate
from rest_framework import serializers
from e_commerce import models
from django.db import connection
#########################################################################################################

# instance = models.Cart_item.objects.filter(cart_item_cart=1)
# cart, total = models.Cart.objects.filter(pk=1)[0], 0

# for i in instance:
#     x1 = i.cart_item_price
#     y1 = i.cart_item_quntity
#     total += x1 * y1
#     print(total)

# cart.cart_total = total
# cart.grand_total = cart.shipping_charge + total
# cart.save()
# print(cart.cart_total, cart.grand_total)



class RegisterSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'mobile', 'address', 'height',
        'gender', 'cup_size', 'size_image', 'human_parsing', 'user_size', 'is_staff','followers', 'visitors')
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
#########################################################################################################


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Review
        fields = '__all__'
#########################################################################################################


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = '__all__'
#########################################################################################################


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cart
        fields = '__all__'
#########################################################################################################


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CartItem
        fields = ('id', 'cart_item_product', 'cart_item_cart', 'cart_item_size', 'cart_item_color',
        'cart_item_quntity', 'cart_item_title', 'cart_item_photo', 'cart_item_price')

        def create(self, validated_data):
            product = models.Product.objects.get(pk=validated_data['cart_item_product'])
            cart = models.Cart.objects.get(cart_user = validated_data['cart_item_cart'])
            image = models.Image.objects.filter(images_product=validated_data['cart_item_product'])[0]
            
            item = models.CartItem.ecommerce.create_item(
                cart_item_product=validated_data['cart_item_product'],
                cart_item_cart=cart.id,
                cart_item_size=validated_data['cart_item_size'],
                cart_item_color=validated_data['cart_item_color'],
                cart_item_quntity=validated_data['cart_item_quntity'],
                cart_item_title=product.product_title,
                cart_item_photo=image.img,
                cart_item_price=product.product_price
            )
            

            cart.cart_total += product.cart_item_price * validated_data['cart_item_quntity']
            cart.save()       

            return item
#########################################################################################################        


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = '__all__'
#########################################################################################################


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Color
        fields = '__all__'
#########################################################################################################


class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Size
        fields = '__all__'

#########################################################################################################

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = '__all__'