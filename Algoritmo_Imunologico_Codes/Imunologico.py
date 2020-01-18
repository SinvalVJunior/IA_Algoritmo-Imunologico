from random import *
import math
import matplotlib.pyplot as plt
import numpy as np

populacao = []
TAM = 500
i = 0
num_geracoes = 500
maiores = []
menores = []
media_ger = []
#-----------Cria a populacao------------------
while(i<TAM):
    v = [uniform(0,10),uniform(0,10),0]
    populacao = populacao + [v]
    i = i+1

l = 0
while l<= num_geracoes:
    #------------Clonagem--------------------------
    def clonar(populacao):
        clonados = []
        for v in populacao:
            clonados = clonados + [v,v,v,v,v]
        return clonados
    populacao = clonar(populacao)
    # --------------Descobre Aptidao---------------------
    def Alpine(x1, x2):
        return (x1 ** (1 / 2) * math.sin(x1)) * (x2 ** (1 / 2) * math.sin(x2))

    def funcaoObjetivo(populacao):
        sum = 0
        for vetor in populacao:
            vetor[2] = Alpine(vetor[0], vetor[1]) + 7
            sum = sum + vetor[2]
        return sum

    funcaoObjetivo(populacao)
    #---------------Mutacao-----------------------------
    def obterMaior(populacao):
        maior = populacao[0]
        for v in populacao:
            if (v[2] > maior[2]):
                maior = v
        return maior
    def mutar(populacao,maior):
        mutados = []
        for v in populacao:
            libera = uniform(0,1)
            valor = -5*(v[2]/maior[2])
            taxa_mutacao = np.exp(valor)
            if(libera < taxa_mutacao):
                valor = uniform(-1,1)
                if(v[0] + valor >=0 and v[0] + valor <=10  ):
                    v[0] = v[0]+valor
                valor = uniform(-1, 1)
                if (v[1] + valor >= 0 and v[1] + valor <=10):
                    v[1] = v[1] + valor
            mutados = mutados+ [[v[0],v[1],0]]
        return mutados

    maior = obterMaior(populacao)
    populacao = mutar(populacao,maior)
    sum = funcaoObjetivo(populacao)
    #---------------Selecionar--------------------------
    def maior(lista):
        maior = lista[0]
        for v in lista:
            if (v[2] > maior[2]):
                maior = v
        return maior
    def selecionar(populacao):
        selecionados = []
        i = 0
        while i < len(populacao):
            v = [populacao[i]]+[populacao[i+1]]+[populacao[i+2]]+[populacao[i+3]]+[populacao[i+4]]
            v = maior(v)
            selecionados = selecionados + [v]
            i = i + 5
        return selecionados
    populacao = selecionar(populacao)
    sum = funcaoObjetivo(populacao)
    #----------Estudo da populacao------------



    def obterMenor(populacao):
        menor = populacao[0]
        for v in populacao:
            if (v[2] < menor[2]):
                menor = v
        return menor

    maior = obterMaior(populacao)
    menor = obterMenor(populacao)
    media = sum / TAM
    maiores.append(maior[2])
    menores.append(menor[2])
    media_ger.append(media)

    l = l+1

geracoes =[]
for v in range(0,num_geracoes+1):
    geracoes = geracoes +[v]

#plt.plot(geracoes,maiores)
#plt.plot(geracoes,menores)
#plt.plot(geracoes,media_ger)
#plt.show()

def funcaoObjetivoCountour(X,Y,tam):
    z = []
    valor = []
    for i in range(0,tam):
        for j in range(0,tam):
                ponto = Alpine(X[i][j], Y[i][j]) + 7
                valor.append(ponto)
        z = z + [valor]
        valor = []
    return z
def toXArray(populacao):
    x = []
    for k in populacao:
        aux = []
        aux = aux + [k[0]]
        x = x + [aux]
    return x
def toYArray(populacao):
    y = []
    for k in populacao:
        aux = []
        aux = aux + [k[1]]
        y = y + [aux]
    return y
def funcaoObjetivo(X,Y,tam):
    z = []
    valor = []
    for i in range(0,tam):
        for j in range(0,tam):
                ponto = Alpine(X[i][j], Y[i][j]) + 7
                valor.append(ponto)
        z = z + [valor]
        valor = []
    return z


x_vals = toXArray(populacao)
y_vals = toYArray(populacao)

fig, ax = plt.subplots()
print(x_vals)
print("--------")
print(y_vals)
ax.plot(x_vals, y_vals,'ro')

ax.set_title('Populaçao Final :')
ax.set_xlabel('x')
ax.set_ylabel('y')

start, stop, n_values = 0, 10, 100
x = np.linspace(start, stop, n_values)
y = np.linspace(start, stop, n_values)
I, J = np.meshgrid(x, y)

Z = funcaoObjetivo(I,J,n_values)
cp = ax.contour(I, J, Z)
plt.colorbar(cp)
ax.clabel(cp, inline=True,
          fontsize=10)

plt.show()
print(maior)