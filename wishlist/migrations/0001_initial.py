# Generated by Django 3.1.4 on 2020-12-19 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('products', '0002_auto_20201209_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile')),
                ('wished_products', models.ManyToManyField(related_name='userwishlists', to='products.Product')),
            ],
        ),
    ]
