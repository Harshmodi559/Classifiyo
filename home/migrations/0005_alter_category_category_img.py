# Generated by Django 4.0 on 2021-12-12 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_chakki_img_chakki_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_img',
            field=models.ImageField(upload_to='images/category/'),
        ),
    ]
