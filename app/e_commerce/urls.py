from django.urls import path, include
from e_commerce import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('register', views.RegisterViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
