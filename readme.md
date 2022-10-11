# fastapi 설치

> pip install fastapi
> pip install uvicorn

### 실행
>uvicorn main:server --reload --host=0.0.0.0 --port=8000
#
# todo list web site 만들기

### mongodb
> pymongo 모듈을 사용해서 처리

# API URL 소개
![image](https://user-images.githubusercontent.com/104962364/195105978-8b328d20-813d-406d-b56a-4ac8042f9647.png)


# Design 구성 (프론트는 바닐라JS로 제작)
* 로그인
![image](https://user-images.githubusercontent.com/104962364/195106222-1ae77743-107a-4a92-8d74-adf03ea11d82.png)

* 회원가입
![image](https://user-images.githubusercontent.com/104962364/195106471-0923e5a1-1f35-402d-80f4-e435a372837c.png)


* 기능 폼1(추가 기능)
![image](https://user-images.githubusercontent.com/104962364/195106626-df12c263-a444-4857-a1d6-8590c8e80528.png)

* 기능 폼2(리스트 조회, node별 삭제 기능)
![image](https://user-images.githubusercontent.com/104962364/195106832-8c7ec594-f2c1-4226-8196-68f7b4691339.png)


# 보안해야되는 상황
```💫일단 1차적으로 만든거라서, secret 이라 jwt 관련한 부분들 .env 로 분리도 안되있고, 대체적으로 만드는거에 중점을 두다보니, 코드가 더럽다.```

  1. 조금 더 로그인 관련해서 다듬기 현재 요청이 많이 없을꺼같아서 accessToken 을 발급하고 db에 저장해서 db안에있는 토큰과 같으면 유효한 형태로 만들었다. 다른 로그인 방식(보안성있는)을 생각하면 좋을거같음.
  
  2. 프론트에서 좀 더 다이나믹하게 내용을 수정, complete 모션, 전체 삭제, 그리고 js 파트에 for문을 foreach로 변경해서 가독성도 올려야할거같음.

  3. 현재 그냥 api 에 접속할때마다 인증을 해야하는데, 형태를 바꿔서 인증부 api 를 개설해서 프론트에서 인증부 api 를 선 진행 후, 나머지 기능을 진행하도록 형식 변경
  
  4. 클래스화도 필요할거 같고, 모델링도 조금 더 생각하고, 겹치는 코드부분이 많은데 하나로 합치는 작업이 필요할거같음.  
