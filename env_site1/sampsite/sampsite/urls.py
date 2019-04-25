"""sampsite URL Configuration

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
from django.conf.urls import url
## url to match the url in the browser
from django.contrib import admin
## admin: load administration site

from sampsite.views import hello_world, root_page, random_number
from django.conf.urls import include

## list all urls to tie to specific functions
## Reg expression: ^ fits start of line, $ fits
## end of line
## reg (\d+) : digit
## include polls.urls, use urls statements from polls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^helloworld/$', hello_world),
    url(r'^$', root_page),
    ## if want to pass value to function, put param in parenthesis.
    url(r'^random/(\d+)$', random_number),
    url(r'^polls/', include('polls.urls')),
    url(r'^img_db/', include('img_db.urls'))
]
