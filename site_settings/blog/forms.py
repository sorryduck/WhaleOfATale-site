from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', ]


class FeedbackForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['cat'] = 'empty'

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'content', ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'cols': 60,
                'rows': 10,
            },
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = ArticleCommentaries
        fields = ['username', 'text', 'article', ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'cols': 70,
                'rows': 3,
            },
            ),
            'article': forms.TextInput(attrs={'value': ' ',
                                              'type': 'hidden',
                                              }
                                       )
        }
