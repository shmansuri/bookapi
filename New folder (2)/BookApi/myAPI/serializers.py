from rest_framework import serializers
from django.db.models import fields
from .models import BookModel

class Bookserializers(serializers.Serializer):
    class Meta:
        model = BookModel
        fields = { 'id', 'title', 'Author','desc','cover_img',  'rating'}
    

    def create(self, validated_data):
        return BookModel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.Author = validated_data.get('Author', instance.Author)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.cover_img = validated_data('cover_img', instance.cover_img)
        return instance