import matplotlib.pyplot as plt

class Item:
    def __init__(self, id, weight, value):
        self.id = id
        self.weight = weight
        self.value = value

def run_exercise_2():
    print("\n--- EJERCICIO 2: GREEDY KNAPSACK (MENOR PESO PRIMERO) ---")
    W = 10
    items = [Item(1, 2, 3), Item(2, 9, 45), Item(3, 8, 32)]
    
    
    sorted_classic = sorted(items, key=lambda x: x.value / x.weight, reverse=True)
    w_c, v_c = 0, 0
    for it in sorted_classic:
        if w_c + it.weight <= W:
            w_c += it.weight
            v_c += it.value
            
   
    sorted_min_w = sorted(items, key=lambda x: x.weight)
    w_m, v_m = 0, 0
    for it in sorted_min_w:
        if w_m + it.weight <= W:
            w_m += it.weight
            v_m += it.value

    print(f"Valor Total Método Clásico (Ratio V/P): {v_c}")
    print(f"Valor Total Método Modificado (Menor Peso): {v_m}")

    # Visualización Gráfica de Barras Comparativa
    methods = ['Clásico (Ratio V/P)', 'Modificado (Menor Peso)']
    values = [v_c, v_m]
    
    plt.figure(figsize=(7, 4))
    bars = plt.bar(methods, values, color=['#2ca02c', '#d62728'])
    plt.title('Ejercicio 2: Comparativa de Valor Total Obtenido (Knapsack)')
    plt.ylabel('Valor Total')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1, f'{yval}', ha='center', va='bottom')
    plt.ylim(0, max(values) + 10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

if __name__ == '__main__':
    run_exercise_2()