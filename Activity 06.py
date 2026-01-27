# Exercíco Aritmético
#1
n1=float(input('Escolha um número'))                  
a=n1-1
s=n1+1

print('O número escolhido foi {}.\n Seu antecessor é {} '.format(n1,a), end='')
print('e seu sucessor é {}.'.format(s))

#Ou
n1=float(input('Escolha um número'))  
print('O número escolhido foi {}, seu antecessor é {} e seu sucessor é {}.'.format(n1,(n1-1),(n1+1)))


#2
n2=float(input('Escolha um número'))
m2=n2*2
m3=n2*3
p=n2**(1/2)

print('O número escolhido foi {}. Seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}.'.format(n2,m2,m3,p))

#ou
n2=float(input('Escolha um número'))
print('O número escolhido foi {}. Seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}.'.format(n2,(n2*2),(n2*3),(n2**(1/2)))


#3
n3=float(input('Qual o valor da sua primeira nota?'))
n4=float(input('Qual o valor da sua segunda nota nota?'))
m=(n3+n4)/2

print('A média das suas notas é {:.2f}.'.format(m))


#4
n5=float(input('Qual é o valor em metros?'))
c=n5*100
mi=n5*1000

print('O valor em metros é {}, esse mesmo valor em centímetros ficou {} e em milímetros ficou {}.'.format(n5,c,mi))


#5
n6=float(input('Tabuada de qual número você quer saber?'))
t1=n6*1
t2=n6*2
t3=n6*3
t4=n6*4
t5=n6*5
t6=n6*6
t7=n6*7
t8=n6*8
t9=n6*9
t10=n6*10

print('===============')
print('{:.0f} x 1 = {}'.format(n6,t1))
print('{:.0f} x 2 = {}'.format(n6,t2))
print('{:.0f} x 3 = {}'.format(n6,t3))
print('{:.0f} x 4 = {}'.format(n6,t4))
print('{:.0f} x 5 = {}'.format(n6,t5))
print('{:.0f} x 6 = {}'.format(n6,t6))
print('{:.0f} x 7 = {}'.format(n6,t7))
print('{:.0f} x 8 = {}'.format(n6,t8))
print('{:.0f} x 9 = {}'.format(n6,t9))
print('{:.0f} x 10 = {}'.format(n6,t10))
print('===============')

#Ou
n6=float(input('Tabuada de qual número você quer saber?'))
print('-'*12)
print('{} x {} = {}'.format(n6,1,n6*1)) #E assim por diante


#6
n7=float(input('Quanto de dinheiro você tem na carteira?'))
do=n7/5,5

print('Com o valor que você tem na carteira pode comprar {:.2f} dólaresn considerando que US$1 é igual a R$5,5.'.format(do))


#7
al=float(input('Qual a altura da sua parede?'))
la=float(input('Qual a largura da sua parede?'))
ar=al*la
tin=ar/2

print('Sua parede tem uma área de {} e para pinta-la será necessario {} litros de tinta.'.format(ar,tin))


#8
p=float(input('Qual o preço do produto?'))
np=p-(p*5/100)

print('O preço do produto com 5% de desconto é {:.2f}.'.format(np))


#9
s=float(input('Qual seu sálario atual?'))
ns=s+(s*15/100)

print('Seu sálario com 15% de aumento será {:.2f}.'.format(ns))


#10
tem=float(input('Qual a temperatura hoje, em °C?'))
f= ((9*tem)/5)+32

print('A temperatura de hoje em Fahrenheit é {}.'.format(f))


#11
dias=float(input('Quantos dias ficou com o carro?'))
km=float(input('Quantos KM rodou?'))
cdias=dias*60
ckm=km*0,15
ctotal=cdias+ckm

print('O total a pagar é de R${:.2f}.'.format(ctotal))
