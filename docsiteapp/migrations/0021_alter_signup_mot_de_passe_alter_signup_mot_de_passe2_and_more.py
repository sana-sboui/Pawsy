# Generated by Django 4.1.7 on 2023-04-18 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docsiteapp', '0020_signup_mot_de_passe2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='Mot_De_Passe',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='signup',
            name='Mot_De_Passe2',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='signup',
            name='Nom',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='signup',
            name='Nom_Utilisateur',
            field=models.CharField(default='', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='Prénom',
            field=models.CharField(default='', max_length=30),
        ),
    ]
