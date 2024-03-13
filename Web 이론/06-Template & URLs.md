### **Template system**
---

**Django Template system**

데이터 표현을 제어하면서, 표현과 관련된 부분을 담당

![](https://velog.velcdn.com/images/lurelight/post/f39e7b8d-9e1f-4c74-b66c-bb2df5021db3/image.png)

![](https://velog.velcdn.com/images/lurelight/post/075f49c2-4a67-4cec-a8ca-d917c9cef311/image.png)

대괄호 2개 작성 시, 띄어쓰기를 해주지 않으면 적용되지 않음!

**Django Template Language (DTL)**

Template 에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템

**DTL 문법 종류**

![](https://velog.velcdn.com/images/lurelight/post/1055505c-decf-4dad-9792-6457712abb8f/image.png)

반드시 딕셔너리 형태를 지녀야 함. 딕셔너리의 key에 해당하는 값을 사용해야 함.

dot(.)를 이용해서 변수의 속성에 접근할 수 있음

![](https://velog.velcdn.com/images/lurelight/post/1c710241-030c-4859-81d3-fa36a2b06778/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6e1e87f2-2bd3-4310-96da-1a6d8f968dbe/image.png)

![](https://velog.velcdn.com/images/lurelight/post/58993ade-e70d-4cde-860c-0a938e921be4/image.png)

![](https://velog.velcdn.com/images/lurelight/post/97d14b2f-0c56-4582-97e2-9130fffdcfac/image.png)

![](https://velog.velcdn.com/images/lurelight/post/4c5b9ede-0bad-4996-97db-0ed44e54d347/image.png)

### **템플릿 상속**
---

**기본 템플릿 구조의 한계**

만약 모든 템플릿에 bootstrap을 적용하려면?

모든 템플릿에 bootstrap CDN을 작성해야 할까?

**템플릿 상속(template inheritance)**

페이지의 공통요소를 포함하고, 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 'skeleton'템플릿을 작성하여 상속 구조를 구축

![](https://velog.velcdn.com/images/lurelight/post/2aabfbe0-6121-4ad2-97cf-c8d76c3ee7c6/image.png)

![](https://velog.velcdn.com/images/lurelight/post/e9a7a61a-0ec1-4766-a212-79538654019d/image.png)

![](https://velog.velcdn.com/images/lurelight/post/eb7553b9-56ad-4951-8f56-b50a8cf566c8/image.png)

![](https://velog.velcdn.com/images/lurelight/post/739dca83-3f9f-4aec-af87-c428ccaa5bcb/image.png)

![](https://velog.velcdn.com/images/lurelight/post/277ba47e-86b4-4b96-bda7-422261bb43ca/image.png)

**HTML form (요청과 응답)**

**데이터를 보내고 가져오기**

HTML 'form' element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기

![](https://velog.velcdn.com/images/lurelight/post/d4c93171-ae5b-4754-b65d-3ad6d169caef/image.png)

![](https://velog.velcdn.com/images/lurelight/post/c92ad592-45bc-48f0-97a1-30b16f729bcc/image.png)

![](https://velog.velcdn.com/images/lurelight/post/606cc247-22d7-44a8-9f4e-94c1d246a6aa/image.png)

![](https://velog.velcdn.com/images/lurelight/post/77e234ca-43e2-4560-b2e1-4fbb9621529c/image.png)

![](https://velog.velcdn.com/images/lurelight/post/46a30357-5d42-40e3-bda6-413991dc042b/image.png)

![](https://velog.velcdn.com/images/lurelight/post/5f990831-8bad-4fdf-a5b0-91dbcf5cef46/image.png)

![](https://velog.velcdn.com/images/lurelight/post/78ff0f71-f138-49ad-a29d-483685aec3a9/image.png)

![](https://velog.velcdn.com/images/lurelight/post/c5614b20-0ef8-45af-bd01-b70bb62247f6/image.png)

![](https://velog.velcdn.com/images/lurelight/post/3b3a62d9-55b3-40df-be99-f89fc6885731/image.png)

action 과 method

**action**

입력 데이터가 전송될 URL 지정 (목적지)

만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐

**method**

데이터를 어떤 방식으로 보낼 것인지 정의

데이터의 HTTP request methods (GET, POST)를 지정

**input element**

사용자의 데이터를 입력받을 수 있는 요소 (type 속성 값에 따라 다양한 유형의 입력 데이터를 받음)

**'name' attribute**

입력한 데이터에 붙이는 이름 (key)

데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근할 수 있음

**Query String Parameters**

사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버로 보내는 방법

문자열은 앰퍼샌드 (&)로 연결된 key=value 쌍으로 구성되며, 기본 URL과는 물음표로 구분됨

![](https://velog.velcdn.com/images/lurelight/post/3b2a0c5c-f64a-45fd-856e-5b13e679b04a/image.png)

![](https://velog.velcdn.com/images/lurelight/post/73021dbe-5efd-42fd-9266-698f5e7bf815/image.png)

![](https://velog.velcdn.com/images/lurelight/post/324b75e3-c473-49c9-829b-ad4ce9add23d/image.png)

![](https://velog.velcdn.com/images/lurelight/post/677e9b84-3d2f-4b37-9f32-026bac1d91a1/image.png)

![](https://velog.velcdn.com/images/lurelight/post/f1f2394a-91cd-4572-86bc-6c0ff618f64a/image.png)

![](https://velog.velcdn.com/images/lurelight/post/fbae06dc-835d-49c1-8b69-c76de6de7ed2/image.png)

![](https://velog.velcdn.com/images/lurelight/post/78147046-b7c7-4ccd-943f-179ad5e5a3b7/image.png)

### **참고**
---

![](https://velog.velcdn.com/images/lurelight/post/f293cf7f-6f38-4543-980d-27bdc03796f6/image.png)

![](https://velog.velcdn.com/images/lurelight/post/c0234bf7-2243-4e0b-9fb3-9ee125c6344e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/79b774dc-259b-4efd-8be8-8ae3189ee67b/image.png)

![](https://velog.velcdn.com/images/lurelight/post/81a6b58a-65c3-4332-afeb-3c2d75387aec/image.png)

**Django URLs**

![](https://velog.velcdn.com/images/lurelight/post/14890748-6996-4337-a057-f60d318a8ce1/image.png)

![](https://velog.velcdn.com/images/lurelight/post/2472ccbf-b4a4-4f76-80aa-7acc93992aa4/image.png)

**변수와 URL**

![](https://velog.velcdn.com/images/lurelight/post/386bcb80-2590-418b-9b45-f5069f357e17/image.png)

![](https://velog.velcdn.com/images/lurelight/post/91617dbc-fded-412f-b9c5-c52d9dea21ad/image.png)

![](https://velog.velcdn.com/images/lurelight/post/7d542c6d-eef7-4cb5-8ef1-69ef3961e8ce/image.png)

![](https://velog.velcdn.com/images/lurelight/post/e4b1e1d6-6cb8-4e5e-9264-a898d101de2e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/96bd2884-00fa-4f36-87e6-363ce2e2d987/image.png)

![](https://velog.velcdn.com/images/lurelight/post/aef85426-4aca-49fc-b90f-9a9dd47b43dd/image.png)

![](https://velog.velcdn.com/images/lurelight/post/f376e3e8-1594-41a0-802f-adb55d6ce19a/image.png)

