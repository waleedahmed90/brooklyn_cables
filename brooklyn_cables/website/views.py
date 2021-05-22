from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
#from .models import Prod

# Create your views here.
def home(request):
    return render(request, 'home.html', {'type_link': 'home', 'Page_Name': "Home"})

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact-us.html')


def request_quote(request):
    return render(request, 'request-a-quote.html')

def product1(request):
    price = "$ "+str(189.99)
    items_left = str(7)
    return render(request, 'PRODUCTS/product-1.html', {'price': price, 'items': items_left})

def product2(request):
    price = "$ "+str(159.99)
    items_left = str(4)
    return render(request, 'PRODUCTS/product-2.html', {'price': price, 'items': items_left})

def all_products(request):

    prods = Product.objects.all()

    return render(request, 'all-products.html', {'prods': prods})


def calcQuote(request):
    first_name = request.POST['firstName']
    last_name  = request.POST['lastName']
    email = request.POST['Email']
    organization = request.POST['orgName']
    message = request.POST['Comments']

    product = request.POST.getlist('prodType')
    color = request.POST.getlist('color')
    units = request.POST.getlist('quantityRadio')
    quantity = request.POST['Quantity']
    units = str(request.POST.get('quantityRadio', False))

    phoneNumber = request.POST['PhoneNumber']

    alpha = " order is requested by: "+first_name+" "+last_name+"\n"
    bravo = "Contact information: "+email+" "+phoneNumber+"\n"
    charlie = "Organization Name: "+organization+"\n"
    delta = "product requested: "+''.join(product)+" ("+''.join(color)+") \n"
    echo = "quantity requested: "+quantity+" units requested: "+''.join(units)+"\n"+message+"\n"
    
    foxtrot = alpha+bravo+charlie+delta+echo

    print(foxtrot)

    response = 'We have received your quotation request. We will get back to you as soon as we can with a request for your address and total cost'

    return render(request, 'request-a-quote.html' , {'response_text': response})




def ContactUs(request):
    first_name = request.POST['firstName']
    last_name  = request.POST['lastName']
    email = request.POST['Email']
    subject = request.POST['Subject']
    message = request.POST['EMAIL_TEXT']
    
    temp = first_name+last_name+email+subject+message

    response = 'We have received your message. We will get back to you as soon as we can.'

    return render(request, 'contact-us.html' , {'response_text': response})


def prod_temp(request, ID):
    product_info = Product.objects.get(id=ID)
    print(id)
    return render(request, 'prod_templ.html', {'prod':product_info})
