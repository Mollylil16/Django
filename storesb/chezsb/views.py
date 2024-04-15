from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate
from .forms import UserLoginForm, UserRegistrationForm
from .models import *  

# Vos vues

def accueil(request):
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
            return redirect('login')

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
    return redirect("index")

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
                return redirect("index")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "Vous devez passer le test reCAPTCHA.")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="utilisateur/login.html",
        context={"form": form}
    )



def barre_de_navigation(request):
    datas = {}
    return render(request, 'barre_de_navigation.html', datas)

def en_tete(request):
    datas = {}
    return render(request, 'en_tete.html', datas)

def catalogue(request):
    articles = Article.objects.filter(est_approuve=True)
    datas = {'articles': articles}
    return render(request, 'blog/catalogue.html', datas)

def shoe(request, id):
    article = Article.objects.get(id=id)
    comments = Comment.objects.all()
    replys = Reply.objects.all()
    datas = {'article': article, 'comments': comments, 'replys': replys}

    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        commentaire = request.POST.get('commentaire')
        if nom and email and commentaire:
            c = Comment(nom=nom, email=email, commentaire=commentaire)
            c.save()
            
    return render(request, 'blog/shoe.html', datas)

def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        commentaire = request.POST.get('sujet')
        
        contact = Contact()
        contact.nom = nom
        contact.email = email
        contact.commentaire = commentaire
        contact.save()
        
    return render(request, 'utilisateur/contact.html')

def creer_actualite(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        auteur = request.POST.get('auteur')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        actualite = Article()
        actualite.titre = titre
        actualite.auteur = auteur
        actualite.description = description
        actualite.image = image
        actualite.save()

        return redirect('catalogue')

    return render(request, 'blog/annonce.html')

@login_required
@permission_required('blog.change_article', raise_exception=True)
def annonce(request):
    articles = Article.objects.all()
    return render(request, 'blog/annonce.html', {'articles': articles})

@login_required
@permission_required('blog.change_article', raise_exception=True)
def approuver_actualite(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.est_approuve = True
    article.save()
    return redirect('annonce')

@login_required
@permission_required('blog.delete_article', raise_exception=True)
def supprimer_actualite(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('annonce')


