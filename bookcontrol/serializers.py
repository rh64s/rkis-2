from rest_framework import serializers
from .models import Book, Category, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=100)
    authors = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), many=True
    )
    year = serializers.IntegerField(required=True, min_value=1000, max_value=9999)
    publisher = serializers.CharField(required=True, max_length=100)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    genre = serializers.CharField(required=True, max_length=100)
    image = serializers.ImageField(use_url=True, required=True)
    text = serializers.HyperlinkedIdentityField(view_name='book-text')

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.authors = validated_data.get('authors', instance.authors)
        instance.year = validated_data.get('year', instance.year)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.category = validated_data.get('category', instance.category)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.image = validated_data.get('image', instance.image)
        instance.text = validated_data.get('text', instance.text)
        instance.save()

    class Meta:
        model = Book