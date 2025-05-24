def contagem_progressiva(n):
    for i in range(1, n+1):
        print(i)

def contagem_regressiva(n):
    for i in range(n, 0):
        print(i)

x = int(input('x? '))
opcao = input('Opção? ')

if opcao in 'Pp':
    contagem_progressiva(x)
else:
    contagem_regressiva(x)