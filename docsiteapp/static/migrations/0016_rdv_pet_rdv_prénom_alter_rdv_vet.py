# Generated by Django 4.1.7 on 2023-04-12 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docsiteapp', '0015_alter_rdv_problème'),
    ]

    operations = [
        migrations.AddField(
            model_name='rdv',
            name='Pet',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rdv',
            name='Prénom',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rdv',
            name='Vet',
            field=models.CharField(choices=[('', 'choisissez un vétérinaire'), ('1', 'ines arfa'), ('2', 'sofiene el ali'), ('3', 'mariem ayed'), ('4', 'Rached hajar'), ('5', 'Ferdaws hanbouli'), ('6', 'Ranime el hkir'), ('7', 'saber bou hada'), ('8', ' ameni bil haj')], max_length=1),
        ),
    ]
