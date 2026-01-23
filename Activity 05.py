# Operadores Aritméticos

# + adição
# - subtração
# * multiplicação
# / divisão
# ** potência ou função interna pow (x,y)
# // divisão inteira
# % resto da divição

# Ordem de Procedência

# 1 ()
# 2 **
# 3 * / // %
# 4 + - 

# Exercíco Curiosidade

nome=input('Qual é seu nome?')
print('Prazer em te conhecer {:20}!'.format(nome)) #Escreverá o nome em 20 caracteres

nome=input('Qual é seu nome?')
print('Prazer em te conhecer {:>20}!'.format(nome)) #Escreverá o nome em 20 caracteres alinhando a direita

nome=input('Qual é seu nome?')
print('Prazer em te conhecer {:<20}!'.format(nome)) #Escreverá o nome em 20 caracteres alinhando a esquerda

nome=input('Qual é seu nome?')
print('Prazer em te conhecer {:^20}!'.format(nome)) #Escreverá o nome em 20 caracteres alinhando no centro

nome=input('Qual é seu nome?')
print('Prazer em te conhecer {:=^20}!'.format(nome)) #Escreverá o nome em 20 caracteres alinhando no centro colocando sinal de igual em volta (pode ser usado com qualquer alinhamento)


# Exercíco Aritmético

n1=float(input('Escolha um valor'))
n2=float(input('Escolha outro valor'))

sa=n1+n2
su=n1-n2
m=n1*n2
d=n1/n2
p=n1**n2
di=n1//n2
r=n1%n2

print('A soma entre os dois numero é {}. A subtração entre os dois numero é {}. A multiplicação entre os dois numero é {:.3f}.'.format(sa,su,m))
print('A divisão entre os dois numero é {}. A potência entre os dois numero é {}. A divisão inteira entre os dois numero é {}.'.format(d,p,di))
print ('Por fim o resto da divisao entre os dois numero é{}.'.format(r))

#Para quebrar uma linha do print colocar \n, para não quebrar a linha coloque ,end=' '

