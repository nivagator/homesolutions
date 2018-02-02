from django.shortcuts import render
from django.contrib import messages

from .forms import ContactModelForm
from .models import Contact

# Create your views here.

def contact_view(request):
    form = ContactModelForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Message sent!")
        context = {
            "form": ContactModelForm()
        }
    else: 
        print("invalid data")
    
    template = 'contact/contact.html'
    return render(request, template, context)