from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.forms import model_to_dict
# --------------------------------------------------------------------------------------------

from .models import *
from .serializers import *

class IndexView(APIView):
    # def get(self, request:Request, pk=None):
    #     if not pk:
    #         serializer = BookSerializer(Book.objects.all(),many=True)
    #         return Response(serializer.data)
    #     else:
    #         return Response((BookSerializer(Book.objects.get(pk=pk))).data)

    # def post(self, request: Request, pk=None):
    #     if pk:
    #         return Response("Method not allowed", status=405)

    #     serializer = BookSerializer(data=request.data)
        
    #     serializer.is_valid(raise_exception=True) 
    #     book = serializer.save()
    #     return Response(book)  
        
    # def put(self, request:Request, pk=None):
    #     if not pk:
    #         return Response("Method not allowed", status=405)
        
    #     try:
    #         book = Book.objects.get(pk=pk)

    #         serializer = BookSerializer(data=request.data, instance= book)
    #         serializer.is_valid(raise_exception=True)
    #         update_book = serializer.save()
            
    #         return Response(BookSerializer(update_book).data)

    #     except Exception as e:
    #         return Response(str(e), status=404)
        
    # def delete(self, request, pk=None):
    #     if not pk:
    #         return Response({'error': "Method DELETE not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    #     try:
    #         book = Book.objects.get(pk=pk)
    #         book.delete()

    #         return Response({'message': "The object has been removed."})
    #     except Book.DoesNotExists:
    #         return Response({'error': "Information not found."}, status=status.HTTP_404_NOT_FOUND)
    pass

class BookShopView(APIView):
    # def get(self, request:Request, pk=None):
    #     if not pk:
    #         serializer = BookShopSerializer(BookShop.objects.all(),many=True)
    #         return Response(serializer.data)
    #     else:
    #         return Response((BookShopSerializer(BookShop.objects.get(pk=pk))).data)

    # def post(self, request: Request, pk=None):
    #     if pk:
    #         return Response("Method not allowed", status=405)

    #     serializer = BookShopSerializer(data=request.data)
        
    #     serializer.is_valid(raise_exception=True) 
    #     bookshop = serializer.save()
    #     return Response(bookshop)  
        
    # def put(self, request:Request, pk=None):
    #     if not pk:
    #         return Response("Method not allowed", status=405)
        
    #     try:
    #         bookshop = BookShop.objects.get(pk=pk)

    #         serializer = BookShopSerializer(data=request.data, instance= bookshop)
    #         serializer.is_valid(raise_exception=True)
    #         update_bookshop = serializer.save()
            
    #         return Response(BookShopSerializer(update_bookshop).data)

    #     except Exception as e:
    #         return Response(str(e), status=404)
        
    # def delete(self, request, pk=None):
    #     if not pk:
    #         return Response({'error': "Method DELETE not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    #     try:
    #         bookshop = BookShop.objects.get(pk=pk)
    #         bookshop.delete()

    #         return Response({'message': "The object has been removed."})
    #     except BookShop.DoesNotExists:
    #         return Response({'error': "Information not found."}, status=status.HTTP_404_NOT_FOUND)
    pass