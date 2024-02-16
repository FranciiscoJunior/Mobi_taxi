import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import psycopg2


def redirecionar_cadastro():
    conexao = psycopg2.connect(
        database='mobtaxi',
        user='postgres',
        password='5870SPFC8196',
        host='localhost',
        port='5433'
    )

    cursor = conexao.cursor()
    window = tk.Tk()

    window.geometry('650x250')
    window.title('MOB TÁXI')

    def cadastrar_mototaxi():
        nome = entrada1.get()
        telefone = entrada2.get()
        marca_moto = entrada3.get()
        placa = entrada4.get()
        dia_trabalho = entrada5.get()

        cursor.execute(F'''INSERT INTO mototaxi (nome, telefone, marca_moto, placa, dia_trabalho) 
    values ('{nome}','{telefone}','{marca_moto}','{placa}','{dia_trabalho}')''')
        conexao.commit()
        tk.messagebox.showinfo(title='AVISO', message='Dados Inseridos')

    def clear_text():
        entrada1.delete(0, END)
        entrada2.delete(0, END)
        entrada3.delete(0, END)
        entrada4.delete(0, END)
        entrada5.delete(0, END)
        entrada6.delete(0, END)

    def botao_sair():
        window.destroy()

    def clear_list():
        for item in pop.get_children():
            pop.delete(item)

    label0 = tk.Label(window, text='CADASTRAR UM NOVO MOTOTAXI', fg='black', font='bold',)
    label0.place(x=200, y=30)

    label1 = tk.Label(window, text='NOME', fg='black')
    label1.place(x=190, y=60)

    entrada1 = Entry(window)
    entrada1.place(x=250, y=60)

    label2 = tk.Label(window, text='TELEFONE', fg='black')
    label2.place(x=190, y=90)

    entrada2 = Entry(window)
    entrada2.place(x=250, y=90)

    label3 = tk.Label(window, text='MARCA MOTO', fg='black')
    label3.place(x=380, y=60)

    entrada3 = Entry(window)
    entrada3.place(x=470, y=60)

    label4 = tk.Label(window, text='PLACA', fg='black')
    label4.place(x=190, y=120)

    entrada4 = Entry(window)
    entrada4.place(x=250, y=120)

    label5 = tk.Label(window, text='DIA TRABALHO', fg='black')
    label5.place(x=380, y=90)

    entrada5 = Entry(window)
    entrada5.place(x=470, y=90)

    label6 = tk.Label(window, text='CPF', fg='black')
    label6.place(x=420, y=120)

    entrada6 = Entry(window)
    entrada6.place(x=470, y=120)

    botao_adicionar = tk.Button(window, fg='black', text='CADASTRAR', bg='light blue', height=2, width=20, command=cadastrar_mototaxi)
    botao_adicionar.place(x=30, y=60)

    botao_limpar = tk.Button(window, fg='black', text='LIMPAR', bg='light blue', height=2, width=10, command=clear_text)
    botao_limpar.place(x=30, y=110)

    botao_sair = tk.Button(window, fg='black', text='VOLTAR', bg='light blue', height=2, width=10, command=botao_sair)
    botao_sair.place(x=110, y=110)

    label01 = tk.Label(window, text='Mob táxi - © v-0.0.1 - Desenvolvido por Francisco Júnior', fg='black', font='bold')
    label01.place(x=150, y=200)