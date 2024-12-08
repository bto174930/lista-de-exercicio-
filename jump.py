import math
import time

def binary_search(arr, left, right, x):
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            return mid  
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1 

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))  
    prev = 0

    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1 
    for i in range(prev, min(step, n)):
        if arr[i] == x:
            return i  
    return -1  

def measure_time():
    n = 100000 
    arr = list(range(n)) 

    x = 78900  
    start_time = time.time()
    index_jump = jump_search(arr, x)
    end_time = time.time()
    print(f"Jump Search - Índice: {index_jump}, Tempo: {end_time - start_time:.6f} segundos")

    start_time = time.time()
    index_binary = binary_search(arr, 0, n - 1, x)
    end_time = time.time()
    print(f"Binary Search - Índice: {index_binary}, Tempo: {end_time - start_time:.6f} segundos")
measure_time()
