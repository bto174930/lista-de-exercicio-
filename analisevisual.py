import matplotlib.pyplot as plt

def merge_sort_visualization(arr):
    arr_copy = arr.copy()
    steps = []

    def merge_sort_step(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_step(arr[:mid])
        right = merge_sort_step(arr[mid:])
        merged = merge(left, right)
        steps.append(merged.copy())
        return merged

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    merge_sort_step(arr_copy)
    return steps

arr = [38, 27, 43, 3, 9, 82, 10]
steps = merge_sort_visualization(arr)

fig, axs = plt.subplots(len(steps), 1, figsize=(10, 2 * len(steps)))
if len(steps) == 1:
    axs = [axs] 

for i, step in enumerate(steps):
    axs[i].bar(range(len(step)), step, color='lightblue')
    axs[i].set_title(f"Etapa {i + 1}")
    axs[i].set_ylim(0, max(arr) + 10)
    axs[i].set_xticks(range(len(step)))
    axs[i].set_ylabel("Valor")
    if i == len(steps) - 1:
        axs[i].set_xlabel("Índice")

plt.tight_layout()
plt.show()
