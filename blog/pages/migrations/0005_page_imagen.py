# Generated by Django 4.2.7 on 2023-12-22 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_remove_page_autor_page__autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='static/assets/img/'),
        ),
    ]
