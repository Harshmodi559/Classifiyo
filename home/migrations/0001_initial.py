# Generated by Django 3.1.4 on 2021-12-04 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_cust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('dop', models.DateField(max_length=14)),
                ('p_name', models.CharField(max_length=50)),
                ('p_desc', models.CharField(max_length=50)),
                ('bill', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='add_items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category_img', models.ImageField(upload_to='images/category/')),
            ],
        ),
    ]
