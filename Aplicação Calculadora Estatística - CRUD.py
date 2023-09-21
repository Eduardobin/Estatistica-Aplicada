from tkinter import *
from tkinter import ttk
#import matplotlib.pyplot as plt 
#Entrada de dados!!
#Import para teste
lista = [["mercado",1000],["agua, luz e net",500],["aluguel",1500],["lazer",600],["cartão de crédito",1200]]
lista2 = [100,101,100,99,95,90,99,99,96,98,102,124,112,106,108,91,90,90,96,93,102,98,103,103,93,93,92]
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
{i[0]}                {i[1]}            {i[2]}               {ac}''')
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


#dist_freq(lista2)
#print(pareto(ordenando(lista)))



def iniciar():
    #Tela1
    Tela_1 = Tk()
    Tela_1.title("Calculadora Estatística")
    Tela_1.configure(background='#1e3743')
    Tela_1.geometry("700x600")
    Tela_1.resizable(True,True)
    Tela_1.maxsize(width=840, height=720)
    Tela_1.minsize(width=583 , height=500)
    #Frame Tela 1
    frame_1 = Frame(Tela_1, bd=4, bg='#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
    frame_1.place(relx=0.025, rely=0.225, relwidth=0.7, relheight=0.5)
    #Widgets
    bt_txt = Button(Tela_1, text='TXT')
    bt_txt.place(relx=0.025, rely=0.125,relwidth=0.1,relheight=0.05)
    bt_sql = Button(Tela_1, text='SQL')
    bt_sql.place(relx=0.125, rely=0.125,relwidth=0.1,relheight=0.05)
    bt_manual = Button(Tela_1, text='Manual', command=insert_manual)
    bt_manual.place(relx=0.225, rely=0.125,relwidth=0.1,relheight=0.05)
    bt_incluir = Button(Tela_1, text='Incluir')
    bt_incluir.place(relx=0.025, rely=0.775,relwidth=0.1,relheight=0.05)
    bt_alterar = Button(Tela_1, text='Alterar')
    bt_alterar.place(relx=0.125, rely=0.775,relwidth=0.1,relheight=0.05)
    bt_excluir = Button(Tela_1, text='Excluir')
    bt_excluir.place(relx=0.225, rely=0.775,relwidth=0.1,relheight=0.05)   
    bt_pareto = Button(Tela_1, text='Pareto')
    bt_pareto.place(relx=0.775, rely=0.45,relwidth=0.15,relheight=0.125)
    bt_medidas = Button(Tela_1, text='Medidas')
    bt_medidas.place(relx=0.775, rely=0.6,relwidth=0.15,relheight=0.125)
    #TreeView
    listaCli = ttk.Treeview(frame_1, height=3, columns=("col1","col2","col3"))
    listaCli.heading("#0", text="#")
    listaCli.heading("#1", text="Descrição")
    listaCli.heading("#2", text="Valor")
    listaCli.column("#0", width=10)
    listaCli.column("#1", width=90)
    listaCli.column("#2", width=50)
    listaCli.place(relx=0.01, rely=0.025, relwidth=0.95, relheight=0.95)
    scroolLista = Scrollbar(frame_1, orient='vertical')
    listaCli.configure(yscroll=scroolLista.set)
    scroolLista.place(relx=0.96, rely=0.025, relwidth=0.04, relheight=0.95)
    Tela_1.mainloop()
    ## Pegar os valores das variáveis

    

def insert_manual():
    
    



    #Tela2
    Tela_2 = Tk()
    Tela_2.title("Inserir Dados Manual")
    Tela_2.configure(background='#1e3743')
    Tela_2.geometry("400x400")
    Tela_2.resizable(True,True)
    Tela_2.maxsize(width=480, height=480)
    Tela_2.minsize(width=333 , height=333)
    #Widgets
    bt_salvar = Button(Tela_2, text='Salvar')
    bt_salvar.place(relx=0.025, rely=0.875,relwidth=0.2,relheight=0.1)
    bt_sair = Button(Tela_2, text='Sair', command=Tela_2.destroy)
    bt_sair.place(relx=0.775, rely=0.875,relwidth=0.2,relheight=0.1)
    bt_add = Button(Tela_2, text='Adicionar', command=add(cod_entry, desc_entry, valor_entry))
    bt_add.place(relx=0.75, rely=0.55,relwidth=0.2,relheight=0.1)
    bt_alterar = Button(Tela_2, text='Alterar')
    bt_alterar.place(relx=0.75, rely=0.65,relwidth=0.2,relheight=0.1)
    ##Frame TreeView
    frame_2 = Frame(Tela_2, bd=4, bg='#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
    frame_2.place(relx=0.025, rely=0.225, relwidth=0.7, relheight=0.5)
    listaCli_2 = ttk.Treeview(frame_2, height=3, columns=("col1","col2","col3"), show="headings")
    listaCli_2.heading("#0", text="#")
    listaCli_2.heading("#1", text="Descrição")
    listaCli_2.heading("#2", text="Valor")
    listaCli_2.column("#0", width=10)
    listaCli_2.column("#1", width=90)
    listaCli_2.column("#2", width=50)
    listaCli_2.place(relx=0.01, rely=0.025, relwidth=0.95, relheight=0.95)
    scroolLista = Scrollbar(frame_2, orient='vertical')
    listaCli_2.configure(yscroll=scroolLista.set)
    scroolLista.place(relx=0.96, rely=0.025, relwidth=0.04, relheight=0.95)
    ## Criação da label e entrada #
    lb_cod = Label(Tela_2, text = "#",bg='#1e3743',fg='white')
    lb_cod.place(relx= 0.75, rely= 0.2 )
    cod_entry = Entry(Tela_2)
    cod_entry.place(relx= 0.75, rely= 0.25, relwidth= 0.2)
    ## Criação da label e entrada descrição
    lb_desc = Label(Tela_2, text = "Descrição", bg='#1e3743', fg='white')
    lb_desc.place(relx= 0.75, rely= 0.3 )
    desc_entry = Entry(Tela_2)
    desc_entry.place(relx= 0.75, rely= 0.35, relwidth= 0.2)
    ## Criação da label e entrada valor
    lb_valor = Label(Tela_2, text = "Valor", bg='#1e3743', fg='white')
    lb_valor.place(relx= 0.75, rely= 0.4 )
    valor_entry = Entry(Tela_2)
    valor_entry.place(relx= 0.75, rely= 0.45, relwidth= 0.2)

    cod = 

    def add(cod, desc, valor):
        lista=[]
        l=[]
        l.append(cod)
        l.append(desc)
        l.append(valor)
        lista.append(l)
        print(lista)
        for (i,d,v) in lista:
            listaCli_2.insert("", "end", values=(i,d,v))
        return lista



    Tela_2.mainloop()
iniciar()    

    
        









