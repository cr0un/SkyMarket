from rest_framework import serializers
from ads.models import Ad, Comment


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою


class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'created_at']


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    author = serializers.StringRelatedField()

    class Meta:
        model = Ad
        fields = ['id', 'title', 'price', 'description', 'author', 'created_at']


class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    author = serializers.StringRelatedField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Ad
        fields = ['id', 'title', 'price', 'description', 'author', 'created_at', 'comments']
