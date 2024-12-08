def bucket_sort(arr, n):
    buckets = [[] for _ in range(n)]
    
    for aluno in arr:
        index = int(aluno["nota"] * n / 100)  
        buckets[index].append(aluno)
    for bucket in buckets:
        bucket.sort(key=lambda x: x["nota"])
    resultado = []
    for bucket in buckets:
        resultado.extend(bucket)
    return resultado
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low]["nota"] and target <= arr[high]["nota"]:
        pos = low + ((target - arr[low]["nota"]) * (high - low)) // (arr[high]["nota"] - arr[low]["nota"])

        if arr[pos]["nota"] == target:
            return arr[pos]
        elif arr[pos]["nota"] < target:
            low = pos + 1
        else:
            high = pos - 1

    return None  

alunos = [
    {"nome": "Carlos", "nota": 88},
    {"nome": "Ana", "nota": 95},
    {"nome": "Pedro", "nota": 78},
    {"nome": "Maria", "nota": 92},
    {"nome": "João", "nota": 63},
    {"nome": "Lucas", "nota": 71},
    {"nome": "Camila", "nota": 85},
    {"nome": "Roberta", "nota": 90}
]

n = len(alunos)
alunos_ordenados = bucket_sort(alunos, n)

print("Alunos ordenados por nota:")
for aluno in alunos_ordenados:
    print(f'{aluno["nome"]}: {aluno["nota"]}')
nota_busca = 90
aluno_encontrado = interpolation_search(alunos_ordenados, nota_busca)

if aluno_encontrado:
    print(f'\nAluno encontrado: {aluno_encontrado["nome"]}, Nota: {aluno_encontrado["nota"]}')
else:
    print("\nAluno não encontrado.")



#Algoritmos estáveis:
#Bubble Sort
#Insertion Sort
#Merge Sort
#Counting Sort
#Radix Sort