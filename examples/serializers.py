from rest_framework import serializers
from .models import Ingredient, Recipe

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('url', 'id', 'name')

# class IngredientSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Ingredient

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)

        for ingredient in ingredients_data:
            ingredient, created = Ingredient.objects.get_or_create(name=ingredient['name'])
            recipe.ingredients.add(ingredient)
        return recipe

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.directions = validated_data['directions']

        for ingredient in ingredients_data:
            ingredient, created = Ingredient.objects.update_or_create(name=ingredient['name'])
            instance.ingredients.add(ingredient)
        return instance
