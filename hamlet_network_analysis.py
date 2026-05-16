import networkx as nx
import pandas as pd
from collections import defaultdict
import json

# Load the GEXF file
G = nx.read_gexf('hamlet.gexf')

print("=" * 80)
print("HAMLET NETWORK ANALYSIS")
print("=" * 80)

# ============================================================================
# 1. BASIC NETWORK INFORMATION
# ============================================================================
print("\n1. BASIC NETWORK INFORMATION")
print("-" * 80)
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
print(f"Network type: {'Directed' if G.is_directed() else 'Undirected'}")

# ============================================================================
# 2. CENTRALITY MEASURES
# ============================================================================
print("\n2. CENTRALITY MEASURES")
print("-" * 80)

# Degree Centrality
degree_centrality = nx.degree_centrality(G)
sorted_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)

print("\nTop 10 - DEGREE CENTRALITY (연결된 이웃의 수)")
print("Character | Degree Centrality | # of Connections")
for i, (node, centrality) in enumerate(sorted_degree[:10], 1):
    degree = G.degree(node)
    label = G.nodes[node].get('label', node)
    print(f"{i:2d}. {label:25s} | {centrality:6.4f} | {degree:3d}")

# Betweenness Centrality
betweenness_centrality = nx.betweenness_centrality(G)
sorted_betweenness = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)

print("\n\nTop 10 - BETWEENNESS CENTRALITY (네트워크 경로 중개 정도)")
print("Character | Betweenness Centrality")
for i, (node, centrality) in enumerate(sorted_betweenness[:10], 1):
    label = G.nodes[node].get('label', node)
    print(f"{i:2d}. {label:25s} | {centrality:8.6f}")

# Closeness Centrality
closeness_centrality = nx.closeness_centrality(G)
sorted_closeness = sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True)

print("\n\nTop 10 - CLOSENESS CENTRALITY (다른 노드까지의 평균 거리)")
print("Character | Closeness Centrality")
for i, (node, centrality) in enumerate(sorted_closeness[:10], 1):
    label = G.nodes[node].get('label', node)
    print(f"{i:2d}. {label:25s} | {centrality:8.6f}")

# Eigenvector Centrality
try:
    eigenvector_centrality = nx.eigenvector_centrality(G, max_iter=1000)
    sorted_eigenvector = sorted(eigenvector_centrality.items(), key=lambda x: x[1], reverse=True)
    
    print("\n\nTop 10 - EIGENVECTOR CENTRALITY (영향력 있는 이웃과의 연결)")
    print("Character | Eigenvector Centrality")
    for i, (node, centrality) in enumerate(sorted_eigenvector[:10], 1):
        label = G.nodes[node].get('label', node)
        print(f"{i:2d}. {label:25s} | {centrality:8.6f}")
except:
    print("\n\nEigenvector Centrality: 계산 불가 (그래프 특성상)")

# ============================================================================
# 3. NETWORK DENSITY
# ============================================================================
print("\n\n3. NETWORK DENSITY")
print("-" * 80)
density = nx.density(G)
print(f"Network Density: {density:.6f}")
print(f"Interpretation: 전체 가능한 연결 중 {density*100:.2f}%가 실제로 존재")
print(f"(완전 연결은 1.0, 연결 없음은 0.0)")

# ============================================================================
# 4. CLUSTERING COEFFICIENT
# ============================================================================
print("\n\n4. CLUSTERING COEFFICIENT (군집화 계수)")
print("-" * 80)

average_clustering = nx.average_clustering(G)
print(f"Average Clustering Coefficient: {average_clustering:.6f}")
print("(각 노드의 이웃들이 서로 얼마나 연결되어 있는지)")

# Top nodes by clustering coefficient
clustering_coeff = nx.clustering(G)
sorted_clustering = sorted(clustering_coeff.items(), key=lambda x: x[1], reverse=True)

