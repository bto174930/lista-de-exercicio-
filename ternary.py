def busca_ternaria(vetor, inicio, fim, elemento):
    if fim >= inicio:
        meio1 = inicio + (fim - inicio) // 3
        meio2 = fim - (fim - inicio) // 3
        
        if vetor[meio1] == elemento:
            return meio1
        if vetor[meio2] == elemento:
            return meio2
        
        if elemento < vetor[meio1]:
            return busca_ternaria(vetor, inicio, meio1 - 1, elemento)
        
        elif elemento > vetor[meio2]:
            return busca_ternaria(vetor, meio2 + 1, fim, elemento)
        
        else:
            return busca_ternaria(vetor, meio1 + 1, meio2 - 1, elemento)
    
    return -1  

vetor = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
elemento = 19
resultado = busca_ternaria(vetor, 0, len(vetor) - 1, elemento)
if resultado != -1:
    print(f"Elemento encontrado no índice: {resultado}")
else:
    print("Elemento não encontrado")


# Comparação de algoritimos
#  Escolher o melhor algoritmo depende do tipo de dados e do tamanho da lista.
#  Para listas ordenadas grandes, Binary Search e Exponential Search são geralmente as melhores opções. 
# Se os dados forem uniformemente distribuídos, Interpolation Search pode ser uma escolha interessante. 
# Para listas menores, Jump Search pode ser mais eficiente.


#Comparação de Algoritmos de Ordenação
# Para listas pequenas ou quase ordenadas, Shell Sort pode ser competitivo, mas Quick Sort e Merge Sort são mais eficientes para listas grandes e desordenadas.
# Selection Sort deve ser evitado para grandes listas devido ao número alto de comparações.
# Bucket Sort e Radix Sort são ideais para tipos específicos de dados e podem ser extremamente rápidos quando bem aplicados.

# Análise de Complexidade
#Busca Binária e Exponential Search são muito eficientes em termos de tempo (logaritmicos) e têm um espaço constante.
#Merge Sort é eficiente e estável, mas requer espaço extra.
#Quick Sort é muito eficiente na prática, mas seu pior caso pode ser 
#Bucket Sort e Radix Sort são muito eficientes quando aplicados a dados específicos 
# (dados numéricos ou uniformemente distribuídos), mas têm complexidade de espaço maior.