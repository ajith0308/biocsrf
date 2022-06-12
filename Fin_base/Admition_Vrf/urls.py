from django.urls import path
from .import views

urlpatterns = [

    path('', views.index, name="Home"),
    #schip
    path('scollership',views.scr, name='schollership'),
    path('scrapply',views.scrapply,name="apply"),
    path('scrdetails',views.scrdetails,name="details"),
    path('csrfrev',views.srcaadvrf,name='Aadhar pannel'),
    path('csrf10rev',views.src10csrf,name='Scholler 10 '),
    path('csrf12rev',views.src12csrf,name=' Scholler1 2'),
    path('scraadverfiy',views.srcaadvrf,name='scholler aadhar verfiy'),
    path('scr10vrf',views.scr10vrf,name='10th verify'),
    path('scr12vrf',views.scr12vrf,name='12th verify'),
     path('profile',views.profile,name='profile'),
    path('table',views.table,name='table'),
    path('sucess',views.sucess,name='sucess'),
    #aadhar 
    path('aadher',views.aadher),
       
      #admission
    path('admition', views.admition,name="admition"),
    path('adminlogin',views.admition_login,name="admissionlogin"),
    path('adtail',views.admtion_deatile,name='dtails'),
    path('ccsrf',views.srccsrf,name='certificate verify pannel'),
   # path('advrf',views.advrf,name='advrf'),
    path('vrf',views.verifyandStore,name='verfiy'),
     #aadhar verification
    path('adr',views.getcsrf,name='retrive'),
    #path('api',views.api,name='api'),
]
