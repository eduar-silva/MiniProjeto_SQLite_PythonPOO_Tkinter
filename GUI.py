import tkinter
from tkinter import *


class Gui:
    def __init__(self):

        self.x_pad = 5
        self.y_pad = 3
        self.width_entry = 30

        self.window = tkinter.Tk()

        self.window.wm_title("PYSQL Versão 1.0")

        self.txtNome = tkinter.StringVar(self.window)
        self.txtSobrenome = tkinter.StringVar(self.window)
        self.txtEmail = tkinter.StringVar(self.window)
        self.txtcpf = tkinter.StringVar(self.window)

        self.lblNome = tkinter.Label(self.window, text="Nome")
        self.lblSobrenome = tkinter.Label(self.window, text="Sobrenome")
        self.lblEmail = tkinter.Label(self.window, text="E-mail")
        self.lblcpf = tkinter.Label(self.window, text="CPF")

        self.entNome = tkinter.Entry(self.window, textvariable=self.txtNome, width=self.width_entry)
        self.entSobrenome = tkinter.Entry(self.window, textvariable=self.txtSobrenome, width=self.width_entry)
        self.entEmail = tkinter.Entry(self.window, textvariable=self.txtEmail, width=self.width_entry)
        self.entcpf = tkinter.Entry(self.window, textvariable=self.txtcpf, width=self.width_entry)

        self.listClientes = tkinter.Listbox(self.window, width=100)
        self.scrollClientes = tkinter.Scrollbar(self.window)

        self.btnViewAll = tkinter.Button(self.window, text='Ver todos')
        self.btnBuscar = tkinter.Button(self.window, text='Buscar')
        self.btnInserir = tkinter.Button(self.window, text='Inserir')
        self.btnUpdate = tkinter.Button(self.window, text='Atualizar Selecionados')
        self.btnDel = tkinter.Button(self.window, text='Deletar Selecionados')
        self.btnClose = tkinter.Button(self.window, text='Fechar')

        self.lblNome.grid(row=0, column=0)
        self.lblSobrenome.grid(row=1, column=0)
        self.lblEmail.grid(row=2, column=0)
        self.lblcpf.grid(row=3, column=0)

        self.entNome.grid(row=0, column=1, padx=50, pady=50)
        self.entSobrenome.grid(row=1, column=1)
        self.entEmail.grid(row=2, column=1)
        self.entcpf.grid(row=3, column=1)

        self.listClientes.grid(row=0, column=2, rowspan=10)
        self.scrollClientes.grid(row=0, column=6, rowspan=10)

        self.btnViewAll.grid(row=4, column=0, columnspan=2)
        self.btnBuscar.grid(row=5, column=0, columnspan=2)
        self.btnInserir.grid(row=6, column=0, columnspan=2)
        self.btnUpdate.grid(row=7, column=0, columnspan=2)
        self.btnDel.grid(row=8, column=0, columnspan=2)
        self.btnClose.grid(row=9, column=0, columnspan=2)

        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.configure(command=self.listClientes.yview)

        for child in self.window.winfo_children():
            widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=self.x_pad, pady=self.y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=self.x_pad, pady=self.y_pad, sticky='N')


    def run(self):
        self.window.mainloop()