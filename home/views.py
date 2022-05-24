from django.db import models
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

# from home.models import add_cust
from .models import Hand_juicer, blender, category, chimney, chopper, induction, madhani, mixer_grinder, motor_pump, water_heater

from . models import Residential_Coolers
from . models import Chakki
from . models import PVC_Pipes
from . models import RO_Spare_Parts
from . models import Electrical_Appliances
from . models import Industrial_Coolers,Tubs

from . models import CustomerForm

from . models import smart
from . models import rockstar
from . models import decent
from . models import freedom_jr
from . models import elegant_jr
from . models import elegant_plus
from . models import elegant
from . models import ageneral
from . models import freedom
from . models import freedom_plus
from . models import freedom_wind
from . models import freedom_storm

from .models import magic_VC
from .models import magic_cook
from .models import super_star
from .models import super_star_plus
from .models import olive
from .models import olive_plus
from .models import olive_plus_SS
from .models import magic_plus
from .models import max_plus
from .models import smart_2hp

from .models import heater,Gasgeyser,iron,kettle,rod,ceiling_fan,pedestal_fan,madhani,Hand_juicer,blender,chopper,mixer_grinder,chimney,induction,purifier,water_heater,motor_pump

from .models import grinding  ## chakki grinding items

from django.contrib import messages

def home(request):
    d = category.objects.all()
    l=""
    if(request.method == "POST"):
        name = request.POST.get('name')
        number = request.POST.get('phno')
        problem=request.POST.get('problem')
        if(name != '' and number != '' and problem !=''):
            b = CustomerForm(customer_name=name, customer_number=number,customer_problem=problem)
            b.save()
            messages.success(request,"Submitted Successfully!!")
        else:
            messages.error(request,"Invalid Credentials")          
    dict = {'categories': d}
    return render(request, "home.html", dict)


# Categories

def categories(request, category_id):
    if(category_id == 1):
        all_prods = Chakki.objects.all()
        grinding_items=grinding.objects.all()
        dict = {'all_prods': all_prods,'grinding_items':grinding_items}
        return render(request, "Aata Chakki.html", dict)

    if(category_id == 2):
        all_residential_prods = Residential_Coolers.objects.all()
        dict = {'all_residential_prods': all_residential_prods}
        return render(request, "Residential Coolers.html", dict)

    if(category_id == 4):
        all_prods = Electrical_Appliances.objects.all()
        dict = {'all_prods': all_prods}
        return render(request, "electrical_category.html", dict)

    if(category_id == 3):
        all_prods = RO_Spare_Parts.objects.all()
        dict = {'all_prods': all_prods}
        return render(request, "RO Spare Parts.html", dict)

    if(category_id == 5):
        all_prods = PVC_Pipes.objects.all()
        dict = {'all_prods': all_prods}
        return render(request, "PVC Pipes.html", dict)

    if(category_id == 6):
        all_industrial_prods = Industrial_Coolers.objects.all()
        dict = {'all_industrial_prods': all_industrial_prods}
        return render(request, "domestic_coolers.html", dict)
    if(category_id==7):
        table=Tubs.objects.all()
        dict={'detail':table}
        return render(request,"Tubs.html",dict)


# Coolers Details
def cooler_products(request, product_id):
    if(product_id == 1):
        d = smart.objects.all()

    elif(product_id == 2):
        d = rockstar.objects.all()

    elif(product_id == 3):
        d = freedom_jr.objects.all()

    elif(product_id == 4):
        d = decent.objects.all()

    elif(product_id == 5):
        d = ageneral.objects.all()

    elif(product_id == 6):
        d = elegant.objects.all()

    elif(product_id == 7):
        d = elegant_jr.objects.all()

    elif(product_id == 8):
        d = elegant_plus.objects.all()

    elif(product_id == 10):
        d = freedom.objects.all()

    elif(product_id == 9):
        d = freedom_plus.objects.all()

    elif(product_id == 11):
        d = freedom_wind.objects.all()

    elif(product_id == 12):
        d = freedom_storm.objects.all()

    if(request.method=="POST"):
        name=request.POST.get('name')        
        phno=request.POST.get('phno')        
        problem=request.POST.get('problem')
        if(name != '' and phno!= '' and problem !=''):
            b = CustomerForm(customer_name=name, customer_number=phno,customer_problem=problem)
            b.save()   

    dict = {'detail': d}    
    return render(request, "cooler_details.html", dict)


def category_page(request):
    return render(request,"categories.html")


def rating_Products(request):
    if(request.method=="POST"):
        rate=request.POST.get("rating")
        # print(type(rate))
        dict={1:"very bad",2:"not good",3:"good",4:"nice",5:"excellent"}
        # result=dict[rate]
        # print(res)
        c=2
        return c



def chakki_products(request, product_id):
    x=rating_Products(request)
    print("result:",x)

    if(product_id == 1):
        d = olive.objects.all()
    elif(product_id == 2):
        d = olive_plus.objects.all()
    elif(product_id == 3):
        d = olive_plus_SS.objects.all()
    elif(product_id == 4):
        d = max_plus.objects.all()

    elif(product_id == 5):
        d = super_star_plus.objects.all()

    elif(product_id == 6):
        d = magic_cook.objects.all()

    elif(product_id == 7):
        d = magic_plus.objects.all()

    elif(product_id == 8):
        d = super_star.objects.all()

    elif(product_id == 9):
        d = magic_VC.objects.all()
    
    elif(product_id == 10):
        d = smart_2hp.objects.all()
    
    if(request.method=="POST"):
        name=request.POST.get('name')        
        phno=request.POST.get('phno')        
        problem=request.POST.get('problem')
        if(name != '' and phno!= '' and problem !=''):
            b = CustomerForm(customer_name=name, customer_number=phno,customer_problem=problem)
            b.save()   

    dict = {'detail': d}
    return render(request, 'chakki_detail.html', dict)


def electrical_products(request, product_id):
    if(product_id == 17): #fans
        d1 = ceiling_fan.objects.all() 
        d2= pedestal_fan.objects.all()
        d=[]
        d.append(d1)
        d.append(d2)
   
    elif(product_id == 18): #cooking
        d2 = mixer_grinder.objects.all() 
        d1 = kettle.objects.all()
       
        d4 = Hand_juicer.objects.all() 
        d5= blender.objects.all()
        d6= madhani.objects.all()
        d7= induction.objects.all()
        d8= chimney.objects.all()
        d9= chopper.objects.all()
        d=[]
        d.append(d1)
        d.append(d2)
        d.append(d4)
        d.append(d5)
        d.append(d6)
        d.append(d7)
        d.append(d8)
        d.append(d9)

    elif(product_id == 19): # fabric
        d1 = iron.objects.all() 
        d=[]
        d.append(d1)
    
    elif(product_id == 20): # water heater
        d1 = water_heater.objects.all()
        d2 = Gasgeyser.objects.all() 
        d3=  rod.objects.all()
        
        d=[]
        d.append(d1)
        d.append(d2)
        d.append(d3)
   
    elif(product_id == 21): # room heater
        d1 = heater.objects.all()
        d=[]
        d.append(d1)
    
    elif(product_id == 22): # water motor pump
        d1 = motor_pump.objects.all()
        d=[]
        d.append(d1)
       

    
    if(request.method=="POST"):
        name=request.POST.get('name')        
        phno=request.POST.get('phno')        
        problem=request.POST.get('problem')
        if(name != '' and phno!= '' and problem !=''):
            b = CustomerForm(customer_name=name, customer_number=phno,customer_problem=problem)
            b.save()   
    dict={'detail':d}
    return render(request,"electric_detail.html",dict)