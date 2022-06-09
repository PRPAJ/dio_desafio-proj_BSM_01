#cabeçário
bv = ' Bem Vindo '
fr = ' AO É OU NÃO É NÚMERO PRIMO.'
print('=*'*50)
print(f'{bv:-^100}')
print(f'{fr: ^100}')
#var
l = []
n = int(input("Digite um número e veja se é ou não um número primo: "))
for i in range (1,n +1):
    if n % i == 0:
        l.append(i)
if len(l) == 2:
    print(f'O número {n} é primo.')
else:
    print(f'O número {n} não é primo, pois é divisível por {l}.')