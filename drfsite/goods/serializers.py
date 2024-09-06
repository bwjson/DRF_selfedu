from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Products

# class ProductModel:
# 	def __init__(self, title, content):
# 		self.title = title
# 		self.content = content

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("title", "content", "category")
        
# def encode():
# 	model = ProductModel('iPhone 15 PRO MAX ULTRA', 'I dont cook I dont clean')
# 	model_sr = ProductsSerializer(model)
# 	print(model_sr.data, type(model_sr.data), sep='\n')
# 	json = JSONRenderer().render(model_sr.data)
# 	print(json, type(model_sr.data), sep='\n')

# def decode():
# 	stream = io.BytesIO(b'{"title":"iPhone 15 PRO MAX ULTRA", "content":"I dont cook I dont clean"}')
# 	data = JSONParser().parse(stream)
# 	serializer = ProductsSerializer(data=data)
# 	serializer.is_valid()
# 	print(serializer.validated_data)