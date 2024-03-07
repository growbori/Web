### **CSS Box Model**
---

**CSS Box Model**

모든 HTML 요소를 사각형 박스로 표현하는 개념

![](https://velog.velcdn.com/images/lurelight/post/2c544122-04bb-4b87-acba-faaf1f74e7a7/image.png)

![](https://velog.velcdn.com/images/lurelight/post/8c696c7e-a666-4972-ab63-7e009325affd/image.png)

**CSS Box Model** 

모든 HTML 요소를 사각형 박스로 표현하는 개념

▷ 내용 (content), 안쪽 여백 (padding), 테두리 (border), 외부 간격(margin)으로 구성되는 개념

![](https://velog.velcdn.com/images/lurelight/post/236643d2-3e7b-4cd4-afa2-2a6eb5719a1d/image.png)

![](https://velog.velcdn.com/images/lurelight/post/d2f071bd-e294-48be-988d-c9bcedd33aac/image.png)

```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .box1 {
      width: 200px;
      padding-left: 25px;
      padding-bottom: 25px;
      margin-left: 25px;
      margin-top: 50px;
      border-width: 3px;
      border-style: solid;
      border-color: black;
    }

    .box2 {
      width: 200px;
      padding: 25px 50px;
      margin: 25px auto;
      border: 1px dashed black;
    }
  </style>
</head>

<body>
  <div class="box1">box1</div>
  <div class="box2">box2</div>
</body>

</html>

```

![](https://velog.velcdn.com/images/lurelight/post/d2327de7-d4a6-4e01-8c34-545a01bc6aa6/image.png)

**width & height 속성**

요소의 너비와 높이를 지정

이때 지정되는 요소의 너비와 높이는 콘텐츠 영역을 대상으로 함

![](https://velog.velcdn.com/images/lurelight/post/27ad6df8-9231-4841-935d-1e4b36b54309/image.png)

**CSS가 width 값을 계산하는 기준**

CSS는 border가 아닌 content의 크기를 width 값으로 지정

![](https://velog.velcdn.com/images/lurelight/post/db87baf5-709c-44aa-9df4-43497cad3d42/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6945e852-e39a-4141-b1b2-0e1839d54240/image.png)

```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .box {
      width: 100px;
      border: 2px solid black;
      padding: 10px;
      margin: 20px;
      background-color: yellow;
    }

    .content-box {
      box-sizing: content-box;
    }

    .border-box {
      box-sizing: border-box;
    }
  </style>
</head>

<body>
  <div class="box content-box">content-box</div>
  <div class="box border-box">border-box</div>
</body>

</html>

```

![](https://velog.velcdn.com/images/lurelight/post/24092eeb-c1d4-4aaa-8897-63e4df2744ab/image.png)

border box로 작업해야 박스 사이즈를 명확히 할 수 있음

![](https://velog.velcdn.com/images/lurelight/post/484ca0dc-0f37-4ba0-bd76-5c335c649b89/image.png)

![](https://velog.velcdn.com/images/lurelight/post/b0589a9e-f7a5-404a-8eae-7ad473e9eae3/image.png)

CSS를 적용하지 않았을 경우, 무조건 좌측 상단에서부터 요소들이 배치됨(글, 사진 무관)

block direction 무조건 아랫방향으로 영향 오른쪽 모든 요소를 차지하고 있기 때문에

![](https://velog.velcdn.com/images/lurelight/post/f2000e61-dd65-4112-81ec-c0220f14f7bf/image.png)

![](https://velog.velcdn.com/images/lurelight/post/ed459201-675e-4fb4-aaae-11d1cd5592c5/image.png)

![](https://velog.velcdn.com/images/lurelight/post/82d91b52-43e8-4860-966c-b408b1703d33/image.png)

![](https://velog.velcdn.com/images/lurelight/post/763edd4f-18cf-4ce2-8122-1b2b69690581/image.png)

정렬의 주체에 중심을 두지 않고 영역을 어떻게 나눌지를 고민해야 함

**기타 display 속성**

![](https://velog.velcdn.com/images/lurelight/post/9223f0a5-08a4-42f5-b5cf-3fa25820765a/image.png)

![](https://velog.velcdn.com/images/lurelight/post/18584874-31d4-4724-a17c-9136fcb0bc68/image.png)

```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    span {
      margin: 20px;
      padding: 20px;
      width: 80px;
      height: 50px;
      background-color: lightblue;
      border: 2px solid blue;
      /* display: inline-block; */
    }

    ul>li {
      background-color: crimson;
      padding: 10px 20px;
      /* display: inline-block; */
    }


    .box {
      /* display: inline-block; */
      width: 100px;
      height: 100px;
      background-color: #4CAF50;
      margin: 10px;
    }

    .container {
      /* text-align: center; */
    }
  </style>
</head>

<body>
  <!-- 1. 이제 다른 요소를 밀어낼 수 있는 span -->
  <p>Lorem ipsum dolor sit amet <span>consectetur</span> adipisicing elit. Animi iusto enim officia exercitationem
    dolorque, quasi velit, dolores, tempora illum odio necessitatibus. Fugit,
    cumque eligendi!</p>

  <!-- 2. 리스트 요소를 가로로 정렬 -->
  <ul>
    <li><a href="#">link</a></li>
    <li><a href="#">link</a></li>
    <li><a href="#">link</a></li>
  </ul>

  <!-- 3. div 요소를 가로로 정렬 -->
  <div class="container">
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
  </div>
</body>

</html>

```

![](https://velog.velcdn.com/images/lurelight/post/35765d7e-5ba2-4c57-8c3a-5be21102e6f9/image.png)

![](https://velog.velcdn.com/images/lurelight/post/b3a72737-ebc9-421a-b7ef-37293d926dab/image.png)

![](https://velog.velcdn.com/images/lurelight/post/645498c1-de1e-4be3-9f4b-773b73a832c3/image.png)

![](https://velog.velcdn.com/images/lurelight/post/b8535a75-9fc6-4a6e-bd8b-27c765a0e24b/image.png)

![](https://velog.velcdn.com/images/lurelight/post/0ddcb582-77fc-4615-a5e7-73cdc290925e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/a6dd09d2-b764-4ab9-9a72-ed0eb8f77965/image.png)

### **CSS Position**
---

**CSS Layout**

각 요소의 위치와 크기를 조정하여 웹 페이지의 디자인을 결정하는 것

Display, Position, Float, Flexbox 등

**CSS Position**

요소를 Normal Flow에서 제거하여 다른 위치로 배치하는 것

다른 요소 위에 올리기, 화면의 특정 위치에 고정시키기 등

![](https://velog.velcdn.com/images/lurelight/post/614aae98-977e-4746-8a9e-8e34b76c8d14/image.png)

![](https://velog.velcdn.com/images/lurelight/post/d913352f-b2de-4940-b212-bec4194526b6/image.png)

absolute의 기준 필요 : static이 아닌 부모 찾음

![](https://velog.velcdn.com/images/lurelight/post/45e4a9be-c7c1-4eec-9cbe-9c3332e5df5c/image.png)

![](https://velog.velcdn.com/images/lurelight/post/08e5bdf9-5535-4a7c-9605-3d3eb3f8955b/image.png)

![](https://velog.velcdn.com/images/lurelight/post/3fb4a733-a2ea-47e9-930e-079b9fbf492d/image.png)

![](https://velog.velcdn.com/images/lurelight/post/3214ed3e-24d0-4356-848c-d0390a328309/image.png)

![](https://velog.velcdn.com/images/lurelight/post/6b8912d0-b66b-4e28-8851-d65a2f22eaff/image.png)

**z-index**

요소가 겹쳤을 때 어떤 요소 순으로 위에 나타낼 지 결정

**z-index 특징**

정수 값을 사용해 Z 축 순서를 지정

더 큰 값을 가진 요소가 작은 값의 요소를 덮음
```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .container {
      position: relative;
    }

    .box {
      position: absolute;
      width: 100px;
      height: 100px;
    }

    .red {
      background-color: red;
      top: 50px;
      left: 50px;
      /* z-index: 3; */
    }

    .green {
      background-color: green;
      top: 100px;
      left: 100px;
      /* z-index: 2; */
    }

    .blue {
      background-color: blue;
      top: 150px;
      left: 150px;
      /* z-index: 1; */
    }
  </style>
</head>

<body>
  <div class="container">
    <div class="box red"></div>
    <div class="box green"></div>
    <div class="box blue"></div>
  </div>
</body>

</html>

```
![](https://velog.velcdn.com/images/lurelight/post/19e17c2f-c164-4cd4-97e4-aad9fea2723f/image.png)

### **참고**
---

**Position의 역할**

전체 페이지에 대한 레이아웃을 구성하는 것이 아닌 페이지 특정 항목의 위치를 조정하는 것

### **CSS Flexbox**
---

**CSS Flexbox**

요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식

▶ 공간 배열 & 정렬

![](https://velog.velcdn.com/images/lurelight/post/0181bdc1-2d41-4a82-9a0a-cb17c5273518/image.png)

**구성 요소**

![](https://velog.velcdn.com/images/lurelight/post/e96e99ca-3ea5-47e6-8331-3e220e6022a8/image.png)

![](https://velog.velcdn.com/images/lurelight/post/57f1686b-37ba-496e-95f2-1c9f196e6183/image.png)

![](https://velog.velcdn.com/images/lurelight/post/0b985bb3-eb36-4371-a3fe-52473b3c3480/image.png)

![](https://velog.velcdn.com/images/lurelight/post/8d4ca9fe-1c5d-4986-83c2-7e4c119cfe86/image.png)

![](https://velog.velcdn.com/images/lurelight/post/62aa264f-b72f-4e05-a1ee-224f5876d329/image.png)

Flex container가 컨트롤 할 것임

**레이아웃 구성**

![](https://velog.velcdn.com/images/lurelight/post/8a1bd31e-0ab1-4767-a5aa-6b0a5ab46ee8/image.png)

![](https://velog.velcdn.com/images/lurelight/post/cc65cd83-afd9-424b-85b6-fc4820b8e1af/image.png)

![](https://velog.velcdn.com/images/lurelight/post/0475bf2f-e3ee-4e34-b951-491d2333e302/image.png)

![](https://velog.velcdn.com/images/lurelight/post/93555e7d-609a-45aa-91c1-f0c3ad7e9c80/image.png)

![](https://velog.velcdn.com/images/lurelight/post/28fbb602-255b-4484-a93d-4c326f74b206/image.png)

![](https://velog.velcdn.com/images/lurelight/post/d1175e36-76f3-44a3-ac06-60d1cc0a78c4/image.png)

![](https://velog.velcdn.com/images/lurelight/post/f6f0466b-419b-49f5-b3b3-2e2866b33dc8/image.png)

![](https://velog.velcdn.com/images/lurelight/post/c05d2c4d-5553-406e-a473-8d0ee18ecc92/image.png)

**목적에 따른 속성 분류**

배치 : flex direction, flex-wrap

공간 분배 : justify-content, align-content

정렬 : align-items, align-self

**속성명 tip**

justify : 주축

align : 교차축

contents → 여러줄

items → 한줄

self → 요소 한개

![](https://velog.velcdn.com/images/lurelight/post/528d66c9-aef0-4677-994a-2c92f22d6a76/image.png)

![](https://velog.velcdn.com/images/lurelight/post/ef25a20c-c75c-440d-b8c7-6c6a2687d9c6/image.png)

![](https://velog.velcdn.com/images/lurelight/post/a05340ed-154d-435f-bb98-84d0766518dc/image.png)


```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .container {
      width: 100%;
      display: flex;
    }

    .item {
      height: 100px;
      color: white;
      font-size: 3rem;
    }

    .item-1 {
      background-color: red;
      flex-basis: 200px;
    }

    .item-2 {
      background-color: green;
      flex-basis: 400px;
    }

    .item-3 {
      background-color: blue;
      flex-basis: 200px;
    }
  </style>
</head>

<body>
  <div class="container">
    <div class="item item-1">1</div>
    <div class="item item-2">2</div>
    <div class="item item-3">3</div>
  </div>
</body>

</html>

```

### **flex-wrap 응용**
---

**반응형 레이아웃**

다양한 디바이스와 화면 크기에 자동으로 적응하여 콘텐츠를 최적으로 표시하는 웹 레이아웃 방식

```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .card {
      width: 80%;
      border: 1px solid black;
      display: flex;
      flex-wrap: wrap;
    }

    img {
      width: 100%;
    }

    .thumbnail {
      flex-basis: 700px;
      flex-grow: 1;
    }

    .content {
      flex-basis: 350px;
      flex-grow: 1;
    }
  </style>
</head>

<body>
  <div class="card">
    <img class="thumbnail" src="images/sample.jpg" alt="sample">
    <div class="content">
      <h2>Heading</h2>
      <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis minus sed expedita ut nihil tempora
        neque autem odio eos, repudiandae blanditiis, molestiae consequatur. Adipisci illo dolor repellat alias
        maiores.
        Aut?</p>
    </div>
  </div>
</body>

</html>

```

![](https://velog.velcdn.com/images/lurelight/post/94500cc8-f0f7-46d7-aa14-4df7f9b1f89a/image.png)

### **정리**
---

![](https://velog.velcdn.com/images/lurelight/post/086212ea-3992-4fd5-be59-5060f41b91b2/image.png)

![](https://velog.velcdn.com/images/lurelight/post/cb197332-d94c-4db1-826c-1944b7273073/image.png)

![](https://velog.velcdn.com/images/lurelight/post/eed8d951-bb0e-4476-ae23-7f50f84d023e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/044ffe7f-8689-45f7-bf9a-17045891d5eb/image.png)

![](https://velog.velcdn.com/images/lurelight/post/9a35e9e5-1ce9-43bf-ae38-3c7768ff1de4/image.png)

![](https://velog.velcdn.com/images/lurelight/post/85298c23-1aa0-49d4-8626-3f081861a837/image.png)

![](https://velog.velcdn.com/images/lurelight/post/916eae4c-efe6-4932-8991-aed2fbc5b4ff/image.png)

![](https://velog.velcdn.com/images/lurelight/post/b610f4dc-5d5a-434a-a2dc-f5690e2aee73/image.png)

![](https://velog.velcdn.com/images/lurelight/post/753b5b9b-1b08-471e-8511-7c249dab34de/image.png)
