from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , SetPasswordForm , PasswordResetForm
from django.contrib.auth import get_user_model
from .models import Article

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='Une adresse e-mail valide, s\'il vous plaît.', required=False)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data.get('email')  
        if commit:
            user.save()

        return user
  
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur ou E-mail'}),
        label="Nom d'utilisateur ou E-mail*")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}))


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'auteur', 'description', 'image']
