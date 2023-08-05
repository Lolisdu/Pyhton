def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador


if __name__ == '__main__':
    lista = ['gato', 'papagaio']
    total_letras = contador_letras(lista)
    print('Total de letras por palavra da lista: {} '.format(total_letras))
