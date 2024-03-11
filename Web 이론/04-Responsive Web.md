### **Bootstrap Grid system**
---
Emmet cheat sheet

[Emmet cheat sheet](https://docs.emmet.io/cheat-sheet/)

vscode 자동 완성 방법

```
# 선택자와 결합자
div>.container>h1{hello}+nav>ul>li*5>a{Link $}
<div>
    <div class="container">
        <h1>hello</h1>
        <nav>
            <ul>
                <li><a href="">Link 1</a></li>
                <li><a href="">Link 2</a></li>
                <li><a href="">Link 3</a></li>
                <li><a href="">Link 4</a></li>
                <li><a href="">Link 5</a></li>
            </ul>
        </nav>
    </div>
</div>
```

**작업 꿀팁**

1. ctrl + l : 라인 한줄만 선택

2. ctrl + alt + 화살표 : 멀티 커서

3. alt + 클릭 : 멀티커서

4. alt를 누른 상태로 화살표를 이동 : 라인 이동 가능 멀티 커서

5. ctrl + d : 동일한 키워드 연속 선택

6. alt + shift + 화살표 : 선택한 라인 복사

**Bootstrap Grid system**

웹 페이지의 레이아웃을 조정하는데 사용되는 12개의 컬럼으로 구성된 시스템

12개로 나누는 이유 → 공약수가 많아서 → 레이아웃을 만들 수 있는 케이스가 많다.

![](https://velog.velcdn.com/images/lurelight/post/1cf499cb-d35a-42f7-a80b-336c9cab7ca9/image.png)

**Grid system 목적**

반응형 디자인을 지원해 웹 페이지를 모바일, 태블릿, 데스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도움

칸 나누기 게임

**반응형 웹 디자인 (Responsive Web Design)**

디바이스의 종류나 화면 크기에 상관 없이, 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술

**Grid system 기본 요소**

1. Container

Column들을 담고 있는 공간

2. Column 

실제 컨텐츠를 포함하는 부분

3. Gutter

컬럼과 컬럼 사이의 여백 영역

1개의 row안에 12개의 column 영역이 구성

▷ 각 요소는 12개 중 몇 개를 차지할 것인지 지정됨

![](https://velog.velcdn.com/images/lurelight/post/41607740-6cec-4fdc-a3c3-afc4c3599071/image.png)

![](https://velog.velcdn.com/images/lurelight/post/9c334566-a89d-4b09-88f8-661c8c78fba1/image.png)

![](https://velog.velcdn.com/images/lurelight/post/a80b40c6-91c3-4c34-bafd-e6af082382f0/image.png)

![](https://velog.velcdn.com/images/lurelight/post/9801b2fc-ce1a-4683-8a69-6706778ee08d/image.png)

![](https://velog.velcdn.com/images/lurelight/post/568ce55a-b828-44cc-bdc1-1b410f8c5af8/image.png)

```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <style>
    .box {
      border: 1px solid black;
      background-color: lightblue;
      text-align: center;
    }
  </style>
</head>

<body>
  <h2 class="text-center">Basic</h2>
  <!-- 양옆에 margin이 생기면서 가운데로 모여짐 -->
  <div class="container">
    <div class="row">
      <!-- col을 적어주면 3등분이 알아서 작동됨 -->
      <div class="box col">col</div>
      <div class="box col">col</div>
      <div class="box col">col</div>
    </div>
    <!-- 3등분을 실행하는 2번째 방법 12칸을 4 칸씩 나눠 가짐-->
    <div class="row">
      <div class="box col-4">col-4</div>
      <div class="box col-4">col-4</div>
      <div class="box col-4">col-4</div>
    </div>
    <!-- 12에서 각 칸 수 만큼 나눔 -->
    <div class="row">
      <div class="box col-2">col-2</div>
      <div class="box col-8">col-8</div>
      <div class="box col-2">col-2</div>
    </div>
  </div>

  <hr>

  <h2 class="text-center">Nesting</h2>
  <div class="container">
    <div class="row">
      <!-- 큰 단위로 먼저 나눔 -->
      <div class="box col-4">col-4</div>
      <div class="box col-8">
        <!-- 8칸 안에서 세부적으로 칸을 나눔 -->
        <div class="row">
          <div class="box col-6">col-6</div>
          <div class="box col-6">col-6</div>
          <div class="box col-6">col-6</div>
          <div class="box col-6">col-6</div>
        </div>
      </div>
    </div>
  </div>

  <hr>
  <!-- 상쇄 -->
  <h2 class="text-center">Offset</h2>
  <div class="container">
    <div class="row">
      <div class="box col-4">col-4</div>
      <div class="box col-4 offset-4">col-4 offset-4</div>
    </div>
    <div class="row">
      <!-- offset-3을 진행해 특정 칸을 비우고 작업 -->
      <div class="box col-3 offset-3">col-3 offset-3</div>
      <div class="box col-3 offset-3">col-3 offset-3</div>
    </div>
    <div class="row">
      <div class="box col-6 offset-3">col-6 offset-3</div>
    </div>
  </div>

  <hr>
  <!-- colum 사이의 간격 (여백) 생성 -->
  <h2 class="text-center">Gutters(gx-0)</h2>
  <div class="container">
    <div class="row gx-0">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>

  <hr>

  <!-- 상하 여백 생성 -->

  <h2 class="text-center">Gutters(gy-5)</h2>
  <div class="container">
    <div class="row gy-5">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>


  <br>
  <!-- gutter를 좌우로 주는 것은 컨테이너에 영향을 줌 -->
  <h2 class="text-center">Gutters(g-5)</h2>
  <div class="container">
    <div class="row g-5">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
    crossorigin="anonymous"></script>
</body>

</html>

```

![](https://velog.velcdn.com/images/lurelight/post/8892ade0-eb40-403e-916c-7b542918dbd8/image.png)

**The Grid System**

CSS가 아닌 편집 디자인에서 나온 개념으로 구성 요소를 잘 배치해서 시각적으로 좋은 결과물을 만들기 위함

기본적으로 안쪽에 있는 요소들의 오와 열을 맞추는 것에서 기인

정보 구조와 배열을 체계적으로 작성하여 정보의 질서를 부여하는 시스템

![](https://velog.velcdn.com/images/lurelight/post/f706e9e4-d929-4978-8ccd-ce2a6a56ac5e/image.png)

### **Grid system for responsive web**
---

**Responsive Web Design**

디바이스 종류나 화면 크기에 상관없이, 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술

![](https://velog.velcdn.com/images/lurelight/post/c5d3f606-8b0b-4a01-952e-79aa38108f8f/image.png)

**Grid system Breakpoints**

웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점

▷ 화면 너비에 따라 6개의 분기점 제공 (xs, sm, md, lg, xl, xxl)

![](https://velog.velcdn.com/images/lurelight/post/333d7bbd-9174-4e3c-b2ea-f5f5bfee4678/image.png)

각 breakpoints 마다 설정된 최대 너비 값 '이상으로' 화면이 커지면 grid system 동작이 변경됨

![](https://velog.velcdn.com/images/lurelight/post/e913dc28-bf4b-413a-b864-d36d2d27b380/image.png)

![](https://velog.velcdn.com/images/lurelight/post/5b4bebcf-342b-4d6c-bb2f-9d13eb61bed1/image.png)

![](https://velog.velcdn.com/images/lurelight/post/c3966c8c-1607-4e58-8765-093798350bb9/image.png)

```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <style>
    .box {
      border: 1px solid black;
      background-color: lightblue;
      text-align: center;
    }
  </style>
</head>

<body>
  <!-- breakpoint 마다 사이즈 조절 -->
  <h2 class="text-center">Breakpoints</h2>
  <div class="container">
    <div class="row">
      <!-- sm 이상일 때 6 칸씩 차지하도록 한다. -->
      <div class="box col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4 box">
        col
      </div>
      <div class="box col-12 col-sm-6 col-md-8 col-lg-3 col-xl-4 box">
        col
      </div>
      <div class="box col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4 box">
        col
      </div>
      <div class="box col-12 col-sm-6 col-md-12 col-lg-3 col-xl-12 box">
        col
      </div>
    </div>

    <hr>

    <h2 class="text-center">Breakpoints + offset</h2>
    <div class="row">
      <div class="box col-12 col-sm-4 col-md-6 box">
        col
      </div>
      <div class="box col-12 col-sm-4 col-md-6 box">
        col
      </div>
      <div class="box col-12 col-sm-4 col-md-6 box">
        col
      </div>
      <!-- md사이즈 이상서부터는 offset이 없다는 것을 명확히 해야함 -->
      <div class="box col-12 col-sm-4 offset-sm-4 col-md-6 offset-md-0 box">
        col
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
    crossorigin="anonymous"></script>
</body>

</html>

```

Grid System은 화면 크기에 따라 12개의 칸을 각 요소에 나누어 주는 것 + 6개의 breakpoint

```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>
  <h2 class="text-center">Grid Cards</h2>
  <div class="container">
    <!-- 갯수로 접근하는 방식 gy 위 아래 간격 주기-->
    <div class="row row-cols-1 row-cols-sm-3 row-cols-md-2 gy-3">
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content.</p>
          </div>
        </div>
      </div>
      <div class="col offset-sm-4 offset-md-0">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
    crossorigin="anonymous"></script>
</body>

</html>

```

### **CSS Layout 종합 정리**
---

![](https://velog.velcdn.com/images/lurelight/post/1a82a21b-45a0-4e7a-b4dc-e4f38795521b/image.png)

![](https://velog.velcdn.com/images/lurelight/post/d763e7da-9ff4-40ea-b24d-08635747a2e9/image.png)

![](https://velog.velcdn.com/images/lurelight/post/2ccbd998-807c-400a-8ce6-3d68c2363239/image.png)

![](https://velog.velcdn.com/images/lurelight/post/8cdad9aa-d80c-4ac1-89e5-ae563e986c2d/image.png)

![](https://velog.velcdn.com/images/lurelight/post/cc32576a-75b2-41ff-8192-394b10ad512c/image.png)

![](https://velog.velcdn.com/images/lurelight/post/0ca6c143-5eb2-4981-877e-770f96e19a82/image.png)

![](https://velog.velcdn.com/images/lurelight/post/4581b2f7-7542-4922-99b5-b214f99bd33f/image.png)



