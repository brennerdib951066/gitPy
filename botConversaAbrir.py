#!/usr/bin/python3


import pyautogui as bot
from time import sleep as s
import webbrowser as web
import requests as api
import flet as ft
import customtkinter as ct
import subprocess as cmd

# FUNÇÔES


def abrirBotConversa(perfil='DIB',campanhaBot='2547'):
    url='https://app.botconversa.com.br/{}/flows'.format(campanhaBot)
    abrir = cmd.Popen(['google-chrome-stable', '--profile-directory={}'.format(perfil),'{}'.format(url)])
    janela.destroy() # fechando a janela

janela = ct.CTk()
janela.title('BotConversa')
janela.geometry('400x350+804+645')
janela.resizable(False,False)

titulo = ct.CTkLabel(
    janela,
    text = 'Onde deseja abrir o bot?',
    font = ('Arial',25),
    anchor = 'center',
    width = 400,
    padx = 15,
    pady = 15
)

botaoDib = ct.CTkButton(
    janela,
    text = 'Campanha DIB',
    height= 45,
    command = lambda: abrirBotConversa() # Aqui ele pegará os argumentos padroẽs, pelo fato de esta vazio aqui

)

botaoViverBem = ct.CTkButton(
    janela,
    text = 'Campanha viver bem(programação)',
    height= 45,
    command = lambda: abrirBotConversa(perfil='programacaoViverBem',campanhaBot='137591')

)

tituloBaixo = ct.CTkLabel(
    janela,
    text = 'Programa produzido por DIB software, venha e também garanta o seu!',
    font = ('Opens-Sans',10),
    anchor = 'e'
)

# Iniciando os elementos na janela
titulo.grid(
    row=0,
    column=0
)

botaoDib.grid(
    row=1,
    column=0,
    padx = 15,
    pady = 15,
    sticky = 'we'

)
botaoViverBem.grid(
    row=2,
    column=0,
    padx = 15,
    sticky = 'we'
)
tituloBaixo.grid(
    row=3,
    column=0
)
janela.mainloop()

