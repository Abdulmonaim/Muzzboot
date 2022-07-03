from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
########################################################################################################################





class Product (models.Model):
    product_title = models.CharField(max_length=100)
    product_details = models.TextField()
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    product_discount = models.DecimalField(max_digits=5, decimal_places=2, default=False)
    product_brand = models.CharField(max_length=75)
    quantity = models.IntegerField()
    quantity_alarm = models.CharField(max_length=100)
    product_date_entry = models.DateField()
    product_rating = models.DecimalField(max_digits=5, decimal_places=1, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    product_category = models.ManyToManyField('Category')
    product_user = models.ManyToManyField('User')
    product_color = models.ManyToManyField('Color')
    product_size = models.ManyToManyField('Size')

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
    user_json = models.JSONField(blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cup_size = models.CharField(max_length=10, blank=True, null=True)
    size_image = models.ImageField(blank=True, null=True)
    human_parsing = models.ImageField(blank=True, null=True)
    user_size = models.CharField(max_length=7, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self): 
        return self.first_name
########################################################################################################################


class Category (models.Model):
    category_title = models.CharField(max_length=75)
    category_gender = models.BooleanField(default=True)
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
    cart_total = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    shipping_charge = models.DecimalField(max_digits=5, decimal_places=2)
    grand_total = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cart_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self): 
        return self.cart_first_name
########################################################################################################################


class Cart_item (models.Model):
    cart_item_title = models.CharField(max_length=75)
    cart_item_photo = models.ImageField(blank=True, null=True)
    cart_item_size = models.CharField(max_length=7)
    cart_item_price = models.DecimalField(max_digits=5, decimal_places=2)
    cart_item_quntity = models.IntegerField()
    cart_item_product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    cart_item_cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self): 
        return self.cart_item_title
########################################################################################################################


class Checked_cart (models.Model):
    checked_cart_id = models.IntegerField(primary_key=True)
    cart_total = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    shipping_charge = models.DecimalField(max_digits=5, decimal_places=2)
    grand_total = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    user_id = models.IntegerField(default=0)
    checked_cart_selling_date = models.DateField() 

    def __str__(self): 
        return self.checked_cart_first_name
########################################################################################################################


class Checked_cart_item (models.Model):
    checked_cart_item_title = models.CharField(max_length=75)
    checked_cart_item_photo = models.ImageField(blank=True, null=True)
    checked_cart_item_size = models.CharField(max_length=7)
    checked_cart_item_price = models.DecimalField(max_digits=5, decimal_places=2)
    checked_cart_item_quntity = models.IntegerField()
    checked_cart = models.ForeignKey(Checked_cart, on_delete=models.CASCADE, blank=True, null=True)
    sales = models.ForeignKey('Sales', on_delete=models.CASCADE, blank=True, null=True)
        
    def __str__(self): 
        return self.checked_cart_item_title
########################################################################################################################


class Images (models.Model):
    images_img = models.ImageField()
    images_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    images_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self): 
        return self.images_img
########################################################################################################################


class Color (models.Model):
    color_name = models.CharField(max_length=75)

    def __str__(self): 
        return self.color_name
########################################################################################################################


class Size (models.Model):
    size_name = models.CharField(max_length=7)
    size_quantity = models.IntegerField()

    def __str__(self): 
        return self.size_name
########################################################################################################################


class Sales(models.Model):
    sales_user = models.ForeignKey(User,  on_delete=models.CASCADE)
