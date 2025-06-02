Selection Sort
° Explicação:

O Selection Sort (ou ordenação por seleção) é um algoritmo de ordenação simples e fácil de entender, que funciona da seguinte forma: Ele percorre uma lista procurando o menor valor e o coloca na primeira posição. Depois procura o segundo menor e coloca na segunda posição. E assim por diante... até a lista estar ordenada.

° Pontos Positivos

1.Simples de entender e implementar O algoritmo é direto: procure o menor valor e coloque no lugar certo.

2.Poucas trocas (swaps) Mesmo que compare bastante, ele só troca quando necessário (no máximo uma vez por posição).

3.Não precisa de memória extra (in-place) Ele organiza uma lista sem precisar criar outra lista, economizando memória.

° Pontos Negativos

Lento para listas grandes Complexidade é O(n²), ou seja, fica bem devagar com muitos elementos.

Ignora se a lista já está quase ordenada Mesmo que a lista seja quase no jeito, ele ainda faz todas as comparações.

Não é estável (por padrão) Se dois valores forem iguais, ele pode trocar a ordem deles na lista final — isso pode ser ruim em alguns contextos (tipo ordenação por nome e idade).

Bubble Sort
°Explicação:

O Bubble Sort (ou ordenação por bolha) é um algoritmo simples que funciona comparando pares de elementos vizinhos e trocando-os de lugar se estiverem na ordem errada. Esse processo se repete várias vezes até que a lista esteja ordenada. O nome "bolha" vem da ideia de que os valores maiores "sobem" para o final da lista a cada passada, como uma bolha subindo na água.

° Pontos Positivos

1.Muito fácil de entender e implementar Ideal para quem está começando com algoritmos.

2.Pode parar antes do final se uma lista já estiver ordenada Dá pra melhorar com uma bandeira para detectar se houve troca.

3.Estável Mantém a ordem dos elementos iguais (importante em ordenações por múltiplos critérios).

° Pontos Negativos

1.Muito lento em listas grandes Tem complexidade O(n²) — compare e troque muito.

2.Faz muitas trocas desnecessárias Troca quase toda hora, mesmo se a lista estiver quase ordenada.

3.Pouco usado na prática Só é bom pra estudo; na vida real, algoritmos melhores são preferidos.

Insertion Sort
° Explicação O Insertion Sort (ou ordenação por inserção) funciona como se você estivesse organizando cartas na mão:

Ele pega um elemento da lista por vez e insere na posição correta dentro da parte que já está ordenada.

° Funcionamento:

Começar do segundo item.

Compare com os anteriores.

Vai mover os maiores pra frente.

Insira o elemento no lugar certo.

° Pontos Positivos

1.Muito eficiente para listas pequenas ou quase ordenadas Se a lista já é quase certa, ele vai rápido.

2.Simples de implementar e entender Ideal para aprender lógica de ordenação.

3.Estável Mantém a ordem de elementos iguais, útil em ordenações múltiplas (ex: nome + idade).

° Pontos Negativos

1.Ineficiente em listas grandes desordenadas Tem complexidade O(n²) no pior caso

2.Muitas comparações e movimentações Se os elementos estiverem longe da posição correta, ele funciona muito.

3.Não é ideal para dados aleatórios em larga escala. Existem algoritmos mais rápidos como Merge, Quick e Heap Sort.

Merge Sort
° Explicação

O Merge Sort (ou ordenação por intercalação) é um algoritmo do tipo "dividir para conquistar".

Ele divide uma lista em duas partes, ordena cada uma recursivamente, e depois intercala (junta) essas partes de forma ordenada.

° Funcionamento:

Divida uma lista no meio até sobrar 1 elemento por pedaço.

Compare e intercala os pedaços, criando listas maiores ordenadas.

Repetir até juntar tudo numa única lista ordenada.

° Pontos Positivos

1.Muito eficiente (O(n log n)) Mesmo no pior caso, ele é rápido e previsível.

2.Estável Mantém a ordem de elementos iguais, útil em ordenações múltiplas.

3.Bom pra listas grandes ou com muitos dados aleatórios Funciona muito bem mesmo com grandes volumes.

° Pontos Negativos

1.Usa memória extra Precisa criar listas auxiliares para fazer a intercalação.

2.Mais complexo de entender que os básicos (Bubble, Insertion) Usa recursão e pode ser difícil pra quem está começando.

3.Menos eficientes em listas pequenas Para posições difíceis, outras técnicas simples podem ser mais rápidas.

Quick Sort
° Explicação

O Quick Sort (ou ordenação rápida) é um algoritmo muito eficiente que também usa a estratégia “dividir para conquistar”, como o Merge Sort. Ele escolhe um pivô, separa a lista em duas partes (valores menores e maiores que o pivô), e ordena cada parte recursivamente.

° Funcionamento:

Escolhe um pivô (geralmente o último elemento).

Coloca todos os elementos menores do que o pivô à esquerda e os maiores à direita.

Repita o processo em cada lado, até que a lista esteja ordenada.

° Pontos Positivos

