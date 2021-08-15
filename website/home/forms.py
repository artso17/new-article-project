from django import forms
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model


class RegisterForm(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email Address')
    password1 = forms.CharField(
        label='New Password', widget=forms.PasswordInput())
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput())

    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     print(username)
    #     qs = User.objects.filter(username=username)
    #     if qs.exists():
    #         raise forms.ValidationError(
    #             'The username is already Picked, please pick another.')

    #     return username

    def clean_password1(self):
        lower = 'abcdefghijklmnopqrstu'
        upper = lower.upper()
        password1 = self.cleaned_data.get("password1")
        ucase = 0
        lcase = 0
        # for i in password1:
        #     if i in upper:
        #         ucase += 1
        #     elif i in lower:
        #         lcase += 1
        # if ucase == 0 or lcase == 0:
        #     raise forms.ValidationError(
        #         'The password should contain at least 1 uppercase and 1 lowercase')
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get("password2")
        return password2

    # def password_match(self):


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
