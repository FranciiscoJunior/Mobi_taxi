import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import psycopg2


def redirecionar_atualizar():
    conexao = psycopg2.connect(
        database='mobtaxi',
        user='postgres',
        password='5870SPFC8196',
        host='localhost',
        port='5433'
    )

    cursor = conexao.cursor()
    window = tk.Tk()

    window.geometry('450x250')
    window.title('MOBILIDADE')

    def atualizar_mototaxi():
        #nome = entrada1.get()
        #print(nome)
        telefone = entrada2.get()
        print(telefone)
        #marca_moto = entrada2.get()
        #print(marca_moto)
        #placa = entrada4.get()
        #print(placa)
        #dia_trabalho = entrada5.get()
        #print(dia_trabalho)
        cpf = entrada6.get()
        print(cpf)

        cursor.execute(F'''UPDATE mototaxi SET telefone = '{telefone}' where codigo = '{cpf}' ''')
        conexao.commit()
        tk.messagebox.showinfo(title='AVISO', message='Dados Atualizados')

    def clear_text():
        #entrada1.delete(0, END)
        entrada2.delete(0, END)
        #entrada3.delete(0, END)
        #entrada4.delete(0, END)
        #entrada5.delete(0, END)
        #entrada6.delete(0, END)

    def botao_sair():
        window.destroy()

    label0 = tk.Label(window, text='ATUALIZAR CADASTRO MOTOTAXI', fg='black')
    label0.place(x=130, y=30)

    #label1 = tk.Label(window, text='NOME', fg='black')
    #label1.place(x=190, y=60)

    #entrada1 = Entry(window)
    #entrada1.place(x=250, y=60)

    label2 = tk.Label(window, text='TELEFONE', fg='black')
    label2.place(x=190, y=60)

    entrada2 = Entry(window)
    entrada2.place(x=250, y=60)

    #label3 = tk.Label(window, text='MARCA MOTO', fg='black')
    #label3.place(x=380, y=60)

    #entrada3 = Entry(window)
    #entrada3.place(x=470, y=60)

    #label4 = tk.Label(window, text='PLACA', fg='black')
    #label4.place(x=190, y=120)

    #entrada4 = Entry(window)
    #entrada4.place(x=250, y=120)

    #label5 = tk.Label(window, text='DIA TRABALHO', fg='black')
    #label5.place(x=380, y=90)

    #entrada5 = Entry(window)
    #entrada5.place(x=470, y=90)

    label6 = tk.Label(window, text='CPF', fg='black')
    label6.place(x=220, y=100)

    entrada6 = Entry(window)
    entrada6.place(x=250, y=100)

    botao_atualizar = tk.Button(window, fg='black', text='ATUALIZAR', bg='light blue', height=2, width=20, command=atualizar_mototaxi)
    botao_atualizar.place(x=30, y=60)

    botao_limpar = tk.Button(window, fg='black', text='LIMPAR', bg='light blue', height=2, width=10, command=clear_text)
    botao_limpar.place(x=30, y=110)

    botao_sair = tk.Button(window, fg='black', text='SAIR', bg='light blue', height=2, width=10, command=botao_sair)
    botao_sair.place(x=110, y=110)