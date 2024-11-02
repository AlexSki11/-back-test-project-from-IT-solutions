from django import forms
from .models import Car, Comment
from rest_framework import serializers


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make','model','year','description']


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class CarSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'description']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']
        

