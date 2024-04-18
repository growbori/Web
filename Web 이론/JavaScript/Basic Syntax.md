### **변수 선언 키워드**
---

**식별자(변수명)작성 규칙**

반드시 문자, 달러 또는 밑줄로 시작

대소문자를 구분

예약어 사용 불가 

- for, if, function 등

**식별자(변수명) Naming case**

카멜 케이스 (camelCase)

- 변수, 객체, 함수에 사용

파스칼 케이스 (PascalCase)

- 클래스, 생성자에 사용

대문자 스네이크 케이스 (SNAKE_CASE)

- 상수(constants)에 사용

**변수 선언 키워드 3가지**

1. let

2. const

3. var

**let**

블록 스코프(block scope)를 갖는 지역 변수를 선언

재할당 가능

재선언 불가능

ES6에서 추가

![](https://velog.velcdn.com/images/lurelight/post/78fe13c2-716b-4a4b-9aca-74fd4a040101/image.png)

**const**

블록 스코프를 갖는 지역변수를 선언

재할당 불가능

재선언 불가능

ES6에서 추가

![](https://velog.velcdn.com/images/lurelight/post/b8e040a7-d774-4b5e-8c99-1ac60d643a6e/image.png)

블록 스코프 (block scope)


if, for, 함수 등의 '중괄호({}) 내부'를 가리킴

블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

![](https://velog.velcdn.com/images/lurelight/post/8be24394-96fb-4510-bf9a-69a1a6adfd96/image.png)

**어떤 변수 선언 키워드를 사용해야 할까?**

기본적으로 const 사용을 권장

재할당이 필요하다면 그때 let으로 변경해서 사용

### **데이터 타입**
---

**원시 자료형 (Primitive type)**

Number, String, Boolean, null, undefined

변수에 값이 직접 저장되는 자료형 (불변, 값이 복사)

**참조 자료형 (Reference type)**

Objects (Object, Array, Function)

객체의 주소가 저장되는 자료형 (가변, 주소가 복사)

**원시 자료형 예시**

변수에 할당될 때 값이 복사됨

- 변수 간에 서로 영향을 미치지 않음

![](https://velog.velcdn.com/images/lurelight/post/70428e7a-43ec-4c75-ae20-bac8ad7f1b7b/image.png)

**참조 자료형 예시**

객체를 생성하면 객체의 메모리 주소를 변수에 할당

- 변수 간에 서로 영향을 미침

![](https://velog.velcdn.com/images/lurelight/post/49ee3e76-c4ba-431a-a25a-cd620b04eedb/image.png)

### **원시 자료형**
---

**원시 자료형 종류**

Number

String

null

undefined

Boolean

**Number**

정수 또는 실수형 숫자를 표현하는 자료형

![](https://velog.velcdn.com/images/lurelight/post/9b33345d-d186-4d99-a60b-ea8e351dc9a6/image.png)

**String**

텍스트 데이터를 표현하는 자료형

![](https://velog.velcdn.com/images/lurelight/post/a6c10806-1e8d-4893-a751-3a743c86b242/image.png)

Template literals(템플릿 리터럴)

내장된 표현식을 허용하는 문자열 작성 방식

Backtick을 이용하며, 여러 줄에 걸쳐 문자열을 정의할 수 있고 JavaScript의 변수를 문자열 안에 바로 연결할 수 있음

표현식은 '$'와 중괄호 (${expression})로 표기

ES6+부터 지원

![](https://velog.velcdn.com/images/lurelight/post/fd6b2933-93a3-4a17-a423-817b03e6cc19/image.png)

**null 과 undefined**

null 

변수의 값이 없음을 의도적으로 표현할 때 사용

undefined

변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨

![](https://velog.velcdn.com/images/lurelight/post/af297213-ce22-454d-95b8-357e347b7dcf/image.png)

**'값이 없음'에 대한 표현이 null과 undefined 2가지인 경우**

JavaScript의 설계 실수

null이 원시 자료형 임에도 불구하고 object로 출력되는 이유는 JavaScript 설계 당시의 버그를 해결하지 않은 것

- 해결하지 못하는 이유는 이미 null 타입에 의존성을 띄고 있는 수 많은 프로그램들이 망가질 수 있기 때문 (하위 호환 유지)

![](https://velog.velcdn.com/images/lurelight/post/a0db00ca-5c1d-4751-af69-6b9bedaa1eb2/image.png)

**Boolean**

조건문 또는 반복문에서 Boolean이 아닌 데이터 타입은 '자동 형변환 규칙'에 따라 true 또는 false로 변환됨

![](https://velog.velcdn.com/images/lurelight/post/b03c8862-d7f1-49dc-8328-ac960fb4f1ed/image.png)

### **연산자**
---

**할당 연산자**

피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자

단축 연산자 지원

![](https://velog.velcdn.com/images/lurelight/post/555f3424-02b2-4afd-ab80-24b438b9e3f6/image.png)

증가 & 감소 연산자

증가 연산자 ('++')

- 피연산자를 증가(1을 더함)시키고 연산자의 위치에 따라 증가하기 전이나 후의 값을 반환

감소 연산자 ('--')

- 피연산자를 감소 (1을 뺌)시키고 연산자의 위치에 따라 감소하기 전이나 후의 값을 반환

→ '+=' 또는 '-='와 같이 더 명시적인 표현으로 작성하는 것을 권장

![](https://velog.velcdn.com/images/lurelight/post/0a2d6543-67b2-4970-a6db-704682613f7c/image.png)

**비교 연산자**

피연산자들(숫자, 문자, Boolean 등)을 비교하고 결과 값을 boolean으로 반환하는 연산자

![](https://velog.velcdn.com/images/lurelight/post/85efc416-926b-4365-a811-c54fb90ed0fb/image.png)

**동등 연산자 (==)**

두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환

'암묵적 타입 변환'을 통해 타입을 일치시킨 후 같은 값인지 비교

두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별

![](https://velog.velcdn.com/images/lurelight/post/1b240c68-c256-4d2f-955e-b94f4d8fbee9/image.png)

**일치 연산자(===)**

두 피연산자의 값과 타입이 모두 같은 경우 true를 반환

같은 객체를 가리키거나, 같은 타입이면서 같은 값인지를 비교

엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음

특수한 경우를 제외하고는 동등 연산자가 아닌 일치 연산자 사용 권장

![](https://velog.velcdn.com/images/lurelight/post/c29235ce-f06e-43b7-a813-bb7273e165f4/image.png)

![](https://velog.velcdn.com/images/lurelight/post/5ad7b372-1b9a-4960-a87c-2ce5971b23aa/image.png)

### 조건문
---

**if**

조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓을 판단

![](https://velog.velcdn.com/images/lurelight/post/3e4ee63b-ced7-409c-8435-2b48ebf02486/image.png)

**삼항 연산자**

![](https://velog.velcdn.com/images/lurelight/post/4938b8e7-8153-4489-9f30-0abe35f23281/image.png)

condition

- 평가할 조건 (true 또는 false로 평가)

expression1

- 조건이 true일 경우 반환할 값 또는 표현식

expression2

- 조건이 false일 경우 반환할 값 또는 표현식

**삼항 연산자 예시**

간단한 조건부 로직을 간결하게 표현할 때 유용

하지만 복잡한 로직이나 대다수의 경우에는 가독성이 떨어질 수 있으므로 적절한 상황에서만 사용할 것

![](https://velog.velcdn.com/images/lurelight/post/111183bc-1524-46e8-9af1-5cfbe8b44bb0/image.png)

**반복문**

while

for

for...in

for...of

**while**

조건문이 참이면 문장을 계속해서 수행

![](https://velog.velcdn.com/images/lurelight/post/3058c106-2dff-458a-88b5-9d8bf15e1645/image.png)

![](https://velog.velcdn.com/images/lurelight/post/e5b5c8f6-450b-4670-b115-37f7450e3a00/image.png)

**for**

특정한 조건이 거짓으로 판별될 때까지 반복

![](https://velog.velcdn.com/images/lurelight/post/02b3cdd9-c4a8-4a2b-b85d-9357c86b7fc8/image.png)

![](https://velog.velcdn.com/images/lurelight/post/4b52adb3-eba6-4ae5-bc4e-c762b7370e40/image.png)

![](https://velog.velcdn.com/images/lurelight/post/a47a7a14-f752-4e1c-af5e-dfc9ec1d2495/image.png)

**for ...in**

객체의 열거 가능한 속성(property)에 대해 반복

![](https://velog.velcdn.com/images/lurelight/post/bc2ec147-0c11-45ee-82f9-a8c7e6b61321/image.png)

![](https://velog.velcdn.com/images/lurelight/post/948b8608-db3e-4747-b235-645b9975a483/image.png)

**for ...of**

반복 가능한 객체(배열, 문자열 등)에 대해 반복

![](https://velog.velcdn.com/images/lurelight/post/3d98e6bf-1199-4e75-a592-a2ab40fbee96/image.png)

![](https://velog.velcdn.com/images/lurelight/post/9b821da6-8884-4532-b9df-0b2ceb6e0885/image.png)

![](https://velog.velcdn.com/images/lurelight/post/941c4937-0fd0-46e2-84a5-d81a9be03379/image.png)

배열 반복과 for ...in

객체 관점에서 배열의 인덱스는 정수 이름을 가진 열거 가능한 속성

for ...in은 정수가 아닌 이름과 속성을 포함하여 열거 가능한 모든 속성을 반환

내부적으로 for ...in은 배열의 반복자가 아닌 속성 열거를 사용하기 때문에 특정 순서에 따라 인덱스를 반환하는 것을 보장할 수 없음

→ for ...in은 인덱스의 순서가 중요한 배열에서는 사용하지 않음

→ 배열에서는 for문, for ...of 를 사용

객체 관점에서 배열의 인덱스는 정수 이름을 가진 속성이기 때문에 인덱스가 출력됨 (순서 보장 X)

![](https://velog.velcdn.com/images/lurelight/post/bcb83fea-c42a-42d6-915b-1e20298d15d9/image.png)

반복문 사용 시 const 사용 여부

for 문

for (let i = 0; i < arr.length; i++) {...}의 경우에는 최초 정의한 i를 '재할당'하면서 사용하기 때문에 const를 사용하면 에러 발생

for ...in, for ...of

재할당이 아니라, 매 반복마다 다른 속성 이름이 변수에 지정되는 것이므로 const를 사용해도 에러가 발생하지 않음

단 const 특징에 따라 블록 내부에서 변수를 수정할 수 없음

![](https://velog.velcdn.com/images/lurelight/post/468489ac-fd1f-4d3d-9d81-290647305c07/image.png)

### **참고**
---

**세미콜론 (semicolon)**

자바스크립트는 문장 마지막 세미콜론 (';')을 선택적으로 사용 가능

세미콜론이 없으면 ASI에 의해 자동으로 세미콜론이 삽입됨 

- ASI (Automatic Semicolon Insertion, 자동 세미콜론 삽입 규칙)

JavaScript를 만든 Brendan Eich 또한 세미콜론 작성을 반대

변수 선언 키워드 - 'var'

ES6 이전에 변수 선언에 사용했던 키워드

재할당 가능 & 재선언 가능

함수 스코프 (function scope)를 가짐

'호이스팅'되는 특성으로 인해 예기치 못한 문제 발생 가능

→ 따라서 ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장

변수 선언 시 var, const, let 키워드 중 하나를 사용하지 않으면 자동으로 var로 선언 됨

**함수 스코프 (function scope)**

함수의 중괄호 내부를 가리킴

함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능

![](https://velog.velcdn.com/images/lurelight/post/4b56a4ca-8954-44e4-a90d-377a22cae25f/image.png)

**호이스팅 (hoisting)**

변수를 선언 이전에 참조할 수 있는 현상

변수 선언 이전의 위치에서 접근 시 undefined를 반환

![](https://velog.velcdn.com/images/lurelight/post/2e6f342c-7f18-446f-a06c-2ff382b618df/image.png)

JavaScript에서 변수들은 실제 실행시에 코드의 최상단으로 끌어 올려지게 되며 (hoisted) 이러한 이유 때문에 var로 선언된 변수는 선언 시에 undefined로 값이 초기화되는 과정이 동시에 발생

![](https://velog.velcdn.com/images/lurelight/post/3aacad15-c568-47d3-9f0e-e6c52f1c144c/image.png)

**NaN을 반환하는 경우 예시**

1. 숫자로서 읽을 수 없음 (Number(undefined))

2. 결과가 허수인 수학 계산식 (Math.sqrt(-1))

3. 피연산자가 NaN (7 ** NaN)

4. 정의할 수 없는 계산식 (0 * Infinity)

5. 문자열을 포함하면서 덧셈이 아닌 계산식 ('가'/3)

