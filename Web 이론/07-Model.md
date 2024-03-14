### **Django URLs**
---

![](https://velog.velcdn.com/images/lurelight/post/c54e178c-6e1f-4b95-b5d3-9fffd1ff9144/image.png)

**URL dispatcher (운항 관리자, 분배기)**

URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결(매핑)

### **App과 URL**
---

**App URL mapping**

각 앱에서 URL을 정의하는 것

▶ 프로젝트와 각 앱이 URL을 나누어 관리하기 편하게 하기 위함

**2번째 앱 pages 생성 후 발생할 수 있는 문제**

view 함수 이름이 같거나 같은 패턴의 URL 주소를 사용하게 되는 경우

아래 코드와 같이 해결해 볼 수 있으나 더 좋은 방법이 필요

URL을 각자 app에서 관리하자

![](https://velog.velcdn.com/images/lurelight/post/c367e169-7a78-4fae-be15-752db6a26d17/image.png)

![](https://velog.velcdn.com/images/lurelight/post/dc3a9039-0466-4a73-b73c-0729c127a4c0/image.png)

![](https://velog.velcdn.com/images/lurelight/post/d28af173-e01b-48d7-b7f8-7a3614278f69/image.png)

![](https://velog.velcdn.com/images/lurelight/post/eabf88f2-44cb-46cb-9c49-0c6793067ab0/image.png)

**include()**

프로젝트 내부 앱들의 URL을 참조할 수 있도록 매핑하는 함수

▶ URL의 일치하는 부분까지 잘라내고, 남은 문자열 부분은 후속 처리를 위해 include 된 URL로 전달

**include 적용**

변경된 프로젝트의 urls.py

![](https://velog.velcdn.com/images/lurelight/post/58296929-589a-4f31-9a14-d314c6ddd511/image.png)

### **URL 이름 지정**
---

**url 구조 변경에 따른 문제점**

![](https://velog.velcdn.com/images/lurelight/post/d480f883-1326-4249-829d-bbe65c823be4/image.png)

**Naming URL patterns**

URL에 이름을 지정하는 것 (path 함수의 name인자를 정의하여 사용)

![](https://velog.velcdn.com/images/lurelight/post/86f33eea-f155-4682-84b5-91817f59b815/image.png)

![](https://velog.velcdn.com/images/lurelight/post/49a7acc0-3ecc-4dca-98ea-7d8da47d887b/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6dd98707-00c0-4aa0-b083-bcbc2fed4b1d/image.png)

![](https://velog.velcdn.com/images/lurelight/post/3df88711-98d7-4670-8e97-12c17f011e9c/image.png)

**URL 이름 공간**

![](https://velog.velcdn.com/images/lurelight/post/ee37606c-bda6-4604-a768-eb4fcff8232e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/ad0ea7e8-822e-4217-bf2c-776016f3f37c/image.png)

![](https://velog.velcdn.com/images/lurelight/post/bc74b4f6-6e5a-4c3a-9084-5cf01ae8ab65/image.png)


### **Model**
---

![](https://velog.velcdn.com/images/lurelight/post/1fe179a7-2f05-4f45-8657-0c362cc95d56/image.png)

**Django Model**

DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공 

▶ 테이블 구조를 설계하는 '청사진(blueprint)'

작성한 데이터를 저장할 수 있음

모델을 작성할 때 필요한 것

1. 필드 이름

2. 필드 데이터 타입

3. (선택) 필드의 제약 조건

![](https://velog.velcdn.com/images/lurelight/post/e7f903d3-5c1e-4176-a02b-b7465ff4fb5e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/8c917737-eedd-4eb5-9f09-67bfc9eb0c34/image.png)

![](https://velog.velcdn.com/images/lurelight/post/259400be-490a-4f70-a290-cfe6e31782da/image.png)

![](https://velog.velcdn.com/images/lurelight/post/da8be01a-bfff-4e33-b3ce-93ae6161c0e2/image.png)

![](https://velog.velcdn.com/images/lurelight/post/ba023611-55d4-480a-809f-9ba9fc9ed7c2/image.png)

![](https://velog.velcdn.com/images/lurelight/post/5dae5932-664e-40df-b23c-3d2ed726545c/image.png)

**제약 조건**

데이터가 올바르게 저장되고 관리되도록 하기 위한 규칙

▶ ex) 숫자만 저장되도록, 문자가 100자 까지만 저장되도록 하는 등

### **Migrations**
---

**Migrations**

model 클래스의 변경사항(필드 생성, 수정 삭제 등)을 DB에 최종 반영하는 방법

![](https://velog.velcdn.com/images/lurelight/post/b2c8cd35-a7ff-4cfc-8c8d-761c07e9e147/image.png)

![](https://velog.velcdn.com/images/lurelight/post/e931c312-2a3c-489e-b511-15b281fac429/image.png)

0001_initial.py 임의로 변경하면 안됨

![](https://velog.velcdn.com/images/lurelight/post/066935de-c98a-439f-b3f4-0fd2717b8831/image.png)

**추가 Migrations**

![](https://velog.velcdn.com/images/lurelight/post/56f6028b-120b-45dc-a8aa-209009028278/image.png)
기본적으로 빈 필드를 추가할 수 없다.

![](https://velog.velcdn.com/images/lurelight/post/dafe95cb-d470-49e6-880d-f8e60b06cea4/image.png)

![](https://velog.velcdn.com/images/lurelight/post/0b318829-7d52-4ed1-9ee8-f95e6498c7cc/image.png)

![](https://velog.velcdn.com/images/lurelight/post/338004c5-d36e-4511-8b85-9201a471f6fd/image.png)

![](https://velog.velcdn.com/images/lurelight/post/4c12f89c-677f-4d23-a89d-2c1850637f38/image.png)

![](https://velog.velcdn.com/images/lurelight/post/8e0764c5-a87b-4fd5-b7a2-c34a242efccf/image.png)

![](https://velog.velcdn.com/images/lurelight/post/60f35e5a-4e10-4ea4-b4b8-f6b531ffecda/image.png)

### **모델 필드**
---

**Model Field**

DB 테이블의 필드(열)을 정의하며, 해당 필드에 저장되는 데이터 타입과 제약조건을 정의

**CharField()**

길이의 제한이 있는 문자열을 넣을 때 사용

(필드의 최대 길이를 결정하는 max_length는 필수 인자)

**TextField()**

글자수가 많을 때 사용

**DateTimeField()**

날짜와 시간을 넣을 때 사용

**DateTimeField의 선택 인자** ★ 단답형

![](https://velog.velcdn.com/images/lurelight/post/952b0e6c-dffa-45c3-bf61-ddf325b6ec29/image.png)

### **Admin site**
---

**Automatic admin interface**

Django는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스를 제공

▶ 데이터 확인 및 테스트 등을 진행하는데 매우 유용

![](https://velog.velcdn.com/images/lurelight/post/9a0db769-d8a3-464d-ab6e-a4a4679044a8/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1708c1ed-1bc5-4d4e-b069-93e85bf8ef94/image.png)

![](https://velog.velcdn.com/images/lurelight/post/5173d778-a277-40ee-bb4e-e29861662d51/image.png)

![](https://velog.velcdn.com/images/lurelight/post/36bb42fb-b5d5-41ed-aa34-40de0fd26ede/image.png)

![](https://velog.velcdn.com/images/lurelight/post/d103579f-43f1-4ee8-b93e-01250f95823b/image.png)

![](https://velog.velcdn.com/images/lurelight/post/c8e919a4-3498-4e15-a472-b4efbb0af355/image.png)

### **참고**
---

![](https://velog.velcdn.com/images/lurelight/post/f02fefb5-2f16-418d-8489-0ddb8e8f6cf3/image.png)

![](https://velog.velcdn.com/images/lurelight/post/963ba186-a5e0-4853-b737-991bd55136f7/image.png)

![](https://velog.velcdn.com/images/lurelight/post/95178d2f-be73-42df-b60c-ac79a8141162/image.png)

![](https://velog.velcdn.com/images/lurelight/post/d6bd2329-f1a4-4823-ab24-5f422aa16cb2/image.png)

![](https://velog.velcdn.com/images/lurelight/post/a9b5dcfc-1810-4508-989c-3c6662e31793/image.png)
