from rest_framework import serializers
from .models import Ingredient, Recipe
from django.db import models

class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient

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
