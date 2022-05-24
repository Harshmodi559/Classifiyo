from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("categories/<int:category_id>/", views.categories, name="categories"),
    path("cooler/<int:product_id>", views.cooler_products, name="coolers_products"),
    path("aatachakki/<int:product_id>",views.chakki_products, name="chakki_products"),
    path("appliances/<int:product_id>",views.electrical_products,name="electrical_products"),
    path("categories/",views.category_page,name="category_page"),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    #    path("ro_spare/<int:product_id>",views.ro_products,name="ro_products"),


]
