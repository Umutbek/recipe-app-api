from rest_framework import serializers

from core.models import Tag, Ingredient


class TagSerializer(serializers.ModelSerializer):
    """Serilizer for tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serilizer for ingredient objects"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)
