# Generated by Django 4.0 on 2021-12-18 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_magic_plus_img4_magic_plus_img5'),
    ]

    operations = [
        migrations.AddField(
            model_name='magic_vc',
            name='img2',
            field=models.ImageField(default='', upload_to='images/product_image/chakki/detailpage/'),
        ),
        migrations.AddField(
            model_name='magic_vc',
            name='img3',
            field=models.ImageField(default='', upload_to='images/product_image/chakki/detailpage/'),
        ),
        migrations.AddField(
            model_name='magic_vc',
            name='img4',
            field=models.ImageField(default='', upload_to='images/product_image/chakki/detailpage/'),
        ),
        migrations.AddField(
            model_name='magic_vc',
            name='img5',
            field=models.ImageField(default='', upload_to='images/product_image/chakki/detailpage/'),
        ),
        migrations.AddField(
            model_name='smart_2hp',
            name='img2',
            field=models.ImageField(default='', upload_to='images/product_image/chakki/detailpage/'),
        ),
        migrations.AddField(
            model_name='smart_2hp',
            name='img3',
            field=models.ImageField(default='', upload_to='images/product_image/chakki/detailpage/'),
        ),
        migrations.AddField(
            model_name='smart_2hp',
            name='img4',
            field=models.ImageField(default='', upload_to='images/product_image/chakki/detailpage/'),
        ),
        migrations.AddField(
            model_name='smart_2hp',
            name='img5',
            field=models.ImageField(default='', upload_to='images/product_image/chakki/detailpage/'),
        ),
    ]
