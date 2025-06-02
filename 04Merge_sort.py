def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        # Ele vai ordenar da esquerda pra direita .
        mergesort(lista, inicio, meio) 
        mergesort(lista, meio, fim)
        # Vai juntar as partes.
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim): 
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left): # Ver quem ta na esquerda se é maior do que o da direita.
            lista[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1

lista = [64, 34, 25, 12, 22, 11, 90]
mergesort(lista)
print(lista)
'''
Vantagens:
- Eficiência Consistente.
- Estável (Preserva a Ordem Relativa de Elementos Iguais).
- Ideal para Grandes Conjuntos de Dados e Ordenação Externa.

Desvantagens:
- Requer Memória Adicional (Espaço Extra).
- Lento para Conjuntos de Dados Muito Pequenos.

'''