# Generated by Django 4.1.7 on 2023-04-02 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docsiteapp', '0006_alter_rdv_date_alter_rdv_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rdv',
            name='Date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='rdv',
            name='Time',
            field=models.DateTimeField(),
        ),
    ]
