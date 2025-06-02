def counting_sort(arr):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m
    for a in arr:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1
    return arr

# Exemplo de uso
print(counting_sort([4, 2, 2, 8, 3, 3, 1]))

'''
Vantagens:
- Muito rápido para inteiros com faixa limitada (O(n + k)).
- 
- 

Desvantagens:
- Não funciona bem com intervalos muito grandes ou dados não inteiros.
- 

'''