#!/usr/bin/env python3.13

import pyautogui as bot
import sys
import time as s

imagens = ['jaTemPlano.png','mudo.png','contatoErrado.png','semInteresse.png','atendeu.png','listaNegra.png']

areaDeTrabalho="/home/brenner/Área de trabalho"
diretorioPythonBase=f"{areaDeTrabalho}/gitPy"


if len(sys.argv) < 3:
    print("Por favor envie sempre dois argumetos")
    exit()

valorConfidence = float(sys.argv[2])
for i in range(len(imagens)):
    #print(f"valor do argumento 2 é: {valorConfidence}")
    #exit()#>
    if not imagens[i].replace('.png',"") in sys.argv:
        continue
    print(sys.argv[1],valorConfidence)
    if sys.argv[1] in imagens[i].replace('.png',""):
        #valorConfidence = 0.8
        imagemAtual = bot.locateCenterOnScreen(f"{diretorioPythonBase}/{imagens[i]}", confidence=valorConfidence)
        bot.moveTo(imagemAtual,duration=1)
        bot.click(imagemAtual)
        break
    imagemAtual = bot.locateCenterOnScreen(f"{diretorioPythonBase}/{imagens[i]}", confidence=valorConfidence)
    bot.moveTo(imagemAtual,duration=1)
    bot.click(imagemAtual)

# if sys.argv[1] in "jaTemPlano":
#     imagemJatemPlano = bot.locateCenterOnScreen(f"{diretorioPythonBase}/{imagens[0]}", confidence=0.7)
#     s.sleep(2)
#     bot.click(imagemJatemPlano)
#
# if sys.argv[1] in "mudo":
#     imagemJatemPlano = bot.locateCenterOnScreen(f"{diretorioPythonBase}/{imagens[1]}", confidence=0.7)
#     s.sleep(2)
#     bot.click(imagemJatemPlano)
#
# if sys.argv[1] in "contatoErrado":
#     imagemJatemPlano = bot.locateCenterOnScreen(f"{diretorioPythonBase}/{imagens[2]}", confidence=0.7)
#     s.sleep(2)
#     bot.click(imagemJatemPlano)
#
# if sys.argv[1] in "semInteresse":
#     imagemJatemPlano = bot.locateCenterOnScreen(f"{diretorioPythonBase}/{imagens[3]}", confidence=0.8)
#     s.sleep(2)
#     bot.click(imagemJatemPlano)
#
# if sys.argv[1] in "atendeu":
#     imagemJatemPlano = bot.locateCenterOnScreen(f"{diretorioPythonBase}/{imagens[4]}", confidence=0.7)
#     s.sleep(2)
#     bot.click(imagemJatemPlano)
