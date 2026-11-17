import math
import random
import matplotlib.pyplot as plt

def dist(c1, c2):
    return math.hypot(c1[0] - c2[0], c1[1] - c2[1])

def path_cost(path, cities):
    return sum(dist(cities[path[i]], cities[path[i-1]]) for i in range(len(path)))

def nearest_neighbor(cities):
    unvisited = set(range(1, len(cities)))
    path = [0]
    while unvisited:
        last = path[-1]
        next_city = min(unvisited, key=lambda city: dist(cities[last], cities[city]))
        path.append(next_city)
        unvisited.remove(next_city)
    return path

def two_opt(path, cities):
    best_path = path
    best_cost = path_cost(path, cities)
    improvements = 0
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(path) - 2):
            for j in range(i + 1, len(path)):
                if j - i == 1: continue # Aristas adyacentes
                
                new_path = best_path[:]
                new_path[i:j] = best_path[j-1:i-1:-1] # Swap 2-opt
                new_cost = path_cost(new_path, cities)
                
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_path = new_path
                    improvements += 1
                    improved = True
                    break # Volver a empezar la búsqueda
            if improved: break
            
    return best_path, best_cost, improvements

if __name__ == '__main__':
    random.seed(42)
    n_cities = 30
    cities = [(random.random()*100, random.random()*100) for _ in range(n_cities)]

    # Escenario 1: Inicialización Aleatoria
    random_path = list(range(n_cities))
    random.shuffle(random_path)
    cost_rand_init = path_cost(random_path, cities)
    final_rand_path, final_rand_cost, imp_rand = two_opt(random_path, cities)

    # Escenario 2: Inicialización con Vecino Más Cercano (NN)
    nn_path = nearest_neighbor(cities)
    cost_nn_init = path_cost(nn_path, cities)
    final_nn_path, final_nn_cost, imp_nn = two_opt(nn_path, cities)

    # Visualización
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.bar(['Aleatorio', 'Nearest Neighbor'], [imp_rand, imp_nn], color=['orange', 'green'])
    ax1.set_title('Número de Mejoras (Swaps) Necesarias')
    ax1.set_ylabel('Mejoras')

    ax2.bar(['Aleatorio', 'Nearest Neighbor'], [final_rand_cost, final_nn_cost], color=['orange', 'green'])
    ax2.set_title('Costo del Óptimo Local Alcanzado')
    ax2.set_ylabel('Distancia Total')
    ax2.set_ylim(bottom=min(final_rand_cost, final_nn_cost) * 0.9)

    plt.suptitle('Comparativa 2-opt TSP (30 ciudades)')
    plt.tight_layout()
    plt.show()