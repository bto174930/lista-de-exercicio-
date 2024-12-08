def binarySearch(arr, left, right, x):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid  
        elif arr[mid] < x:
            left = mid + 1  
        else:
            right = mid - 1  
    return -1  

def exponentialSearch(arr, n, x):
    if arr[0] == x:
        return 0
    i = 1
    while i < n and arr[i] <= x:
        i *= 2
    return binarySearch(arr, i // 2, min(i, n - 1), x)

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    n = len(arr)
    x = 13  

    result = exponentialSearch(arr, n, x)
    if result != -1:
        print(f"Elemento encontrado na posição {result}")
    else:
        print("Elemento não encontrado")
