from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('admition', views.admition,name="admition"),
    path('scollership',views.scr, name='schollership'),
    path('fingerprint',views.mfstest),
    path('adminlogin',views.admition_login,name="admissionlogin"),
    path('profile',views.profile,name='profile'),
    path('table',views.table,name='table'),
    path('adr',views.arev,name='retrive'),
    #path('api',views.api,name='api'),
]
