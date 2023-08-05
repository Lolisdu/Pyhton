contador_letras = lambda lista: [len (x) for x in lista]

lista_animais = ['gato', 'peixe', 'girafa']
print(contador_letras(lista_animais))

soma = lambda a,b: a + b
subtracao = lambda a,b: a - b

print(soma(5, 10))
print(subtracao(25, 15))

calculadora = {
    'soma': lambda a,b: a + b,
    'subtracao': lambda a,b: a - b,
    'multiplicacao': lambda a,b: a * b,
    'divisao': lambda a,b: a / b,

}
print(type(calculadora))
soma = calculadora ['soma']
multiplicacao = calculadora ['multiplicacao']
print('Soma total de : {}'.format(soma(10, 50)))
print('A multiplicação é : {}'.format(multiplicacao( 10, 2)))