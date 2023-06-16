# Generated by Django 4.1.7 on 2023-04-16 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docsiteapp', '0018_rename_prenom_rdv_prénom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=30)),
                ('Prénom', models.CharField(max_length=30)),
                ('Nom_Utilisateur', models.CharField(max_length=30, unique=True)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Mot_De_Passe', models.CharField(max_length=30)),
            ],
        ),
    ]