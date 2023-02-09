frutas = []


def ordenar_crescente(frutas):
    n = len(frutas)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if frutas[j] < frutas[max_index]:
                max_index = j
        frutas[i], frutas[max_index] = frutas[max_index], frutas[i]
    return frutas


for n in range(5):
    texto = str(input('Digite uma fruta: '))
    frutas.append(texto)
    ordenar_crescente(frutas)
print(frutas)

# Este algoritmo percorre o array de números, um elemento por vez.
# Em cada iteração, o algoritmo procura o índice do elemento máximo no subarray que ainda não foi ordenado.
# Quando o índice do elemento máximo é encontrado, ele é trocado com o elemento na posição atual (i).
# O processo é repetido até que todos os elementos tenham sido comparados e trocados de lugar, resultando em um array ordenado em ordem crescente.
