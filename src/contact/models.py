from datetime import datetime, date
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.utils.encoding import smart_text

# from localflavors.us.use_states import STATE_CHOICES
# from localflavors.us.models import USStateField

from .validators import phone_regex

# Create your models here.

YES_NO_CHOICES = (
    ('yes', 'Yes'),
    ('no', 'No'),
)

STATES = (('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))

class Contact(models.Model):
    CONTACT_PREF_CHOICES = (
        ('email', 'Email'),
        ('phone', 'Phone'),
    )
    TIME_PREF_CHOICES = (
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
    )
    name            = models.CharField(max_length=240, null=False, blank=False)
    address         = models.CharField(max_length=240, null=True, blank=True)
    city            = models.CharField(max_length=240, null=False, blank=False)
    state           = models.CharField(max_length=50, choices=STATES, null=False, blank=False)
    zipcode         = models.CharField(max_length=10, null=False, blank=False)
    phone_number    = models.CharField(validators=[phone_regex], max_length=17, null=False, blank=False) # validators should be a list
    email           = models.EmailField(max_length=240, null=False, blank=False)
    realtor         = models.CharField(max_length=10, verbose_name='Are you a realtor?', choices=YES_NO_CHOICES, default='no')
    contact_pref    = models.CharField(max_length=10, verbose_name='How should we contact you?', choices=CONTACT_PREF_CHOICES, default='email', null=False, blank=False)
    contact_time_pref = models.CharField(max_length=20, verbose_name='When should we contact you?', choices=TIME_PREF_CHOICES, default='evening', null=False, blank=False)
    message         = models.TextField(null=True, blank=True)   
    timestamp       = models.DateTimeField(auto_now_add=True)
     
    def __str__(self): 
        return smart_text(self.name)

# need post save receiver function
def contact_model_post_save_reciever(sender, instance, created, *args, **kwargs):
    print("after save")
    send_mail(
        'Subject',
        'Message',
        'gavin@sineanalytics.com', # from
        ['gavingreer@mac.com'], #to
        fail_silently = False,
    )
    print('email sent')
    

post_save.connect(contact_model_post_save_reciever, sender=Contact)