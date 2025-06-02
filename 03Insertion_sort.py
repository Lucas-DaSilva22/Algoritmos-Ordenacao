def insertion_sort(lista):
    chaves = len(lista)
    for i in range(1, chaves):
        chave = lista[i]
        # posicao_anterior é o índice do elemento na parte ordenada, à esquerda da 'chave'
        posicao_anterior = i - 1

        # Enquanto não chegar ao início da lista o elemento na 'posicao_anterior' for maior que a 'chave'
        while posicao_anterior >= 0 and lista[posicao_anterior] > chave:
            # Desloca o elemento atual para a direita para abrir espaço
            lista[posicao_anterior + 1] = lista[posicao_anterior]
            # Move para a próxima posição à esquerda
            posicao_anterior = posicao_anterior - 1

        # Insere a 'chave' na posição correta (onde o loop parou de mover)
        lista[posicao_anterior + 1] = chave

lista = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(lista)
print(lista)


'''
Vantagens:
- Simplicidade e Facilidade de Implementação.
- Eficiente para Conjuntos de Dados Pequenos.
- Eficiente para Conjuntos de Dados Quase Ordenados.
- Mantém a Ordem Relativa de Elementos Iguais.
- Baixo Custo de Memória.

Desvantagens:
- Ineficiência para Grandes Conjuntos de Dados Aleatórios.
- Pode Ser Mais Lento que Outros Algoritmos.

'''