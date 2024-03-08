1. 구조 / 스타일링

2. 레이아웃, 배치, 공간 배분, 정렬 (position, flexbox)

3. Toolkit

### **Bootstrap**
---

**Bootstrap**

CSS 프론트엔드 프레임워크 (Toolkit)

미리 만들어진 다양한 디자인 요소들을 제공하여 웹 사이트를 빠르고 쉽게 개발할 수 있도록 함

![](https://velog.velcdn.com/images/lurelight/post/bb95c7c0-9543-4417-b187-0575310206f4/image.png)

![](https://velog.velcdn.com/images/lurelight/post/8ed1d052-34ae-4fa6-ba46-eb84de4242df/image.png)

**CDN (Content Delivery Network)**

지리적 제약 없이 빠르고 안전하게 콘텐츠를 전송할 수 있는 전송 기술

서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화 (웹 페이지 로드 속도를 높임)

지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 전달

![](https://velog.velcdn.com/images/lurelight/post/4c65ccbc-1697-4699-b897-429997c0b8f7/image.png)

![](https://velog.velcdn.com/images/lurelight/post/213493d7-5e7f-4033-aebe-185c73160de1/image.png)

![](https://velog.velcdn.com/images/lurelight/post/dd06d3b0-364f-4920-befa-c5077e01d8be/image.png)

![](https://velog.velcdn.com/images/lurelight/post/80adac3b-d845-4565-a035-6c3dbe546456/image.png)

rem = 16px를 기준으로 상대적으로 나타낸 크기

Bootstrap에는 특정한 규칙이 있는 클래스 이름으로 스타일 및 레이아웃이 미리 작성되어 있음

**Reset CSS**

모든 HTML 요소 스타일을 일관된 기준으로 재설정하는 간결하고 압축적인 규칙 세트

▷ HTML Element, Table, List 등의 요소들에 일관성 있게 스타일을 적용시키는 기본 단계

**Reset CSS 사용 배경**

모든 브라우저는 각자의 'user agent stylesheet'를 가지고 있음 

- 웹사이트를 보다 읽기 편하게 하기 위해

문제는 이 설정이 브라우저마다 상이하다는 것

모든 브라우저에서 웹 사이트를 동일하게 보이게 만들어야 하는 개발자에겐 매우 골치 아픈 일

모두 똑같은 스타일 상태로 만들고 스타일 개발을 시작하자!

![](https://velog.velcdn.com/images/lurelight/post/fe1cb71a-a84b-4589-a5ff-3a0339859f67/image.png)

**Normalize CSS**

Reset CSS 방법 중 대표적인 방법

웹 표준 기준으로 브라우저 중 하나가 불일치 한다면 차이가 있는 브라우저를 수정하는 방법

- 경우에 따라 IE 또는 EDGE 브라우저는 표준에 따라 수정할 수 없는 경우도 있는데, 이 경우 IE 또는 EDGE 스타일을 나머지 브라우저에 적용시킴

![](https://velog.velcdn.com/images/lurelight/post/6276c527-745f-4977-ae19-5cdf0f3c2e2f/image.png)

### **Bootstrap 활용**
---

**Typography**

제목, 본문 텍스트, 목록 등

**Display headings**

기존 Heading보다 더 눈에 띄는 제목이 필요할 경우

(더 크고 약간 다른 스타일)

![](https://velog.velcdn.com/images/lurelight/post/83a338d3-84b9-417f-8742-181b7c02bc6a/image.png)

**Inline text elements**

HTML inline 요소에 대한 스타일

![](https://velog.velcdn.com/images/lurelight/post/87629e35-10aa-4600-8e55-2ac490e647a8/image.png)

**List**

HTML list 요소에 대한 스타일

![](https://velog.velcdn.com/images/lurelight/post/9bf67712-9c4e-4bf5-b93b-a06751ee561d/image.png)

### **Color**
---

**Bootstrap Color system**

Bootstrap이 지정하고 제공하는 색상 시스템

**Colors**

Text, Border, Background 및 다양한 요소에 사용하는 Bootstrap의 색상 키워드

**Bootstrap Component**

Bootstrap에서 제공하는 UI 관련 요소

▶ 버튼, 네비게이션 바, 카드, 폼, 드롭다운 등

**Component 이점**

일관된 디자인을 제공하여 웹 사이트의 구성 요소를 구축하는데 유용하게 활용

### **참고**
---

![](https://velog.velcdn.com/images/lurelight/post/fd8f6630-ed98-4ea9-971d-d29ffabb753a/image.png)

**Bootstrap을 사용하는 이유**

가장 많이 사용되는 CSS 프레임워크

사전에 디자인된 다양한 컴포넌트 및 기능

- 빠른 개발과 유지 보수

손쉬운 반응형 웹 디자인 구현

커스터마이징(customizing)이 용이

크로스 브라우징(Cross browsing) 지원

- 모든 주요 브라우저에서 작동하도록 설계되어 있음

개발자의 자유도가 제한되는 단점이 있음

개발에서는 생산성도 중요 따라서 Bootstap을 사용해서 빠르게 제작하는 점은 강점임

**Semantic Web**

![](https://velog.velcdn.com/images/lurelight/post/df748a9f-19bc-480f-b585-f1d6161b42df/image.png)

**Semantic in HTML**

![](https://velog.velcdn.com/images/lurelight/post/a4f574cc-0ab4-4428-9de1-9cb864fba7d8/image.png)

**HTML Semantic Element**

기본적인 모양과 기능 이외에 의미를 가지는 HTML 요소

▶ 검색 엔진 및 개발자가 웹 페잊 콘텐츠를 이해하기 쉽도록

### **Semantic in CSS**
---

**CSS 방법론**

CSS를 효율적이고 유지보수가 용이하게 작성하기 위한 일련의 가이드라인

**OOCSS (Object Oriented CSS)**

객체 지향적 접근법을 적용하여 CSS를 구성하는 방법론

**OOCSS 기본 원칙**

1. 구조와 스킨을 분리

구조와 스킨을 분리함으로써 재사용 가능성을 높임

모든 버튼의 공통 구조를 정의 + 각각의 스킨(배경색과 폰트 색상)을 정의

![](https://velog.velcdn.com/images/lurelight/post/7829ec35-7fa0-44e9-8d68-0e5fca4a2379/image.png)

2. 컨테이너와 콘텐츠를 분리

객체에 직접 적용하는 대신 객체를 둘러싸는 컨테이너에 스타일을 적용

스타일을 정의할 때 위치에 의존적인 스타일을 사용하지 않도록 함

콘텐츠를 다른 컨테이너로 이동시키거나 재배치할 때 스타일이 깨지는 것을 방지

![](https://velog.velcdn.com/images/lurelight/post/60fdb2bf-c3b4-42cb-94ca-c78f1cfcb48c/image.png)

### **참고**
---

**책임과 역할**

HTML 콘텐츠의 구조와 의미

CSS 레이아웃과 디자인

**의미론적인 마크업이 필요한 이유**

검색엔진 최적화(SEO)

- 검색 엔진이 해당 웹 사이트를 분석하기 쉽게 만들어 검색 순위에 영향을 줌

웹 접근성

- 웹 사이트, 도구, 기술이 고령자나 장애를 가진 사용자들이 사용할 수 있도록 설계 및 개발하는 것

- ex) 스크린 리더를 통해 전맹 시각장애 사용자들에게 웹의 글씨를 읽어줌
