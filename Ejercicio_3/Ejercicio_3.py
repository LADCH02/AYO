import random
import math
import matplotlib.pyplot as plt

def calc_dist(tour, cities):
    """Calcula la distancia Euclidiana total de una ruta cerrada."""
    return sum(math.hypot(cities[tour[i]][0]-cities[tour[(i+1)%len(tour)]][0], 
                          cities[tour[i]][1]-cities[tour[(i+1)%len(tour)]][1]) for i in range(len(tour)))

def nearest_neighbor_tour(cities):
    """Genera una solución inicial usando la heurística del Vecino Más Cercano."""
    n = len(cities)
    unvisited = set(range(n))
    current = random.choice(list(unvisited))
    tour = [current]
    unvisited.remove(current)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: math.hypot(cities[current][0] - cities[city][0], cities[current][1] - cities[city][1]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    return tour

def two_opt_search(tour, cities):
    """Aplica 2-opt y retorna la mejor ruta, el costo final y el número de mejoras."""
    best_tour = list(tour)
    improvements_count = 0
    improved = True
    n = len(best_tour)
    
    while improved:
        improved = False
        for i in range(n - 1):
            for j in range(i + 2, n + 1):
                if j - i == 1 and i == 0 and j == n:
                    continue  
                new_tour = best_tour[:i] + list(reversed(best_tour[i:j])) + best_tour[j:]
                if calc_dist(new_tour, cities) < calc_dist(best_tour, cities):
                    best_tour = new_tour
                    improvements_count += 1
                    improved = True
                    break
            if improved:
                break
                
    final_cost = calc_dist(best_tour, cities)
    return best_tour, final_cost, improvements_count

def run_exercise_3():
    print("--- EJERCICIO 3: BÚSQUEDA LOCAL 2-OPT PARA TSP (EXPERIMENTO REAL) ---")
    
    improvements_rnd, costs_rnd = [], []
    improvements_nn, costs_nn = [], []
    
    num_experiments = 30
    print(f"Ejecutando {num_experiments} experimentos independientes...")
    
    for seed in range(num_experiments):
        random.seed(seed)
        cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(15)]
        
       
        t_rnd = list(range(len(cities)))
        random.shuffle(t_rnd)
        _, cost_r, imp_r = two_opt_search(t_rnd, cities)
        improvements_rnd.append(imp_r)
        costs_rnd.append(cost_r)
        
        
        t_nn = nearest_neighbor_tour(cities)
        _, cost_n, imp_n = two_opt_search(t_nn, cities)
        improvements_nn.append(imp_n)
        costs_nn.append(cost_n)

    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
  
    ax1.boxplot([improvements_rnd, improvements_nn], tick_labels=['Inicio Aleatorio', 'Vecino Más Cercano'])
    ax1.set_title('Número de Mejoras (Iteraciones 2-opt)')
    ax1.set_ylabel('Cantidad de Iteraciones')
    ax1.grid(True, linestyle='--', alpha=0.7)
    
   
    ax2.boxplot([costs_rnd, costs_nn], tick_labels=['Inicio Aleatorio', 'Vecino Más Cercano'])
    ax2.set_title('Calidad del Óptimo Alcanzado (Costo Final)')
    ax2.set_ylabel('Distancia Total de la Ruta')
    ax2.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    run_exercise_3()