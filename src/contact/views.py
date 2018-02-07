from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import ContactModelForm
from .models import Contact

# Create your views here.
class ContactSuccessView(TemplateView):
    print("contact success class view")
    template_name = "contact/success.html"


class ContactFormView(CreateView):
    print("contact form class view")
    model = Contact
    form_class = ContactModelForm
    template = 'contact/contact.html' 
    success_url = '/success/'
    # success_message = "Message recieved! You're one step closer to selling your home!"

# def contact_view(request):
#     form = ContactModelForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.save()
#         messages.success(request, "Message sent!")
#         context = {
#             "form": ContactModelForm()
#         }
#     else: 
#         print("invalid data")
    
#     template = 'contact/contact.html'
#     return render(request, template, context)