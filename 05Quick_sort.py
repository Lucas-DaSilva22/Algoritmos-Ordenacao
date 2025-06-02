def quicksort(lista, inicio=0, fim=None):
    # Se 'fim' não foi especificado (na primeira chamada), definimos como o último índice da lista.
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        # 'posicao_do_pivo' será o índice onde o pivô fica depois de tudo menor estar à esquerda e tudo maior à direita.
        posicao_do_pivo = partition(lista, inicio, fim)

        # Vai do 'inicio' original até a posição ANTES do pivô.
        quicksort(lista, inicio, posicao_do_pivo - 1)

        # Chama o quicksort recursivamente para a sublista dos elementos maiores que o pivô.
        # Vai da posição DEPOIS do pivô até o 'fim'.
        quicksort(lista, posicao_do_pivo + 1, fim)

def partition(lista, inicio, fim):
    # Escolhemos o último elemento da sublista como o pivô.
    # O pivô é o valor de referência para a organização.
    pivot = lista[fim]

    # 'limite_menores' é um ponteiro que marca o fim da "zona" onde os elementos menores ou iguais ao pivô devem estar.
    limite_menores = inicio

    # 'indice_atual_analise' vai percorrer a sublista, analisando cada elemento (do início até um antes do pivô).
    for indice_atual_analise in range(inicio, fim):
        # Se o elemento que estamos analisando ('lista[indice_atual_analise]') for menor ou igual ao pivô:
        if lista[indice_atual_analise] <= pivot:
            # Trocamos o elemento analisado ('lista[indice_atual_analise]') com o elemento que está na posição 'limite_menores'.
            lista[indice_atual_analise], lista[limite_menores] = lista[limite_menores], lista[indice_atual_analise]
            
            # Depois da troca, avançamos o 'limite_menores' para a próxima posição,
            # pois agora mais um elemento menor/igual está na sua zona correta.
            limite_menores = limite_menores + 1

    # Quando o loop termina, todos os elementos (exceto o pivô) foram comparados.
    # 'limite_menores' agora aponta para o lugar onde o pivô deve ir.
    # Trocamos o pivô (que estava no 'fim' da sublista) para a sua posição final correta.
    lista[limite_menores], lista[fim] = lista[fim], lista[limite_menores]
    
    # Retornamos o índice final do pivô.
    return limite_menores

lista = [64, 34, 25, 12, 22, 11, 90]
quicksort(lista)
print(lista)

'''
Vantagens:
- Muito Rápido na Prática.
- Requer Pouca Memória Adicional

Desvantagens:
- Pior Caso de Desempenho (O(N²)): Se por azar o pivô escolhido for o maior número.
- Desempenho no Pior Caso para Memória Recursiva: Para listas muito grandes, isso pode levar a um erro de "Stack Overflow" (estouro de pilha).

'''