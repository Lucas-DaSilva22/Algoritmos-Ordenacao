def selection_sort(lista):
    chave = len(lista)
    for indice_atual in range(chave - 1):
        min_index = indice_atual
        for i in range(indice_atual + 1, chave):
            if lista[i] < lista[min_index]:
                min_index = i
        if min_index != indice_atual:
            lista[indice_atual], lista[min_index] = lista[min_index], lista[indice_atual]

lista = [10, 2, 4, 5, 1, 3, 20, 87, 52, 54, 15]
selection_sort(lista)
print(lista)

"""
Insertion Sort

Vantagens:
- A vantagem da ordenação por seleção é sua simplicidade e requisitos mínimos de memória. 
- É fácil de entender e implementar, o que a torna uma boa opção para o ensino de conceitos básicos de ordenação

Desvantagens:
- A complexidade temporal da ordenação por seleção de O(n^2) significa que, 
à medida que o número de elementos no conjunto de dados aumenta, 
o tempo necessário para ordenar aumenta drasticamente. Isso a torna impraticável para matrizes ou listas grandes.

"""
