def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivô = arr[0]
    menores = [x for x in arr[1:] if x < pivô]
    maiores = [x for x in arr[1:] if x >= pivô]
    return quick_sort(menores) + [pivô] + quick_sort(maiores)

palavras = ["banana", "maçã", "cereja", "data"]
palavras_ordenadas = quick_sort(palavras)
print(palavras_ordenadas)
 

#Merge Sort e Quick Sort foram adaptados para ordenar palavras (strings) em ordem alfabética usando comparações lexicográficas.
#Binary Search foi adaptado para pesquisar uma palavra em uma lista de palavras já ordenadas em ordem alfabética.
#A lista precisa estar ordenada antes de usar o Binary Search, o que pode ser feito com Merge Sort ou Quick Sort.





#Análise de Complexidade
#Algoritmos como Busca Binária e Quick Sort têm complexidade mais eficiente para grandes conjuntos de dados.
#Algoritmos de ordenação simples (Bubble Sort, Selection Sort, Insertion Sort) têm O(n²) e são ineficientes para grandes volumes.
#Merge Sort e Heap Sort têm O(n log n), sendo mais eficientes, com Merge Sort exigindo mais espaço.