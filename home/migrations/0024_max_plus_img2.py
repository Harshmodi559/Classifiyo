# Generated by Django 4.0 on 2021-12-18 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_magic_vc_img2_magic_vc_img3_magic_vc_img4_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='max_plus',
            name='img2',
            field=models.ImageField(default='', upload_to='images/product_image/chakki/detailpage/'),
        ),
    ]