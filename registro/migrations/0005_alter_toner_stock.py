# Generated by Django 4.1.3 on 2022-12-21 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toner',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
