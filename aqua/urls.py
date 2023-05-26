from django.urls import path
from .views import *
from aqua import views

# from .views import index, products, contact, sendmail, Signup, Login
from .views import product, product_details
urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about, name='about'),
    path('products/', product.as_view(), name='product'),
    path('product/<slug:str>/', product_details.as_view(), name='product_details'),
    path('service/', views.services, name='service'),
    path('contact-us/', contact.as_view(), name='contact')
    # path('contact-us/', views.contact, name='contact'),

    ]