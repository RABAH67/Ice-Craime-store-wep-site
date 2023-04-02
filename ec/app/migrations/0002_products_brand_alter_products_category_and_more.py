# Generated by Django 4.1.7 on 2023-03-28 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='brand',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(blank=True, choices=[('ML', 'Milk'), ('CD', 'Curd'), ('LS', 'Lessi'), ('MK', 'Milkchaik'), ('PN', 'Panner'), ('GH', 'Ghee'), ('IC', 'Ice-crime')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='composition',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='discoanted_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='discription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='prodap',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
        migrations.AlterField(
            model_name='products',
            name='selling_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
