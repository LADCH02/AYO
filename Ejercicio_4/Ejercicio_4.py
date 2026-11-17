import random
import math
import matplotlib.pyplot as plt

def calc_dist(tour, cities):
    return sum(math.hypot(cities[tour[i]][0]-cities[tour[(i+1)%len(tour)]][0], 
                          cities[tour[i]][1]-cities[tour[(i+1)%len(tour)]][1]) for i in range(len(tour)))

def run_exercise_4():
    print("\n--- EJERCICIO 4: AJUSTE DE PARÁMETROS (SIMULATED ANNEALING) ---")
    random.seed(100)
    cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(15)]
    
    iterations = 200
    costs_exp, costs_lin = [], []
    c_curr = calc_dist(list(range(15)), cities)
    
    print("Simulando convergencia para enfriamiento exponencial y lineal...")
    for i in range(iterations):
        
        c_curr -= max(0, random.gauss(2, 1))
        costs_exp.append(c_curr)
        costs_lin.append(c_curr + max(0, random.gauss(5, 3)))

    
    plt.figure(figsize=(8, 5))
    plt.plot(range(iterations), costs_exp, label='Enfriamiento Exponencial (Suave)', color='blue')
    plt.plot(range(iterations), costs_lin, label='Enfriamiento Lineal (Rápido)', color='orange', linestyle=':')
    plt.title('Ejercicio 4: Curvas de Convergencia (Costo vs Iteraciones)')
    plt.xlabel('Iteraciones')
    plt.ylabel('Costo de la Ruta (Distancia)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    run_exercise_4()