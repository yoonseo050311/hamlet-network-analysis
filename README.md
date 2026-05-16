# Hamlet Network Analysis 🎭

완성된 Hamlet 네트워크 분석 프로젝트입니다.

## 📦 파일 구성

```
hamlet-network-analysis/
├── hamlet_network_analysis.py   # 메인 분석 스크립트 (8KB)
├── hamlet.gexf                   # 네트워크 데이터
├── requirements.txt              # 의존성
└── README.md                     # 상세 문서
```

## ✅ 분석 완료 항목

### 1️⃣ Centrality (중심성 분석)
- **Degree Centrality**: 직접 상호작용 정도
- **Betweenness Centrality**: 중개자 역할 정도  
- **Closeness Centrality**: 네트워크 내 거리
- **Eigenvector Centrality**: 영향력 있는 이웃과의 연결

### 2️⃣ Density (네트워크 밀도)
- 전체 가능한 연결 대비 실제 연결 비율
- 0~1 범위 (1에 가까울수록 촘촘함)

### 3️⃣ Clustering (군집화)
- Average Clustering Coefficient
- 각 노드별 군집화 계수
- 지역 커뮤니티 형성 정도

### 4️⃣ Community Detection (커뮤니티)
- Greedy Modularity 알고리즘
- 자동 그룹 분류
- Modularity 점수

### 5️⃣ Core-Periphery (중심-주변부)
- K-core 분해
- 네트워크 구조 분석

### 6️⃣ Distance Metrics (거리)
- Average Shortest Path Length
- Network Diameter
- Connected Components

## 🚀 빠른 시작

```bash
# 1. 라이브러리 설치
pip install -r requirements.txt

# 2. 분석 실행
python hamlet_network_analysis.py
```

## 📊 예상 결과

### 주요 인물 중심성 순위
1. **Hamlet** - 주인공, 최고 Degree
2. **Claudius** - 왕, 권력의 중심
3. **Horatio** - 신뢰할 수 있는 친구
4. **Polonius** - 정보 수집 역할
5. **Gertrude** - 여왕, 중요한 연결점

### 커뮤니티 구조 (예상)
- **Core 그룹**: Hamlet, Claudius, Gertrude, Horatio
- **정보원**: Polonius, Rosencrantz, Guildenstern
- **주변 인물**: Marcellus, Ghost, Fortinbras

## 📈 출력 형식

```
================================================================================
HAMLET NETWORK ANALYSIS
================================================================================

1. BASIC NETWORK INFORMATION
- Number of nodes: 13
- Number of edges: 31
- Network type: Undirected

2. CENTRALITY MEASURES
- Top 10 Degree Centrality
- Top 10 Betweenness Centrality
- Top 10 Closeness Centrality
- Top 10 Eigenvector Centrality

3. NETWORK DENSITY
- Density: 0.xxxx

4. CLUSTERING COEFFICIENT
- Average: 0.xxxx
- Top 10 by Clustering

5. COMMUNITY DETECTION
- Communities found: x
- Modularity: 0.xxxx

6. CONNECTED COMPONENTS
- Status: Fully Connected

7. NETWORK DISTANCE METRICS
- Average Path Length: x.xxxx
- Diameter: x

8. CORE-PERIPHERY STRUCTURE
- Core levels identified

9. SUMMARY TABLE
- Top 5 characters by combined centrality
```

## 🔍 해석 가이드

### Centrality 해석
- **Degree**: 직접 만나는 사람 수
- **Betweenness**: 사람들 사이의 연결고리 역할
- **Closeness**: 네트워크 전체와의 근접도
- **Eigenvector**: 중요한 사람들과의 연결도

### Density 해석
- `< 0.3`: 느슨한 네트워크
- `0.3 ~ 0.7`: 중간 정도
- `> 0.7`: 촘촘한 네트워크

### Community 해석
- 혈연, 충성도, 권력 관계로 자동 분류
- Modularity 높을수록 더 잘 분리됨

## 📚 학습 자료

이 프로젝트는 다음을 학습하는데 도움이 됩니다:
- 네트워크 그래프 이론
- 중심성 지수 개념
- 커뮤니티 탐지 알고리즘
- 실제 데이터 분석

## 🎯 향후 확장 계획

- [ ] NetworkX 시각화 (PyVis)
- [ ] 대화형 대시보드 (Streamlit)
- [ ] 동적 네트워크 분석
- [ ] PageRank 분석
- [ ] 영향력 전파 모델링

## 📖 참고 자료

- NetworkX 문서: https://networkx.org/
- Graph Theory: https://en.wikipedia.org/wiki/Graph_theory
- Hamlet: https://en.wikipedia.org/wiki/Hamlet

---

**저자**: yoonseo050311  
**생성일**: 2026-05-16  
**라이선스**: MIT  
**상태**: ✅ 완성
