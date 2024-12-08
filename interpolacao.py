
def interpolation_search(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high and key >= arr[low] and key <= arr[high]:
        if arr[high] == arr[low]:  
            break
        pos = low + ((high - low) // (arr[high] - arr[low])) * (key - arr[low])

        if arr[pos] == key:
            return pos

        if arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1

    return -1  

def binary_search(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            return mid

        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1  

if __name__ == "__main__":
    uniform = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    non_uniform = [1, 3, 7, 15, 31, 63, 127, 255, 511]

    key = 31 

    print("Teste do Interpolation Search em lista uniforme:")
    result = interpolation_search(uniform, key)
    if result != -1:
        print(f"Elemento encontrado no índice {result}")
    else:
        print("Elemento não encontrado")

    print("\nTeste do Interpolation Search em lista não uniforme:")
    result = interpolation_search(non_uniform, key)
    if result != -1:
        print(f"Elemento encontrado no índice {result}")
    else:
        print("Elemento não encontrado")

    print("\nTeste do Binary Search em lista uniforme:")
    result = binary_search(uniform, key)
    if result != -1:
        print(f"Elemento encontrado no índice {result}")
    else:
        print("Elemento não encontrado")

    print("\nTeste do Binary Search em lista não uniforme:")
    result = binary_search(non_uniform, key)
    if result != -1:
        print(f"Elemento encontrado no índice {result}")
    else:
        print("Elemento não encontrado")
