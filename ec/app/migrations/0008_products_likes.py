# Generated by Django 4.1.7 on 2023-04-02 14:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_remove_cart_ordred_remove_cart_ordred_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='likes',
            field=models.ManyToManyField(related_name='prodect_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
