from django.shortcuts import render, redirect

from contact_us.forms import contact_us_form


# Create your views here.

def contact_us(request):
    if request.method == 'POST':
        contact_us = contact_us_form(request.POST)
        if contact_us.is_valid():
            print(contact_us.cleaned_data)
            return redirect('home-page')
    contact_us = contact_us_form()
    return render(request,'contact_us/contact-us.html',{
        'contact_us' : contact_us
    })