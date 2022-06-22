from django.urls import path, include
from e_commerce import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('register', views.RegisterViewSet)
router.register('product', views.Product_ViewSet)
router.register('review', views.Review_ViewSet)
router.register('category', views.Category_ViewSet)
router.register('cart', views.Cart_item_ViewSet)
router.register('cart_item', views.Cart_item_ViewSet)
router.register('images', views.Images_ViewSet)
router.register('color', views.Color_ViewSet)
router.register('size', views.Size_ViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
