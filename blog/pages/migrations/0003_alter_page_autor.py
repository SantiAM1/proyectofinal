# Generated by Django 4.2.7 on 2023-12-21 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='autor',
            field=models.CharField(max_length=60),
        ),
    ]