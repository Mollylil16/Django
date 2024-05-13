from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , SetPasswordForm , PasswordResetForm
from django.contrib.auth import get_user_model
from .models import Article, Commentaire, Product

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
        fields = ['titre', 'contenu']

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['auteur', 'contenu']

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Quantité')

class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(max_length=100, label='Adresse de livraison')

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']

class ContactForm(forms.Form):
    name = forms.CharField(label='Nom', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)