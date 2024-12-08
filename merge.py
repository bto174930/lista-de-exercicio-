# Ordenar Números Inteiros
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    left_arr = arr[left:left + n1]
    right_arr = arr[mid + 1:mid + 1 + n2]

    i = j = k = left
    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def printArray(arr):
    print(" ".join(map(str, arr)))

arr = [38, 27, 43, 3, 9, 82, 10]
print("Array original:")
printArray(arr)

mergeSort(arr, 0, len(arr) - 1)

print("Array ordenado:")
printArray(arr)
