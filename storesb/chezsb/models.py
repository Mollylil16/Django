from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)


    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

 
    def __str__(self):
        return self.nom

    @property
    def url_image(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    date_commande = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

   

    def __str__(self):
        return str(self.id)

    @property
    def frais_livraison(self):
        frais_livraison = False
        articles_commande = self.articlecommande_set.all()
        for article in articles_commande:
            if not article.produit.digital:
                frais_livraison = True
                break
        return frais_livraison

    @property
    def total_panier(self):
        articles_commande = self.articlecommande_set.all()
        total = sum([article.get_total for article in articles_commande])
        return total

    @property
    def nombre_articles_panier(self):
        articles_commande = self.articlecommande_set.all()
        total = sum([article.quantite for article in articles_commande])
        return total

class ArticleCommande(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, null=True)
    commande = models.ForeignKey(Commande, on_delete=models.SET_NULL, null=True)
    quantite = models.IntegerField(default=0, null=True, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)


    @property
    def get_total(self):
        total = self.produit.prix * self.quantite
        return total

class AdresseLivraison(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    commande = models.ForeignKey(Commande, on_delete=models.SET_NULL, null=True)
    adresse = models.CharField(max_length=200, null=False)
    ville = models.CharField(max_length=200, null=False)
    etat = models.CharField(max_length=200, null=False)
    code_postal = models.CharField(max_length=200, null=False)
    date_ajout = models.DateTimeField(auto_now_add=True)

   

    def __str__(self):
        return self.adresse


class Comment(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    commentaire = models.TextField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return self.nom

class Reply(models.Model):
    nom = models.CharField(max_length=255)
    message = models.TextField()
    commentaire = models.ForeignKey(Comment, on_delete=models.CASCADE)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)

  

    def __str__(self):
        return self.nom

class Contact(models.Model):
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    commentaire = models.TextField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nom

class Article(models.Model):
    titre = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='articles/')

    est_approuve = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)

   

    def __str__(self):
        return self.titre

class Shoe(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
