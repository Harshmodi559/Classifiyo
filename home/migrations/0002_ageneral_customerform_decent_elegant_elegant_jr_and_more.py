# Generated by Django 4.0 on 2021-12-12 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ageneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('name_img', models.ImageField(upload_to='images/product_image/ag/')),
                ('main_img', models.ImageField(upload_to='images/product_image/ag/')),
                ('Motor', models.CharField(max_length=200)),
                ('Pump', models.CharField(max_length=200)),
                ('Cooling_Area', models.CharField(max_length=200)),
                ('Air_Delivery', models.CharField(max_length=200)),
                ('Electrical', models.CharField(max_length=200)),
                ('Wattage', models.CharField(max_length=200)),
                ('Max_Current', models.CharField(max_length=200)),
                ('Exhaust_or_Kit', models.CharField(max_length=200)),
                ('Fan_Diameter', models.CharField(max_length=200)),
                ('Water_Capacity', models.CharField(max_length=200)),
                ('Cooling_Media', models.CharField(max_length=200)),
                ('Dimensions_of_Product', models.CharField(max_length=200)),
                ('Weight_of_Product', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='decent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('name_img', models.ImageField(upload_to='images/product_image/decent/')),
                ('main_img', models.ImageField(upload_to='images/product_image/decent/')),
                ('Motor', models.CharField(max_length=200)),
                ('Pump', models.CharField(max_length=200)),
                ('Cooling_Area', models.CharField(max_length=200)),
                ('Air_Delivery', models.CharField(max_length=200)),
                ('Electrical', models.CharField(max_length=200)),
                ('Wattage', models.CharField(max_length=200)),
                ('Max_Current', models.CharField(max_length=200)),
                ('Exhaust_or_Kit', models.CharField(max_length=200)),
                ('Fan_Diameter', models.CharField(max_length=200)),
                ('Water_Capacity', models.CharField(max_length=200)),
                ('Cooling_Media', models.CharField(max_length=200)),
                ('Dimensions_of_Product', models.CharField(max_length=200)),
                ('Weight_of_Product', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='elegant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('name_img', models.ImageField(upload_to='images/product_image/eleg/')),
                ('main_img', models.ImageField(upload_to='images/product_image/eleg/')),
                ('Motor', models.CharField(max_length=200)),
                ('Pump', models.CharField(max_length=200)),
                ('Cooling_Area', models.CharField(max_length=200)),
                ('Air_Delivery', models.CharField(max_length=200)),
                ('Electrical', models.CharField(max_length=200)),
                ('Wattage', models.CharField(max_length=200)),
                ('Max_Current', models.CharField(max_length=200)),
                ('Exhaust_or_Kit', models.CharField(max_length=200)),
                ('Fan_Diameter', models.CharField(max_length=200)),
                ('Water_Capacity', models.CharField(max_length=200)),
                ('Cooling_Media', models.CharField(max_length=200)),
                ('Dimensions_of_Product', models.CharField(max_length=200)),
                ('Weight_of_Product', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='elegant_jr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('name_img', models.ImageField(upload_to='images/product_image/elegant_jr/')),
                ('main_img', models.ImageField(upload_to='images/product_image/elegant_jr/')),
                ('Motor', models.CharField(max_length=200)),
                ('Pump', models.CharField(max_length=200)),
                ('Cooling_Area', models.CharField(max_length=200)),
                ('Air_Delivery', models.CharField(max_length=200)),
                ('Electrical', models.CharField(max_length=200)),
                ('Wattage', models.CharField(max_length=200)),
                ('Max_Current', models.CharField(max_length=200)),
                ('Exhaust_or_Kit', models.CharField(max_length=200)),
                ('Fan_Diameter', models.CharField(max_length=200)),
                ('Water_Capacity', models.CharField(max_length=200)),
                ('Cooling_Media', models.CharField(max_length=200)),
                ('Dimensions_of_Product', models.CharField(max_length=200)),
                ('Weight_of_Product', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='elegant_plus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('name_img', models.ImageField(upload_to='images/product_image/eleg_plus/')),
                ('main_img', models.ImageField(upload_to='images/product_image/eleg_plus/')),
                ('Motor', models.CharField(max_length=200)),
                ('Pump', models.CharField(max_length=200)),
                ('Cooling_Area', models.CharField(max_length=200)),
                ('Air_Delivery', models.CharField(max_length=200)),
                ('Electrical', models.CharField(max_length=200)),
                ('Wattage', models.CharField(max_length=200)),
                ('Max_Current', models.CharField(max_length=200)),
                ('Exhaust_or_Kit', models.CharField(max_length=200)),
                ('Fan_Diameter', models.CharField(max_length=200)),
                ('Water_Capacity', models.CharField(max_length=200)),
                ('Cooling_Media', models.CharField(max_length=200)),
                ('Dimensions_of_Product', models.CharField(max_length=200)),
                ('Weight_of_Product', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='freedom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('name_img', models.ImageField(upload_to='images/product_image/fr/')),
                ('main_img', models.ImageField(upload_to='images/product_image/fr/')),
                ('Motor', models.CharField(max_length=200)),
                ('Pump', models.CharField(max_length=200)),
                ('Cooling_Area', models.CharField(max_length=200)),
                ('Air_Delivery', models.CharField(max_length=200)),
                ('Electrical', models.CharField(max_length=200)),
                ('Wattage', models.CharField(max_length=200)),
                ('Max_Current', models.CharField(max_length=200)),
                ('Exhaust_or_Kit', models.CharField(max_length=200)),
                ('Fan_Diameter', models.CharField(max_length=200)),
                ('Water_Capacity', models.CharField(max_length=200)),
                ('Cooling_Media', models.CharField(max_length=200)),
                ('Dimensions_of_Product', models.CharField(max_length=200)),
                ('Weight_of_Product', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='freedom_jr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('name_img', models.ImageField(upload_to='images/product_image/fr_jr/')),
                ('main_img', models.ImageField(upload_to='images/product_image/fr_jr/')),
                ('Motor', models.CharField(max_length=200)),
                ('Pump', models.CharField(max_length=200)),
                ('Cooling_Area', models.CharField(max_length=200)),
                ('Air_Delivery', models.CharField(max_length=200)),
                ('Electrical', models.CharField(max_length=200)),
                ('Wattage', models.CharField(max_length=200)),
                ('Max_Current', models.CharField(max_length=200)),
                ('Exhaust_or_Kit', models.CharField(max_length=200)),
                ('Fan_Diameter', models.CharField(max_length=200)),
                ('Water_Capacity', models.CharField(max_length=200)),
                ('Cooling_Media', models.CharField(max_length=200)),
                ('Dimensions_of_Product', models.CharField(max_length=200)),
                ('Weight_of_Product', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='freedom_plus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('name_img', models.ImageField(upload_to='images/product_image/fr_plus/')),
                ('main_img', models.ImageField(upload_to='images/product_image/fr_plus/')),
                ('Motor', models.CharField(max_length=200)),
                ('Pump', models.CharField(max_length=200)),
                ('Cooling_Area', models.CharField(max_length=200)),
                ('Air_Delivery', models.CharField(max_length=200)),
                ('Electrical', models.CharField(max_length=200)),
                ('Wattage', models.CharField(max_length=200)),
                ('Max_Current', models.CharField(max_length=200)),
                ('Exhaust_or_Kit', models.CharField(max_length=200)),
                ('Fan_Diameter', models.CharField(max_length=200)),
                ('Water_Capacity', models.CharField(max_length=200)),
                ('Cooling_Media', models.CharField(max_length=200)),
                ('Dimensions_of_Product', models.CharField(max_length=200)),
                ('Weight_of_Product', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='freedom_storm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('name_img', models.ImageField(upload_to='images/product_image/fr_storm/')),
                ('main_img', models.ImageField(upload_to='images/product_image/fr_storm/')),
                ('Motor', models.CharField(max_length=200)),
                ('Pump', models.CharField(max_length=200)),
                ('Cooling_Area', models.CharField(max_length=200)),
                ('Air_Delivery', models.CharField(max_length=200)),
                ('Electrical', models.CharField(max_length=200)),
                ('Wattage', models.CharField(max_length=200)),
                ('Max_Current', models.CharField(max_length=200)),
                ('Exhaust_or_Kit', models.CharField(max_length=200)),
                ('Fan_Diameter', models.CharField(max_length=200)),
                ('Water_Capacity', models.CharField(max_length=200)),
                ('Cooling_Media', models.CharField(max_length=200)),
                ('Dimensions_of_Product', models.CharField(max_length=200)),
                ('Weight_of_Product', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='freedom_wind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('name_img', models.ImageField(upload_to='images/product_image/fr_wind/')),
                ('main_img', models.ImageField(upload_to='images/product_image/fr_wind/')),
                ('Motor', models.CharField(max_length=200)),
                ('Pump', models.CharField(max_length=200)),
                ('Cooling_Area', models.CharField(max_length=200)),
                ('Air_Delivery', models.CharField(max_length=200)),
                ('Electrical', models.CharField(max_length=200)),
                ('Wattage', models.CharField(max_length=200)),
                ('Max_Current', models.CharField(max_length=200)),
                ('Exhaust_or_Kit', models.CharField(max_length=200)),
                ('Fan_Diameter', models.CharField(max_length=200)),
                ('Water_Capacity', models.CharField(max_length=200)),
                ('Cooling_Media', models.CharField(max_length=200)),
                ('Dimensions_of_Product', models.CharField(max_length=200)),
                ('Weight_of_Product', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='rockstar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('name_img', models.ImageField(upload_to='images/product_image/rockstar/')),
                ('main_img', models.ImageField(upload_to='images/product_image/rockstar/')),
                ('Motor', models.CharField(max_length=200)),
                ('Pump', models.CharField(max_length=200)),
                ('Cooling_Area', models.CharField(max_length=200)),
                ('Air_Delivery', models.CharField(max_length=200)),
                ('Electrical', models.CharField(max_length=200)),
                ('Wattage', models.CharField(max_length=200)),
                ('Max_Current', models.CharField(max_length=200)),
                ('Exhaust_or_Kit', models.CharField(max_length=200)),
                ('Fan_Diameter', models.CharField(max_length=200)),
                ('Water_Capacity', models.CharField(max_length=200)),
                ('Cooling_Media', models.CharField(max_length=200)),
                ('Dimensions_of_Product', models.CharField(max_length=200)),
                ('Weight_of_Product', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='smart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('name_img', models.ImageField(upload_to='images/product_image/smart/')),
                ('main_img', models.ImageField(upload_to='images/product_image/smart/')),
                ('Motor', models.CharField(max_length=200)),
                ('Pump', models.CharField(max_length=200)),
                ('Cooling_Area', models.CharField(max_length=200)),
                ('Air_Delivery', models.CharField(max_length=200)),
                ('Electrical', models.CharField(max_length=200)),
                ('Wattage', models.CharField(max_length=200)),
                ('Max_Current', models.CharField(max_length=200)),
                ('Exhaust_or_Kit', models.CharField(max_length=200)),
                ('Fan_Diameter', models.CharField(max_length=200)),
                ('Water_Capacity', models.CharField(max_length=200)),
                ('Cooling_Media', models.CharField(max_length=200)),
                ('Dimensions_of_Product', models.CharField(max_length=200)),
                ('Weight_of_Product', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='add_items',
            new_name='category',
        ),
        migrations.CreateModel(
            name='RO_Spare_Parts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ro_img1', models.ImageField(upload_to='images/ro/')),
                ('category4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
        migrations.CreateModel(
            name='Residential_Coolers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('coolers_img1', models.ImageField(upload_to='images/coolers/')),
                ('category2_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
        migrations.CreateModel(
            name='PVC_Pipes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pvc_img1', models.ImageField(upload_to='images/pvc/')),
                ('category5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
        migrations.CreateModel(
            name='Industrial_Coolers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('coolers_img1', models.ImageField(upload_to='images/coolers/')),
                ('category2_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
        migrations.CreateModel(
            name='Electrical_Appliances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('appliances_img1', models.ImageField(upload_to='images/appliances/')),
                ('category3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
        migrations.CreateModel(
            name='Chakki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Chakki_img', models.ImageField(upload_to='images/chakki/')),
                ('category1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]