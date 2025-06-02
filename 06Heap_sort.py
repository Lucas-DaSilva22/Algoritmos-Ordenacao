def reorganizar_heap(lista, tamanho_heap, indice_raiz):
    maior_elemento = indice_raiz

    filho_esquerdo = 2 * indice_raiz + 1
    filho_direito = 2 * indice_raiz + 2

    if filho_esquerdo < tamanho_heap and lista[maior_elemento] < lista[filho_esquerdo]:
        maior_elemento = filho_esquerdo

    if filho_direito < tamanho_heap and lista[maior_elemento] < lista[filho_direito]:
        maior_elemento = filho_direito

    if maior_elemento != indice_raiz:
        lista[indice_raiz], lista[maior_elemento] = lista[maior_elemento], lista[indice_raiz]  # Troca os valores
        reorganizar_heap(lista, tamanho_heap, maior_elemento) # Continua reorganizando a subárvore

def ordenar_com_heap(lista_para_ordenar):
    tamanho = len(lista_para_ordenar)

    # PRIMEIRA FASE: (organizar a lista como um heap)
    # Começa do último nó "pai" que não é folha e vai até a raiz
    for i in range(tamanho // 2 - 1, -1, -1):
        reorganizar_heap(lista_para_ordenar, tamanho, i)

    # SEGUNDA FASE: Extrair elementos um por um do heap e colocá-los em ordem
    # Percorre a lista do último elemento ao segundo elemento
    for i in range(tamanho - 1, 0, -1):
        # Move o maior elemento atual para o final da parte não ordenada
        lista_para_ordenar[i], lista_para_ordenar[0] = lista_para_ordenar[0], lista_para_ordenar[i]
        reorganizar_heap(lista_para_ordenar, i, 0)
        
    return lista_para_ordenar

# Exemplo de uso:
minha_lista = [12, 11, 13, 5, 6, 7]
print(f"Lista original: {minha_lista}")
lista_ordenada = ordenar_com_heap(minha_lista)
print(f"Lista ordenada: {lista_ordenada}")

'''
Vantagens:
- Eficiência Consistente
- Bom para Grandes Conjuntos de Dados
- Complexidade O(n log n)

Desvantagens:
- Não é um Algoritmo Estável
- Pior Desempenho na Prática

'''