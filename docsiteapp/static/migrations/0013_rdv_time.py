# Generated by Django 4.1.7 on 2023-04-02 22:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('docsiteapp', '0012_remove_rdv_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='rdv',
            name='Time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
