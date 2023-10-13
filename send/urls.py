from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
     path('send_mail/', views.send_email_form, name='send_email_form'),
     path('save_data/', views.save_data, name='save_data'),
     
]