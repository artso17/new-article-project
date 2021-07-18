from django import forms
from .models import *
from django.contrib.auth.models import User, Group


class GroupForm(forms.ModelForm):
    """Form definition for Group."""

    class Meta:
        """Meta definition for Groupform."""

        model = Group
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'permissions': forms.CheckboxSelectMultiple()
        }


class UserForm(forms.ModelForm):
    """Form definition for User."""

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'last_login', 'date_joined', 'groups', 'is_active']
        exclude = ['password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'True'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}),
            'last_login': forms.DateInput(attrs={'class': 'form-control', 'readonly': 'True'}),
            'groups': forms.CheckboxSelectMultiple(),
            'date_joined': forms.DateInput(attrs={'class': 'form-control', 'readonly': 'True'})
        }


class CategoryForm(forms.ModelForm):
    """Form definition for Category."""

    class Meta:
        """Meta definition for Categoryform."""

        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class ArticleForm(forms.ModelForm):
    """Form definition for Article."""

    class Meta:
        """Meta definition for Articleform."""

        model = Article
        exclude = ['likes']
        fields = '__all__'

        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'hidden',
                # 'readonly': 'True'
            }
            ),
            'category': forms.CheckboxSelectMultiple(),
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
