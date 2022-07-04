from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
########################################################################################################################

class EcommerceManager(models.Manager):

    def create_item(self, cart_item_product, cart_item_cart, cart_item_size, cart_item_color,
    cart_item_quntity, cart_item_title, cart_item_photo, cart_item_price):

        item = self.model(cart_item_product=cart_item_product, cart_item_cart=cart_item_cart,
        cart_item_size=cart_item_size, cart_item_color=cart_item_color, cart_item_quntity=cart_item_quntity,
        cart_item_title=cart_item_title, cart_item_photo=cart_item_photo, cart_item_price=cart_item_price)
        item.save(using=self._db)

        return item    






class UserProfileManager(BaseUserManager):
    

    """Manager for user profiles"""
    def create_user(self, first_name, last_name, email, password, mobile='', address=''):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, password=password, mobile=mobile, address=address)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, first_name, last_name, email, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(first_name, last_name, email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user
########################################################################################################################


class User (AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=75)
    followers = models.IntegerField(default=0)
    visitors = models.IntegerField(default=0)
    size_image = models.ImageField(blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cup_size = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    user_json = models.JSONField(blank=True, null=True)
    human_parsing = models.ImageField(blank=True, null=True)
    user_size = models.CharField(max_length=7, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    gender = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self): 
        return self.first_name
########################################################################################################################


class Category (models.Model):
    category_title = models.CharField(max_length=75)
    category_gender = models.BooleanField(default=False)
    category_description = models.CharField(max_length=100)

    def __str__(self): 
        return self.category_title
########################################################################################################################


class Cart (models.Model):
    # cart_first_name = models.CharField(max_length=50)
    # cart_last_name = models.CharField(max_length=50)
    # cart_email = models.EmailField(max_length=255, unique=True)
    # cart_mobile = models.CharField(max_length=15)
    # address = models.CharField(max_length=75)
    cart_total = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=0)
    shipping_charge = models.DecimalField(max_digits=5, decimal_places=2, default=25)
    grand_total = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=0)
    cart_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self): 
        return str(self.cart_total)
########################################################################################################################


class CartItem (models.Model):
    cart_item_product = models.ForeignKey('Product', on_delete=models.CASCADE)
    cart_item_cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    cart_item_size = models.CharField(max_length=7)
    cart_item_color = models.CharField(max_length=7)
    cart_item_quntity = models.IntegerField(default=1)
    cart_item_title = models.CharField(max_length=75, blank=True, null=True)
    cart_item_photo = models.ImageField(blank=True, null=True)
    cart_item_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ecommerce = EcommerceManager()
    objects = models.Manager
    
    def __str__(self): 
        return str(self.cart_item_title)
    

    

########################################################################################################################


class CheckedCart (models.Model):
    checked_cart_id = models.IntegerField(primary_key=True)
    cart_total = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    shipping_charge = models.DecimalField(max_digits=5, decimal_places=2)
    grand_total = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    user_id = models.IntegerField(default=0)
    checked_cart_selling_date = models.DateField() 

    def __str__(self): 
        return str(self.checked_cart_id)
########################################################################################################################


class CheckedCartItem (models.Model):
    checked_cart_item_title = models.CharField(max_length=75)
    checked_cart_item_photo = models.ImageField(blank=True, null=True)
    checked_cart_item_size = models.CharField(max_length=7)
    checked_cart_item_price = models.DecimalField(max_digits=5, decimal_places=2)
    checked_cart_item_quntity = models.IntegerField(default=1)
    checked_cart = models.ForeignKey(CheckedCart, on_delete=models.CASCADE, blank=True, null=True)
    sales = models.ForeignKey('Sales', on_delete=models.CASCADE, blank=True, null=True)
    product_id = models.IntegerField(default=0)
        
    def __str__(self): 
        return self.checked_cart_item_title
########################################################################################################################


class Size (models.Model):
    size_name = models.CharField(max_length=7)

    def __str__(self): 
        return self.size_name
########################################################################################################################


class Color (models.Model):
    color_name = models.CharField(max_length=15)

    def __str__(self): 
        return self.color_name
########################################################################################################################


class Quantity (models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity_size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity_color = models.ForeignKey(Color, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    quantity_alarm = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self): 
        return str(self.quantity)
########################################################################################################################


class Product (models.Model):
    product_title = models.CharField(max_length=100)
    product_details = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    product_brand = models.CharField(max_length=75)
    max_quantity = models.IntegerField(default=0)
    product_date_entry = models.DateField()
    product_rating = models.DecimalField(max_digits=5, decimal_places=1, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    product_category = models.ManyToManyField(Category)
    product_vendor = models.ManyToManyField(User)

    def __str__(self): 
        return self.product_title
########################################################################################################################


class Review (models.Model):
    review_rating = models.DecimalField(max_digits=5, decimal_places=1, default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_content = models.TextField()
    review_date = models.DateField()
    review_product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    review_user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True )

    def __str__(self): 
        return str(self.review_user)
########################################################################################################################


class Image (models.Model):
    img = models.ImageField()
    images_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    images_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self): 
        return str(self.img)
########################################################################################################################


class Sales(models.Model):
    sales_user = models.ForeignKey(User,  on_delete=models.CASCADE)

