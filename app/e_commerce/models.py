from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin






class Product (models.Model):
    Product_name = models.CharField(max_length=75)
    Product_meta_title = models.CharField(max_length=100)
    Product_description = models.CharField(max_length=100)
    Product_shop = models.CharField(max_length=40)
    Product_content = models.TextField()
    Product_purchase_price = models.DecimalField(max_digits=5, decimal_places=2)
    Product_discount = models.DecimalField(max_digits=5, decimal_places=2)
    Product_sale_price = models.DecimalField(max_digits=5, decimal_places=2)
    Product_quantity = models.IntegerField()
    # Product_active = models.BooleanField()
    Product_brand = models.ForeignKey('brand', on_delete=models.CASCADE, blank=True, null=True)
    Product_type_product = models.ManyToManyField('Product_type')
    Category_product = models.ManyToManyField('Category')
    product_user = models.ManyToManyField('User')



    def __str__(self): 
        return self.Product_name


class Product_type (models.Model):
    Product_type_name = models.CharField(max_length=75)
    Product_type_description = models.CharField(max_length=100)
    # Product_type_active = models.BooleanField()


    def __str__(self): 
        return self.Product_type_name


class Product_review (models.Model):
    Product_review_name = models.CharField(max_length=75)
    Product_review_ratin = models.SmallIntegerField()
    Product_review_content = models.TextField()
    # Product_review_active = models.BooleanField()
    Product_review_product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self): 
        return self.Product_review_name



class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name, password):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        # password =  make_password(password, 'qwertyuiop','md5')
        user = self.model(email=email, name=name, password=password)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user





class User (AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    mobile = models.CharField(max_length=15)
    gender = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']





    def __str__(self): 
        return self.name

# class account (models.Model):
#     account_name = models.CharField(max_length=50)   
#     account_password = models.CharField(max_length=32)
#     account_hint_question = models.CharField(max_length=32)
#     account_answer = models.CharField(max_length=32)
#     # account_active = models.BooleanField()
#     account_user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    # def __str__(self): 
    #     return self.account_name



class Category (models.Model):
    Category_name = models.CharField(max_length=75)
    Category_meta_title = models.CharField(max_length=100)
    Category_description = models.CharField(max_length=100)
    Category_content = models.TextField()
    # Category_active = models.BooleanField()
    Category_parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self): 
        return self.Category_name


class Order (models.Model):
    Order_first_name = models.CharField(max_length=50)
    Order_middle_name = models.CharField(max_length=50)
    Order_last_name = models.CharField(max_length=50)
    Order_email = models.EmailField(max_length=255, unique=True)
    Order_mobile = models.CharField(max_length=15)
    Order_token = models.CharField(max_length=100)
    Order_description = models.CharField(max_length=100)
    Order_discount = models.DecimalField(max_digits=5, decimal_places=2)
    Order_item_discount = models.DecimalField(max_digits=5, decimal_places=2)
    Order_sub_total = models.DecimalField(max_digits=5, decimal_places=2)
    Order_total = models.DecimalField(max_digits=5, decimal_places=2)
    Order_grand_total = models.DecimalField(max_digits=5, decimal_places=2)
    # Order_active = models.BooleanField()
    Order_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    

    def __str__(self): 
        return self.Order_first_name


class Order_item (models.Model):
    Order_item_content = models.TextField()
    Order_item_price = models.DecimalField(max_digits=5, decimal_places=2)
    Order_item_discount = models.DecimalField(max_digits=5, decimal_places=2)
    Product_quantity = models.IntegerField()
    Order_item_product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    Order_item_order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self): 
        return str(self.Order_item_price)


class Transaction (models.Model):
    Transaction_code = models.CharField(max_length=100)
    Transaction_content = models.TextField()
    Transaction_type = models.SmallIntegerField()
    Transaction_mode = models.SmallIntegerField()
    Transaction_status = models.SmallIntegerField()
    Transaction_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    Transaction_order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self): 
        return self.Transaction_content



class Brand (models.Model):
    Brand_name = models.CharField(max_length=75)
    Brand_logo = models.CharField(max_length=75)
    Brand_description = models.CharField(max_length=100)
    # Brand_active = models.BooleanField()

    def __str__(self): 
        return self.Brand_name


class Images (models.Model):
    Images_img = models.ImageField()
    Images_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Images_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Color (models.Model):
    Color_name = models.CharField(max_length=75)
    Color_product = models.ManyToManyField(Product)

class Size (models.Model):
    size = models.FloatField()
    Size_product = models.ManyToManyField(Product)


class Address (models.Model):
    Address_address = models.CharField(max_length=50)
    Address_zipcode = models.CharField(max_length=50)
    Address_active = models.BooleanField()
    Address_user = models.ManyToManyField(User)

    
