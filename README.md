# Practice Django api server

## 환경설정

### Pipenv가 안되는경우

> pip install --user pipenv 명령어를 이용하여 설치하였는데 pipenv를 찾을수 없는경우에는

> > pip list 에서 virtualenv 이 설치되어있는지 확인 해주시고  
> > pip uninstall virtualenv  
> > pip uninstall pipenv  
> > pip install pipenv  
> > 하면됨

### pipenv 설정 후 작업

> pipenv --three (Python3 환경설정으로 초기화)  
> pipenv shell 로 버블안으로들어간다.(페키지를 프로젝트에만 설치하기 위하여)

### Django 시작하기

> django-admin startproject config  
> 생성된 config파일을 최상단으로 옮김

### Linter 설정(flake8)

> pipenv install flake8 --dev --pre
> ctrl+shift+p > select linter검색 flake8선택 후 설치

### Formatter 설정(우측하단에 자동으로 뜨면 해당 설정으로사용)

> black 설치 pipenv install black --dev --pre
> .vscode settings.json에 black사용 추가 "python.formatting.provider": "black"

### 언어별 Formatter셋팅 setting.json에 직접들어가서 수정해야된다.(언어별 설정)

## Create Application in Django

### Application이란 함수들의 집합

> django-admin startapp (Application 이름) 로 application을생성할 수 있음  
> 생성된 applictaion은 config/settings.py에 등록해줘야함

## 서버 실행법

> pipenv shell(bubble로 접속)  
> python manage.py makemigrations  
> python manage.py migrate  
> python manage.py runserver
> python manage.py createsuperuser <-django admin사용을 위한 super user만들기

## Admin에 값추가

> 각 applications에 admin에 model register
> usermodel로 만들기
> 모델이 추가하고싶은 값 추가(https://docs.djangoproject.com/en/3.2/ref/models/fields/)
> makemigrations > migrate
> admin패널에서 확인가능

### Django Admin Model

> https://docs.djangoproject.com/en/3.2/ref/contrib/admin/

### MetaClass

> https://docs.djangoproject.com/en/3.2/ref/models/options/#ordering
> abstract 설정  
> django_admin에 이름 수정
>
> > verbose_name = 단수형이름
> > verbose_name_plural = 복수형이름
> > ordering = 정렬순서

## Core Apps 만들기(Common)

> django-admin startapp core  
> Core모델은 DB에저장하는게 아니고 상속받아서 사용할 것이기 때문에 DB에 넣지 말아야한다. -> Meta Class만들어야한다.
