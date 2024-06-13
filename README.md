# Running-mate
- 달리기, 자전거 운동을 기록하고 공유하는 서비스입니다.
- 운동코스를 추천하고 운동용품 정보를 추천하는 커뮤니티

## 목차
1. [팀 소개](#팀-소개)
2. [프로젝트 소개](#프로젝트-소개)
3. [WBS](#wbs)
4. [요구사항](#요구사항)
5. [기술 및 개발환경](#기술-및-개발환경)
6. [배포](#배포)
7. [ERD](#erd)
8. [프로젝트 구조](#프로젝트-구조)
9. [API 명세서](#api-명세서)
10. [화면 설계](#화면-설계)
11. [데모 라이브](#데모-라이브)
12. [관련 이슈](#관련-이슈)
13. [회고](#회고)
---
1. ## 팀 소개

1-1. 이스트소프트 백엔드 개발자 양성과정 오르미 3기 
파이널프로젝트 팀 런닝메이트 입니다.

|팀 원|박지만|송대현|김강토|신호용|
|---|---|---|---|---|
|역할|Backend - 운동기록<br> Frontend - 커뮤니티|Backend - 운동 코스 <br> Frontend - 운동 기록 앱 <br> CI / CD|Backend - 커뮤니티, 운동용품 추천 <br> Frontend - 로그인|Backend - 회원 <br> 배포|
|GitHub|[jmp7911](https://github.com/jmp7911)|[UkiDelly](https://github.com/UkiDelly)|[gangto33](https://github.com/gangto33)|[hoyonzz](https://github.com/hoyonzz)|

1-2. 협업 방식
- [코딩컨벤션](https://github.com/ormi3-2-4/Frontend-Web/wiki/%08%ED%98%91%EC%97%85-%EC%BB%A8%EB%B2%A4%EC%85%98) : WiKi 문서
- GitHub Flow
---
2. ## 프로젝트 소개

2-1. 목적
- 달리기,자전거 등의 운동으로 지역 네트워크를 연결하는 프로젝트 입니다.

2-2. 주요 기능
- GPS를 활용하여 달리기, 자전거 등 운동을 기록합니다.
- 운동기록을 분석하여 제공합니다.
- 운동기록을 공유하거나 코스를 추천할 수 있습니다.
- 운동용품 정보를 공유합니다.

---
3. ## WBS

![WBS](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/baa3660a-5206-4ee4-9096-cb6c3e262c58)

---
4. ## 요구사항

|회원|운동 기록|커뮤니티|
|---|---|---|
|![user](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/cb473ad5-23cf-4fcf-8029-e86c818c8749)|![record](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/6adf248b-275e-43f5-bee9-e31fcb78dae9)|![community](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/c323677a-0c77-4111-8785-a649c981f3e7)|
|운동용품 추천|운동 코스||
|![recommend](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/3250373c-809b-4b70-816a-fe2edf4c1460)|![course](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/d1cc3ef1-1ab8-4bfe-bc2a-ab045c692a01)||

---

5. ## 기술 및 개발환경
### Backend
<div>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">
    <img src="https://img.shields.io/badge/GDAL-5CAE58?style=for-the-badge&logo=GDAL&logoColor=white">
    <img src="https://img.shields.io/badge/Mysql-4479A1?style=for-the-badge&logo=Mysql&logoColor=white">
</div>

### Frontend
<div>
    <img src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=Flutter&logoColor=white">
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white">
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white">
    <img src="https://img.shields.io/badge/Leaflet-199900?style=for-the-badge&logo=Leaflet&logoColor=white">
</div>


### Cloud
<div>
    <img src="https://img.shields.io/badge/Amazone_LightSail-569A31?style=for-the-badge&logo=Amazon&logoColor=white">
</div>

### IDE & Cooperation
<div>
    <img src="https://img.shields.io/badge/Pycharm-000000?style=for-the-badge&logo=Pycharm&logoColor=white">
    <img src="https://img.shields.io/badge/visual_Studio_Code-007ACC?style=for-the-badge&logo=visualStudioCode&logoColor=white">
    <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
    <img src="https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white">
</div>

---
6. ## 배포

- 모바일 : [안드로이드](https://drive.google.com/file/d/1Jq1NFXwTxuaPCt5_OMZaVGTYFBCv_bnL/view?usp=drive_link)

- 웹 어플리케이션 : [m.running-mate.kro.kr](http://m.running-mate.kro.kr)

- 백엔드 : [running-mate.kro.kr](http://m.running-mate.kro.kr)

![gunicorn](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/ddde3751-f8de-4f5b-8dd5-12f24aec6c9e)

![image](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/e0cbb428-3795-41d0-8394-f6e7404e0cdf)

---
7. ## ERD
![Running Mate](https://github.com/ormi3-2-4/Running-mate/assets/37658328/4e2fb501-8682-442d-b6d1-a132ca6eabb8)

---

8. ## 프로젝트 구조

### Backend
```
community
 ┣ migrations
 ┣ __init__.py
 ┣ admin.py
 ┣ apps.py
 ┣ models.py
 ┣ tests.py
 ┗ views.py
 course
 ┣ migrations
 ┣ __init__.py
 ┣ admin.py
 ┣ apps.py
 ┣ models.py
 ┣ serializer.py
 ┣ tests.py
 ┣ urls.py
 ┗ views.py
 recommend
 ┣ migrations
 ┣ __init__.py
 ┣ admin.py
 ┣ apps.py
 ┣ models.py
 ┣ tests.py
 ┗ views.py
 record
 ┣ migrations
 ┣ templates
 ┃ ┗ maps.html
 ┣ __init__.py
 ┣ admin.py
 ┣ apps.py
 ┣ forms.py
 ┣ models.py
 ┣ permissions.py
 ┣ serializers.py
 ┣ tests.py
 ┣ urls.py
 ┗ views.py
 running_mate
 ┣ __init__.py
 ┣ asgi.py
 ┣ consumer.py
 ┣ settings.py
 ┣ urls.py
 ┗ wsgi.py
 user
 ┣ migrations
 ┣ __init__.py
 ┣ admin.py
 ┣ apps.py
 ┣ models.py
 ┣ serializers.py
 ┣ tests.py
 ┣ urls.py
 ┗ views.py
 .env
 .gitignore
 db.sqlite3
 manage.py
 requirements.txt
 schema.yml
```
9. ## API 명세서
|end-point|GET|POST|PATCH|DELETE|Description|
|---|---|---|---|---|---|
|user/info|O|---|O|---|사용자 프로필|
|record|O|O|---|---|운동기록|
|record/<int:pk>|O|---|---|O|운동기록 상세|
|record/<int:pk>/finish|---|---|O|---|운동기록 종료|
|record/<int:pk>/image|---|O|---|---|인증샷|
|course|O|O|---|---|달리기 코스|
|course/<int:pk>|O|---|O|O|달리기 코스 상세|
|recommend|O|O|O|O|운동용품 추천|
|recommend/<int:pk>|O|---|O|O|운동용품 추천 상세|
|community|O|O|O|O|운동 공유 커뮤니티|
|community/<int:pk>|O|---|O|O|운동공유 커뮤니티 상세|

[swagger URL](http://running-mate.kro.kr/api/schema/swagger-ui/)

---
10. ## 화면 설계
- [Figma](https://www.figma.com/file/KuQDyazSTgOMttmP3tneYV/%ED%99%94%EB%A9%B4-%EC%84%A4%EA%B3%84?type=design&node-id=0-1&mode=design&t=pgDemkq1xKR9rZeO-0)

10-1. Mobile Application
|로그인|회원 가입|메인 화면|
|---|---|---|
|![image](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/743e91e6-9b35-4e2b-acd0-b351ad363937)|![image](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/7ab036e2-cac6-4b8c-a646-6a51ba1c0c5e)|![image](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/fa5b95a5-20e6-46f4-9e60-b37ad600c816)|
|운동 기록|히스토리|히스토리 상세|
|![image](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/696f8702-c6f3-4f7c-ba8d-339ac2a99a39)|![image](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/7ac6981c-a92d-4f22-acc4-f82c8f01561d)|![image](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/b667f514-a220-4ccf-ab1f-ec45d0f16c07)|

10-2. Web Application
|커뮤니티|글 쓰기|글 상세|
|---|---|---|
|![image](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/f95051b2-01af-4777-a28c-e5e6ecdff262)|![image](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/c628d83a-9ead-4d17-aded-67d80936f65a)|![image](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/6b65e3e8-02ac-461e-90e3-fc7dc4977529)|

---
11. ## 데모 라이브

- 모바일 (안드로이드)

[![mobile](https://img.youtube.com/vi/N-0c5iZS3Ks/hqdefault.jpg)](https://youtube.com/shorts/N-0c5iZS3Ks?si=XY04Ev00SdHl1Ehw)

- 웹 어플리케이션

|로그인|회원가입|
|---|---|
|![login](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/3b141cd1-84cd-40ae-9366-f2c52281f644)|![register](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/9f98144b-ac12-4f8b-9d93-664b178e531f)|
|글 쓰기|댓글 쓰기|
|![write](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/7dfbd4b5-0dc9-49b3-9231-309f4cd2bcb0)|![comment](https://github.com/ormi3-2-4/Frontend-Web/assets/37658328/d887bf98-c4f5-4345-8b0f-a489a6c3bb0f)|

---
12. ## 관련 이슈

- Field name username is not valid for model

원인

django-rest-auth 라이브러리에서는 기본 시리얼라이저가 셋팅되어 있습니다.
```sh
USER_DETAILS_SERIALIZER = 'rest_auth.views.UserDetailsView'
```
커스텀 유저에 username을 email 로 사용하였는데
기본 시리얼라이저에서 username을 참조하려고 해서 에러가 발생하였습니다.

해결 

다음과 같이 유저 모델을 명시하고 시리얼라이저에 username을 삭제하여 해결하였습니다.
```sh
AUTH_USER_MODEL = 'user.User'
```
---

- GPS 좌표 활용

좌표데이터들의 집합을 활용해 거리를 구하기위해 GeoDjango를 사용하였습니다.
GeoDjango는 다양한 형식의 공간 데이터를 제공하고 데이터 조작을 위한 인터페이스를 제공하며,
Django 외에 추가적인 설치사항이 요구됩니다.

1. 공간 데이터베이스
  - SQLite, MySQL, MongoDB 등 많은 RDBMS 와 NoSQL 애플리케이션이 공간 데이터베이스를 지원합니다.
  - MySQL을 채택하였기 때문에 Django ORM을 사용할 수 있습니다.
2. 지리 공간 라이브러리
  - GDAL Library 설치 하였습니다.

 djgeojson.fields.LineStringField 타입에 좌표들을 저장하였고
 이를 활용하여 좌표간의 거리를 계산하고 지도에 표시하였습니다.

---

- DateField Non-editable

models.DateTimeField에 Admin 페이지에서 생성/ 수정이 불가능한 문제가 발생하였습니다.

원인

auto_now, auto_add_now를 추가하면 editable=False 가 기본값이 되어 editable=True로 명시하여도 수정할 수 없게 되었습니다.

해결

auto_now, auto_add_now를 제거하고, 서버측에서 시간을 넣어주는 방향으로 수정하였습니다.

---
13. ## 회고

- 박지만 : 운동기록 백엔드 담당

개발자만 4명 이상의 규모로 협업은 처음인데 좋은 경험이었다. 

GitHub Flow에 익숙해지고 테스트코드를 작성하여 프론트와 통신에서 발생할 오류를 미연에 줄이는 것이 좋았다.

기획단계에 시간을 충분히 쏟아서 미팅시간을 줄이고 코드에 집중해 볼 수 있었다.

---

- 송대현 : FrontEnd 전 부분, 운동코스 백엔드 담당

일정이 정해져 있는 프로젝트를 협업해보는 것은 처음이였다.

시간이 3주밖에 주어지지 않았기 때문에 그런 걸수도 있겠지만, 생각보다 촉박한 일정이였던 것 같다. 

또한 Django에서 Api 서버를 만들때 Dto를 만드는 방식이 타 프레임워크랑 다르고, 또 많은 기능이 이미 구현되어 있기 때문인지 적응하기 힘들었고 디버깅도 힘들었던 것같다.

---

- 김강토 : 커뮤니티, 운동용품 추천 백엔드 담당

처음 하는 협업에서 잘 할 수 있을까 하는 의문과 걱정이 들었으나, 걱정이 무색할 만큼 팀원들과 소통이 잘 되었고 확실한 계획과 분업을 하여 방황하지 않을 수 있었다.

프로젝트를 하면서 DRF 와 serializer, Viewset 을 조금 더 친숙하게 사용할 수 있게 되었고,

팀원 분들의 의견과 도움을 받으며 훨씬 많이 성장할 수 있는 계기가 된 값진 프로젝트였다.

---

- 신호용 : 회원, 운동코스 백엔드 담당

프로젝트를 협업해서 진행해보는 경험이 처음이라 많이 긴장했지만, 팀원들이 많이 도와주고

수준에 맞는 임무들을 맡게 배려해줘서 하나씩 해결해갈 수 있었습니다. 배포를 처음 진행하다보니

많은 시간이 소요되고, 많은 문제들이 있었지만 팀원들이 도와주고 기다려줘서 해낼 수 있었고

좋은 경험이 될 수 있었던 것 같습니다.

---


