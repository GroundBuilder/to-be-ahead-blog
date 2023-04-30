from .models import Comment   #, Profile
from django import forms
# from django.contrib.auth.models import User # New
# from django.contrib.auth.forms import UserCreationForm # New


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

# New below
# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     # Configuration
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']