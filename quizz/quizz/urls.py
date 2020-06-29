
from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    path('adminlogin/', include('AdminLogin.urls')),
    path('adminlogin/hello/admin/', admin.site.urls),
    path('Facultylogin/', include('Facultylogin.urls')),
    path('', include('Welcome.urls')),
    path('Student/login/', include('login.urls')),
    path('Student/register/', include('Register.urls')),
    path('Student/', include('Student_Page.urls')),
]
