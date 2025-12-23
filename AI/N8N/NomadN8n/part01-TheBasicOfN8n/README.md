# N8N의 기본

## 첫 번째 워크플로우

워크플로우는 3가지 구성 요소가 있다.

1. trigger: 워크플로우의 시작점, 이벤트를 감지해서 워크플로우를 시작한다.
  * manual, event, scheduled..
2. node: 특정 일을 수행하는 작업 단위
  * 입력을 받아 출력을 만들어낸 후 다음 노드로 전달한다.
3. edge: 노드 간 데이터 흐름을 이어주는 화살표


Manual Trigger -> HTTP Request