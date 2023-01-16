def interval_scheduling(comecoLista, finalLista):
    resultado = list()

    index = list(range(len(comecoLista)))
    index.sort(key=lambda i: finalLista[i])
    tempoEventoPassado = 0
    for i in index:
        if comecoLista[i] >= tempoEventoPassado:
            resultado.append(i)
            tempoEventoPassado = finalLista[i]

    return resultado

if __name__ == "__main__":
    T = int(input())

    for index in range(T):
        N = int(input())

        comecoLista = list()
        finalLista = list()

        if not N:
            break

        for index in range(N):
            comeco, final = map(int, input().split())
            comecoLista.append(comeco)
            finalLista.append(final)

        resultado = interval_scheduling(comecoLista, finalLista)
        print(len(resultado))