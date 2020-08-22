Django Study
============

1. 서버 셋팅

    1. python 설치. (나는 pyenv를 사용함)
    
    2. django 디렉토리 생성.
        ```commandline
        mkdir django_tutorial       
        ```
   
    3. python3 가상환경 생성 && 가상 환경 사용.
        ```commandline
        python3 -m env myvenv
        source myvenv/bin/activate
        ```
   
        >가상환경을 사용하는 이유???<br>
        >1. 자신이 원하는 환경을 셋팅했을때 다른 python 프로젝트에 영향을 주지 않기위해 독립적인 작업환경을 만드는 것이다.<br>예를들면 프로젝트 1에서는 A 라이브러리 1버전이 필요하고 프로젝트 2에서는 A 라이브러리 2버전이 필요한 경우, <br>A 라이브러리를 각각의 프로젝트에 따로 설치해서 필요버전(환경)이 서로 다른 프로젝트에 영향을 주지 않음.
        >2. 해당 프로젝트에 필요한 라이브러리들만 모아서 설치되 가능하기때문에 불필요 라이브러리가 같이 설치되는 등의 불필요한 라이브러리설치를 줄일 수 있음.
        >3. 라이브러리뿐 아니라 파이썬 버전 자체가 다른 경우도 있음. (python 2 OR 3)
    
    4. django 프로젝트 생성
        ```commandline
        django-admin startproject mysite .
        ```
    
    5. 생성된 프로젝트 directory 구조   
        >![django 프로젝트 구조](./img/project_paths.png)        
        >- manage.py : django에서 사용하는 스크립트. 사이트 관리를 도와주는 역할.
        >- settings.py : 웹사이트 설정을 모아놓은 파일.
        >- urls.py : 서버 url 구조가 있는 파일. (urlresolver???)
        

2. API 생성. (설문조사 기능 만들기)

    1. polls Directoy 생성.
       ```commandline
       python manage.py startapp polls
       ```
       
    2. polls/views.py에 view 작성하기. (아직은 view가 뭐하는 놈인지 모르는 상황)
        ```python
        from django.http import HttpResponse
       
        def index(request):
           return HttpResponse("Hello, world. You're at the polls index.")
        ```
     
    3. polls/urls.py파일 생성 & view를 호출하기 위해 URL과 연결하기.
        ```python
        from django.urls import path

        from . import views

        urlpatterns = [
           path('', views.index, name='index'),
        ]   
        ```
       
    4. mysite/urls.py 파일 수정.
        ```python
        from django.contrib import admin
        from django.urls import include, path

        urlpatterns = [
           path('polls/', include('polls.urls')),
           path('admin/', admin.site.urls),
        ]
        ```
        >* URLconf는 장고에서 URL과 일치하는 뷰를 찾기 위한 패턴들의 집합.
        >* mysite/urls.py가 최상위 URLconf.
        >* include를 이용해서 다른 URLconf(urls.py??)를 참조 할수 있도록 함.
        >* 다른 url 패턴이 생길때 마다 include를 이용해 패턴을 추가해야함. (admin.site.urls는 제외.)
        >* mysite.urls(가장 최초의 url 확인)에서 url 확인. => 일치하는 url이 확인되면 해당 URLconf에 요청을 넘김. => 동일한 패턴을 확인하게되면 해당 url과 연결되어있는 views를 실행.