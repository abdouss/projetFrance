from django.urls import path
from . import views
from .views import (Pam_update,pam_detail,pam_delete,Utilite_update,Utilite_delete,Pam_list)

urlpatterns = [
    path('new_Pam/', views.PamCreate.as_view(), name='new_Pam'),
    path(r'(?P<slug>[\w-]+)/edit/', Pam_update, name='pam_update'),
    path(r'(?P<slug>[\w-]+)/', pam_detail, name='pam_detail'),
    path(r'(?P<slug>[\w-]+)/delete/', pam_delete, name='pam_delete'),
    path('new_Utilite/', views.UtiliteCreate.as_view(), name='new_utilite'),
    path(r'(?P<slug>[\w-]+)/utilite/(?P<pk>\d+)/edit/', Utilite_update, name='Utilite_update'),
   	path(r'(?P<slug>[\w-]+)/utilite/(?P<pk>\d+)/delete/', Utilite_delete, name='Utilite_delete'),
   	path('listing/', Pam_list, name='Pam_list'),

]
