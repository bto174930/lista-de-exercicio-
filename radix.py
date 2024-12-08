def counting_sort(arr, exp, base):
    n = len(arr)
    output = [0] * n 
    count = [0] * base 
    
    for i in range(n):
        index = arr[i] // exp % base  
        count[index] += 1
    
    for i in range(1, base):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp % base
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr, base=10):
    max_val = max(arr)
    
    exp = 1  
    while max_val // exp > 0:
        counting_sort(arr, exp, base)
        exp *= base

numbers = [170, 45, 75, 90, 802, 24, 2, 66]
print("Antes de ordenar:", numbers)

radix_sort(numbers, base=10)  
print("Depois de ordenar (base 10):", numbers)

numbers_bin = [170, 45, 75, 90, 802, 24, 2, 66]
print("Antes de ordenar (base 2):", numbers_bin)

radix_sort(numbers_bin, base=2)  
print("Depois de ordenar (base 2):", numbers_bin)
