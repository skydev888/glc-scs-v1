from django.contrib.auth.forms import (
            AuthenticationForm
)


class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる



# 追加：ユーザー登録
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    last_name = forms.CharField(
        max_length=30,
        required=False,
        help_text='オプション',
        label='苗字'
    )
    first_name = forms.CharField(
        max_length=30,
        required=False,
        help_text='オプション',
        label='名前'
    )
    email = forms.EmailField(
        max_length=254,
        help_text='必須 有効なメールアドレスを入力してください。',
        label='Eメールアドレス'
    )

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name',  'email', 'password1', 'password2',)
