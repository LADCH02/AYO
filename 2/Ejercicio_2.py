import matplotlib.pyplot as plt

def greedy_knapsack(items, capacity, sort_key, reverse_order):
    # Ordenar los objetos según el criterio elegido
    sorted_items = sorted(items, key=lambda x: x[sort_key], reverse=reverse_order)
    
    total_value = 0
    total_weight = 0
    selected_items = []
    
    for item in sorted_items:
        if total_weight + item['weight'] <= capacity:
            selected_items.append(item['name'])
            total_weight += item['weight']
            total_value += item['value']
            
    return selected_items, total_weight, total_value

if __name__ == '__main__':
    # Instancia pequeña diseñada para que "menor peso" falle
    items = [
        {'name': 'A', 'weight': 1, 'value': 1, 'ratio': 1},
        {'name': 'B', 'weight': 2, 'value': 2, 'ratio': 1},
        {'name': 'C', 'weight': 5, 'value': 20, 'ratio': 4}
    ]
    capacity = 5

    # Método 1: Menor peso primero (menor a mayor)
    sel_w, w_w, v_w = greedy_knapsack(items, capacity, 'weight', False)
    
    # Método 2: Ratio Valor/Peso (mayor a menor)
    sel_r, w_r, v_r = greedy_knapsack(items, capacity, 'ratio', True)

    # Visualización
    labels = ['Menor Peso Primero', 'Valor / Peso']
    valores = [v_w, v_r]
    pesos = [w_w, w_r]

    fig, ax1 = plt.subplots(figsize=(8, 5))
    
    ax1.bar(labels, valores, color=['salmon', 'lightblue'])
    ax1.set_ylabel('Valor Total Obtenido', color='black')
    ax1.set_title(f'Greedy Knapsack (Capacidad = {capacity})\nSelección Peso: {sel_w} | Selección Ratio: {sel_r}')
    
    # Añadir texto con la capacidad usada
    for i, v in enumerate(valores):
        ax1.text(i, v + 0.5, f'Valor: {v}\nPeso Usado: {pesos[i]}/{capacity}', ha='center')

    plt.ylim(0, 25)
    plt.show()