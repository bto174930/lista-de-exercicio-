livros = [
    {"ISBN": "978-3-16-148410-0", "titulo": "Aprendendo Python", "autor": "João Silva"},
    {"ISBN": "978-1-61-729057-3", "titulo": "Estruturas de Dados", "autor": "Maria Oliveira"},
    {"ISBN": "978-0-13-235088-4", "titulo": "Algoritmos e Estruturas de Dados", "autor": "Carlos Souza"},
    {"ISBN": "978-0-321-72242-6", "titulo": "Programação em C", "autor": "Ana Costa"},
    {"ISBN": "978-0-12-374514-9", "titulo": "Computação para Iniciantes", "autor": "Pedro Lima"}
]

livros_ordenados = sorted(livros, key=lambda livro: livro["ISBN"])

def busca_binaria(livros, isbn_alvo):
    inicio = 0
    fim = len(livros) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        livro_meio = livros[meio]
        
        if livro_meio["ISBN"] == isbn_alvo:
            return livro_meio 
        elif livro_meio["ISBN"] < isbn_alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return None  
isbn_busca = "978-0-13-235088-4"
livro_encontrado = busca_binaria(livros_ordenados, isbn_busca)

if livro_encontrado:
    print(f'Livro encontrado: {livro_encontrado["titulo"]}, Autor: {livro_encontrado["autor"]}, ISBN: {livro_encontrado["ISBN"]}')
else:
    print("Livro não encontrado.")
