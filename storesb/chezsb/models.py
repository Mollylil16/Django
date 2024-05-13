from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    auteur = models.CharField(max_length=50)
    date_de_publication = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/', default='assets/img/')

    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    auteur = models.CharField(max_length=50)
    contenu = models.TextField()
    date_de_publication = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentaires')

    def __str__(self):
        return f"Commentaire de {self.auteur} sur {self.article.titre}"

class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)  # True for like, False for dislike
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['article', 'user']

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    quantity = models.PositiveIntegerField() 

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    # Autres champs selon vos besoins

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1) 

class ShippingZone(models.Model):
    name = models.CharField(max_length=100)
    # Autres champs selon vos besoins
