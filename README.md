# Hamlet Network Analysis 🎭

Shakespeare의 Hamlet 작품에서 등장인물들 간의 상호작용을 네트워크 분석합니다.

## 📊 분석 항목

### 1. **Centrality Measures (중심성 분석)**
네트워크에서 각 인물의 중요도를 측정합니다.

- **Degree Centrality**: 직접 상호작용한 인물의 수
- **Betweenness Centrality**: 다른 인물들 사이의 "중개자" 역할 정도
- **Closeness Centrality**: 네트워크의 다른 인물들까지의 평균 거리
- **Eigenvector Centrality**: 영향력 있는 인물들과의 연결 정도

### 2. **Network Density (네트워크 밀도)**
- 전체 가능한 상호작용 중 실제 존재하는 상호작용의 비율
- 네트워크의 연결 정도를 나타냄 (0~1, 1에 가까울수록 촘촘함)

### 3. **Clustering Coefficient (군집화 계수)**
- 각 인물의 주변 인물들이 서로 얼마나 연결되어 있는지
- 높을수록 더 촘촘한 지역 커뮤니티 형성

### 4. **Community Detection (커뮤니티 탐지)**
- Greedy Modularity 알고리즘으로 자동 감지
- 유사한 상호작용 패턴을 가진 인물 그룹 식별
- Modularity 점수로 커뮤니티 분리 정도 측정

### 5. **Core-Periphery Structure (핵심-주변부 구조)**
- K-core 분해로 네트워크의 중심부와 주변부 구분
- 높은 core number일수록 네트워크의 중심에 위치

### 6. **Distance Metrics (거리 지표)**
- Average Shortest Path Length: 평균 최단 거리
- Diameter: 네트워크의 가장 먼 두 인물 사이의 거리

## 🚀 사용 방법

### 요구사항
```bash
pip install -r requirements.txt
```

### 실행
```bash
python hamlet_network_analysis.py
```

## 📈 해석 가이드

### Centrality가 높은 인물
- **Hamlet**: 주인공으로서 가장 많은 상호작용
- **Claudius**: 왕으로서 권력의 중심
- **Horatio**: 여러 그룹 간의 중개 역할

### Community 분석
- 혈연 관계, 충성도, 권력 관계 등으로 그룹 형성
- 가족: Hamlet, Gertrude, Claudius, Laertes, Ophelia, Polonius
- 정보 수집: Rosencrantz, Guildenstern
- 주변 인물: 배우, 선원, 무덤팜이 등

### Density 해석
- 낮은 밀도 (0.3 이하): 느슨한 네트워크
- 높은 밀도 (0.7 이상): 촘촘한 네트워크
- Hamlet 네트워크는 중간 정도의 밀도

## 📁 파일 구조

```
hamlet-network-analysis/
├── hamlet_network_analysis.py  # 메인 분석 스크립트
├── hamlet.gexf                  # 네트워크 데이터 (GEXF 형식)
├── requirements.txt             # 필수 라이브러리
└── README.md                    # 이 파일
```

## 🔗 데이터 포맷

### GEXF (Graph Exchange XML Format)
- nodes: 등장인물 정보
  - label: 인물 이름
  - number-of-words: 대사 단어 수
  - sex: 성별
  
- edges: 상호작용
  - weight: 상호작용 빈도

## 📊 예상 결과

분석 결과는 다음을 포함합니다:
- 각 인물의 중심성 지표 순위
- 탐지된 커뮤니티 및 멤버
- 네트워크 밀도 및 군집화 계수
- 핵심 인물 (core structure)
- 네트워크 거리 지표

## 💡 활용

이 분석은 다음에 활용될 수 있습니다:
- 문학 작품 분석
- 사회 네트워크 분석 학습
- 네트워크 시각화 및 모델링
- 그래프 이론 응용

---

**Author**: yoonseo050311  
**Date**: 2026-05-16  
**License**: MIT
