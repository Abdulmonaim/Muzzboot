# from pyexpat import model
# from wsgiref import validate
from rest_framework import serializers
from e_commerce import models
#########################################################################################################



class RegisterSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.User
        fields = ('first_name', 'last_name', 'email', 'password', 'mobile', 'address', 'height',
         'cup_size', 'size_image', 'human_parsing', 'user_size','gender', 'is_staff','followers', 'visitors')
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
            address=validated_data['address'],
            gender=validated_data['gender'],
            is_staff=validated_data['is_staff']
        )

        models.Cart.objects.create_cart(user)

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
        fields = ['cart_item_product', 'cart_item_cart', 'cart_item_size', 'cart_item_color', 'cart_item_quantity',
        'cart_item_title', 'cart_item_photo', 'cart_item_price']

    def create(self, validated_data):
        product = models.Product.objects.get(id=validated_data['cart_item_product'].id)
        cart = models.Cart.objects.get(id=validated_data['cart_item_cart'].id)
        image = models.Image.objects.filter(images_product=validated_data['cart_item_product'])[0]

        item = models.CartItem.objects.create_item(
            cart_item_product=validated_data['cart_item_product'],
            cart_item_cart=cart,
            cart_item_size=validated_data['cart_item_size'],
            cart_item_color=validated_data['cart_item_color'],
            cart_item_quantity=validated_data['cart_item_quantity'],
            cart_item_title=validated_data['cart_item_product'],
            cart_item_photo=image.img,
            cart_item_price=product.product_price
        )       

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