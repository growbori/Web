### **Web Application**
---

**Web application (web service) 개발**

인터넷을 통해 사용자에게 제공되는 소프트웨어 프로그램을 구축하는 과정

다양한 디바이스 (모바일, 태블릿, PC등)에서 웹 브라우저를 통해 접근하고 사용할 수 있음

**클라이언트와 서버**

웹의 동작 방식

우리는 컴퓨터 혹은 모바일 기기로 웹 페이지를 보게 될 때까지 무슨 일이 일어날까?

![](https://velog.velcdn.com/images/lurelight/post/164b3924-0cda-4a94-8840-8493c0209bc8/image.png)

**Client (클라이언트)**

서비스를 요청하는 주체 (웹 사용자의 인터넷에 연결된 장치, 웹 브라우저)

**Server (서버)**

클라이언트의 요청에 응답하는 주체 (웹 페이지, 앱을 저장하는 컴퓨터)

![](https://velog.velcdn.com/images/lurelight/post/c2a84574-ed37-441c-94ed-5053a1574578/image.png)

**우리가 웹 페이지를 보게 되는 과정**

1. 웹 브라우저(클라이언트)에서 'google.com'을 입력

2. 브라우저는 인터넷에 연결된 전 세계 어딘 가에 있는 구글 컴퓨터 (서버)에게 'Google 홈페이지.html' 파일을 달라고 요청

3. 요청을 받은 구글 컴퓨터는 데이터베이스에서 'Google 홈페이지.html'파일을 찾아 응답

4. 전달받은 'Google 홈페이지.html' 파일을 사람이 볼 수 있도록 웹 브라우저가 해석해주면서 사용자는 구글의 메인 페이지를 보게 됨

### **Frontend & Backend**
---

웹 개발에서의 Frontend와 Backend

**Frontend (프론트엔드)**

사용자 인터페이스 (UI)를 구성하고, 사용자가 애플리케이션과 상호작용할 수 있도록 함

- HTML, CSS, JavaScript, 프론트엔드 프레임워크 등

**Backend (백엔드)**

서버 측에서 동작하며, 클라이언트의 요청에 대한 처리와 데이터베이스와의 상호작용 등을 담당

- 서버 언어 (Python, Java 등) 및 백엔드 프레임워크, 데이터베이스, API, 보안 등

![](https://velog.velcdn.com/images/lurelight/post/0f870aa2-60d3-4adc-b888-2529ac983d44/image.png)

![](https://velog.velcdn.com/images/lurelight/post/445db471-e10b-41aa-8cc7-500aebd99756/image.png)

### **Framework**
---

![](https://velog.velcdn.com/images/lurelight/post/feb85030-7d92-4120-bf60-83319962e1d0/image.png)

**Web Framework**

웹 어플리케이션을 빠르게 개발할 수 있도록 도와주는 도구 (개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공)

**Django framework**

**django**

Python 기반의 대표적인 웹 프레임워크

**왜 Django를 사용할까?**

다양성

- Python 기반으로 소셜 미디어 및 빅데이터 관리 등 광범위한 서비스 개발에 적합

확장성

- 대량의 데이터에 대해 빠르고 유연하게 확장할 수 있는 기능을 제공

보안

- 취약점으로부터 보호하는 보안 기능이 기본적으로 내장되어 있음

커뮤니티 지원

- 개발자를 위한 지원, 문서 및 업데이트를 제공하는 활성화된 커뮤니티

![](https://velog.velcdn.com/images/lurelight/post/89837a1f-f3ae-4c6d-845c-03888c8cadda/image.png)

![](https://velog.velcdn.com/images/lurelight/post/f5dff7bd-878c-4a93-abea-aab08075b30a/image.png)

목표 ▶ Django를 사용해서 서버를 구현할 것

**가상 환경**

Python 어플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 <span style='color:red;'>독립적인</span> 실행 환경

**가상 환경이 필요한 시나리오 1** 

1. 한 개발자가 2개의 프로젝트 (A와 B)를 진행한다.

2. 프로젝트 A는 request 패키지 버전 1을 사용해야 한다.

3. 프로젝트 B는 request 패키지 버전 2를 사용해야 한다.

4. 하지만 파이썬 환경에서 패키지는 1개의 버전만 존재할 수 있다.

5. A와 B 프로젝트의 다른 패키지 버전 사용을 위한 <span style='color:red;'>독립적인 개발 환경</span>이 필요하다.

**가상 환경이 필요한 시나리오 2** 

1. 한 개발자가 2개의 프로젝트 (A와 B)를 진행한다.

2. 프로젝트 A는 water라는 패키지를 사용해야 한다.

3. 프로젝트 B는 fire라는 패키지를 사용해야 한다.

4. 하지만 파이썬 환경에서 water패키지와 fire 패키지를 함께 사용하면 충돌이 발생하기 때문에 설치할 수 없다.

5. A와 B 프로젝트의 패키지 충돌을 피하기 위해 각각 <span style='color:red;'>독립적인 개발 환경</span>이 필요하다.

![](https://velog.velcdn.com/images/lurelight/post/171b7371-ebfe-4377-8fa6-424074502f50/image.png)

python -m venv 가상환경을 만들겠다는 명령어

![](https://velog.velcdn.com/images/lurelight/post/1d6a1b0e-6c71-435e-8a24-7995349af8fd/image.png)

![](https://velog.velcdn.com/images/lurelight/post/7e5f5954-caae-4829-884f-95ec727e36d9/image.png)

![](https://velog.velcdn.com/images/lurelight/post/0ccc63e3-7780-4b9f-9ed0-30d383d1f4b4/image.png)

![](https://velog.velcdn.com/images/lurelight/post/3b0e7c5c-717e-406a-9ddb-03f2c9dbaaef/image.png)

**의존성 패키지**

한 소프트웨어 패키지가 다른 패키지의 기능이나 코드를 사용하기 때문에 그 패키지가 존재해야만 제대로 작동하는 관계

사용하려는 패키지가 설치되지 않았거나, 호환되는 버전이 아니면 오류가 발생하거나 예상치 못한 동작을 보일 수 있음

![](https://velog.velcdn.com/images/lurelight/post/b92713a5-66d5-485c-86cc-586175ee6aff/image.png)

![](https://velog.velcdn.com/images/lurelight/post/b71ff8bd-ea84-4458-b3bf-fe1f10ac97f9/image.png)

**의존성 패키지 관리의 중요성**

개발 환경에서는 각각의 프로젝트가 사용하는 패키지와 그 버전을 명확히 관리하는 것이 중요

▶ 가상 환경 & 의존성 패키지 관리

**파이썬 개발자라면 암묵적으로 requirements.txt, venv를 사용함**

가상환경은 들어가는 개념이 아닌 ON, OFF의 개념임

### **Django 프로젝트**
---

![](https://velog.velcdn.com/images/lurelight/post/27ea5913-f1fc-44dd-8dee-8e8793c44805/image.png)

![](https://velog.velcdn.com/images/lurelight/post/a61444b8-875a-44cf-b63a-ca1bd86de78f/image.png)

![](https://velog.velcdn.com/images/lurelight/post/ea347932-36d9-4611-807b-a00ebb44ca0d/image.png)

![](https://velog.velcdn.com/images/lurelight/post/c1a89f72-583c-4ab4-8659-031ae16c80c6/image.png)

![](https://velog.velcdn.com/images/lurelight/post/07f89e85-79d8-4cc5-8713-b7b74dc8a946/image.png)

**가상 환경을 사용하는 이유**

의존성 관리

- 라이브러리 및 패키지를 각 프로젝트마다 독립적으로 사용 가능

팀 프로젝트 협업

- 모든 팀원들이 동일한 환경과 의존성 위에서 작업하여 버전간 충돌을 방지

**LTS (Long-Term Support)**

프레임워크나 라이브러리 등의 소프트웨어에서 장기간 지원되는 안정적인 버전을 의미할 때 사용

기업이나 대규모 프로젝트에서는 소프트웨어 업그레이드에 많은 비용과 시간이 필요하기 때문에 안정적이고 장기간 지원되는 버전이 필요

![](https://velog.velcdn.com/images/lurelight/post/8234e3fc-53b5-4a78-adff-17e935ff23fe/image.png)

**Django Design Pattern**

**디자인 패턴**

소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책 (공통적인 문제를 해결하는데 쓰이는 형식화 된 관행)

▶ 애플리케이션의 구조는 이렇게 구성하자 라는 관행

**MVC 디자인 패턴 (Model, View, Controller)**

애플리케이션을 구조화하는 대표적인 패턴 ('데이터' & '사용자 인터페이스' & '비즈니스 로직'을 분리)

▶ 시각적인 요소와 뒤에서 실행하는 로직을 서로 영향 없이, 독립적이고 쉽게 유지 보수 할 수 있는 애플리케이션을 만들기 위해

**MTV 디자인 패턴 (Model, Template, View)**

Django에서 애플리케이션을 구조화하는 패턴 (기존 MVC 패턴과 동일하나 단순히 명칭을 다르게 정의한 것)

![](https://velog.velcdn.com/images/lurelight/post/20e8b4e3-2f21-423b-8769-3672d576eb79/image.png)

### **Project & App**
---

![](https://velog.velcdn.com/images/lurelight/post/7f3debed-8af6-4ee9-b271-7e1071c7afbb/image.png)

**Django project**

애플리케이션의 집합 (DB 설정, URL 연결, 전체 앱 설정 등을 처리)

**Django application**

독립적으로 작동하는 기능 단위 모듈 (각자 특정한 기능을 담당하며 다른 앱들과 함께 하나의 프로젝트를 구성)

Ctrl + C : 강제 종료

![](https://velog.velcdn.com/images/lurelight/post/d239b0cb-af08-4528-8b79-789bd9798dbe/image.png)

![](https://velog.velcdn.com/images/lurelight/post/2db1db2b-3ef2-4e75-8eac-331fe41ad4b8/image.png)

![](https://velog.velcdn.com/images/lurelight/post/92bc9c06-d44d-45c2-b771-bc10d0e5280b/image.png)

![](https://velog.velcdn.com/images/lurelight/post/f0df5580-2a37-4176-9090-6ee70fd25742/image.png)

파일이 firstpjt와 동등한 위치에 생성됨

![](https://velog.velcdn.com/images/lurelight/post/d66e151f-22e3-4dc2-bb4f-c26b6a31185d/image.png)

앞쪽에 등록하는 것을 권장

![](https://velog.velcdn.com/images/lurelight/post/2f5db276-c2d6-49f8-9f9c-f874f07b1aff/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1e54966d-c5a1-44a6-b95a-66db78488a33/image.png)

![](https://velog.velcdn.com/images/lurelight/post/5a8adcff-ca11-40e3-b601-aeb0878b9f0e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/b34e8009-ff72-4caa-a4f5-253f3978e28e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/68f16ca7-22bc-48a3-bef9-837c00a54d2c/image.png)

### **요청과 응답**
---

![](https://velog.velcdn.com/images/lurelight/post/683f792c-474a-493f-840a-21c70f4f9d36/image.png)

![](https://velog.velcdn.com/images/lurelight/post/38d0760c-a045-49cf-b66b-d099d37c1c42/image.png)

![](https://velog.velcdn.com/images/lurelight/post/b33d3133-8be5-4b9a-9b71-3a4a645510e7/image.png)

![](https://velog.velcdn.com/images/lurelight/post/e47ba45b-8a04-4563-930f-25b4cc83df74/image.png)

![](https://velog.velcdn.com/images/lurelight/post/4a262879-1f27-4f16-8d69-addcac8ebfe4/image.png)

![](https://velog.velcdn.com/images/lurelight/post/90f40985-2c2d-45e9-a648-739f6439a35d/image.png)

![](https://velog.velcdn.com/images/lurelight/post/3851665a-d65b-4a09-8d8e-22e354cb50c1/image.png)

![](https://velog.velcdn.com/images/lurelight/post/acc64380-8532-4627-bfae-70acb57177f1/image.png)

![](https://velog.velcdn.com/images/lurelight/post/b9157ab3-c0a2-443c-ab1b-c194463127f2/image.png)

![](https://velog.velcdn.com/images/lurelight/post/e99a9e4f-d263-4bc1-8cc2-231d257e3fa2/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1bd96625-2eb7-42b9-8775-d314616e7db6/image.png)

![](https://velog.velcdn.com/images/lurelight/post/28e87af7-ac95-4f19-b204-d20cfb62ab04/image.png)

![](https://velog.velcdn.com/images/lurelight/post/bd5afe98-8326-4552-b1e5-0a8d3ed4c5be/image.png)

![](https://velog.velcdn.com/images/lurelight/post/73402d25-15c8-463a-ba3c-e6f410079b6e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/69bc4bbe-f53f-465b-a8db-a8d1eeec729f/image.png)

![](https://velog.velcdn.com/images/lurelight/post/39554a02-f20b-43bc-bfab-0f9207a40691/image.png)

![](https://velog.velcdn.com/images/lurelight/post/84c01159-ddcd-41d1-a341-8f58ad8d20a5/image.png)

![](https://velog.velcdn.com/images/lurelight/post/25c9b5ce-c47b-420f-bf1f-f4fe4daa2dcc/image.png)
