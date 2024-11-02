from django import forms
from .models import Car, Comment

class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make','model','year','description']


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        