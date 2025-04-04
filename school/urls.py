from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('',views.login,name='login'),
    path('home',views.home,name='home'),
    path('dept',views.dept,name='dept'),
    path('teach',views.teach,name='teach'),
    path('stud',views.stud,name='stud'),
    path('add_dept',views.add_dept,name='add_dept'),
    path('add_teach',views.add_teach,name='add_teach'),
    path('add_stud',views.add_stud,name='add_stud'),
    path('aboutus',views.aboutus,name="aboutus"),
    

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)