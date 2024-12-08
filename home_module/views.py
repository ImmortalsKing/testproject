from django.shortcuts import render

# Create your views here.

def index_page(request):
    return render(request,'home_module/index_page.html')

def header_component(request):
    return render(request,'shared/site-header.html')

def footer_component(request):
    return render(request,'shared/site-footer.html')