1.Muito rápido na prática Mesmo que o pior caso seja O(n²), geralmente ele roda com eficiência O(n log n).

2.In-place Não precisa de muita memória extra — reorganiza na própria lista.

3.Bom para grandes volumes de dados É um dos mais usados ​​em bibliotecas e sistemas reais.

° Pontos Negativos

1.Não é estável Elementos iguais podem trocar de posição.

2.Pior caso é ruim (O(n²)) Pode acontecer se escolher sempre o pior pivô (por exemplo, o menor ou maior número da lista).

3.Mais complexo de implementar que Bubble ou Insertion Usa recursão e manipulação de índices com mais cuidado.

Heap Sort
° Explicação

O Heap Sort é um algoritmo de ordenação baseado em uma estrutura chamada heap, que é uma árvore binária especial (normalmente um max-heap). Ele transforma a lista em um heap, onde o elemento maior sempre fica no topo (início da lista), e vai tirando esse elemento maior e colocando no fim da lista, um por um.

° Funcionamento:

transforma a lista em um max-heap.

Troque o primeiro (maior) pelo último da lista.

Reduza o tamanho do heap e reorganize para manter o heap máximo.

Repete até tudo estar ordenado.

° Pontos Positivos

1.Complexidade sempre garantida: O(n log n) Mesmo no pior caso, continua eficiente.

2.Não é recursivo (pode ser implementado iterativamente). Não há risco de estouro de pilha.

3.Funciona bem mesmo com dados desordenados Desempenho consistente independente da entrada.

° Pontos Negativos

1.Não é estável Pode mudar a ordem de elementos iguais.

2.Mais difícil de implementar que os básicos Requer conhecimento de árvore binária e manipulação de índices.

3.Desempenho prático menor que o Quick Sort em muitos casos, apesar da garantia teórica, pode ser mais lento em listas pequenas.

Counting Sort
° Explicação

O Counting Sort (ou ordenação por contagem) é um algoritmo muito rápido, mas com uma condição: Só funciona bem com números inteiros não-negativos e com valores dentro de um intervalo pequeno. Ele conta quantas vezes cada número aparece na lista e reconstrói a lista ordenada com base nessas contagens.

° Funcionamento:

Encontre o maior número da lista.

Cria uma lista auxiliar (contagem[]) para contar quantas vezes cada número aparece.

Usa essa contagem para montar a lista final ordenada.

° Pontos Positivos

1.Muito rápido (O(n + k)) Quando k (o maior número) é pequeno, é supereficiente.

2.Estável Mantém a ordem dos elementos iguais.

3.Simples e direto Fácil de implementar para números inteiros.

° Pontos Negativos

1.Só funciona com inteiros não-negativos

2.Consome muita memória se o maior número para muito grande

3.Não funciona bem com números decimais ou negativos

Classificação por Radix
° Explicação

O Radix Sort (ou ordenação por base) é um algoritmo que não compara números diretamente, como o Bubble, Insertion, etc. Ele organiza os números pelos seus dígitos, primeiro pela unidade, depois pela dezena, centena... até que tudo esteja ordenado.

° Funcionamento:

Encontra o maior número da lista (pra saber quantos dígitos precisa analisar).

Ordene os números pelo dígito das unidades (1s).

Depois, pelas faixas (10s).

Depois, pelas centenas (100s).

Vai repetindo até todos os dígitos que serão usados.

Usa Counting Classifique internamente para ordenar por cada dígito.

° Pontos Positivos

1.Muito eficiente com números inteiros grandes Especialmente quando os números têm muitos dígitos, mas o número total de elementos não é gigante.

2.Não usa comparação direta entre os números Isso pode ser uma vantagem dependendo do contexto.

3.Estável Mantém a ordem de elementos iguais, desde que o algoritmo auxiliar (como Counting Sort) também seja estável.

° Pontos Negativos

1.Só funciona com inteiros (ou precisa adaptar muito pra strings e decimais).

2.Consome memória extra Por usar Contagem Classificar várias vezes.

3.Pode ser lento se os números tiverem muitos dígitos e a lista por pequena Às vezes outros algoritmos são mais simples e mais rápidos em listas menores.

Bucket Sort
° Explicação

O Bucket Sort (ordenação por baldes) é um algoritmo ideal quando: Os valores estão distribuídos de forma uniforme (ex: notas de 0.0 a 10.0) ou são números decimais.

° Funcionamento:

Divide os elementos em baldes (listas menores) com base no intervalo dos valores.

Ordena cada balde individualmente (pode usar Insertion Sort ou qualquer outro).

Junta todos os baldes para formar a lista final ordenada.

° Pontos Positivos

1.Muito rápido quando os dados são bem distribuídos.

2.Bom para números decimais ou dados contínuos.

3.Estável, se o sort interno for estável.

° Pontos Negativos

1.Requer conhecimento da distribuição dos dados Se os dados forem mal distribuídos, ele perde eficiência.

2.Consome memória com muitos baldes

3.Desempenho depende do sort interno em cada balde
