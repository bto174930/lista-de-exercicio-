def quick_sort(arr, pivot_strategy="last"):
    
    if len(arr) <= 1:
        return arr
    if pivot_strategy == "first":
        pivot = arr[0]
    elif pivot_strategy == "middle":
        pivot = arr[len(arr) // 2]
    else:  
        pivot = arr[-1]
    low, high = 0, len(arr) - 1

    while True:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low >= high:
            break
        arr[low], arr[high] = arr[high], arr[low]

    if pivot_strategy == "first":
        arr[0], arr[high] = arr[high], arr[0]
    elif pivot_strategy == "middle":
        arr[len(arr) // 2], arr[high] = arr[high], arr[len(arr) // 2]
    else:
        arr[-1], arr[high] = arr[high], arr[-1]
    quick_sort(arr[:high], pivot_strategy)
    quick_sort(arr[high + 1:], pivot_strategy)

    return arr
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr, pivot_strategy="middle")
print(f"Lista ordenada: {sorted_arr}")
