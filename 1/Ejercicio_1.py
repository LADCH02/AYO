import multiprocessing as mp
import time
import random
import matplotlib.pyplot as plt

def estimate_pi_worker(samples):
    inside = sum(1 for _ in range(samples) if random.random()**2 + random.random()**2 <= 1)
    return inside

def run_parallel_pi(total_samples, p):
    samples_per_process = total_samples // p
    start = time.time()
    with mp.Pool(p) as pool:
        results = pool.map(estimate_pi_worker, [samples_per_process] * p)
    pi_estimate = (4.0 * sum(results)) / total_samples
    return time.time() - start

# BLOQUE REQUERIDO EN WINDOWS PARA MULTIPROCESSING
if __name__ == '__main__':
    procesos = [1, 2, 4, 8]
    tiempos = [run_parallel_pi(10**7, p) for p in procesos]
    speedups = [tiempos[0] / t for t in tiempos]

    plt.plot(procesos, speedups, marker='o', label='Speedup Real')
    plt.plot(procesos, procesos, linestyle='--', color='gray', label='Speedup Ideal')
    plt.xlabel('Número de Procesos')
    plt.ylabel('Speedup')
    plt.legend()
    plt.show()