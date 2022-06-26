from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator






class Product (models.Model):
    Product_title = models.CharField(max_length=100)
    Product_details = models.TextField()
    Product_price = models.DecimalField(max_digits=5, decimal_places=2)
    Product_discount = models.DecimalField(max_digits=5, decimal_places=2)
    Product_is_active = models.BooleanField(default=True)
    Product_brand = models.CharField(max_length=75)
    Product_category = models.ManyToManyField('Category')
    Product_user = models.ManyToManyField('User')
    product_color = models.ManyToManyField('Color')
    product_size = models.ManyToManyField('Size')



    def __str__(self): 
        return self.Product_title



class Review (models.Model):
    Review_rating = models.SmallIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    Review_content = models.TextField()
    Review_product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    Review_user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True )

    def __str__(self): 
        return self.Review_user



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


    def create_superuser(self, email, first_name, last_name, password):
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
    Category_title = models.CharField(max_length=75)
    Category_gender = models.BooleanField(default=True)
    Category_description = models.CharField(max_length=100)
    Category_is_active = models.BooleanField(default=True)

    def __str__(self): 
        return self.Category_title


class Cart (models.Model):
    Cart_first_name = models.CharField(max_length=50)
    Cart_last_name = models.CharField(max_length=50)
    Cart_email = models.EmailField(max_length=255, unique=True)
    Cart_mobile = models.CharField(max_length=15)
    Cart_total = models.DecimalField(max_digits=5, decimal_places=2)
    Cart_shipping = models.DecimalField(max_digits=5, decimal_places=2)
    Cart_grand_total = models.DecimalField(max_digits=5, decimal_places=2)
    Cart_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    cart_product = models.ManyToManyField('Cart_item')

    def __str__(self): 
        return self.Cart_first_name



class Cart_item (models.Model):
    Cart_item_title = models.CharField(max_length=75)
    Cart_item_photo = models.ImageField()
    Cart_item_size = models.CharField(max_length=7)
    Cart_item_price = models.DecimalField(max_digits=5, decimal_places=2)
    Cart_item_quntity = models.IntegerField()
    Cart_item_product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    Cart_item_image = models.ForeignKey('Images', on_delete=models.CASCADE, blank=True, null=True)
    
    
    
    
    def __str__(self): 
        return self.Cart_item_title


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



class Images (models.Model):
    Images_img = models.ImageField()
    Images_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Images_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self): 
        return self.Images_img



class Color (models.Model):
    Color_name = models.CharField(max_length=75)

    def __str__(self): 
        return self.Color_name


class Size (models.Model):
    size_name = models.CharField(max_length=7)
    size_quantity = models.IntegerField()

    def __str__(self): 
        return self.size_name


