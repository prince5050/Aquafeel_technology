from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from aqua.models import *

# Create your views here.
def home(request):
    return render(request, 'layout/index.html')
def about(request):
    return render(request, 'pages/about.html')

class product(ListView):
    model = Product
    context_object_name = 'product'
    template_name = 'pages/products.html'
    queryset = Product.objects.filter(status=1)

class product_details(ListView):
    model = Product
    context_object_name = 'product'
    template_name = 'pages/product_details.html'
    success_message = 'Request For Qutation is Send Successfully'
    def get_queryset(self):
        return Product.objects.filter(pk=self.request.GET.get('pro_id')).first()

    def post(self, request, *args, **kwargs):
        product_name = request.POST.get('product_name').replace(" ", "")
        pro_id = request.POST.get('product_id')
        con_obj = Qutation_for_product.objects.create(product_id=request.POST.get('product_id'),
                                         name=request.POST.get('name'), email=request.POST.get('email'),
                                         mobile=request.POST.get('mobile'), subject=request.POST.get('mobile'),
                                         company_name=request.POST.get('company_name'),
                                         message=request.POST.get('message'))
        con_obj.save()
        messages.success(request, product_details.success_message)
        return redirect('/product/'+product_name+'?pro_id='+pro_id)


class contact(CreateView):
    model = Contact
    template_name = 'pages/contact.html'
    success_message = 'Message Sent successfully'
    fields = '__all__'
    # success_url = 'contact'

    def post(self, request, *args, **kwargs):
        request_from = request.POST.get('request_from')
        con_obj = Contact.objects.create(name=request.POST.get('name'), email=request.POST.get('email'),
                                         mobile=request.POST.get('mobile'), subject=request.POST.get('mobile'),
                                         company_name=request.POST.get('company_name'),
                                         message=request.POST.get('message'), request_from=request.POST.get('request_from'))
        con_obj.save()
        messages.success(request, contact.success_message)
        if request_from == '1':
            return redirect('contact')
        elif request_from == '2':
            return redirect('about')
        else:
            return redirect('service')




def services(request):
    return render(request, 'pages/services.html')

# def contact(request):
#     return render(request, 'pages/contact.html')



# def product_list(request):
#         pro_obj = Product.objects.all()
#         data = {'product': pro_obj}
#         return render(request, 'pages/products.html', data)
# def product_details(request):
#         pro_obj = Product.objects.all()
#         data = {'product': pro_obj}
#         return render(request, 'pages/products.html', data)
