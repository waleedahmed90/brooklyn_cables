from django.urls import path
from . import views

#path(name_displayed_in_url, rendering_function, tag_name)
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact-us', views.contact_us, name='ContactUs'),
    path('request-a-quote', views.request_quote, name = 'RequestQuote'),
    path('product-1', views.product1, name='product1'),
    path('product-2', views.product2, name='product2'),
    path('all-products', views.all_products, name='all-products'),
    path('calcQuote', views.calcQuote, name='calculate-quote'),
    path('ContactUs', views.ContactUs, name='contact-us'),
    path('product-details/<int:ID>', views.prod_temp, name='prod_temp')   
]