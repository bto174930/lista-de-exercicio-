import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

def plot_list_comparison(original, sorted_arr):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    ax1.bar(range(len(original)), original, color='lightblue')
    ax1.set_title("Lista Original")
    ax1.set_ylim(0, max(original) + 10)

    ax2.bar(range(len(sorted_arr)), sorted_arr, color='lightgreen')
    ax2.set_title("Lista Ordenada")
    ax2.set_ylim(0, max(sorted_arr) + 10)

    plt.tight_layout()
    plt.show()

def main():
    print("Escolha uma opção:")
    print("1. Gerar lista aleatória")
    print("2. Fornecer uma lista manualmente")
    input_choice = int(input("Digite o número da opção: "))

    if input_choice == 1:
        n = int(input("\nDigite o tamanho da lista: "))
        arr = random.sample(range(1, 10000), n)
    elif input_choice == 2:
        arr = list(map(int, input("\nDigite os números separados por espaço: ").split()))
    else:
        print("Escolha inválida.")
        return

    print(f"\nLista gerada (primeiros 10 elementos): {arr[:10]}...")
    
    print("\nEscolha um algoritmo de ordenação:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Quick Sort")
    sort_choice = int(input("Digite o número do algoritmo: "))
    
    sorted_arr = arr.copy()
    if sort_choice == 1:
        print("\nExecutando Bubble Sort...")
        sorted_arr, sort_time = measure_time(bubble_sort, sorted_arr)
    elif sort_choice == 2:
        print("\nExecutando Selection Sort...")
        sorted_arr, sort_time = measure_time(selection_sort, sorted_arr)
    elif sort_choice == 3:
        print("\nExecutando Quick Sort...")
        sorted_arr = quick_sort(sorted_arr)
        sort_time = time.time() - start_time  
    else:
        print("Escolha inválida.")
        return

    plot_list_comparison(arr, sorted_arr)
    print(f"\nTempo de execução da ordenação: {sort_time:.6f} segundos")

    target = int(input("\nDigite o número a ser buscado na lista ordenada: "))

    print("\nEscolha um algoritmo de busca:")
    print("1. Busca Linear")
    print("2. Busca Binária")
    search_choice = int(input("Digite o número do algoritmo: "))

    if search_choice == 1:
        print("\nExecutando Busca Linear...")
        search_result, search_time = measure_time(linear_search, sorted_arr, target)
    elif search_choice == 2:
        print("\nExecutando Busca Binária...")
        search_result, search_time = measure_time(binary_search, sorted_arr, target)
    else:
        print("Escolha inválida.")
        return

    print(f"\nTempo de execução da busca: {search_time:.6f} segundos")
    
    if search_result != -1:
        print(f"Elemento encontrado no índice {search_result}.")
    else:
        print("Elemento não encontrado.")

if __name__ == "__main__":
    main()
