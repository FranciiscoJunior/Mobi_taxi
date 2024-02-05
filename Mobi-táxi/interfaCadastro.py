import tkinter as tk
from tkinter import *
from tkinter import ttk
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

windowCadastro = tk.Tk()

windowCadastro.geometry('900x550')
windowCadastro.title('MOBILIDADE')

def interface_cadastro():
