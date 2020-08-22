"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

# path ( route, view)
# 요청이 들어오면 urlpatterns를 순서대로 비교하면서 일치하는 패턴을 찾는다.
# 패턴들은 GET, POST의 매개변수나 도메인 이름을 검색하지 않는다.
# 예를들면 https://www.example.com/myapp/ 이 요청된 경우,
# URLconf 는 오직 myapp/ 부분만 확인함.
# https://www.example.com/myapp/?page=3, 같은 요청에도,
# URLconf 는 역시 myapp/ 부분만 확인함.

