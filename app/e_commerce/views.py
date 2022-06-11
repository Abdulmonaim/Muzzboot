from django.http import Http404
from .models import * 
from .serializers import * 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters, viewsets
# from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import generics



class Product_list (APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = Product_serializer(product, many=True)
        return Response(serializer.data)
        

class Product_review_list (APIView):
    def get(self, request):
        product_review = Product_review.objects.all()
        serializer = Product_review_serializer(product_review, many=True)
        return Response(serializer.data)

class Images_list (APIView):
    def get(self, request):
        images = Images.objects.all()
        serializer = Images_serializer(images, many=True)
        return Response(serializer.data)

class Product_type_list (APIView):
    def get(self, request):
        product_type = Product_type.objects.all()
        serializer = Product_type_serializer(product_type, many=True)
        return Response(serializer.data)




class Register (generics.GenericAPIView):
    serializer_class = Register_Serializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": Register_Serializer(user, context=self.get_serializer_context()).data,})



class Category_list (APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = Category_serializer(category, many=True)
        return Response(serializer.data)




class Order_list (APIView):
    def get(self, request):
        order = Order.objects.all()
        serializer = Order_serializer(order, many=True)
        return Response(serializer.data)


class Order_item_list (APIView):
    def get(self, request):
        order_item = Order_item.objects.all()
        serializer = Order_item_serializer(order_item, many=True)
        return Response(serializer.data)


class Transaction_list (APIView):
    def get(self, request):
        transaction = Transaction.objects.all()
        serializer = Transaction_serializer(transaction, many=True)
        return Response(serializer.data)


class Brand_list (APIView):
    def get(self, request):
        brand = Brand.objects.all()
        serializer = Brand_serializer(brand, many=True)
        return Response(serializer.data)



class Product_pk (APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = Product_serializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = Product_serializer(product, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        Product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#filter
