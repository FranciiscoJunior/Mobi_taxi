import tkinter as tk
from tkinter import *
from tkinter import ttk
from cadastro import redirecionar_cadastro
from atualizar import redirecionar_atualizar
from Deletar import deletar_mototaxi
from tkinter import messagebox
import psycopg2

conexao = psycopg2.connect(
    database='mobtaxi',
    user='postgres',
    password='5870SPFC8196',
    host='localhost',
    port='5433'
)

cursor = conexao.cursor()
window = tk.Tk()

window.geometry('900x350')
window.title('MOB TÁXI')


def redirecionar_cadastro_mototaxi():
    redirecionar_cadastro()


def redirecionar_atualizar_mototaxi():
    redirecionar_atualizar()


def redirecionar_deletar_mototaxi():
    deletar_mototaxi()


def visualizar_mototaxi():
    cursor.execute(f'''SELECT * FROM mototaxi ''')
    dados_mototaxi = cursor.fetchall()
    for item in pop.get_children():
        pop.delete(item)
    for dado in dados_mototaxi:
        pop.insert("", END, values=(dado[0], dado[2], dado[1], dado[3], dado[4], dado[5]))


def clear_list():
    for item in pop.get_children():
        pop.delete(item)


def botao_sair():
    window.destroy()


label0 = tk.Label(window, text='Mototaxistas disponíveis', fg='black', font='bold')
label0.place(x=360, y=20)

label00 = tk.Label(window, text='Menu', fg='black', font='bold')
label00.place(x=80, y=20)

botao_sair = tk.Button(window, fg='black', text='SAIR', bg='light blue', height=2, width=10, command=botao_sair)
botao_sair.place(x=30, y=250)

botao_clear = tk.Button(window, fg='black', text='LIMPAR', bg='light blue', height=2, width=10, command=clear_list)
botao_clear.place(x=110, y=250)

botao_adicionar = tk.Button(window, fg='black', text='CADASTRAR', bg='light blue', height=2, width=20,
                            command=redirecionar_cadastro_mototaxi)
botao_adicionar.place(x=30, y=50)

botao_atualizar = tk.Button(window, fg='black', text='ATUALIZAR', bg='light blue', height=2, width=20,
                            command=redirecionar_atualizar_mototaxi)
botao_atualizar.place(x=30, y=100)

botao_deletar = tk.Button(window, fg='black', text='DELETAR', bg='light blue', height=2, width=20,
                        command=redirecionar_deletar_mototaxi)
botao_deletar.place(x=30, y=150)

botao_visualizar = tk.Button(window, fg='black', text='VISUALIZAR', bg='light blue', height=2, width=20,
                            command=visualizar_mototaxi)
botao_visualizar.place(x=30, y=200)

pop = ttk.Treeview(window, selectmode='browse')
pop.place(x=200, y=60)

label01 = tk.Label(window, text='Mob táxi - © v - 0.0.1 - Desenvolvido por Francisco Júnior', fg='black', font='bold')
label01.place(x=260, y=300)

pop["columns"] = ("0", "1", "2", "3", "4", "5")
pop['show'] = 'headings'
pop.column("0", width=115, anchor='c')
pop.column("1", width=115, anchor='c')
pop.column("2", width=115, anchor='c')
pop.column("3", width=115, anchor='c')
pop.column("4", width=115, anchor='c')
pop.column("5", width=115, anchor='c')

pop.heading("0", text="CÓDIGO")
pop.heading("1", text="TELEFONE")
pop.heading("2", text="NOME MOTORISTA")
pop.heading("3", text="MARCA DA MOTO")
pop.heading("4", text="PLACA DA MOTO")
pop.heading("5", text="DIA DE TRABALHO")

window.mainloop()