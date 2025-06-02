def bubble_sort(lista):
    chave = len(lista)
    for indice_atual in range(chave-1):  # Faz várias rodadas de organização
        for i in range(chave-1):  # Em cada rodada, olha cada par
            if lista[i] > lista[i+1]: # Se o numero da frente for maior que o de trás...
                # troca de elementos mas posições i e i+1
                lista[i], lista[i+1] = lista[i+1], lista[i] # ...troca eles de lugar

# Exemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(lista)
print(lista)

'''
Vantagens:
- Fácil de Entender e Codificar.
- Mantém a Ordem Relativa de Elementos Iguais.
- Pouco Uso de Memória.

Desvantagens:
- Ineficiente Mesmo para Listas Quase Ordenadas (Sem a Otimização).
- Muito Lento para Listas Grandes. Para uma lista de 10 elementos, 10 x 10 = 100 operações. Para 1000 elementos, 1000 x 1000 = 1.000.000.
- Não É a Melhor Escolha para a Maioria dos Casos.

'''