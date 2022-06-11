from django.urls import path, include
from e_commerce import views

urlpatterns = [
    path('Product_list/', views.Product_list.as_view()),
    path('Product_review_list/', views.Product_review_list.as_view()),
    path('images_list/', views.Images_list.as_view()),
    path('product_type_list/', views.Product_type_list.as_view()),
    path('register/', views.Register.as_view()),
    path('category_list/', views.Category_list.as_view()),
    path('order_list/', views.Order_list.as_view()),
    path('order_item_list/', views.Order_item_list.as_view()),
    path('transaction_list/', views.Transaction_list.as_view()),
    path('brand_list/', views.Brand_list.as_view()),
    path('product_pk/<int:pk>', views.Product_pk.as_view()),

]
