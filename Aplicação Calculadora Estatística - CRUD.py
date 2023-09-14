import tkinter as tk
import math
#Entrada de dados!!
#Import para teste
lista = [["mercado",1000],["agua, luz e net",500],["aluguel",1500],["lazer",600],["cartão de crédito",1200]]
#Processamento Pareto
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


print(f'{pareto(ordenando(lista))}')