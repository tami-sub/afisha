"""project URL Configuration


The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from . import views
from django.urls import path
urlpatterns = [
    path(r'', views.indexRender, name="index"),
    path(r'register', views.register, name="register"),
    path(r'signin', views.signin, name="signin"),
    path(r'newmoder', views.newmoder, name="newmoder"),
    path(r'adminpanel', views.adminpanel, name="adminpanel"),
    path(r'moderpanel', views.moderpanel, name="moderpanel"),
    path(r'accounts', views.accounts, name="accounts"),
    path(r'addcinema', views.addcinema, name="addcinema"),
    path(r'addmovie', views.addmovie, name="addmovie"),
    path(r'afisha', views.afisha, name="afisha"),
    path(r'cinema', views.cinema, name="cinema"),
    path(r'newschedule', views.newschedule, name='newschedule'),
    path(r'schedule', views.schedule, name='schedule'),
    path(r'userpanel', views.userpanel, name='userpanel'),
    path(r'allschedule', views.allschedule, name='allschedule'),
    path(r'exit', views.exit, name="exit")

]