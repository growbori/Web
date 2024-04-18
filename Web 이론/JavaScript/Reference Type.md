### **함수**
---

**Function**

참조 자료형에 속하며 모든 함수는 Function object

**참조 자료형 (Reference type)**

Objects (Object, Array, Function)

객체의 주소가 저장되는 자료형 (가변, 주소가 복사)

### **함수 정의**
---

**함수 구조**

![](https://velog.velcdn.com/images/lurelight/post/b422e503-8e9f-4401-b7b4-faa6e67fb4fa/image.png)

function 키워드

함수의 이름

함수의 매개변수

함수의 body를 구성하는 statements

※ return 값이 없다면 undefined 를 반환

**함수 정의 2가지 방법**

선언식 (function declaration)

표현식 (function expression)

![](https://velog.velcdn.com/images/lurelight/post/b8f5b7cb-0ea4-4e02-b09a-eecc43a3c32e/image.png)

**함수 표현식 특징**

함수 이름이 없는 '익명 함수'를 사용할 수 있음

선언식과 달리 표현식으로 정의한 함수는 호이스팅 되지 않으므로 함수를 정의하기 전에 먼저 사용할 수 없음

![](https://velog.velcdn.com/images/lurelight/post/1bee852a-f3d6-43b0-a6d7-e58a840305a9/image.png)

![](https://velog.velcdn.com/images/lurelight/post/3d9ffc9b-3f28-4a7c-a343-f0effb5b4364/image.png)

### **매개변수**
---

**매개변수 정의 방법**

1. 기본 함수 매개변수(Default function parameter)

전달하는 인자가 없거나 undefined가 전달될 경우 이름 붙은 매개변수를 기본값으로 초기화

![](https://velog.velcdn.com/images/lurelight/post/2bab5ef9-60a1-4874-b08d-a90a078117e9/image.png)

2. 나머지 매개변수

임의의 수의 인자를 '배열'로 허용하여 가변 인자를 나타내는 방법

※ 작성 규칙

- 함수 정의 시 나머지 매개변수는 하나만 작성할 수 있음

- 나머지 매개변수는 함수 정의에서 매개변수 마지막에 위치해야 함

![](https://velog.velcdn.com/images/lurelight/post/db7e5f8b-d2e1-40e8-8e83-64eac1031f97/image.png)

**매개변수와 인자 개수가 불일치할 때**

매개변수 개수 > 인자 개수

누락된 인자는 undefined로 할당

![](https://velog.velcdn.com/images/lurelight/post/132f9610-66f0-46ed-95c3-58cbfff1c232/image.png)

매개변수 개수 < 인자 개수

초과 입력한 인자는 사용하지 않음

![](https://velog.velcdn.com/images/lurelight/post/87d28a3a-82c7-4279-9072-ac5e9801e3bc/image.png)

### **Spread syntax**

**'...' (Spread syntax)**

전개 구문

배열이나 문자열과 같이 반복 가능한 항목을 펼치는 것 (확장, 전개)

전개 대상에 따라 역할이 다름

- 배열이나 객체의 요소를 개별적인 값으로 분리하거나 다른 배열이나 객체의 요소를 현재 배열이나 객체에 추가하는 등

1. 함수와의 사용

- 함수 호출시 인자 확장

![](https://velog.velcdn.com/images/lurelight/post/e5790b9a-cfcd-4b89-9745-5284801fbb37/image.png)

- 나머지 매개변수 (압축)

![](https://velog.velcdn.com/images/lurelight/post/bfe792b2-b392-4a6c-91e5-58fd16346696/image.png)

2. 객체와의 사용 (객체 파트에서 진행)

3. 배열과의 사용 (배열 파트에서 진행)

### **화살표 함수**
---

**화살표 함수 표현식 (Arrow function expressions)**

함수 표현식의 간결한 표현법

![](https://velog.velcdn.com/images/lurelight/post/a98f8229-789f-4f83-8516-73ed4c8d4fba/image.png)

![](https://velog.velcdn.com/images/lurelight/post/5e316709-306d-4e04-9db5-c6db2f78417a/image.png)

![](https://velog.velcdn.com/images/lurelight/post/606e4911-08cb-493d-9312-b9741459cbbc/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6f596c16-1d94-44bb-a1a2-51c02124eb30/image.png)

### **참고**
---

![](https://velog.velcdn.com/images/lurelight/post/25c2a115-9741-4430-9f6d-7ed6ac0a2c77/image.png)

### **객체**
---

**Object**

키로 구분된 데이터 집합(data collection)을 저장하는 자료형

**객체 구조**

중괄호('{}')를 이용해 작성

중괄호 안에는 key : value 쌍으로 구성된 속성 (property)를 여러 개 작성 가능

key는 문자형만 허용

value는 모든 자료형 허용

![](https://velog.velcdn.com/images/lurelight/post/b4a3b0f5-921e-45c7-9354-ba166348e6a6/image.png)

**속성 참조**

점('.', chaining operator) 또는 대괄호 ('[]')로 객체 요소 접근

key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

![](https://velog.velcdn.com/images/lurelight/post/a77012d6-efc3-41ec-bcde-0d6f8d3a4fa7/image.png)

![](https://velog.velcdn.com/images/lurelight/post/87521d62-42cf-488d-b67f-195a7d111535/image.png)

**'in' 연산자**

속성이 객체에 존재하는지 여부를 확인

![](https://velog.velcdn.com/images/lurelight/post/a04fc0b1-31ff-44d2-9391-6b750266d86b/image.png)

### **객체와 함수**
---

**Method**

객체 속성에 정의된 함수

**Method 사용 예시**

object.method() 방식으로 호출

메서드는 객체를 '행동'할 수 있게 함

![](https://velog.velcdn.com/images/lurelight/post/06414656-8e96-4b7b-a06f-b61695ffbd16/image.png)

### **this**
---

**Method** 

객체 속성에 정의된 함수

▶ 'this' 키워드를 사용해 객체에 대한 특정한 작업을 수행할 수 있음

**'this' keyword**

함수나 메서드를 호출한 객체를 가리키는 키워드

▶ 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용

![](https://velog.velcdn.com/images/lurelight/post/b10d108a-ca60-4dd0-8111-7c978267bdd9/image.png)

![](https://velog.velcdn.com/images/lurelight/post/e60c53b4-50ba-4c3a-b6fb-2209dff76392/image.png)

![](https://velog.velcdn.com/images/lurelight/post/bc9b88d0-3315-4485-8217-2da8c0c6f7cc/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1361580d-9a08-4f60-827f-718d86f7ec0f/image.png)

![](https://velog.velcdn.com/images/lurelight/post/0e781308-3eec-456a-a9b0-b0f823003750/image.png)

**JavaScript 'this' 정리**

JavaScript의 함수는 호출될 때 this를 암묵적으로 전달 받음

JavaScript에서 this는 함수가 '호출되는 방식'에 따라 결정되는 현재 객체를 나타냄

Python의 self와 Java의 this 선언 시 이미 값이 정해지는 것에 비해 JavaScript의 this는 함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정됨 (동적 할당)

this가 미리 정해지지 않고 호출 방식에 의해 결정되는 것은 

장점

- 함수(메서드)를 하나만 만들어 여러 객체에서 재사용할 수 있다는 것

단점

- 이런 유연함이 실수로 이어질 수 있다는 것

▶ 개발자는 this의 동작 방식을 충분히 이해하고 장점을 취하면서 실수를 피하는데 집중

### **추가 객체 문법**
---

**1. 단축 속성**

키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축 구문을 사용할 수 있음

![](https://velog.velcdn.com/images/lurelight/post/10a765de-77f8-4d65-ab74-94cf8a3f0577/image.png)

**2. 단축 메서드**

메서드 선언 시 function 키워드 생략 가능

![](https://velog.velcdn.com/images/lurelight/post/dfbba8bc-afa3-4ea9-9ba8-88670cfc51c2/image.png)

**3. 계산된 속성 (computed property name)**

키가 대괄호([])로 둘러쌓여 있는 속성

▶ 고정된 값이 아닌 변수 값을 사용할 수 있음

![](https://velog.velcdn.com/images/lurelight/post/772ee2e6-f329-4ad0-ba94-4d5518c1e475/image.png)

**4. 구조 분해 할당 (destructing assignment)**

배열 또는 객체를 분해하여 객체 속성을 변수에 쉽게 할당할 수 있는 문법

![](https://velog.velcdn.com/images/lurelight/post/90f205ec-a075-4a68-bbfb-510c7e4c9628/image.png)

'함수의 매개변수'로 객체 구조 분해 할당 활용 가능

![](https://velog.velcdn.com/images/lurelight/post/6dec347b-eb4b-458f-9359-fb0d234da141/image.png)

**5. Object with '전개 구문'**

객체 복사

- 객체 내부에서 객체 전개

얕은 복사에 활용 가능

![](https://velog.velcdn.com/images/lurelight/post/90044a66-8846-475b-8733-e16ef361d72b/image.png)

**6. 유용한 객체 메서드**

Object.keys()

Object.values()

![](https://velog.velcdn.com/images/lurelight/post/01e7be0f-190e-40c1-9809-fc416716dafa/image.png)

**7. Optional chaining ('?.')**

속성이 없는 중첩 객체를 에러 없이 접근할 수 있는 방법

만약 참조 대상이 null 또는 undefined라면 에러가 발생하는 것 대신 평가를 멈추고 undefined를 반환

![](https://velog.velcdn.com/images/lurelight/post/b9503d76-a211-494a-ad44-470c3a2c0c05/image.png)

만약 Optional chaining을 사용하지 않는다면 다음과 같이 '&&' 연산자를 사용해야 함

![](https://velog.velcdn.com/images/lurelight/post/73b8ba0a-afe5-4336-88a0-d90fbf8c18b2/image.png)

**Optional chaining 장점**

참조로 누락될 가능성이 있는 경우 연결된 속성으로 접근할 때 더 짧고 간단한 표현식을 작성할 수 있음

어떤 속성이 필요한지에 대한 보증이 확실하지 않은 경우에 객체의 내용을 보다 편리하게 탐색할 수 있음

**Optional chaining 주의사항**

1. Optional chaining은 존재하지 않아도 괜찮은 대상에만 사용해야 함 (남용 X)

- 왼쪽 평가 대상이 없어도 괜찮은 경우에만 선택적으로 사용

- 중첩 객체를 에러 없이 접근하는 것이 사용 목적이기 때문

![](https://velog.velcdn.com/images/lurelight/post/f6c415be-979a-444e-871b-1ee52ff38871/image.png)

2. Optional chaining 앞의 변수는 반드시 선언되어 있어야 함

![](https://velog.velcdn.com/images/lurelight/post/79d0b316-8cdb-48d5-a536-58edee33298d/image.png)

**Optional chaining 정리**

1. obj?.prop

- obj가 존재하면 obj.prop를 반환하고, 그렇지 않으면 undefined를 반환

2. obj?.[prop]

- obj가 존재하면 obj[prop]를 반환하고, 그렇지 않으면 undefined 를 반환

3. obj?.method

- obj가 존재하면 obj.method()를 호출하고, 그렇지 않으면 undefined를 반환

### **JSON**
---

**JSON**

'JavaScript Object Notation'

Key-value 형태로 이루어진 자료 표기법

Javascript의 Object와 유사한 구조를 가지고 있지만 JSON은 형식이 있는 문자열

Javascript에서 JSON을 사용하기 위해서는 Object 자료형으로 변경해야 함

![](https://velog.velcdn.com/images/lurelight/post/839928e9-b158-4b57-bfc0-94dca297ecec/image.png)

### **참고**
---

![](https://velog.velcdn.com/images/lurelight/post/1f01abf1-a4c4-4a87-b244-077186712dac/image.png)

![](https://velog.velcdn.com/images/lurelight/post/0b4baa69-dba0-4206-9b95-294cb8523af6/image.png)

![](https://velog.velcdn.com/images/lurelight/post/f4055dc1-b236-4b41-9f60-7d8a42346607/image.png)

### **배열**
---

**Object**

키로 구분된 데이터 집합(data collection)을 저장하는 자료형

▶ 이제는 순서가 있는 collection이 필요

**Array**

순서가 있는 데이터 집합을 저장하는 자료구조

**배열 구조**

대괄호('[]')를 이용해 작성

요소 자료형 : 제약 없음

length 속성을 사용해 배열에 담긴 요소가 몇 개인지 알 수 있음

![](https://velog.velcdn.com/images/lurelight/post/952043d7-0dd0-4223-9715-3c3595cabb2c/image.png)

### **배열 메서드**
---

![](https://velog.velcdn.com/images/lurelight/post/6f88bb60-9d33-4bc7-89a8-d6868d6d55fc/image.png)

**push**

배열 끝에 요소를 추가

![](https://velog.velcdn.com/images/lurelight/post/e8642181-ecec-4d8b-a95b-ba2f09b661ab/image.png)

**pop()**

배열 끝 요소를 제거하고, 제거한 요소를 반환

![](https://velog.velcdn.com/images/lurelight/post/d48d10b0-ff6f-47f5-87c7-1ff4154a8eb9/image.png)

**unshift()**

배열 앞에 요소를 추가

![](https://velog.velcdn.com/images/lurelight/post/4880d76d-806e-48bb-a4a8-a2dbaefaf28d/image.png)

**shift()**

배열 앞 요소를 제거하고, 제거한 요소를 반환

![](https://velog.velcdn.com/images/lurelight/post/e2d975b6-328a-4b4f-a7ce-127f188b4709/image.png)

### **Array helper method**
---

**Array helper methods**

배열 조작을 보다 쉽게 수행할 수 있는 특별한 메서드 모임

**Array helper method**

ES6에 도입

배열의 각 요소를 순회하며 각 요소에 대해 함수 (콜백 함수)를 호출

▶ 메서드 호출 시 인자로 함수(콜백함수)를 받는 것이 특징

**콜백 함수 (Callback function)**

다른 함수에 인자로 전달하는 함수

▶ 외부 함수 내에서 호출되어 일종의 루틴이나 특정 작업을 진행

![](https://velog.velcdn.com/images/lurelight/post/e7b02f20-7fe9-4051-87d1-12693d13f1fc/image.png)

![](https://velog.velcdn.com/images/lurelight/post/52a830c0-2d24-41c7-80e3-f107dc51911e/image.png)

**forEach()**

배열의 각 요소를 반복하며 모든 요소에 대해 함수(콜백함수)를 호출

**forEach 구조**

![](https://velog.velcdn.com/images/lurelight/post/79ee98b1-7e8a-46c3-a30d-0fe0c7d3930d/image.png)

콜백함수는 3가지 매개변수로 구성

1. item : 처리할 배열의 요소

2. index : 처리할 배열 요소의 인덱스 (선택 인자)

3. array : forEach를 호출한 배열 (선택 인자)

반환 값

undefined

![](https://velog.velcdn.com/images/lurelight/post/c9b2daa0-553e-43bf-bccc-aac054906b9e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/4260aff2-9b0d-4a49-bfaf-eaf322b05554/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6fb15efd-12d1-4601-b618-54cc1a4bd6af/image.png)

![](https://velog.velcdn.com/images/lurelight/post/390c8b1c-0c8d-458d-b485-6b7a951bcfff/image.png)

![](https://velog.velcdn.com/images/lurelight/post/09c64d85-5033-4a79-adff-5499014aab27/image.png)

**map()**

배열의 모든 요소에 대해 함수를 호출하고, 반환 된 호출 결과 값을 모아 새로운 배열의 반환

![](https://velog.velcdn.com/images/lurelight/post/7868e758-9694-4cee-8286-e5d033e86448/image.png)

![](https://velog.velcdn.com/images/lurelight/post/983cea4e-a0d8-4020-a8be-1eae400379e3/image.png)

![](https://velog.velcdn.com/images/lurelight/post/a03af380-42b7-4f2f-a6f0-1edcf559971e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/bc0509db-5968-4cca-aaaa-93271d10dc6f/image.png)

![](https://velog.velcdn.com/images/lurelight/post/d12d900b-ae6e-4fb4-8c33-cb5e3051cf28/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1a2005d0-58dc-44f3-85ef-95dd2821af9a/image.png)

![](https://velog.velcdn.com/images/lurelight/post/af4aaf29-cf96-491a-ba11-1e4670bf5280/image.png)

![](https://velog.velcdn.com/images/lurelight/post/e1028c88-0739-4d38-9894-24bfbd36b1d0/image.png)

### **추가 배열 문법**
---

**Array with '전개 구문'**

![](https://velog.velcdn.com/images/lurelight/post/01129526-7996-45e3-af9b-246553d1de0e/image.png)

### **참고**
---

**콜백함수 구조를 사용하는 이유**

1. 함수의 재사용성 측면

함수를 호출하는 코드에서 콜백 함수의 동작을 자유롭게 변경할 수 있음

예를 들어, map 함수는 콜백 함수를 인자로 받아 배열의 각 요소를 순회하며 콜백 함수를 실행

이때, 콜백 함수는 각 요소를 변환하는 로직을 담당하므로, map 함수를 호출하는 코드는 간결하고 가독성이 높아짐

2. 비동기적 처리 측면

setTimeout 함수는 콜백 함수를 인자로 받아 일정 시간이 지난 후에 실행됨

이때 setTimeout 함수는 비동기적으로 콜백 함수를 실행하므로, 다른 코드의 실행을 방해하지 않음 (비동기 JavaScript에서 자세히 진행 예정)

![](https://velog.velcdn.com/images/lurelight/post/e9f44f35-09b5-419e-85b8-9178f0e75fb2/image.png)

**forEach에서 break하는 대안**

forEach에서는 break 키워드를 사용할 수 없음

대신 some 과 every의 특징을 활용해 마치 break를 사용하는 것처럼 활용할 수 있음

![](https://velog.velcdn.com/images/lurelight/post/a0347746-de50-45f5-932e-d3252df82bc6/image.png)

some을 활용한 예시

- 콜백 함수가 true를 반환하면 즉시 순회를 중단하는 특징을 활용

![](https://velog.velcdn.com/images/lurelight/post/9c7317d6-0f07-40a5-b244-b705317288bc/image.png)

every를 활용한 예시

- 콜백 함수가 false를 반환하면 즉시 순회를 중단하는 특징을 활용

![](https://velog.velcdn.com/images/lurelight/post/65961b2f-42cf-4dcb-8bf7-4a9360e291af/image.png)

**'배열은 객체다'**

배열도 키와 속성들을 담고 있는 참조 타입의 객체

배열의 요소를 대괄호 접근법을 사용해 접근하는 건 객체 문법과 같음 

- 배열의 키는 문자

숫자형 키를 사용함으로써 배열은 객체 기본 기능 이외에도 '순서가 있는 컬렉션'을 제어하게 해주는 특별한 메서드를 제공하는 것

배열은 인덱스를 키로 가지며 length 속성을 갖는 특수한 객체

![](https://velog.velcdn.com/images/lurelight/post/2c3cd509-0751-49ec-975b-23f4bbf8f537/image.png)