# Generated by Django 4.0 on 2021-12-18 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_magic_cook_img3_magic_cook_img4_magic_cook_img5_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='magic_plus',
            name='img4',
            field=models.ImageField(default='', upload_to='images/product_image/chakki/detailpage/'),
        ),
        migrations.AddField(
            model_name='magic_plus',
            name='img5',
            field=models.ImageField(default='', upload_to='images/product_image/chakki/detailpage/'),
        ),
    ]
