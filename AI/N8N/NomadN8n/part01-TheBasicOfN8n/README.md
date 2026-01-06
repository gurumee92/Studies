# N8N의 기본

## Your First Workflow

워크플로우는 3가지 구성 요소가 있다.

1. trigger: 워크플로우의 시작점, 이벤트를 감지해서 워크플로우를 시작한다.
  * manual, event, scheduled..
2. node: 특정 일을 수행하는 작업 단위
  * 입력을 받아 출력을 만들어낸 후 다음 노드로 전달한다.
3. edge: 노드 간 데이터 흐름을 이어주는 화살표

목표:
1. Manual Trigger 생성
2. API(`https://zenquotes.io/api/random`)에서 명언을 받는 노드 생성 및 1번에 연결

숙제:
* Manual Trigger -> HTTP Request

## Data Flow

목표: 
1. Manual Trigger 생성
2. API(`https://zenquotes.io/api/random`)에서 명언을 받는 노드 생성 및 1번에 연결
3. AI를 활용하여 한글 번역하는 노드 생성 및 2번 노드에 연결
  * `{{Author}}: {{Quote}}` 형태로 만들어보자.


숙제: 
* Manual Trigger -> HTTP Request -> Gemini (Message Model) 

## Expressions and Schedules

표현 식은 `{{ JS expression }}`를 따름. 

```js
// {{ expression }}
{{ $json.q }}

// or function
{{ new Date() }}
```

모든 노드는 빌트인 변수들과 함수들이 있다. (ex: `$json`)

클라우드를 사용할 경우, Manual Trigger 구성 시, 실행할 때마다 실행 횟수에는 들어가지 않는다. 이것은 Scheduled Trigger 구성 시 자동으로 실행할 때 세는 횟수를 의미한다.

목표:
1. Manual Trigger 생성
2. API(`https://zenquotes.io/api/random`)에서 명언을 받는 노드 생성 및 1번에 연결
3. AI를 활용하여 한글 번역하는 노드 생성 및 2번 노드에 연결
4. Gmail 노드 생성 및 3번 연결
  * `Options` 유의해서 보기

숙제: 
* Manual Trigger -> HTTP Request -> Gemini -> Gmail
* Manual Trigger => Scheduled Trigger로 변경해보자.

## Execution Order

노드를 복제할 수 있다. 보통 워크플로우는 위에서 아래 순서대로 실행된다.

목표:
1. Manual Trigger 생성
2. API(`https://zenquotes.io/api/random`)에서 명언을 받는 노드 생성 및 1번에 연결
3. AI를 활용하여 1가지 언어로 번역하는 노드 생성 및 2번 노드에 연결
  1. 한국어
  2. 프랑스어
  3. 독일어
4. 3-1, 3-2, 3-3 각각 Gmail 노드를 복사 후 연결하여 결과 보내기

숙제: 
* Manual Trigger -> HTTP Request -> Gemini -> Gmail
                 -> HTTP Request -> Gemini -> Gmail

## Practice Project

조금 더 복잡한 노드를 만들어보자.

목표:
1. Manual Trigger 생성
2. API(`https://icanhazdadjoke.com`)에서 명언을 받는 노드 생성 및 1번에 연결
3. If 노드 생성, 응답 코드 체크 `{{ $json.status }}`
  1. false 일 경우, Wait 노드 생성 및, 2번 앞에 연결
  2. true일 경우, 4번 연결
4. AI 노드 생성 및 3-2번 노드 연결
  * 이 조크가 웃긴지 알려줘 `<joke>{{ $json.joke }}</joke>`
  * 결과를 text로 is_funny or is_not_funny로 나타내
  * 지독한 유머 비평가야
5. If 노드 생성 4번 노드 결과 응답이 2개 중 하나인지 판단
  1. false일 경우, 4번 노드 연결
  2. true일 경우, 6번 노드 
6. If 노드 생성 5번 노드 결과가 is_funny인지 판단
  1. false일 겨우 Wait 노드 생성해서 2번으로 돌아감.
  2. true일 경우 7번 노드 연결
7. Gmail 노드 생성 및 6-1번 노드 연결
  * 이전 2번 노드의 응답 결과를 이용한다.

```posh
> Invoke-WebRequest -Uri https://icanhazdadjoke.com/ -Header @{'Accept'= 'application/json'
```