#!/usr/bin/env python2


import pyautogui as bot
from time import sleep as s
import webbrowser as web
import requests as api
import flet as ft
import customtkinter as ct
import subprocess as cmd

# Criando funções

def desligar():
    print('Você clicou em desligar')
    s(2)
    # Desligando o pc no linux
    desligando = cmd.run(['systemctl','poweroff','-i'])

def reiniciar():
    print('Você clicou em REINICIAR')
    s(2)
    # Desligando o pc no linux
    desligando = cmd.run(['systemctl','reboot','-i'])

def suspender():
    print('Você clicou em SUSPENDER')
    s(2)
    # Desligando o pc no linux
    desligando = cmd.run(['systemctl','suspend','-i'])

# Criando a janela do programa
janela = ct.CTk()
janela.title('AÇÔES DO SISTEMA')
janela.geometry('400x350')
janela.resizable(False,False)

# Criando Label
labelTop = ct.CTkLabel(
    janela,
    text = 'AÇÔES:',
    font = ('Arial',25),
    #bg_color = 'blue',
    padx = 10,
    pady = 10,
    anchor = 'w'
)

# Botões
botaoDesligar = ct.CTkButton(
    janela,
    text = 'DESLIGAR',
    font = ('Opens-Sans',18),
    height = 45,
    hover_color = 'lightblue',
    command = desligar
)

botaoReiniciar = ct.CTkButton(
    janela,
    text = 'REINICIAR',
    font = ('Opens-Sans',18),
    height = 45,
    hover_color = 'black',
    command = reiniciar
)

botaoSuspender = ct.CTkButton(
    janela,
    text = 'SUSPENDER',
    font = ('Opens-Sans',18),
    height = 45,
    hover_color = 'black',
    command = suspender
)

# adicionando os elementos na janela
labelTop.pack(fill='x',pady=(15))
botaoDesligar.pack(fill='x',padx = (5),pady = (5))
botaoReiniciar.pack(fill='x',padx = (5),pady = (5))
botaoSuspender.pack(fill='x',padx = (5),pady = (5))
# Chamando a janela para a tela
janela.mainloop()
