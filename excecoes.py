
lista = [1, 10]
try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 0
    numero = lista[3]
    print('Fechando arquivo')
    arquivo.close()
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação Aritmética')
except IndexError:
    print('Erro ao acessar um indice inválido na lista')
except BaseException as ex:
    print('Erro desconhecido.Erro: ()'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Fechando arquivo')
    arquivo.close()

