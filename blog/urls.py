from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('',views.post, name='post'),
    

    
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('details/<int:id>',views.details, name='details'),
    path('create/',views.create,name='create'),

    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
]
