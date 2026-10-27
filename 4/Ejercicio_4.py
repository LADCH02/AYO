import math
import random
import time
import matplotlib.pyplot as plt

def dist(c1, c2): return math.hypot(c1[0] - c2[0], c1[1] - c2[1])
def path_cost(path, cities): return sum(dist(cities[path[i]], cities[path[i-1]]) for i in range(len(path)))

def simulated_annealing(cities, cooling_type='exponential'):
    n = len(cities)
    current_path = list(range(n))
    random.shuffle(current_path)
    current_cost = path_cost(current_path, cities)
    
    T = 1000.0
    T_min = 1.0
    
    costs_history = []
    start_time = time.time()
    
    while T > T_min:
        costs_history.append(current_cost)
        
        # Generar vecino aleatorio 2-opt
        i, j = sorted(random.sample(range(1, n), 2))
        new_path = current_path[:]
        new_path[i:j] = current_path[j-1:i-1:-1]
        new_cost = path_cost(new_path, cities)
        
        delta = new_cost - current_cost
        
        # Criterio de aceptación
        if delta < 0 or random.random() < math.exp(-delta / T):
            current_path = new_path
            current_cost = new_cost
            
        # Enfriamiento
        if cooling_type == 'exponential':
            T *= 0.995
        else: # linear
            T -= 0.5
            
    exec_time = time.time() - start_time
    return current_cost, costs_history, exec_time

if __name__ == '__main__':
    random.seed(42)
    cities = [(random.random()*100, random.random()*100) for _ in range(30)]

    cost_exp, hist_exp, time_exp = simulated_annealing(cities, 'exponential')
    cost_lin, hist_lin, time_lin = simulated_annealing(cities, 'linear')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Gráfica 1: Convergencia
    ax1.plot(hist_exp, label='Exponencial (alpha=0.995)')
    ax1.plot(hist_lin, label='Lineal (alpha=0.5)')
    ax1.set_title('Curvas de Convergencia')
    ax1.set_xlabel('Iteraciones')
    ax1.set_ylabel('Costo del Recorrido')
    ax1.legend()

    # Gráfica 2: Tiempo vs Calidad
    ax2.scatter([time_exp], [cost_exp], color='blue', s=100, label='Exponencial')
    ax2.scatter([time_lin], [cost_lin], color='red', s=100, label='Lineal')
    ax2.set_title('Tiempo de Ejecución vs Calidad')
    ax2.set_xlabel('Tiempo (segundos)')
    ax2.set_ylabel('Costo Final (Menor es mejor)')
    ax2.legend()

    plt.show()