from django.db import models
from django.db.models.deletion import CASCADE
from django import forms

# Create your models here.


class add_cust(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    dop = models.DateField(max_length=14)
    cust_id = models.AutoField
    p_name = models.CharField(max_length=50)
    p_desc = models.CharField(max_length=50)
    bill = models.IntegerField()

    # def __str__(self):
    # return self.name

class category(models.Model):
    name = models.CharField(max_length=100)
    category_img = models.ImageField(upload_to='images/category/')

    def __str__(self):
        return self.name

#categories

class Chakki(models.Model):
    category1 = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    Chakki_img = models.ImageField(upload_to='images/chakki/')

    def __str__(self):
        return self.name

class Residential_Coolers(models.Model):
    category2 = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="")
    coolers_img = models.ImageField(upload_to='images/coolers/')

    def __str__(self):
        return self.name

class Industrial_Coolers(models.Model):
    category3 = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="")
    coolers_img = models.ImageField(upload_to='images/coolers/')

    def __str__(self):
        return self.name

class Electrical_Appliances(models.Model):
    category4 = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    appliances_img = models.ImageField(upload_to='images/appliances/')

    def __str__(self):
        return self.name

class RO_Spare_Parts(models.Model):
    category5 = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ro_img = models.ImageField(upload_to='images/ro/')

    def __str__(self):
        return self.name

class PVC_Pipes(models.Model):
    category6 = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pvc_img = models.ImageField(upload_to='images/pvc/')

    def __str__(self):
        return self.name

class Tubs(models.Model):
    category7 = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    size1=models.CharField(max_length=100)
    capacity1=models.CharField(max_length=100)
    size2=models.CharField(max_length=100)
    capacity2=models.CharField(max_length=100)
    size3=models.CharField(max_length=100)
    capacity3=models.CharField(max_length=100)
    size4=models.CharField(max_length=100)
    capacity4=models.CharField(max_length=100)
    size5=models.CharField(max_length=100)
    capacity5=models.CharField(max_length=100)
    
    tubs_img = models.ImageField(upload_to='images/tubs/')
    
    def __str__(self):
        return self.name



