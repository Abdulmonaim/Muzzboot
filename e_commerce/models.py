from django.db import models


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


class User (models.Model):
    User_first_name = models.CharField(max_length=50)
    User_middle_name = models.CharField(max_length=50)
    User_last_name = models.CharField(max_length=50)
    User_email = models.CharField(max_length=50)
    User_mobile = models.CharField(max_length=15)
    User_password = models.CharField(max_length=32)
    User_gender = models.CharField(max_length=15)
    User_intro = models.TimeField()
    User_profile = models.TimeField()
    User_product = models.ManyToManyField(Product) 

    def __str__(self): 
        return self.User_first_name

class User_account (models.Model):
    User_account_user_name = models.CharField(max_length=50)   
    User_account_password = models.CharField(max_length=32)
    User_account_hash_code = models.CharField(max_length=150)
    User_account_salt = models.CharField(max_length=150)
    User_account_hint_question = models.CharField(max_length=32)
    User_account_answer = models.CharField(max_length=32)
    # User_account_active = models.BooleanField()
    User_account_user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self): 
        return self.User_account_user_name



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
    Order_email = models.CharField(max_length=50)
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
    Images_url = models.TextField()
    Images_physical_path = models.TextField()
    Images_size = models.DecimalField(max_digits=10, decimal_places=3)
    Images_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Images_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Color (models.Model):
    Color_name = models.CharField(max_length=75)
    Color_product = models.ManyToManyField(Product)

class Size (models.Model):
    size = models.FloatField()
    Size_product = models.ManyToManyField(Product)