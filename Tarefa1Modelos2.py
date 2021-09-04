#Jonas Silva de Paiva
#Modelos2 
#Programa para realizar a conjectura de Collatz.

import matplotlib.pyplot as plt

#Craindo a variável number e os vetores "listas" necessárias para o programa
number=int(input('Escolha um número não fracionado para analisar a conjectura de Collatz:\n'))

lista = []
iters = []

#Criamos uma função (def) para pode instanciar em qualquer momento

def collatz(number):

    while number !=1:
        if number% 2 == 0:
            number= number//2
            lista.append(number)   
            iters.append(len(lista))
        else:
           number=  3 * number + 1
           lista.append(number)  
           iters.append(len(lista))  

collatz(number) #instância

#o operador len pega quantas vezes a lista leu o número escolhido
x = len(lista)  

#Lista dos números trabalhados
print('\nA lista dos números trabalhados do número escolhido: \n{} \n' . format(lista))

#Lista das iterações realizadas
print('\nA lista das iterações do número escolhido: \n{} \n' . format(iters))

print('O número escolhido foi {} \n' . format(number))
print('O número de iterações foi {} \n'.format(x))

#Gráfico de Collatz do número selecionado
plt.plot(iters, lista)
plt.xlabel('Número de iterações')
plt.ylabel('Número de casos')
plt.title('Conjectura de Collatz')
plt.show()

#Gráfico de Collatz em Log
plt.yscale('log')
plt.plot(iters, lista)
plt.xlabel('Número de iterações')
plt.ylabel('Número de casos')
plt.title('Conjectura de Collatz em Log')
plt.show()

#Criando o for para varrer os números entre 1 e 1000 para saber o maior número de iterações
for number in range(1, 1000):
    collatz(number)
    maiorValorInters = max(iters)
print('Maior valor de iterações entre 1 e 1000 números é {}'.format(maiorValorInters))

#Fim de programa Tarefa1Modelos2.py