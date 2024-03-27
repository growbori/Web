### **Django Form**
---

**HTML 'form'**

지금까지 사용자로부터 데이터를 받기 위해 활용한 방법 그러나 비정상적인 혹은 악의적인 요청을 필터링 할 수 없음 

→ 유효한 데이터인지에 대한 확인 필요

**유효성 검사**

수집한 데이터가 정확하고 유효한지 확인하는 과정

**유효성 검사 구현**

유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복 범위, 보안 등 많은 것을 고려해야 함

이런 과정와 기능을 직접 개발하는 것이 아닌 Django가 제공하는 Form을 사용

### **Form Class**
---

**Django Form**

사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구

→ 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공

![](https://velog.velcdn.com/images/lurelight/post/16065f04-6c7c-43b5-9c51-c8e4801cba65/image.png)

![](https://velog.velcdn.com/images/lurelight/post/3e2e0d9c-b88b-4c91-ba7e-74a1806ab315/image.png)

![](https://velog.velcdn.com/images/lurelight/post/f3f968b2-6d0b-4a30-bad0-448b731bc277/image.png)

![](https://velog.velcdn.com/images/lurelight/post/4669fe16-2c18-4108-8259-6134ced035c6/image.png)

![](https://velog.velcdn.com/images/lurelight/post/075280c5-eec9-470b-b5cd-ca017d6257ad/image.png)

![](https://velog.velcdn.com/images/lurelight/post/662fc5c9-a3b1-4813-85f5-94c75397519f/image.png)

### **Widgets**
---

**Widgets**

HTML 'input' element의 '표현'을 담당

![](https://velog.velcdn.com/images/lurelight/post/78228c73-5e37-40b5-bde8-c852c833f6fb/image.png)

### **Django Modelform**
---

**Form**

사용자 입력 데이터를 DB에 저장하지 않을 때 (ex. 로그인)

**ModelForm**

사용자 입력 데이터를 DB에 저장해야 할 때 (ex. 게시글 작성, 회원 가입)

![](https://velog.velcdn.com/images/lurelight/post/96d4bd63-c594-4eff-919c-fdb683e205dd/image.png)

![](https://velog.velcdn.com/images/lurelight/post/00b21b7e-5d21-403f-a9d8-7155b2e88777/image.png)

**Meta class**

ModelForm의 정보를 작성하는 곳

![](https://velog.velcdn.com/images/lurelight/post/39cafad6-775f-4f12-ae9d-4c389b98fce3/image.png)

![](https://velog.velcdn.com/images/lurelight/post/957dcef7-aad4-4010-bbe9-ad7b5f3a6c61/image.png)

![](https://velog.velcdn.com/images/lurelight/post/1a1c96a6-9add-4f3f-8178-6c9ddcada722/image.png)

**is_valid()**

여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 Boolean으로 반환

![](https://velog.velcdn.com/images/lurelight/post/8c3f87a9-3550-4b8d-bd14-4286ee33fbe8/image.png)

![](https://velog.velcdn.com/images/lurelight/post/587cf3c2-6e9f-4fc4-9fe1-4c90a8eb1833/image.png)

![](https://velog.velcdn.com/images/lurelight/post/0c037d92-d6aa-451f-9a30-df9fb66e3000/image.png)

**save()**

데이터베이스 객체를 만들고 저장

![](https://velog.velcdn.com/images/lurelight/post/9fe6f86f-a348-48c3-b8c2-7c3d57377f18/image.png)

**Django Form 정리**

사용자로부터 데이터를 수집하고 처리하기 위한 강력하고 유연한 도구

HTML form의 생성, 데이터 유효성 검사 및 처리를 쉽게 할 수 있도록 도움

### **Handling HTTP requests**
---

**view 함수 구조 변화**

new & create view 함수간 공통점

데이터 생성을 구현하기 위함

new & create view 함수간 차이점

new는 GET method 요청만을, create는 POST method 요청만을 처리

HTTP request method 차이점을 활용해 동일한 목적을 가지는 2개의 view 함수를 하나로 구조화

![](https://velog.velcdn.com/images/lurelight/post/ec2b2015-b02f-495e-a0ed-75971bfb3feb/image.png)

![](https://velog.velcdn.com/images/lurelight/post/daff38ee-2f7f-48bf-b7df-1d85eb38c097/image.png)

![](https://velog.velcdn.com/images/lurelight/post/9d75392a-d048-46b4-94e3-57d3f7b8cd2e/image.png)

![](https://velog.velcdn.com/images/lurelight/post/c3a07e32-506a-4d84-9a8a-a127dbebcf0a/image.png)

![](https://velog.velcdn.com/images/lurelight/post/178adefa-414a-4b8d-bf37-734726bd4978/image.png)

![](https://velog.velcdn.com/images/lurelight/post/ebfb8f9f-50d9-4009-b8a3-745ca066befc/image.png)

![](https://velog.velcdn.com/images/lurelight/post/c6ee246e-8fbe-428a-bc14-da004e848d8a/image.png)

![](https://velog.velcdn.com/images/lurelight/post/adcfb37c-1ca7-4133-8e93-3dd917d3ef24/image.png)

![](https://velog.velcdn.com/images/lurelight/post/da2f8bc2-d88b-4158-b9bf-82c49199175b/image.png)

![](https://velog.velcdn.com/images/lurelight/post/31e983dd-9765-4179-aba6-efa0b887222e/image.png)

