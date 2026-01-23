# Exercíco Aritmético
#1
n1=float(input('Escolha um número'))                  
a=n1-1
s=n1+1

print('O numero escolhido foi {}.\n Seu antecessor é {} '.format(n1,a), end='')
print('e seu sucessor é {}.'.format(s))

#2
n2=float(input('Escolha um número'))
m2=n2*2
m3=n2*3
p=n2**2

print('O numero escolhido foi {}. Seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}.'.format(n2,m2,m3,p))

#3
n3=float(input('Qual o valor da sua primeira nota?'))
n4=float(input('Qual o valor da sua segunda nota nota?'))
m=(n3+n4)/2

print('A média das suas notas é {}.'.format(m))

#4
n5=float(input('Qual é o valor em metros?'))
c=n5*100
mi=n5*1000

print('O valor em metros é {}, esse mesmo valor em centímetros ficou {} e em milímetros ficou {}.'.format(n5,c,mi))