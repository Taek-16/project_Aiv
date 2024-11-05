# 3D Point Cloud Processing and 2D Projection System
Python 3.10.12

## 개요
이 프로젝트는 3D 포인트 클라우드 데이터를 처리하여 2D로 투영하는 시스템입니다. 
주된 기능으로는 노이즈 제거, 2D depth map 및 heat map 생성, YAML 설정 파일을 통한 설정 관리 등이 포함됩니다.

## 기능
- 3D 포인트 클라우드 데이터 로드 (.ply, .pcd)
- 노이즈 제거 (statistical outlier removal)
- 2D depth map 및 heat map 생성
- YAML 설정 파일을 통한 외부 설정 관리
- 설정에 따른 로그 관리

## 실행
```bash
python main.py
```

## 테스트 실행
```bash
pytest-3 tests/
```

## 사용 방법

### 요구사항 설치
```bash
pip install -r requirements.txt
