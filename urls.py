from django.urls import path, include 

urlpatterns = [
  path('api/', include('sw_contact_form.api.urls')),
]