print("\nTop 10 - CLUSTERING COEFFICIENT")
print("Character | Clustering Coefficient")
for i, (node, coeff) in enumerate(sorted_clustering[:10], 1):
    label = G.nodes[node].get('label', node)
    print(f"{i:2d}. {label:25s} | {coeff:8.6f}")

# ============================================================================
# 5. COMMUNITY DETECTION (Modularity 기반 커뮤니티)
# ============================================================================
print("\n\n5. COMMUNITY DETECTION (커뮤니티/클러스터 탐지)")
print("-" * 80)

from networkx.algorithms import community

# Using Greedy Modularity Communities
communities = list(community.greedy_modularity_communities(G))
modularity = community.modularity(G, communities)

print(f"Number of communities detected: {len(communities)}")
print(f"Modularity score: {modularity:.6f}")
print("(높을수록 더 잘 분리된 커뮤니티를 의미, 1에 가까울수록 좋음)")

print("\nCommunities:")
for i, comm in enumerate(communities, 1):
    characters = [G.nodes[node].get('label', node) for node in comm]
    print(f"\n  Community {i} ({len(comm)} members):")
    for char in sorted(characters):
        print(f"    - {char}")

# ============================================================================
# 6. CONNECTED COMPONENTS
# ============================================================================
print("\n\n6. CONNECTED COMPONENTS")
print("-" * 80)

if nx.is_connected(G):
    print("The network is FULLY CONNECTED (모든 노드가 연결됨)")
else:
    components = list(nx.connected_components(G))
    print(f"Number of connected components: {len(components)}")
    for i, comp in enumerate(components, 1):
        print(f"  Component {i}: {len(comp)} nodes")

# ============================================================================
# 7. AVERAGE PATH LENGTH & DIAMETER
# ============================================================================
print("\n\n7. NETWORK DISTANCE METRICS")
print("-" * 80)

if nx.is_connected(G):
    avg_path_length = nx.average_shortest_path_length(G)
    diameter = nx.diameter(G)
    print(f"Average Shortest Path Length: {avg_path_length:.4f}")
    print(f"Network Diameter: {diameter}")
    print("(네트워크의 가장 먼 두 노드 사이의 거리)")
else:
    print("Network is not connected - metrics not applicable")

# ============================================================================
# 8. CORE-PERIPHERY STRUCTURE
# ============================================================================
print("\n\n8. CORE-PERIPHERY STRUCTURE (k-core decomposition)")
print("-" * 80)

core_number = nx.core_number(G)
max_core = max(core_number.values())
print(f"Maximum core number: {max_core}")

for core_level in range(max_core, max(0, max_core - 3), -1):
    core_nodes = [node for node, k in core_number.items() if k >= core_level]
    if core_nodes:
        characters = [G.nodes[node].get('label', node) for node in core_nodes]
        print(f"\nCore-{core_level} ({len(core_nodes)} nodes):")
        for char in sorted(characters):
            print(f"  - {char}")

# ============================================================================
# 9. SUMMARY STATISTICS TABLE
# ============================================================================
print("\n\n9. CHARACTER CENTRALITY SUMMARY (상위 5명)")
print("-" * 80)
print(f"{'Rank':<5} {'Character':<25} {'Degree':<8} {'Betweenness':<12} {'Closeness':<12} {'Clustering':<12}")
print("-" * 74)

# Create combined ranking
combined_scores = {}
for node in G.nodes():
    combined_scores[node] = (
        degree_centrality[node] +
        betweenness_centrality[node] +
        closeness_centrality[node] +
        clustering_coeff[node]
    ) / 4

top_5 = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)[:5]

for rank, (node, _) in enumerate(top_5, 1):
    label = G.nodes[node].get('label', node)
    print(f"{rank:<5} {label:<25} {degree_centrality[node]:<8.4f} {betweenness_centrality[node]:<12.6f} {closeness_centrality[node]:<12.6f} {clustering_coeff[node]:<12.6f}")

print("\n" + "=" * 80)
print("END OF ANALYSIS")
print("=" * 80)
