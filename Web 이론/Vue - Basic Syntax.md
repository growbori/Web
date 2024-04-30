### **Template Syntax**
---

**Template Syntax**

DOM을 기본 구성 요소 인스턴스의 데이터에 선언적으로 바인딩(Vue Instance와 DOM을 연결)할 수 있는 HTML 기반 템플릿 구문 (확장된 문법 제공)을 사용

**Template Syntax 종류**

1. Text Interpolation

2. Raw HTML

3. Attribute Bindings

4. JavaScript Expressions

**1. Text Interpolation**

![](https://velog.velcdn.com/images/lurelight/post/e35f452f-992f-42c2-bb50-7bf6419ec362/image.png)

데이터 바인딩의 가장 기본적인 형태

이중 중괄호 구문 (콧수염 구문)을 사용

콧수염 구문은 해당 구성 요소 인스턴스의 msg 속성 값으로 대체

msg 속성이 변경될 때마다 업데이트됨

**2. Raw HTML**

![](https://velog.velcdn.com/images/lurelight/post/dd514aa5-e1da-4644-9bae-7bebbb5e6b6b/image.png)

**3. Attribute Bindings**

![](https://velog.velcdn.com/images/lurelight/post/a002da9f-f2e9-4d58-aff0-9bd62f1ace47/image.png)

**4. JavaScript Expressions**

![](https://velog.velcdn.com/images/lurelight/post/15f58a7d-a597-4257-8d6e-4fed188cf05a/image.png)

**Expressions 주의사항**

각 바인딩에는 하나의 단일 표현식만 포함될 수 있음

- 표현식은 값으로 평가할 수 있는 코드 조각 (return 뒤에 사용할 수 있는 코드여야 함)

![](https://velog.velcdn.com/images/lurelight/post/4b8b0288-3dce-4341-84b6-d2cc9b40df1a/image.png)

### **Directive**
---

**Directive**

'v-' 접두사가 있는 특수 속성

**Directive 특징**

Directive의 속성 값은 단일 JavaScript 표현식이어야 함 (v-for, v-on 제외)

표현식 값이 변경될 때 DOM에 반응적으로 업데이트를 적용

![](https://velog.velcdn.com/images/lurelight/post/9694cbf4-c5b7-4c4e-94bb-b255865cbe12/image.png)

![](https://velog.velcdn.com/images/lurelight/post/fb66e357-c244-4d48-a00d-14ee821821b1/image.png)

**Directive - 'Arguments'**

일부 directive는 directive 뒤에 콜론 (':')으로 표시되는 인자를 사용할 수 있음

![](https://velog.velcdn.com/images/lurelight/post/b9c8fdf3-7789-40fc-98d9-e4054dc38248/image.png)

Directive - 'Modifiers'

'.(dot)'로 표시되는 특수 접미사로, directive가 특별한 방식으로 바인딩되어야 함을 나타냄

![](https://velog.velcdn.com/images/lurelight/post/79cda699-afbb-45f6-b742-2bd63b7be91a/image.png)

![](https://velog.velcdn.com/images/lurelight/post/f95e4c8f-2231-412a-ae1b-81003ea4b6c7/image.png)

### **Dynamically data binding**
---

**v-bind**

하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 동적으로 바인딩

**v- bind 사용처**

1. Attribute Bindings

2. Class and Style Bindings

**Attribute Bindings**

![](https://velog.velcdn.com/images/lurelight/post/863f7b75-93ac-4843-85c7-16b6c0eb49f9/image.png)

![](https://velog.velcdn.com/images/lurelight/post/3f5be17a-e965-4f75-94e0-2ad7ac2b3c05/image.png)

![](https://velog.velcdn.com/images/lurelight/post/03ee4d58-7c39-45b4-a454-20de57a0da20/image.png)

![](https://velog.velcdn.com/images/lurelight/post/018ca0fc-985b-48d2-841d-abea24fa9590/image.png)

### **Class and Style Bindings**
---

**Class and Style Bindings**

class와 style은 모두 HTML 속성이므로 다른 속성과 마찬가지로 v-bind를 사용해 동적으로 문자열 값을 할당할 수 있음

Vue는 class 및 style 속성 값을 v-bind로 사용할 때 객체 또는 배열을 활용하여 작성할 수 있도록 함

- 단순히 문자열 연결을 사용하여 이러한 값을 생성하는 것은 번거롭고 오류가 발생하기가 쉽기 때문

**Class and Style Bindings가 가능한 경우**

1. Binding HTML Classes

1.1 Binding to Objects

1.2 Binding to Arrays

2. Binding Inline Styles

2.1 Binding to Objects

2.2 Binding to Arrays

**1.1 Binding HTML Classes - Binding to Objects**

객체를 : class 에 전달하여 클래스를 동적으로 전환할 수 있음

![](https://velog.velcdn.com/images/lurelight/post/76c49d8e-79a4-4c0f-8498-e34d957d45e9/image.png)

객체에 더 많은 필드를 포함하여 여러 클래스를 전환할 수 있음

![](https://velog.velcdn.com/images/lurelight/post/c73d6092-6ee2-420d-afa0-ede76b07e44e/image.png)

반드시 inline 방식으로 작성하지 않아도 됨

반응형 변수를 활용해 객체를 한번에 작성하는 방법

![](https://velog.velcdn.com/images/lurelight/post/7c9e4e2b-b95c-48ca-8f71-ae4e8eeff36b/image.png)

**Binding HTML Classes - Binding to Arrays**

:class를 배열에 바인딩하여 클래스 목록을 적용할 수 있음

![](https://velog.velcdn.com/images/lurelight/post/c722518c-e643-487a-8146-bde30bbe6890/image.png)

배열 구문 내에서 객체 구문을 사용하는 경우

![](https://velog.velcdn.com/images/lurelight/post/3a92f393-6a27-4a51-bf14-afb8ca1ddb8d/image.png)

**2.1 Binding Inline Styles - Binding to Objects**

:style은 JavaScript 객체 값에 대한 바인딩을 지원 (HTML style 속성에 해당)

![](https://velog.velcdn.com/images/lurelight/post/9730c9cf-4f8e-44f9-83d8-d19e1226a6e9/image.png)

실제 CSS에서 사용하는 것처럼 :style은 kebab-cased 키 문자열로 지원 (단, camelCase 작성을 권장)

![](https://velog.velcdn.com/images/lurelight/post/318fd26f-1e49-4779-86c7-8a9ed1f050c5/image.png)

반드시 inline 방식으로 작성하지 않아도 됨

반응형 변수를 활용해 객체를 한번에 작성하는 방법

![](https://velog.velcdn.com/images/lurelight/post/1c1d4762-1c8d-4fc4-a0b7-126621f1969d/image.png)

**2.2 Binding Inline Styles - Binding to Arrays**

여러 스타일 객체를 배열에 작성해서 :style을 바인딩할 수 있음

작성한 객체는 병합되어 동일한 요소에 적용

![](https://velog.velcdn.com/images/lurelight/post/a6eceb50-9b25-45f5-9134-bbd1fa5c8099/image.png)

### **Event Handling**
---

**v-on**

DOM 요소에 이벤트 리스너를 연결 및 수신

![](https://velog.velcdn.com/images/lurelight/post/cb17f407-543f-4240-9375-2e7c6720090e/image.png)

**1. Inline handlers**

Inline handlers는 주로 간단한 상황에 사용

![](https://velog.velcdn.com/images/lurelight/post/3107d90d-e97f-4d4a-8c95-84fc0c0aecd0/image.png)

**2. Method Handlers**

Inline handlers로는 불가능한 대부분의 상황에서 사용

![](https://velog.velcdn.com/images/lurelight/post/c5d2679d-0668-407d-b44e-a42f33ef1a8d/image.png)

Method Hanlers는 이를 트리거하는 기본 DOM Event 객체를 자동으로 수신

![](https://velog.velcdn.com/images/lurelight/post/528ba5cc-0036-482f-b7b6-f7b2e4e3d98a/image.png)

Inline Handlers에서의 메서드 호출

메서드 이름에 직접 바인딩하는 대신 Inline Handlers에서 메서드를 호출할 수도 있음

이렇게 하면 기본 이벤트 대신 사용자 지정 인자를 전달할 수 있음

![](https://velog.velcdn.com/images/lurelight/post/45c8ac00-a36e-4449-9f93-4fa03d072c1c/image.png)

**Inline Handlers에서의 event 인자에 접근하기**

Inline Handlers에서 원래 DOM 이벤트에 접근하기

$event 변수를 사용하여 메서드에 전달

![](https://velog.velcdn.com/images/lurelight/post/defbcfaf-a296-4b18-b4f0-2ea0875370c1/image.png)

**Event Modifiers**

Vue는 v-on에 대한 Event Modifiers를 제공해 event.preventDefault()와 같은 구문을 메서드에서 작성하지 않도록 함

stop, prevent, self 등 다양한 modifier를 제공

→ 메서드는 DOM이벤트에 대한 처리보다는 데이터에 관한 논리를 작성하는 것에 집중할 것

![](https://velog.velcdn.com/images/lurelight/post/6e520422-fd37-47ec-b97c-28c37ae03c70/image.png)

**Key Modifiers**

Vue는 키보드 이벤트를 수신할 때 특정 키에 관한 별도 modifiers를 사용할 수 있음

![](https://velog.velcdn.com/images/lurelight/post/7f579a1c-0294-4ba9-9420-b5be691bb377/image.png)

### **Form Input Bindings**
---

**Form Input Bindings**

form을 처리할 때 사용자가 input에 입력하는 값을 실시간으로 JavaScript 상태에 동기화해야 하는 경우 (양방향 바인딩)

**양방향 바인딩 방법**

1. v-bind와 v-on을 함께 사용

2. v-model 사용

**1. v-bind와 v-on을 함께 사용**

1. v-bind를 사용하여 input 요소의 value 속성 값을 입력 값으로 사용

2. v-on을 사용하여 input이벤트가 발생할 때마다 input 요소의 value 값을 별도 반응형 변수에 저장하는 핸들러를 호출

![](https://velog.velcdn.com/images/lurelight/post/102a2b1c-ce62-4a71-82d1-63e6f8d37793/image.png)

![](https://velog.velcdn.com/images/lurelight/post/bb72d99b-bc99-4824-ae00-8300ead0727e/image.png)

**v-model**

form input 요소 또는 컴포넌트에서 양방향 바인딩을 만듦

**2. v-model 사용**

v-model을 사용하여 사용자 입력 데이터와 반응형 변수를 실시간 동기화

![](https://velog.velcdn.com/images/lurelight/post/19ed18a9-a995-464b-857b-776ca9b3832e/image.png)

▷ IME가 필요한 언어(한국어, 중국어, 일본어 등)의 경우 v-model이 제대로 업데이트되지 않음

▷ 해당 언어에 대해 올바르게 응답하려면 v-bind와 v-on 방법을 사용해야 함

**v-model과 다양한 입력(input) 양식**

v-model은 단순 Text input 뿐만 아니라 Checkbox, Radio, Select 등 다양한 타입의 사용자 입력 방식과 함께 사용 가능

![](https://velog.velcdn.com/images/lurelight/post/989afd9e-0e71-4dd8-a383-fc3c7b727768/image.png)

![](https://velog.velcdn.com/images/lurelight/post/488cad48-3840-4f83-af38-89c5b2b06ea3/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1c2444b2-c7ca-4959-ad05-8b92c8b8058e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/f9ba4bfb-8714-4d8c-b8d9-7d4acd127c1c/image.png)

![](https://velog.velcdn.com/images/lurelight/post/f0438455-455b-49ab-9426-c42381150ab3/image.png)

### **참고**
---

**'$' 접두어가 붙은 변수**

Vue 인스턴스 내에서 제공되는 내부 변수

사용자가 지정한 반응형 변수나 메서드와 구분하기 위함

주로 Vue 인스턴스 내부 상태를 다룰 때 사용

**IME (Input Method Editor)**

사용자가 입력 장치에서 기본적으로 사용할 수 없는 문자(비영어권 언어)를 입력할 수 있도록 하는 운영 체제 구성 프로그램

일반적으로 키보드 키보다 자모가 더 많은 언어에서 사용해야 함

▷ IME가 동작하는 방식과 Vue의 양방향 바인딩(v-model) 동작 방식이 상충하기 때문에 한국어 입력 시 예상대로 동작하지 않았던 것

