import multiprocessing
import time
import random
import matplotlib.pyplot as plt

def monte_carlo_pi_chunk(num_points):
    inside = 0
    random.seed()
    for _ in range(num_points):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1.0:
            inside += 1
    return inside

def run_exercise_1():
    print("--- EJERCICIO 1: ACELERACIÓN PARALELA (MONTE CARLO PI) ---")
    total_points = 10_000_000
    process_list = [1, 2, 4, 8]
    times = []
    speedups = []
    base_time = None

    for p in process_list:
        start = time.time()
        with multiprocessing.Pool(processes=p) as pool:
            pool.map(monte_carlo_pi_chunk, [total_points // p] * p)
        elapsed = time.time() - start
        
        if p == 1:
            base_time = elapsed
            sp = 1.0
        else:
            sp = base_time / elapsed
            
        times.append(elapsed)
        speedups.append(sp)
        print(f"Procesos: {p:2d} | Tiempo: {elapsed:.4f}s | Speedup: {sp:.2f}x")

    
    plt.figure(figsize=(8, 5))
    plt.plot(process_list, speedups, marker='o', linewidth=2, label='Speedup Observado', color='blue')
    plt.plot(process_list, process_list, linestyle='--', color='red', label='Speedup Ideal (Linear)')
    plt.title('Ejercicio 1: Aceleración Paralela (Speedup vs Procesos)')
    plt.xlabel('Número de Procesos (p)')
    plt.ylabel('Speedup (Sp)')
    plt.xticks(process_list)
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    run_exercise_1()