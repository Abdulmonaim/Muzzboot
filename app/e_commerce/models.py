from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator



# class Transaction (models.Model):
#     Transaction_code = models.CharField(max_length=100)
#     Transaction_content = models.TextField()
#     Transaction_type = models.SmallIntegerField()
#     Transaction_mode = models.SmallIntegerField()
#     Transaction_status = models.SmallIntegerField()
#     Transaction_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
#     Transaction_order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)

#     def __str__(self): 
#         return self.Transaction_content



class Product (models.Model):
    product_title = models.CharField(max_length=100)
    product_details = models.TextField()
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    product_discount = models.DecimalField(max_digits=5, decimal_places=2)
    product_is_active = models.BooleanField(default=True)
    product_brand = models.CharField(max_length=75)
    product_review = models.SmallIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    product_category = models.ManyToManyField('Category')
    product_user = models.ManyToManyField('User')
    product_color = models.ManyToManyField('Color')
    product_size = models.ManyToManyField('Size')

    def __str__(self): 
        return self.product_title



class Review (models.Model):
    review_rating = models.SmallIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_content = models.TextField()
    review_product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    review_user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)

    # class Meta:
    #     db_table = 'review'

    # def __str__(self): 
    #     return self.Review_user


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


class User (AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=75)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self): 
        return self.first_name



class Category (models.Model):
    category_title = models.CharField(max_length=75)
    category_gender = models.BooleanField(default=True)
    category_description = models.CharField(max_length=100)
    category_is_active = models.BooleanField(default=True)

    # class Meta:
    #     db_table = 'category'
    # def __str__(self): 
    #     return self.Category_title



class Cart (models.Model):
    cart_first_name = models.CharField(max_length=50)
    cart_last_name = models.CharField(max_length=50)
    cart_email = models.EmailField(max_length=255, unique=True)
    cart_mobile = models.CharField(max_length=15)
    cart_total = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cart_shipping = models.DecimalField(max_digits=5, decimal_places=2)
    cart_grand_total = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cart_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    cart_product = models.ManyToManyField('Cart_item')

    def __str__(self): 
        return self.cart_first_name


class Cart_item (models.Model):
    cart_item_title = models.CharField(max_length=75)
    cart_item_photo = models.ImageField()
    cart_item_size = models.CharField(max_length=7)
    cart_item_price = models.DecimalField(max_digits=5, decimal_places=2)
    cart_item_quntity = models.IntegerField()
    cart_item_product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    cart_item_image = models.ForeignKey('Images', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self): 
        return self.cart_item_photo


# class Checked_cart (models.Model):
#     checked_cart_first_name = models.CharField(max_length=50)
#     checked_cart_last_name = models.CharField(max_length=50)
#     checked_cart_email = models.EmailField(max_length=255, unique=True)
#     checked_cart_mobile = models.CharField(max_length=15)
#     checked_cart_total = models.DecimalField(max_digits=5, decimal_places=2)
#     checked_cart_shipping = models.DecimalField(max_digits=5, decimal_places=2)
#     checked_cart_grand_total = models.DecimalField(max_digits=5, decimal_places=2)
#     checked_cart_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
#     checked_cart_product = models.ManyToManyField('Checked_cart_item')

#     def __str__(self): 
#         return self.Checked_cart_first_name



class Images (models.Model):
    images_img = models.ImageField()
    images_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    images_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self): 
        return self.images_img



class Color (models.Model):
    color_name = models.CharField(max_length=75)

    def __str__(self): 
        return self.color_name


class Size (models.Model):
    size_name = models.CharField(max_length=7)
    size_quantity = models.IntegerField()

    def __str__(self): 
        return self.size_name
