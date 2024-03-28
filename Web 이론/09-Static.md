### **Static Files**
---

**Static Files (정적 파일)**

서버 측에서 변경되지 않고 고정적으로 제공되는 파일 (이미지, JS, CSS 파일 등)

**웹 서버와 정적 파일**

웹 서버의 기본 동작은 특정 위치(URL)에 있는 자원을 요청(HTTP request) 받아서 응답(HTTP response)을 처리하고 제공하는 것

![](https://velog.velcdn.com/images/lurelight/post/dbb9521a-6e8c-4006-94ad-22ebdfdd94b3/image.png)

이는 '자원에 접근 가능한 주소가 있다'는 의미

웹 서버는 요청받은 URL로 서버에 존재하는 정적 자원을 제공함

→ 정적 파일을 제공하기 위한 경로(URL)가 있어야 함

### **Static files 제공하기**
---

**Static Files 제공하기**

1. 기본 경로에서 제공하기

2. 추가 경로에서 제공하기

**Static files 기본 경로**

app폴더/static

![](https://velog.velcdn.com/images/lurelight/post/c83e610d-6450-4f4d-8df8-1e4c7f4d0482/image.png)

![](https://velog.velcdn.com/images/lurelight/post/d054dea7-1704-4be2-b254-3b4a7c347272/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6d3332d3-be32-4875-8f63-1c1ee3f70a29/image.png)

**STATIC_URL**

기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL

→ 실제 파일이나 디렉토리가 아니며, URL로만 존재

![](https://velog.velcdn.com/images/lurelight/post/186c18a5-969c-4b47-8fe6-0572924253b7/image.png)

**URL + STATIC_URL + 정적 파일 경로**

http://127.0.0.1:8000/static/articles/sample-1.png

**Static files 추가 경로**

STATICFILES_DIRS에 문자열 값으로 추가 경로 설정

**STATICFILES_DIRS**

정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트

![](https://velog.velcdn.com/images/lurelight/post/8481eec3-ff8f-4817-a960-2193c647f52c/image.png)

![](https://velog.velcdn.com/images/lurelight/post/0bb565a5-662a-45c8-be0c-8be92180920f/image.png)

![](https://velog.velcdn.com/images/lurelight/post/fc42d7d7-9ad2-4738-a426-2913e966ed2f/image.png)

![](https://velog.velcdn.com/images/lurelight/post/04c870fd-74b1-4db2-abae-7194008953ec/image.png)

정적 파일을 제공하려면 요청에 응답하기 위한 URL이 필요

사진 업로드가 안되면 장고를 껏다가 키면 됨!

상속을 위해선 extend를 사용함, 이때 load는 무조건 extend 아래에 있어야 함


### **Media_files**
---

**Media Files**

사용자가 웹에서 업로드하는 정적 파일 (user-uploaded)

**ImageField() 이미지 업로드**

이미지 업로드에 사용하는 모델 필드

◆ 이미지 객체가 직접 저장되는 것이 아닌 '이미지 파일의 경로'가 문자열로 DB에 저장

**미디어 파일 제공을 위한 사전 준비**

1. setting.py 에 MEDIA_ROOT, MEDIA_URL 설정

2. 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 url 지정

**MEDIA_ROOT**

실제 미디어 파일들이 위치하는 디렉토리의 절대 경로

**MEDIA_URL**

MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성 (STATIC_URL과 동일한 역할)

![](https://velog.velcdn.com/images/lurelight/post/dba78512-0be0-4ed5-9047-16ce4e6b34fa/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1cc3e54d-33bc-4450-b988-b2fe8c61c5fb/image.png)

![](https://velog.velcdn.com/images/lurelight/post/d29aef67-5139-42fa-a6b4-0ec02051511e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/65ac79f1-d6f4-4621-84f6-690c1dca86fb/image.png)

![](https://velog.velcdn.com/images/lurelight/post/2c293063-2a22-46be-9a19-906ef87800c9/image.png)

![](https://velog.velcdn.com/images/lurelight/post/ba6e60d6-c8f3-450d-bc24-b8b7386bec11/image.png)

![](https://velog.velcdn.com/images/lurelight/post/b3e78794-49f6-4056-8cf5-08f633949159/image.png)

동일한 이미지를 여러번 삽입할 경우, 장고가 알아서 이름을 변경함

### **업로드 이미지 제공**
---

![](https://velog.velcdn.com/images/lurelight/post/f2dcb4c5-4e9f-43d9-aef0-9c04164e3810/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6bbf6d4c-8b48-471c-85db-6cf5641fd16a/image.png)

![](https://velog.velcdn.com/images/lurelight/post/7bc5a0d9-422c-4f64-b0de-0d8027275650/image.png)

![](https://velog.velcdn.com/images/lurelight/post/0a4dd955-8fb2-441e-a42a-5601a6be539e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/90f9b63b-34ce-49ce-8dbe-90634009c296/image.png)

### **참고**
---

models.py 파일 수정한 경우 python manage.py makemigrations 다시 하기!

![](https://velog.velcdn.com/images/lurelight/post/1590e20e-d72c-44bd-9aa5-5600b9a0356a/image.png)

![](https://velog.velcdn.com/images/lurelight/post/df66c01b-0d84-4301-94ba-31056ad446c9/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6aaa9273-f1fa-4512-b6ef-c0f2a849fc9e/image.png)

db,splite3 안에 내용을 만들때, appname_이름 형태로 작성해 주는 것이 약속~!