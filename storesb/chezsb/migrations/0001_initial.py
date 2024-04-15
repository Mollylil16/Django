# Generated by Django 5.0.4 on 2024-04-15 08:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('auteur', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='articles/')),
                ('est_approuve', models.BooleanField(default=False)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('commentaire', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('commentaire', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prix', models.FloatField()),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_commande', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chezsb.client')),
            ],
        ),
        migrations.CreateModel(
            name='AdresseLivraison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(max_length=200)),
                ('ville', models.CharField(max_length=200)),
                ('etat', models.CharField(max_length=200)),
                ('code_postal', models.CharField(max_length=200)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chezsb.client')),
                ('commande', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chezsb.commande')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleCommande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField(blank=True, default=0, null=True)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('commande', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chezsb.commande')),
                ('produit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chezsb.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('commentaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chezsb.comment')),
            ],
        ),
    ]
