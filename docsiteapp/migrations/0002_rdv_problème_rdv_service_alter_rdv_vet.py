# Generated by Django 4.1.7 on 2023-04-02 14:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('docsiteapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rdv',
            name='Problème',
            field=models.CharField(default=django.utils.timezone.now, max_length=240),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rdv',
            name='Service',
            field=models.CharField(choices=[('', 'Choisissez un service'), ('1', 'Consultation'), ('2', 'Vaccinations'), ('3', 'Micropuçage'), ('4', 'Pension'), ('5', 'Soins Dentaires')], default="''", max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rdv',
            name='Vet',
            field=models.CharField(choices=[('', 'choisissez un vétérinaire'), ('1', 'Ameni Bil Haj'), ('2', 'Salma Daachoucha'), ('3', 'Mouhamed Ayed'), ('4', 'Mouhamed Ayed'), ('5', 'Slimen Simsim')], max_length=1),
        ),
    ]
