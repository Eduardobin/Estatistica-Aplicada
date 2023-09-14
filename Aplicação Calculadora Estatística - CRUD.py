import tkinter as tk
import math
#Entrada de dados!!
#Import para teste
lista = [["mercado",1000],["agua, luz e net",500],["aluguel",1500],["lazer",600],["cartão de crédito",1200]]
lista2 = [100,101,100,99,95,90,99,96,98,102,124,112,106,108,91,90,90,96,93,102,98,103,103,93,93,92]
#Processamento Pareto [str,num]
def pareto(lista):
    lr=[]
    soma=0
    p=0
    for i in lista:
        soma=soma+i[1]
    for i in lista:
        r=(i[1]/soma)*100
        lr.append(r)
    for i in lr:
        lista[p].append(i)
        p+=1
    print(f'''
Tabela análise de pareto
Descrição                   Valor           percent             ac.percert            
''')
    ac=0
    for i in lista:
        ac=ac+i[2]
        print(f'''
{i[0]}           {i[1]}            {i[2]}               {ac}''')
#Ordenando lista formato [str,num]
def ordenando (lista):
    listord=[]
    L=len(lista)
    v=True
    while L!=0:
        m=0
        y = lista[m]
        for i in lista:
            if y[1]>i[1]: 
                y=i
        for i in lista:
            if y[1]<=i[1]:
                v=True
            else:
                v=False    
        if v == True:        
            lista.remove(y)
            listord.append(y)
        L=len(lista)
    print('lista ordenada = ', listord)
    return listord
#Medidas e tabelas de distribuição de frequência
def dist_freq(lista):
    lista.sort()
    tamanho = len(lista)
    media = sum(lista)/len(lista)
    maximo = max(lista)
    minimo = min(lista)
    amplitude = maximo-minimo
    if tamanho%2 == 0:
        mediana = (lista[(tamanho//2)-1]+lista[(tamanho//2)])/2
        quartis1 = (lista[((tamanho//2)//2)-1]+lista[((tamanho//2)//2)])/2
        quartis3 = (lista[(tamanho*3//4)]+lista[(tamanho*3//4)+1])/2
    else:
        mediana = lista[(tamanho//2)-1]
        quartis1 = lista[((tamanho//2)//2)-1]
        quartis3 = lista[(tamanho*3//4)+1]
    iqr = quartis3-quartis1
    outup = quartis3 + 1.5*iqr
    outdown = quartis1 - 1.5*iqr
    dados_out = []
    for i in lista:
        if i > outup or i < outdown:
            dados_out.append(i)
#moda autoral
    moda=[]
    x=0
    y=0
    for i in lista:
        x=lista.count(i)
        if x > y:
            moda=[]
            y=x
            moda.append(i)
        elif x == y:
            if i not in moda:
                moda.append(i)
    print(media)
    print(maximo)
    print(minimo)
    print(amplitude)
    print(quartis1)
    print(mediana)
    print(quartis3)
    print(lista)
    print('dados fora: ',dados_out)
    print(moda)


dist_freq(lista2)