class CustomerForm(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_number = models.IntegerField()
    customer_problem = models.CharField(max_length=2000, default="")

    def __str__(self):
        return self.customer_name



# chakki grinding capacity
class grinding(models.Model):
    inherit=models.ForeignKey(category, on_delete=models.CASCADE)
    img=models.ImageField(upload_to="image/chakki/")
    name=models.CharField(max_length=40)
    capacity=models.CharField(max_length=20)

    def __str__(self):
        return self.name



# Cooler Products Model

class smart(models.Model):
    text = models.CharField(max_length=2000)
    name_img = models.ImageField(upload_to='images/product_image/smart/')
    main_img = models.ImageField(upload_to='images/product_image/smart/')

    Motor = models.CharField(max_length=200)
    Pump = models.CharField(max_length=200)
    Cooling_Area = models.CharField(max_length=200)
    Air_Delivery = models.CharField(max_length=200)
    Electrical = models.CharField(max_length=200)
    Wattage = models.CharField(max_length=200)
    Max_Current = models.CharField(max_length=200)
    Exhaust_or_Kit = models.CharField(max_length=200)
    Fan_Diameter = models.CharField(max_length=200)
    Water_Capacity = models.CharField(max_length=200)
    Cooling_Media = models.CharField(max_length=200)
    Dimensions_of_Product = models.CharField(max_length=200)
    Weight_of_Product = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.name

class rockstar(models.Model):
    text = models.CharField(max_length=2000)
    name_img = models.ImageField(upload_to='images/product_image/rockstar/')
    main_img = models.ImageField(upload_to='images/product_image/rockstar/')
    Motor = models.CharField(max_length=200)
    Pump = models.CharField(max_length=200)
    Cooling_Area = models.CharField(max_length=200)
    Air_Delivery = models.CharField(max_length=200)
    Electrical = models.CharField(max_length=200)
    Wattage = models.CharField(max_length=200)
    Max_Current = models.CharField(max_length=200)
    Exhaust_or_Kit = models.CharField(max_length=200)
    Fan_Diameter = models.CharField(max_length=200)
    Water_Capacity = models.CharField(max_length=200)
    Cooling_Media = models.CharField(max_length=200)
    Dimensions_of_Product = models.CharField(max_length=200)
    Weight_of_Product = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.name

class ageneral(models.Model):
    text = models.CharField(max_length=2000)
    name_img = models.ImageField(upload_to='images/product_image/ag/')
    main_img = models.ImageField(upload_to='images/product_image/ag/')
    Motor = models.CharField(max_length=200)
    Pump = models.CharField(max_length=200)
    Cooling_Area = models.CharField(max_length=200)
    Air_Delivery = models.CharField(max_length=200)
    Electrical = models.CharField(max_length=200)
    Wattage = models.CharField(max_length=200)
    Max_Current = models.CharField(max_length=200)
    Exhaust_or_Kit = models.CharField(max_length=200)
    Fan_Diameter = models.CharField(max_length=200)
    Water_Capacity = models.CharField(max_length=200)
    Cooling_Media = models.CharField(max_length=200)
    Dimensions_of_Product = models.CharField(max_length=200)
    Weight_of_Product = models.CharField(max_length=200)

    # def __str__(self):
    # return self.name

class freedom(models.Model):
    text = models.CharField(max_length=2000)
    name_img = models.ImageField(upload_to='images/product_image/fr/')
    main_img = models.ImageField(upload_to='images/product_image/fr/')
    Motor = models.CharField(max_length=200)
    Pump = models.CharField(max_length=200)
    Cooling_Area = models.CharField(max_length=200)
    Air_Delivery = models.CharField(max_length=200)
    Electrical = models.CharField(max_length=200)
    Wattage = models.CharField(max_length=200)
    Max_Current = models.CharField(max_length=200)
    Exhaust_or_Kit = models.CharField(max_length=200)
    Fan_Diameter = models.CharField(max_length=200)
    Water_Capacity = models.CharField(max_length=200)
    Cooling_Media = models.CharField(max_length=200)
    Dimensions_of_Product = models.CharField(max_length=200)
    Weight_of_Product = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.name

class freedom_plus(models.Model):
    text = models.CharField(max_length=2000)
    name_img = models.ImageField(upload_to='images/product_image/fr_plus/')
    main_img = models.ImageField(upload_to='images/product_image/fr_plus/')
    Motor = models.CharField(max_length=200)
    Pump = models.CharField(max_length=200)
    Cooling_Area = models.CharField(max_length=200)
    Air_Delivery = models.CharField(max_length=200)
    Electrical = models.CharField(max_length=200)
    Wattage = models.CharField(max_length=200)
    Max_Current = models.CharField(max_length=200)
    Exhaust_or_Kit = models.CharField(max_length=200)
    Fan_Diameter = models.CharField(max_length=200)
    Water_Capacity = models.CharField(max_length=200)
    Cooling_Media = models.CharField(max_length=200)
    Dimensions_of_Product = models.CharField(max_length=200)
    Weight_of_Product = models.CharField(max_length=200)

    # def __str__(self):
    # return self.name

class freedom_jr(models.Model):
    text = models.CharField(max_length=2000)
    name_img = models.ImageField(upload_to='images/product_image/fr_jr/')
    main_img = models.ImageField(upload_to='images/product_image/fr_jr/')
    Motor = models.CharField(max_length=200)
    Pump = models.CharField(max_length=200)
    Cooling_Area = models.CharField(max_length=200)
    Air_Delivery = models.CharField(max_length=200)
    Electrical = models.CharField(max_length=200)
    Wattage = models.CharField(max_length=200)
    Max_Current = models.CharField(max_length=200)
    Exhaust_or_Kit = models.CharField(max_length=200)
    Fan_Diameter = models.CharField(max_length=200)
    Water_Capacity = models.CharField(max_length=200)
    Cooling_Media = models.CharField(max_length=200)
    Dimensions_of_Product = models.CharField(max_length=200)
    Weight_of_Product = models.CharField(max_length=200)

    # def __str__(self):
    # return self.name

class freedom_wind(models.Model):
    text = models.CharField(max_length=2000)
    name_img = models.ImageField(upload_to='images/product_image/fr_wind/')
    main_img = models.ImageField(upload_to='images/product_image/fr_wind/')
    Motor = models.CharField(max_length=200)
    Pump = models.CharField(max_length=200)
    Cooling_Area = models.CharField(max_length=200)
    Air_Delivery = models.CharField(max_length=200)
    Electrical = models.CharField(max_length=200)
    Wattage = models.CharField(max_length=200)
    Max_Current = models.CharField(max_length=200)
    Exhaust_or_Kit = models.CharField(max_length=200)
    Fan_Diameter = models.CharField(max_length=200)
    Water_Capacity = models.CharField(max_length=200)
    Cooling_Media = models.CharField(max_length=200)
    Dimensions_of_Product = models.CharField(max_length=200)
    Weight_of_Product = models.CharField(max_length=200)

    # def __str__(self):
    # return self.name

class freedom_storm(models.Model):
    text = models.CharField(max_length=2000)
    name_img = models.ImageField(upload_to='images/product_image/fr_storm/')
    main_img = models.ImageField(upload_to='images/product_image/fr_storm/')
    Motor = models.CharField(max_length=200)
    Pump = models.CharField(max_length=200)
    Cooling_Area = models.CharField(max_length=200)
    Air_Delivery = models.CharField(max_length=200)
    Electrical = models.CharField(max_length=200)
    Wattage = models.CharField(max_length=200)
    Max_Current = models.CharField(max_length=200)
    Exhaust_or_Kit = models.CharField(max_length=200)
    Fan_Diameter = models.CharField(max_length=200)
    Water_Capacity = models.CharField(max_length=200)
    Cooling_Media = models.CharField(max_length=200)
    Dimensions_of_Product = models.CharField(max_length=200)
    Weight_of_Product = models.CharField(max_length=200)

    # def __str__(self):
    # return self.name

class elegant(models.Model):
    text = models.CharField(max_length=2000)
    name_img = models.ImageField(upload_to='images/product_image/eleg/')
    main_img = models.ImageField(upload_to='images/product_image/eleg/')
    Motor = models.CharField(max_length=200)
    Pump = models.CharField(max_length=200)
    Cooling_Area = models.CharField(max_length=200)
    Air_Delivery = models.CharField(max_length=200)
    Electrical = models.CharField(max_length=200)
    Wattage = models.CharField(max_length=200)
    Max_Current = models.CharField(max_length=200)
    Exhaust_or_Kit = models.CharField(max_length=200)
    Fan_Diameter = models.CharField(max_length=200)
    Water_Capacity = models.CharField(max_length=200)
    Cooling_Media = models.CharField(max_length=200)
    Dimensions_of_Product = models.CharField(max_length=200)
    Weight_of_Product = models.CharField(max_length=200)

    # def __str__(self):
    # return self.name

class elegant_plus(models.Model):
    text = models.CharField(max_length=2000)
    name_img = models.ImageField(upload_to='images/product_image/eleg_plus/')
    main_img = models.ImageField(upload_to='images/product_image/eleg_plus/')
    Motor = models.CharField(max_length=200)
    Pump = models.CharField(max_length=200)
    Cooling_Area = models.CharField(max_length=200)
    Air_Delivery = models.CharField(max_length=200)
    Electrical = models.CharField(max_length=200)
    Wattage = models.CharField(max_length=200)
    Max_Current = models.CharField(max_length=200)
    Exhaust_or_Kit = models.CharField(max_length=200)
    Fan_Diameter = models.CharField(max_length=200)
    Water_Capacity = models.CharField(max_length=200)
    Cooling_Media = models.CharField(max_length=200)
    Dimensions_of_Product = models.CharField(max_length=200)
    Weight_of_Product = models.CharField(max_length=200)

    # def __str__(self):
    # return self.name

class elegant_jr(models.Model):
    text = models.CharField(max_length=2000)
    name_img = models.ImageField(upload_to='images/product_image/elegant_jr/')
    main_img = models.ImageField(upload_to='images/product_image/elegant_jr/')
    Motor = models.CharField(max_length=200)
    Pump = models.CharField(max_length=200)
    Cooling_Area = models.CharField(max_length=200)
    Air_Delivery = models.CharField(max_length=200)
    Electrical = models.CharField(max_length=200)
    Wattage = models.CharField(max_length=200)
    Max_Current = models.CharField(max_length=200)
    Exhaust_or_Kit = models.CharField(max_length=200)
    Fan_Diameter = models.CharField(max_length=200)
    Water_Capacity = models.CharField(max_length=200)
    Cooling_Media = models.CharField(max_length=200)
    Dimensions_of_Product = models.CharField(max_length=200)
    Weight_of_Product = models.CharField(max_length=200)

    # def __str__(self):
    # return self.name

class decent(models.Model):
    text = models.CharField(max_length=2000)
    name_img = models.ImageField(upload_to='images/product_image/decent/')
    main_img = models.ImageField(upload_to='images/product_image/decent/')
    Motor = models.CharField(max_length=200)
    Pump = models.CharField(max_length=200)
    Cooling_Area = models.CharField(max_length=200)
    Air_Delivery = models.CharField(max_length=200)
    Electrical = models.CharField(max_length=200)
    Wattage = models.CharField(max_length=200)
    Max_Current = models.CharField(max_length=200)
    Exhaust_or_Kit = models.CharField(max_length=200)
    Fan_Diameter = models.CharField(max_length=200)
    Water_Capacity = models.CharField(max_length=200)
    Cooling_Media = models.CharField(max_length=200)
    Dimensions_of_Product = models.CharField(max_length=200)
    Weight_of_Product = models.CharField(max_length=200)

    # def __str__(self):
    # return self.name


# chakki products

class olive(models.Model):
    name = models.CharField(max_length=100, default="")
    img = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img2 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img3 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img4 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img5 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    capacity = models.CharField(max_length=500, default="")
    p1 = models.CharField(max_length=300, default="")
    p2 = models.CharField(max_length=300, default="")
    p3 = models.CharField(max_length=300, default="")
    p4 = models.CharField(max_length=300, default="")
    p5 = models.CharField(max_length=300, default="")
    p6 = models.CharField(max_length=300, default="")
    p7 = models.CharField(max_length=300, default="")
    p8 = models.CharField(max_length=300, default="")
    gurantee = models.CharField(max_length=300, default="")
    design = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.name

class olive_plus(models.Model):
    name = models.CharField(max_length=100, default="")
    img = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/')
    img2 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img3 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img4 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img5 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    capacity = models.CharField(max_length=500)
    p1 = models.CharField(max_length=300)
    p2 = models.CharField(max_length=300)
    p3 = models.CharField(max_length=300)
    p4 = models.CharField(max_length=300)
    p5 = models.CharField(max_length=300)
    p6 = models.CharField(max_length=300)
    p7 = models.CharField(max_length=300)
    p8 = models.CharField(max_length=300)
    gurantee = models.CharField(max_length=300)
    design = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class olive_plus_SS(models.Model):
    name = models.CharField(max_length=100, default="")
    img = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/')
    img2 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img3 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img4 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img5 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    capacity = models.CharField(max_length=500)
    p1 = models.CharField(max_length=300)
    p2 = models.CharField(max_length=300)
    p3 = models.CharField(max_length=300)
    p4 = models.CharField(max_length=300)
    p5 = models.CharField(max_length=300)
    p6 = models.CharField(max_length=300)
    p7 = models.CharField(max_length=300)
    p8 = models.CharField(max_length=300)
    gurantee = models.CharField(max_length=300)
    design = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class max_plus(models.Model):
    name = models.CharField(max_length=100, default="")
    img = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/')
    img2 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img3 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img4 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img5 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    capacity = models.CharField(max_length=500)
    p1 = models.CharField(max_length=300)
    p2 = models.CharField(max_length=300)
    p3 = models.CharField(max_length=300)
    p4 = models.CharField(max_length=300)
    p5 = models.CharField(max_length=300)
    p6 = models.CharField(max_length=300)
    p7 = models.CharField(max_length=300)
    p8 = models.CharField(max_length=300)
    gurantee = models.CharField(max_length=300)
    design = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class super_star_plus(models.Model):
    name = models.CharField(max_length=100, default="")
    img = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/')
    img2 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img3 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img4 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img5 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    capacity = models.CharField(max_length=500)
    p1 = models.CharField(max_length=300)
    p2 = models.CharField(max_length=300)
    p3 = models.CharField(max_length=300)
    p4 = models.CharField(max_length=300)
    p5 = models.CharField(max_length=300)
    p6 = models.CharField(max_length=300)
    p7 = models.CharField(max_length=300)
    p8 = models.CharField(max_length=300)
    p9 = models.CharField(max_length=300)
    p10 = models.CharField(max_length=300)
    p11 = models.CharField(max_length=300)
    p12 = models.CharField(max_length=300)
    gurantee = models.CharField(max_length=300)
    design = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class magic_plus(models.Model):
    name = models.CharField(max_length=100, default="")
    img = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/')
    img2 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img3 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img4 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img5 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")

    capacity = models.CharField(max_length=500)
    p1 = models.CharField(max_length=300)
    p2 = models.CharField(max_length=300)
    p3 = models.CharField(max_length=300)
    p4 = models.CharField(max_length=300)
    p5 = models.CharField(max_length=300)
    p6 = models.CharField(max_length=300)
    p7 = models.CharField(max_length=300)
    p8 = models.CharField(max_length=300)
    p9 = models.CharField(max_length=300)
    p10 = models.CharField(max_length=300)
    p11 = models.CharField(max_length=300)
    p12 = models.CharField(max_length=300)
    gurantee = models.CharField(max_length=300)
    design = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class magic_cook(models.Model):
    name = models.CharField(max_length=100, default="")
    img = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/')
    img2 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img3 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img4 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img5 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    capacity = models.CharField(max_length=500)
    p1 = models.CharField(max_length=300)
    p2 = models.CharField(max_length=300)
    p3 = models.CharField(max_length=300)
    p4 = models.CharField(max_length=300)
    p5 = models.CharField(max_length=300)
    p6 = models.CharField(max_length=300)
    p7 = models.CharField(max_length=300)
    p8 = models.CharField(max_length=300)
    p9 = models.CharField(max_length=300)
    p10 = models.CharField(max_length=300)
    p11 = models.CharField(max_length=300)
    p12 = models.CharField(max_length=300)
    gurantee = models.CharField(max_length=300)
    design = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class super_star(models.Model):
    name = models.CharField(max_length=100, default="")
    img = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/')
    img2 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img3 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img4 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img5 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    capacity = models.CharField(max_length=500)
    p1 = models.CharField(max_length=300)
    p2 = models.CharField(max_length=300)
    p3 = models.CharField(max_length=300)
    p4 = models.CharField(max_length=300)
    p5 = models.CharField(max_length=300)
    p6 = models.CharField(max_length=300)
    p7 = models.CharField(max_length=300)
    p8 = models.CharField(max_length=300)
    p9 = models.CharField(max_length=300)
    p10 = models.CharField(max_length=300)
    p11 = models.CharField(max_length=300)
    p12 = models.CharField(max_length=300)
    gurantee = models.CharField(max_length=300)
    design = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class magic_VC(models.Model):
    name = models.CharField(max_length=100, default="")
    img = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/')
    img2 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img3 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img4 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img5 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    capacity = models.CharField(max_length=500)
    p1 = models.CharField(max_length=300)
    p2 = models.CharField(max_length=300)
    p3 = models.CharField(max_length=300)
    p4 = models.CharField(max_length=300)
    p5 = models.CharField(max_length=300)
    p6 = models.CharField(max_length=300)
    p7 = models.CharField(max_length=300)
    p8 = models.CharField(max_length=300)
    p9 = models.CharField(max_length=300)
    p10 = models.CharField(max_length=300)
    p11 = models.CharField(max_length=300)
    p12 = models.CharField(max_length=300)
    gurantee = models.CharField(max_length=300)
    design = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class smart_2hp(models.Model):
    name = models.CharField(max_length=100, default="")
    img = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/')
    img2 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img3 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img4 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    img5 = models.ImageField(
        upload_to='images/product_image/chakki/detailpage/', default="")
    capacity = models.CharField(max_length=500)
    p1 = models.CharField(max_length=300)
    p2 = models.CharField(max_length=300)
    p3 = models.CharField(max_length=300)
    p4 = models.CharField(max_length=300)
    p5 = models.CharField(max_length=300)
    p6 = models.CharField(max_length=300)
    p7 = models.CharField(max_length=300)
    gurantee = models.CharField(max_length=300)

    design = models.CharField(max_length=300)

    def __str__(self):
        return self.name


# electrical

class heater(models.Model):
    modelname = models.CharField(max_length=100)
    img = models.ImageField(
        upload_to='images/product_image/electric/detailpage/')
    gurantee = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    p3 = models.CharField(max_length=100)
    p4 = models.CharField(max_length=100)

class Gasgeyser(models.Model):
    modelname = models.CharField(max_length=100)
    img = models.ImageField(
        upload_to='images/product_image/electric/detailpage/')
    gurantee = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    p3 = models.CharField(max_length=100)
    p4 = models.CharField(max_length=100)
    p5 = models.CharField(max_length=100)

class iron(models.Model):
    modelname = models.CharField(max_length=100)
    img = models.ImageField(
        upload_to='images/product_image/electric/detailpage/')
    gurantee = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    p3 = models.CharField(max_length=100)
    p4 = models.CharField(max_length=100)

class kettle(models.Model):
    modelname = models.CharField(max_length=100)
    img = models.ImageField(
        upload_to='images/product_image/electric/detailpage/')
    gurantee = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    p3 = models.CharField(max_length=100)
    p4 = models.CharField(max_length=100)

class rod(models.Model):
    modelname = models.CharField(max_length=100)
    img = models.ImageField(
        upload_to='images/product_image/electric/detailpage/')
    gurantee = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    p3 = models.CharField(max_length=100)
    p4 = models.CharField(max_length=100)

class ceiling_fan(models.Model):
    modelname = models.CharField(max_length=100)
    img = models.ImageField(
        upload_to='images/product_image/electric/detailpage/')
    gurantee = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    p3 = models.CharField(max_length=100)
    p4 = models.CharField(max_length=100)

class pedestal_fan(models.Model):
    modelname = models.CharField(max_length=100)
    img = models.ImageField(
        upload_to='images/product_image/electric/detailpage/')
    gurantee = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    p3 = models.CharField(max_length=100)
    p4 = models.CharField(max_length=100)

class madhani(models.Model):
    modelname = models.CharField(max_length=100)
    img = models.ImageField(
        upload_to='images/product_image/electric/detailpage/')
    gurantee = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    p3 = models.CharField(max_length=100)
    p4 = models.CharField(max_length=100)

class Hand_juicer(models.Model):
    modelname = models.CharField(max_length=100)
    img = models.ImageField(
        upload_to='images/product_image/electric/detailpage/')
    gurantee = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    p3 = models.CharField(max_length=100)
    p4 = models.CharField(max_length=100)

class blender(models.Model):
    modelname = models.CharField(max_length=100)
    img = models.ImageField(
        upload_to='images/product_image/electric/detailpage/')
    gurantee = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    p3 = models.CharField(max_length=100)
    p4 = models.CharField(max_length=100)

class chopper(models.Model):
    modelname = models.CharField(max_length=100)
    img = models.ImageField(
        upload_to='images/product_image/electric/detailpage/')
    gurantee = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    p3 = models.CharField(max_length=100)
    p4 = models.CharField(max_length=100)
    
class mixer_grinder(models.Model):
    modelname = models.CharField(max_length=100)
    img = models.ImageField(
        upload_to='images/product_image/electric/detailpage/')
    gurantee = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    p3 = models.CharField(max_length=100)
    p4 = models.CharField(max_length=100)
    
class chimney(models.Model):
    modelname = models.CharField(max_length=100)
    img = models.ImageField(
        upload_to='images/product_image/electric/detailpage/')
    gurantee = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    p3 = models.CharField(max_length=100)
    p4 = models.CharField(max_length=100)

class induction(models.Model):
    modelname = models.CharField(max_length=100)
    img = models.ImageField(
        upload_to='images/product_image/electric/detailpage/')
    gurantee = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    p3 = models.CharField(max_length=100)
    p4 = models.CharField(max_length=100)

class purifier(models.Model):
    modelname = models.CharField(max_length=100)
    img = models.ImageField(
        upload_to='images/product_image/electric/detailpage/')
    gurantee = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    p3 = models.CharField(max_length=100)
    p4 = models.CharField(max_length=100)

class water_heater(models.Model):
    modelname = models.CharField(max_length=100)
    img = models.ImageField(
        upload_to='images/product_image/electric/detailpage/')
    gurantee = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    p3 = models.CharField(max_length=100)
    p4 = models.CharField(max_length=100)

class motor_pump(models.Model):
    modelname = models.CharField(max_length=100)
    img = models.ImageField(
        upload_to='images/product_image/electric/detailpage/')
    gurantee = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    p3 = models.CharField(max_length=100)
    p4 = models.CharField(max_length=100)



