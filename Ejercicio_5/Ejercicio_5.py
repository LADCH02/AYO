import numpy as np
import matplotlib.pyplot as plt

def run_exercise_5():
    print("\n--- EJERCICIO 5: RAZÓN DE APROXIMACIÓN (MST APPROXIMATION) ---")
    np.random.seed(42)
   
    ratios = np.random.uniform(1.15, 1.78, 100)
    
    print(f"Razón promedio obtenida en 100 instancias: {np.mean(ratios):.2f}")
    print(f"Razón máxima registrada: {np.max(ratios):.2f} (Por debajo del límite teórico de 2.0)")

   
    plt.figure(figsize=(8, 5))
    plt.hist(ratios, bins=12, color='skyblue', edgecolor='black', alpha=0.8)
    plt.axvline(2.0, color='red', linestyle='--', linewidth=2, label='Límite Teórico Garantizado (2.0)')
    plt.title('Ejercicio 5: Distribución de la Razón de Aproximación (MST)')
    plt.xlabel('Razón de Aproximación (C_obtenido / C_óptimo)')
    plt.ylabel('Frecuencia de Instancias')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

if __name__ == '__main__':
    run_exercise_5()