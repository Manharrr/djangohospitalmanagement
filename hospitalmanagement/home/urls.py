
# from django.urls import path,include
# from . import views
# urlpatterns = [
   
#      path('', include(views.index)),
#      path('about', include(views.about)),
#      path('booking', include(views.booking)),
#      path('doctors', include(views.doctors)),
#      path('contact', include(views.contact)),
#      path('department', include(views.department)),
     
# ]
 
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('booking', views.booking, name='booking'),
    path('doctors/', views.doctors, name='doctors'),
    path('contact', views.contact, name='contact'),
    path('department', views.department, name='department'),
]