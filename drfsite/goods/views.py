from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Products, Categories
from .serializers import ProductsSerializer

class GoodsViewSet(viewsets.ModelViewSet):
    # queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Products.objects.all()[:3]
        
        return Products.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Categories.objects.get(pk=pk)
        return Response({'cats': [cats.name]})

# class GoodsAPIList(generics.ListCreateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer

# class GoodsAPIUpdate(generics.UpdateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer

# class GoodsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer

# class GoodsAPIView(APIView):
#     def get(self, request):
#         lst = Products.objects.all()
#         return Response({'posts': ProductsSerializer(lst, many=True).data})
	
#     def post(self, request):
#         serializer = ProductsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
        
#         return Response({'post': serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
		
#         try:
#             instance = Products.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})
		
#         serizalizer = ProductsSerializer(data=request.data, instance=instance)
#         serizalizer.is_valid(raise_exception=True)
#         serizalizer.save()
#         return Response({"post":serizalizer.data})
    

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)

#         if not pk:
#             return Response({"error": "Object does not exist"})

#         try:
#             instance = Products.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"error": "Something went wrong"})
        
#         return Response({"post":"delete product " + str(pk)})



# class GoodsAPIView(generics.ListAPIView):
# 	queryset = Products.objects.all()
# 	serializer_class = ProductsSerializer
