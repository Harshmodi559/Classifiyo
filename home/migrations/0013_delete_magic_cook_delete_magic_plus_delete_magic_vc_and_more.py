# Generated by Django 4.0 on 2021-12-13 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_magic_cook_magic_plus_max_plus_olive_olive_plus_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='magic_cook',
        ),
        migrations.DeleteModel(
            name='magic_plus',
        ),
        migrations.DeleteModel(
            name='magic_VC',
        ),
        migrations.DeleteModel(
            name='max_plus',
        ),
        migrations.DeleteModel(
            name='olive',
        ),
        migrations.DeleteModel(
            name='olive_plus',
        ),
        migrations.DeleteModel(
            name='olive_plus_SS',
        ),
        migrations.DeleteModel(
            name='super_star',
        ),
        migrations.AddField(
            model_name='super_star_plus',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
