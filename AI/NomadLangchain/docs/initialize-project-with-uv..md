# uv로 프로젝트 생성하기


`uv` 프로젝트 생성
```
uv init .
```

`venv` 생성
```
uv venv .venv
```

`venv` 활성화
```
.venv/Scripts/activate
```

의존성 설치
```
uv pip sync .\requirements.txt
```

파이썬 버전 변경 (가상환경 비활성화한 이후에 해야 함.)
```
uv venv --python 3.11
```