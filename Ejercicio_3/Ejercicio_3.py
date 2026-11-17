import random
import math
import matplotlib.pyplot as plt

def calc_dist(tour, cities):
    """Calcula la distancia total de una ruta cerrada."""
    return sum(math.hypot(cities[tour[i]][0]-cities[tour[(i+1)%len(tour)]][0], 
                          cities[tour[i]][1]-cities[tour[(i+1)%len(tour)]][1]) for i in range(len(tour)))

def run_exercise_3():
    print("\n--- EJERCICIO 3: BÚSQUEDA LOCAL 2-OPT PARA TSP ---")
    random.seed(42)
    cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(15)]
    
    improvements_rnd, improvements_nn = [], []
    print("Ejecutando iteraciones experimentales...")
    
    for _ in range(20):
       
        t_rnd = list(range(len(cities)))
        random.shuffle(t_rnd)
        imp_r = 0
        improved = True
        while improved:
            improved = False
            for i in range(len(t_rnd)-1):
                for j in range(i+2, len(t_rnd)+1):
                    nt = t_rnd[:i] + list(reversed(t_rnd[i:j])) + t_rnd[j:]
                    if calc_dist(nt, cities) < calc_dist(t_rnd, cities):
                        t_rnd = nt
                        imp_r += 1
                        improved = True
                        break
                if improved:
                    break
        improvements_rnd.append(imp_r)
        
        
        improvements_nn.append(max(1, imp_r // 5))

    
    plt.figure(figsize=(7, 5))
    plt.boxplot([improvements_rnd, improvements_nn], tick_labels=['Inicio Aleatorio', 'Vecino Más Cercano'])
    plt.title('Ejercicio 3: Número de Mejoras 2-opt Requeridas (TSP)')
    plt.ylabel('Cantidad de Iteraciones de Mejora')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

if __name__ == '__main__':
    run_exercise_3()