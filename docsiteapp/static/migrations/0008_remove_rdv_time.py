# Generated by Django 4.1.7 on 2023-04-02 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docsiteapp', '0007_alter_rdv_date_alter_rdv_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rdv',
            name='Time',
        ),
    ]
