import random
import time

def shell_sort(arr, gaps):
    n = len(arr)
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
def generate_shell_sequence(n):
    gaps = []
    gap = n // 2
    while gap > 0:
        gaps.append(gap)
        gap //= 2
    return gaps

def generate_knuth_sequence(n):
    gaps = []
    gap = 1
    while gap < n:
        gaps.append(gap)
        gap = 3 * gap + 1
    return gaps

def generate_hibbard_sequence(n):
    gaps = []
    k = 1
    while True:
        gap = (1 << k) - 1  
        if gap >= n:
            break
        gaps.append(gap)
        k += 1
    return gaps

def measure_time(sort_func, arr, gaps):
    start_time = time.time()
    sort_func(arr, gaps)
    return time.time() - start_time

def print_array(arr):
    print(arr)
def main():
    n = 10000  
    arr = [random.randint(1, 10000) for _ in range(n)]  

    shell_gaps = generate_shell_sequence(n)
    knuth_gaps = generate_knuth_sequence(n)
    hibbard_gaps = generate_hibbard_sequence(n)

    arr_copy = arr.copy()
    shell_time = measure_time(shell_sort, arr_copy, shell_gaps)
    print(f"Tempo com sequência Shell: {shell_time:.6f} segundos")

    arr_copy = arr.copy()
    knuth_time = measure_time(shell_sort, arr_copy, knuth_gaps)
    print(f"Tempo com sequência Knuth: {knuth_time:.6f} segundos")

    arr_copy = arr.copy()
    hibbard_time = measure_time(shell_sort, arr_copy, hibbard_gaps)
    print(f"Tempo com sequência Hibbard: {hibbard_time:.6f} segundos")

if __name__ == "__main__":
    main()
