import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import psycopg2


def deletar_mototaxi():
    conexao = psycopg2.connect(
        database='mobtaxi',
        user='postgres',
        password='5870SPFC8196',
        host='localhost',
        port='5433'
    )

    cursor = conexao.cursor()
    window = tk.Tk()

    window.geometry('350x250')
    window.title('MOBILIDADE')

    def deletar_mototaxi():
        cpf = entrada6.get()

        cursor.execute(f'''DELETE FROM mototaxi where codigo = '{cpf}' ''')
        conexao.commit()
        tk.messagebox.showinfo(title='AVISO', message='Dados Deletados')

        def clear_text():
            entrada6.delete(0, END)

        def botao_sair():
            window.destroy()

    label6 = tk.Label(window, text='CPF', fg='black')
    label6.place(x=70, y=60)

    entrada6 = Entry(window)
    entrada6.place(x=100, y=60)

    botao_deletar = tk.Button(window, fg='black', text='DELETAR', bg='light blue', height=2, width=20, command=deletar_mototaxi)
    botao_deletar.place(x=80, y=90)

    botao_limpar = tk.Button(window, fg='black', text='LIMPAR', bg='light blue', height=2, width=10, command=clear_text)
    botao_limpar.place(x=30, y=110)

    botao_sair = tk.Button(window, fg='black', text='SAIR', bg='light blue', height=2, width=10, command=botao_sair)
    botao_sair.place(x=110, y=110)