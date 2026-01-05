# N8N의 기본

## My First Workflow

워크플로우는 3가지 구성 요소가 있다.

1. trigger: 워크플로우의 시작점, 이벤트를 감지해서 워크플로우를 시작한다.
  * manual, event, scheduled..
2. node: 특정 일을 수행하는 작업 단위
  * 입력을 받아 출력을 만들어낸 후 다음 노드로 전달한다.
3. edge: 노드 간 데이터 흐름을 이어주는 화살표


Manual Trigger -> HTTP Request

## Data Flow

목표: 
1. API에서 명언을 받는 노드 생성 (`https://zenquotes.io/api/random`)
2. ChatGPT를 활용하여 한글 번역하는 노드 생성 및 1번 노드에 연결
  * `{{Author}}: {{Quote}}` 형태로 만들어보자.


Manual Trigger -> HTTP Request -> OpenAI (Message Model) 

## Expressions and Schedules

표현 식은 `{{ JS expression }}`를 따름. 

```js
// {{ expression }}
{{ $json.q }}
```

모든 노드는 빌트인 변수들과 함수들이 있다. (ex: `$json`)

1. API에서 명언을 받는 노드 생성 (`https://zenquotes.io/api/random`)
2. ChatGPT를 활용하여 한글 번역하는 노드 생성 및 1번 노드에 연결
  * `{{Author}}: {{Quote}}` 형태로 만들어보자.
3. Gmail에 결과 보내기

숙제: 
* Manual Trigger -> Scheduled Trigger로 변경해보자.

## ㄸㅌ