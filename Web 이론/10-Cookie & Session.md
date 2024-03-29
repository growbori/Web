![](https://velog.velcdn.com/images/lurelight/post/cec73d00-86f3-46b7-8ad3-0fc161a21332/image.png)

### **Cookie & Session**
---

**HTTP**

HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 규약 → 웹(WWW)에서 이루어지는 모든 데이터 교환의 기초

**HTTP 특징**

비 연결 지향 (Connectionless)

- 서버는 요청에 대한 응답을 보낸 후 연결을 끊음

무상태 (stateless)

- 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음

**상태가 없다는 것은**

장바구니에 담은 상품을 유지할 수 없음

로그인 상태를 유지할 수 없음

→ 상태를 유지하기 위한 기술이 필요

### **쿠키**
---

**쿠키 (Cookie)**

서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각

→ 클라이언트 측에서 저장되는 작은 데이터 파일이며, 사용자 인증, 추적, 상태 유지 등에 사용되는 데이터 저장 방식

![](https://velog.velcdn.com/images/lurelight/post/d2b10a81-ee01-4616-a4de-4a7b843a56b7/image.png)

![](https://velog.velcdn.com/images/lurelight/post/c60bb609-e596-416f-af67-0afb4d5aea42/image.png)

![](https://velog.velcdn.com/images/lurelight/post/716d4508-6b0c-46e1-9ba8-b2b168b1939d/image.png)

**쿠키 사용 원리**

1. 브라우저(클라이언트)는 쿠키를 KEY-VALUE의 데이터 형식으로 저장

2. 이렇게 쿠키를 저장해 놓았다가, 동일한 서버에 재요청시 저장된 쿠키를 함께 전송

→ 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용 됨

- 이를 이용해 사용자의 로그인 상태를 유지할 수 있음

- 상태가 없는(stateless) HTTP 프로토콜에서 상태 정보를 기억 시켜주기 때문

![](https://velog.velcdn.com/images/lurelight/post/a3b8f0f5-9cef-4647-884a-891b9ee3a6b7/image.png)

![](https://velog.velcdn.com/images/lurelight/post/b6b0822c-0f34-4d76-b243-141cbfc84fc4/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1139888a-9566-4c47-974f-885231e62dff/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1e17eff5-3a84-4516-be5b-722aafb6841f/image.png)

![](https://velog.velcdn.com/images/lurelight/post/090dd92c-1709-431f-984e-b6743aac6365/image.png)

**쿠키 사용 목적**

1. 세션 관리 (Session management)

- 로그인, 아이디 자동 완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리

2. 개인화 (Personalization)

- 사용자 선호, 테마 등의 설정

3. 트래킹 (Tracking)

- 사용자 행동을 기록 및 분석

**세션 (Session)**

서버 측에서 생성되어 클라이언트와 서버 간의 상태를 유지 상태 정보를 저장하는 데이터 저장 방식

→ 쿠키에 세션 데이터를 저장하여 매 요청시마다 세션 데이터를 함께 보냄

**세션 작동 원리**

1. 클라이언트가 로그인을 하면 서버가 session 데이터를 생성 후 저장

2. 생성된 session 데이터에 인증할 수 있는 session id를 발급

3. 발급한 session id를 클라이언트에게 응답

4. 클라이언트는 응답 받은 session id를 쿠키에 저장

5. 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키 (session id가 저장된) 를 서버에 전달

6. 쿠키는 요청 때마다 서버에 함께 전송되므로 서버에서 session id를 확인해 로그인 되어있다는 것을 알도록 함

서버 측에서는 세션 데이터를 생성 후 저장하고 이 데이터에 접근할 수 있는 세션 ID를 생성

이 ID를 클라이언트 측으로 전달하고, 클라이언트는 쿠키에 이 ID를 저장

이후 클라이언트가 같은 서버에 재요청 시마다 저장해 두었던 쿠키도 요청과 함께 전송

→ 예를 들어 로그인 상태를 유지하기 위해 로그인 되어있다는 사실을 입증하는 데이터를 매 요청마다 계속해서 보내는 것

**쿠키와 세션의 목적**

서버와 클라이언트 간의 '상태'를 유지

### **참고**
---

**쿠키 종류 별 Lifetime(수명)**

1. Session cookie

- 현재 세션(current session)이 종료되면 삭제됨

- 브라우저 종료와 함께 세션이 삭제됨

2. Persistent cookies

- Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제됨

**세션 in Django**

Django는 'database-backed sessions' 저장 방식을 기본 값으로 사용

session 정보는 DB의 django_session 테이블에 저장됨

Django는 요청 안에 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session 데이터를 알아냄

Django는 우리가 session 메커니즘(복잡한 동작 원리)에 대부분을 생각하지 않게끔 많은 도움을 줌

### **Authentication System**
---

**Django Authentication System (인증 시스템)**

사용자 인증과 관련된 기능을 모아놓은 시스템

**Authentication (인증)**

사용자가 자신이 누구인지 확인하는 것 (신원 확인)

![](https://velog.velcdn.com/images/lurelight/post/91acae3a-95e6-4918-aecc-f19d9484d6c7/image.png)

### **Custom User model**
---

**Custom user model 로 '대체'하기**

django가 기본적으로 제공하는 User model이 아닌 직접 작성한 User model을 사용하기 위해

**User 클래스를 대체하는 이유**

우리는 지금까지 별도의 User 클래스 정의 없이 내장된 auth앱에 작성된 User 클래스를 사용했음

별도의 설정 없이 사용할 수 있어 간편하지만, 개발자가 직접 수정할 수 없는 문제가 존재

![](https://velog.velcdn.com/images/lurelight/post/028c04ba-2bd9-4afb-91b6-5051fdaf1a87/image.png)

![](https://velog.velcdn.com/images/lurelight/post/42311d4b-94dc-4fec-b94f-669d3704cdd2/image.png)

![](https://velog.velcdn.com/images/lurelight/post/0f26d8e2-3a2c-4f52-81c0-0f58d30ecdbb/image.png)

![](https://velog.velcdn.com/images/lurelight/post/d683ad55-adb0-4272-9b21-fbc4763e1eec/image.png)

**AUTH_USER_MODEL**

Django 프로젝트의 User를 나타내는데 사용하는 모델을 지정

#### ※ 주의 ※

프로젝트 중간에 AUTH_USER_MODEL을 변경할 수 없음

→ 이미 프로젝트가 진행되고 있을 경우 데이터베이스 초기화 후 진행

![](https://velog.velcdn.com/images/lurelight/post/378c3650-252d-4ac7-9838-167874146ae9/image.png)

프로젝트를 시작하며 반드시 User 모델을 대체해야 한다.

- Django는 새 프로젝트를 시작하는 경우 (기본 User 모델이 충분하더라도) 커스텀 User 모델을 설정하는 것을 강력하게 권장하고 있음

- 커스텀 User 모델은 기본 User 모델과 동일하게 작동 하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문

※ 단 User 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함

### **Login & Logout**
---

**Login **

Session 을 Create 하는 과정

**AuthenticationForm()**

로그인 인증에 사용할 데이터를 입력 받는 built-in form

![](https://velog.velcdn.com/images/lurelight/post/53f1dd1c-b58f-47c9-8c5a-584bcd04654e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/078db796-518a-49f1-96e4-4fdddd8e5778/image.png)

![](https://velog.velcdn.com/images/lurelight/post/18f58a3f-6eb0-4f34-823a-084bda842399/image.png)

**login(request, user)**

AuthenticationForm을 통해 인증된 사용자를 로그인 하는 함수

**get_user()**

AuthenticationForm의 인스턴트 메서드

→ 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환

![](https://velog.velcdn.com/images/lurelight/post/4d4716d9-5cfa-43e4-bb7d-007ecfcf1e07/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1223dc3d-981e-449e-947d-4b9876a68887/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6056bc55-95e7-493b-8648-a860c76154e9/image.png)

**Logout**

Session을 Delete하는 과정

**logout(request)**

현재 요청에 대한 Session Data를 DB에서 삭제

클라이언트의 쿠키에서도 Session Id를 삭제

![](https://velog.velcdn.com/images/lurelight/post/4b4ac699-4f9a-4229-b96b-cc28274cf3ec/image.png)

![](https://velog.velcdn.com/images/lurelight/post/ecb56bfc-2634-4d7e-b663-a39333c9dba2/image.png)

### **Template with Authentication data**
---

**Template with Authentication data**

템플릿에서 인증 관련 데이터를 출력하는 방법

![](https://velog.velcdn.com/images/lurelight/post/d15bb439-24fd-4159-819f-11a84edaf65a/image.png)

![](https://velog.velcdn.com/images/lurelight/post/730425dd-2af0-4d31-ad1a-e21da6f00ee9/image.png)

### **참고**
---

![](https://velog.velcdn.com/images/lurelight/post/29d919b3-e23c-4071-b366-037dae8c5434/image.png)

![](https://velog.velcdn.com/images/lurelight/post/75384b9e-6d6b-4ced-a35f-b437afee2377/image.png)

**'AbstractUser' Class**

'관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본 클래스'

Abstract base classes (추상 기본 클래스)

몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스

데이터베이스 테이블을 만드는데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가됨

**User 모델 대체하기 Tip**

User 모델을 대체하는 순서를 숙지하기 어려울 경우 해당 공식 문서를 보며 순서대로 진행하는 것을 권장

