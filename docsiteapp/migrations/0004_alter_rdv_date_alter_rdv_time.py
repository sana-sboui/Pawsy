# Generated by Django 4.1.7 on 2023-04-02 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docsiteapp', '0003_rdv_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rdv',
            name='Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rdv',
            name='Time',
            field=models.TimeField(),
        ),
    ]
