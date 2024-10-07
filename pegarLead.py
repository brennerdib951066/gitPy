#!/usr/bin/env python3


import pyautogui as bot
from time import sleep as s
import webbrowser as web
import requests as api
import flet as ft



def clicarCadastrar():
    qtdUsuario = input('(deixe vazio para usar qtd pdrão) quantidade:   '.upper())
    if not qtdUsuario:
        qtd = 52
    else:
        qtd = qtdUsuario
    print(qtd)
    s(5)
    for i in range(qtd):
        s(1)
        bot.click(950,450)

clicarCadastrar()

