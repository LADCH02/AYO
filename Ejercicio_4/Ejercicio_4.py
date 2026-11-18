import random
import math
import time
import matplotlib.pyplot as plt

def calc_dist(tour, cities):
    """Calcula la distancia Euclidiana total de una ruta cerrada."""
    return sum(math.hypot(cities[tour[i]][0]-cities[tour[(i+1)%len(tour)]][0], 
                          cities[tour[i]][1]-cities[tour[(i+1)%len(tour)]][1]) for i in range(len(tour)))

def simulated_annealing_tsp(cities, cooling_type="exponential", max_iter=400):
    """Ejecuta Recocido Simulado con 2-opt y registra la historia de costos real."""
    start_time = time.time()
    n = len(cities)
    current_tour = list(range(n))
    random.shuffle(current_tour)
    
    current_cost = calc_dist(current_tour, cities)
    best_tour = list(current_tour)
    best_cost = current_cost
    
    temp = 1000.0
    cost_history = [current_cost]
    
    for _ in range(max_iter):
        if temp < 1e-3:
            break
        # Operador de movimiento 2-opt
        i = random.randint(0, n - 2)
        j = random.randint(i + 2, n)
        neighbor = current_tour[:i] + list(reversed(current_tour[i:j])) + current_tour[j:]
        n_cost = calc_dist(neighbor, cities)
        
        delta = n_cost - current_cost
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current_tour = neighbor
            current_cost = n_cost
            if current_cost < best_cost:
                best_tour = list(current_tour)
                best_cost = current_cost
                
        cost_history.append(current_cost)
        
        # Esquemas de enfriamiento
        if cooling_type == "exponential":
            temp *= 0.94
        else:
            temp -= (1000.0 / max_iter)
            
    elapsed_time = time.time() - start_time
    return best_cost, elapsed_time, cost_history

def run_exercise_4():
    print("--- EJERCICIO 4: SIMULATED ANNEALING (RIGUROSO) ---")
    random.seed(42)
    cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(15)]
    
    # 1. Obtener curvas de convergencia reales de una corrida
    _, _, history_exp = simulated_annealing_tsp(cities, cooling_type="exponential", max_iter=300)
    _, _, history_lin = simulated_annealing_tsp(cities, cooling_type="linear", max_iter=300)
    
    # 2. Experimento múltiple para Tiempo vs Calidad
    times_exp, costs_exp = [], []
    times_lin, costs_lin = [], []
    
    print("Ejecutando 30 experimentos comparativos...")
    for seed in range(30):
        random.seed(seed)
        c_e, t_e, _ = simulated_annealing_tsp(cities, "exponential", max_iter=300)
        times_exp.append(t_e)
        costs_exp.append(c_e)
        
        c_l, t_l, _ = simulated_annealing_tsp(cities, "linear", max_iter=300)
        times_lin.append(t_l)
        costs_lin.append(c_l)

    # Visualización con 2 subgráficas requeridas
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Gráfica 1: Curvas de convergencia reales
    ax1.plot(history_exp, label='Enfriamiento Exponencial', color='blue', linewidth=2)
    ax1.plot(history_lin, label='Enfriamiento Lineal', color='orange', linestyle='--', linewidth=2)
    ax1.set_title('Curvas de Convergencia (Costo Real vs Iteraciones)')
    ax1.set_xlabel('Iteraciones')
    ax1.set_ylabel('Costo de la Ruta')
    ax1.legend()
    ax1.grid(True)
    
    # Gráfica 2: Tiempo de Ejecución vs Calidad de la Solución Final
    ax2.scatter(times_exp, costs_exp, color='blue', label='Exponencial', alpha=0.8, s=70)
    ax2.scatter(times_lin, costs_lin, color='orange', label='Lineal', alpha=0.8, s=70)
    ax2.set_title('Tiempo de Ejecución vs. Calidad de la Solución Final')
    ax2.set_xlabel('Tiempo de Ejecución (segundos)')
    ax2.set_ylabel('Costo Final (Distancia)')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    run_exercise_4()