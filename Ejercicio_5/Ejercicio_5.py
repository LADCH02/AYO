import math
import random
import itertools
import networkx as nx
import matplotlib.pyplot as plt

def dist(c1, c2): return math.hypot(c1[0] - c2[0], c1[1] - c2[1])
def path_cost(path, cities): return sum(dist(cities[path[i]], cities[path[i-1]]) for i in range(len(path)))

def exact_tsp(cities):
    # Calcula el óptimo exacto mediante fuerza bruta (solo viable para n <= 10)
    best_cost = float('inf')
    for perm in itertools.permutations(range(1, len(cities))):
        p = [0] + list(perm)
        c = path_cost(p, cities)
        if c < best_cost: best_cost = c
    return best_cost

def mst_tsp_approximation(cities):
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            G.add_edge(i, j, weight=dist(cities[i], cities[j]))
            
    # 1. Obtener el Árbol de Expansión Mínima
    mst = nx.minimum_spanning_tree(G)
    
    # 2. Recorrido Pre-orden (DFS) con atajos para generar el tour
    mst_path = list(nx.dfs_preorder_nodes(mst, source=0))
    return path_cost(mst_path, cities), mst_path

if __name__ == '__main__':
    ratios = []
    mst_costs, opt_costs = [], []
    
    # Evaluar 100 instancias de 9 ciudades
    for _ in range(100):
        cities = [(random.random()*100, random.random()*100) for _ in range(9)]
        
        opt_cost = exact_tsp(cities)
        mst_cost, _ = mst_tsp_approximation(cities)
        
        ratios.append(mst_cost / opt_cost)
        mst_costs.append(mst_cost)
        opt_costs.append(opt_cost)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # 1. Histograma de la Razón de Aproximación
    ax1.hist(ratios, bins=15, color='purple', alpha=0.7, edgecolor='black')
    ax1.axvline(2.0, color='red', linestyle='dashed', linewidth=2, label='Límite Teórico (2.0)')
    ax1.axvline(1.0, color='green', linestyle='dashed', linewidth=2, label='Óptimo (1.0)')
    ax1.set_title('Razón de Aproximación MST (100 instancias)')
    ax1.set_xlabel('$C_{obtenido} / C_{óptimo}$')
    ax1.set_ylabel('Frecuencia')
    ax1.legend()

    # 2. Boxplot comparativo
    ax2.boxplot([opt_costs, mst_costs], labels=['Óptimo Exacto', 'Aproximación MST'])
    ax2.set_title('Distribución de Costos (9 Ciudades)')
    ax2.set_ylabel('Costo del Recorrido')

    plt.tight_layout()
    plt.show()