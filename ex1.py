def ordenar_decrescente(numbers):
    n = len(numbers)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if numbers[j] > numbers[max_index]:
                max_index = j
        numbers[i], numbers[max_index] = numbers[max_index], numbers[i]
    return numbers

numbers = [3, 7, 4, 9, 5, 2, 6, 1]
print(ordenar_decrescente(numbers))
# Este algoritmo percorre o array de números, um elemento por vez.
# Em cada iteração, o algoritmo procura o índice do elemento máximo no subarray que ainda não foi ordenado.
# Quando o índice do elemento máximo é encontrado, ele é trocado com o elemento na posição atual (i).
# O processo é repetido até que todos os elementos tenham sido comparados e trocados de lugar, resultando em um array ordenado em ordem decrescente.
