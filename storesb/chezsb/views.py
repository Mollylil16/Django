from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate
from .forms import UserLoginForm, UserRegistrationForm, ArticleForm, CommentaireForm, ContactForm
from .models import *
from django.http import JsonResponse  



def acceuil(request):
    articles = Article.objects.all()
    datas = {'articles': articles}
    return render(request, 'blog/acceuil.html', datas)

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return redirect('acceuil')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="utilisateur/register.html",
        context={"form": form}
    )

@login_required

def custom_logout(request):
    logout(request)
    messages.info(request, "Déconnexion réussie!")
    return redirect("acceuil")

def custom_login(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user) 
                messages.success(request, f"Bonjour <b>{user.username}</b>! Vous êtes connecté.")
                return redirect("acceuil")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "Vous devez passer le test reCAPTCHA.")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="blog/acceuil.html",
        context={"form": form}
    )



def liste_articles(request):
    articles = Article.objects.all()
    return render(request, 'liste_articles.html', {'articles': articles})

def detail_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    commentaires = article.commentaires.all()
    return render(request, 'detail_article.html', {'article': article, 'commentaires': commentaires})


def like_article(request, article_id):
    if request.method == 'POST':
        article = Article.objects.get(pk=article_id)
        user = request.user
        # Vérifier si l'utilisateur a déjà liké/disliké l'article
        like, created = Like.objects.get_or_create(article=article, user=user)
        if created:
            # Si l'utilisateur n'a pas encore liké/disliké l'article, enregistrer son choix
            like.is_like = True
            like.save()
    return redirect('detail_article', article_id=article_id)

def dislike_article(request, article_id):
    if request.method == 'POST':
        article = Article.objects.get(pk=article_id)
        user = request.user
        # Vérifier si l'utilisateur a déjà liké/disliké l'article
        like, created = Like.objects.get_or_create(article=article, user=user)
        if created:
            # Si l'utilisateur n'a pas encore liké/disliké l'article, enregistrer son choix
            like.is_like = False
            like.save()
    return redirect('detail_article', article_id=article_id)

def get_like_status(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    liked = False
    if request.user.is_authenticated:
        liked = Like.objects.filter(article=article, user=request.user).exists()
    return JsonResponse({'liked': liked})

def publier_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.auteur = request.user  # Assurez-vous d'ajouter l'auteur de l'article
            article.save()
            return redirect('liste_articles')
    else:
        form = ArticleForm()
    return render(request, 'publier_article.html', {'form': form})

def commenter_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.article = article
            commentaire.save()
            return redirect('detail_article', article_id=article_id)
    else:
        form = CommentaireForm()
    return render(request, 'commenter_article.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, is_ordered=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    order_item.quantity += 1
    order_item.save()
    return redirect('product_list')

def view_cart(request):
    order = Order.objects.get(user=request.user, is_ordered=False)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'cart.html', {'order': order, 'order_items': order_items})
def checkout(request):
    order = Order.objects.get(user=request.user, is_ordered=False)
    order_items = OrderItem.objects.filter(order=order)
    # Logique pour afficher les détails de la commande et le formulaire de paiement
    return render(request, 'checkout.html', {'order': order, 'order_items': order_items})

def process_order(request):
    order = Order.objects.get(user=request.user, is_ordered=False)
    # Logique pour traiter la commande et effectuer le paiement
    order.is_ordered = True
    order.save()
    # Redirection vers une page de confirmation de commande
    return redirect('order_confirmation')

def order_confirmation(request):
    # Logique pour afficher la page de confirmation de commande
    return render(request, 'order_confirmation.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Traitement du formulaire de contact ici
            # Par exemple, envoyer un e-mail
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def privacy_policy_view(request):
    return render(request, 'privacy_policy.html')

def terms_of_use_view(request):
    return render(request, 'terms_of_use.html')

def presentation_view(request):
    return render(request, 'presentation.html')

def cookies_banner_view(request):
    return render(request, 'cookies_banner.html')

def catalogue(request):
    articles = Article.objects.all()  # Récupérez tous les produits depuis la base de données
    return render(request, 'blog/catalogue.html', {'article': articles})

def create_annonce(request):
    # Votre logique de vue pour créer une annonce
    return render(request, 'votre_template.html')
