# Generated by Django 4.1.7 on 2023-05-06 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docsiteapp', '0031_contacter_signup_delete_contact_remove_rdv_prénom_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rdv',
            old_name='Prenom',
            new_name='Prénom',
        ),
    ]
