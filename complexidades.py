def busca_binaria(arr, alvo):
    inicio = 0
    fim = len(arr) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        palpite = arr[meio]

        if palpite == alvo:
            return True
        elif palpite < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return False

palavras = ["banana", "cereja", "maçã", "uva"]
palavra_busca = "cereja"
encontrada = busca_binaria(palavras, palavra_busca)
print(encontrada)  

palavra_busca = "laranja"
encontrada = busca_binaria(palavras, palavra_busca)
print(encontrada) 
