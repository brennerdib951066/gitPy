#!/usr/bin/env python3


import pyautogui as bot
from time import sleep as s
import webbrowser as web
import requests as api
import flet as ft
import tkinter as tk
from tkinter import messagebox as ms

escrever = ['live','brenner santos','7382090817','live','denner pereira','5561 96657918','live','brenner oliveira','9599112456','live','ricardo lunes','9599578944','live','marcus cacete','959595','live','lucas amorim','56456454','live','fabio souza','455645654','live','ordiga marteiga','4564545','live','gabriel silva','4565778968','live','gabriela preta','456478752','live','lacal locate','8854456656','live','cogilau','885544566','live','bando bandoleiro','5656565611','live','hugo souza','4564564','live','carlos vasco','456423624','live','virginia vaga','4565422362','live','ivan vam','45654113','live','hiago vago','45641266','live','rato rocha','565656','live','marcel gandara','45645561152','live','marcelino marchal','45454','live','choque super','655415465','live','cabral ruger','789875654','live','leticia hamal','899665544','live','andreson silva','65255156','live','paulo palulinho','44566544','live','laura melo','54565116','live','lais moriais','45654135858','live','paula fernandes','4966541256','live','paula tolada','223364456','live','tarsontay','45656777','live','rock lee','25655844','live','kimimaro','6362541','live','kiba','86756547','live','tobi','56998745','live','hinata','32514455','live','him','6958477','live','shidori','5855456419','live','tobirama','87879456','live','marchareu lambda','5444879456','live','kakaroto','4577451','live','veditta','45564155498','live','kuririn','554985414','live','chichi','4548469','live','cell','456745','live','kurama','78945645','live','sasuke','44456874111','live','flavio ham','4595455654']
escrever2 = ['live','obdiencia sempre','541254455','live','cedo se vai','5561 96657944','live','Seu francisco respeita são januário','959911245600','live','Tocando como sempres','95995789414','live','hiro kasahara','9595945','live','luca lukinha','5645645444','live','solta o vaso','45564565477','live','a pedra caiu no meu pé','4564545111','live','me sujei de lama','45657789682','live','briguei no transito','456478751112','live','quis bater e apanhou','88544566562','live','solta a corda e deixa ele cair do penhasco','88554456600','live','se o trem passe em cima de você o que veria? nada!','565656561199877','live','imagina se o vaso fala-se','456456488','live','que banho porco','45642362465','live','o feijao cansou do joão','456542236221','live','sua mao robou e tessado o decipou','4565411334','live','ao som do forro','4564126644','live','o gato preguiçoso apanhba do rato','565656222','live','que cama dura essa sua','45645561133','live','foi eu e dai?','454547666','live','o choque fez você mudar de cor','655415465221','live','existe negro gato?','789875654222','live','quem foi o primeiro a tirar leite? a leticia','8996655441','live','quem nadou andando e ainda tinha um som? o anderson','6525515621','live','o simples complicou','445665444441','live','maurcio malfeitor','5456511634','live','morde que eu gosto','4565413585811','live','o cao que muito late esta cheio de ração','49665412562211','live','tamnho G de gordo','223364456111','live','hiro san','245656777','live','jota j','125655844','live','kuabara','63625413','live','genkay','8675654744','live','senjutsu','569987452121','live','alegria','3251554','live','him pedeu um rim','695847755','live','machi','585545641911','live','ameagari no machi no sumi','878794562222','live','kimiwa','54448794562','live','sakura-chan','4577451222','live','aloprado','455641554981','live','ta danado de bommm','55498541422','live','vida chaim','4548469454325','live','shamaym','4567453333','live','kakashi','7894564533','live','sasukeeeeee','44456874111333','live','bam bam bam','4595455654']


duasTelas = 'yes'
i = 0

print(len(escrever))
if duasTelas == 'yes':
    print('É duas telas')
    s(3)
    bot.click(900,1315,duration=0.50)
    for lista in "Escrever[1]","Escrever[2]":
        i += 1
        print('{}) {}'.format(i,lista))
    opcao = input("Escolha uma opção:   ")
    if opcao == 1:
        for escrevi in escrever:
            s(5.5)
            bot.write('{}\n'.format(escrevi))

    else:
        for escrevi in escrever2:
            s(5.5)
            bot.write('{}\n'.format(escrevi))


from pegarLead import clicarCadastrar as cc
pergunta = ms.askyesno('O que deseja fazer','Deseja clicar em cadastrar no sistema viver bem?')
if pergunta:
    print('BELEZA ENTAO')
    cc() # chamdno a função do outro arquivo caso precise
else:
    print('SAINDO')

#print(len(escrever)/3)

