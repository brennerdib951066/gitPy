#!/usr/bin/env python3

import flet as ft
#from tkinter import messagebox
def valores(e):
    valorEmail = inputEmail.value
    valorSenha = inputSenha.value

    print('{}\n{}'.format(valorEmail,valorSenha))

    if valorEmail or valorSenha:
        if valorEmail in 'brenner'  and valorSenha in '652516':
            messagebox.showinfo('SUCESSO','Login realizado com sucesso {}'.format(valorEmail))
            print('LOGIN')
        else:
            messagebox.showerror('ERRO','Não encontramos a credêncial fornecida {}'.format(valorEmail))
    else:
        messagebox.showerror('ERRO','Forneça suas credênciais, por favor'.format(valorEmail))

def funcao(e):
    print('Me chamou')

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = "adaptive"
    # CRIANDO OS ELEMENTOS DA JANELA
    texto = ft.Text("カタカナ", size=80, color="pink600", italic=True)
    # Iniciando o alfabeto
    textア = ft.Text("ア",size=60,tooltip='A')
    textイ = ft.Text("イ",size=60,tooltip='I')
    textウ = ft.Text("ウ",size=60,tooltip='U')
    textエ = ft.Text("エ",size=60,tooltip='E')
    textオ = ft.Text("オ",size=60,tooltip='O')
    # FAMILIA DO KA
    textカ = ft.Text("カ",size=60,tooltip='KA')
    textキ = ft.Text("キ",size=60,tooltip='KI')
    textク = ft.Text("ク",size=60,tooltip='KU')
    textケ = ft.Text("ケ",size=60,tooltip='KE')
    textコ = ft.Text("コ",size=60,tooltip='KO')
    # FAMILIA DO SA
    textサ = ft.Text("サ",size=60,tooltip='SA')
    textシ = ft.Text("シ",size=60,tooltip='SHI')
    textス = ft.Text("ス",size=60,tooltip='SU')
    textセ = ft.Text("セ",size=60,tooltip='SE')
    textソ = ft.Text("ソ",size=60,tooltip='SO')
    # FAMILIA DO TA
    textタ = ft.Text("タ",size=60,tooltip='TA')
    textチ = ft.Text("チ",size=60,tooltip='TI')
    textツ = ft.Text("ツ",size=60,tooltip='TSU')
    textテ = ft.Text("テ",size=60,tooltip='TE')
    textト = ft.Text("ト",size=60,tooltip='TO')
    # FAMILIA DO NA
    textナ = ft.Text("ナ",size=60,tooltip='NA')
    textニ = ft.Text("ニ",size=60,tooltip='NI')
    textヌ = ft.Text("ヌ",size=60,tooltip='NU')
    textネ = ft.Text("ネ",size=60,tooltip='NE')
    textノ = ft.Text("ノ",size=60,tooltip='NO')
    # FAMILIA DO HA
    textハ = ft.Text("ハ",size=60,tooltip='HA')
    textヒ = ft.Text("ヒ",size=60,tooltip='HI')
    textフ = ft.Text("フ",size=60,tooltip='FU')
    textヘ = ft.Text("ヘ",size=60,tooltip='HE')
    textホ = ft.Text("ホ",size=60,tooltip='HO')
    # FAMILIA DO MA
    textマ = ft.Text("マ",size=60,tooltip='MA')
    textミ = ft.Text("ミ",size=60,tooltip='MI')
    textム = ft.Text("ム",size=60,tooltip='MU')
    textメ = ft.Text("メ",size=60,tooltip='ME')
    textモ = ft.Text("モ",size=60,tooltip='MO')
    # FAMILIA DO YA
    textヤ = ft.Text("ヤ",size=60,tooltip='YA')
    textYI = ft.Text("",size=60)
    textユ = ft.Text("ユ",size=60,tooltip='YO')
    textYE = ft.Text("",size=60)
    textヨ = ft.Text("ヨ",size=60,tooltip='YU')
    # FAMILIA DO RA
    textラ = ft.Text("ラ",size=60,tooltip='RA')
    textリ = ft.Text("リ",size=60,tooltip='RI')
    textル = ft.Text("ル",size=60,tooltip='RU')
    textレ = ft.Text("レ",size=60,tooltip='RE')
    textロ = ft.Text("ロ",size=60,tooltip='RO')
    # FAMILIA DO WA
    textワ = ft.Text("ワ",size=60,tooltip='WA')
    textWI = ft.Text("",size=60)
    textWU = ft.Text("",size=60)
    textWE = ft.Text("",size=60)
    textヲ = ft.Text("ヲ",size=60,tooltip='WO')
    textン = ft.Text("ン",size=60)
    # FAMILIA DO NN
    textン = ft.Text("ン",size=60,tooltip='UM')

    # LABEL DE INFORMAÇÂO
    textInfo = ft.Text('Apenas uma vizualização de uma das formas de escritas japonesa, neste caso KATAKANA')

    grupoTextHiragana =  ft.Container(
                ft.Row(

                    wrap=True,
                    controls = [texto],
                    alignment=ft.MainAxisAlignment.CENTER
                )


            )

    grupoVogal = ft.Container(

                    ft.Column(
                         wrap=True,
                           controls = [textア,textイ,textウ,textエ,textオ]
                        ),
                    bgcolor='#ffffff',
                    border_radius=10
                )
    grupoKA = ft.Container(
                    ft.Column(
                         wrap=True,
                           controls = [textカ,textキ,textク,textケ,textコ]
                        ),
                    bgcolor='#ffffff',
                    border_radius=10
                )
    grupoSA = ft.Container(
                    ft.Column(
                         wrap=True,
                           controls = [textサ,textシ,textス,textセ,textソ]
                        ),
                    bgcolor='#ffffff',
                    border_radius=10
                )
    grupoTA = ft.Container(
                    ft.Column(
                         wrap=True,
                           controls = [textタ,textチ,textツ,textテ,textト]
                        ),
                    bgcolor='#ffffff',
                    border_radius=10
                )

    grupoNA = ft.Container(
                    ft.Column(
                         wrap=True,
                           controls = [textナ,textニ,textヌ,textネ,textノ]
                        ),
                    bgcolor='#ffffff',
                    border_radius=10
                )
    grupoHA = ft.Container(
                    ft.Column(
                         wrap=True,
                           controls = [textハ,textヒ,textフ,textヘ,textホ]
                        ),
                    bgcolor='#ffffff',
                    border_radius=10
                )
    grupoMA = ft.Container(
                    ft.Column(
                         wrap=True,
                           controls = [textマ,textミ,textム,textメ,textモ]
                        ),
                    bgcolor='#ffffff',
                    border_radius=10
                )
    grupoYA = ft.Container(
                    ft.Column(
                         wrap=True,
                           controls = [textヤ,textYI,textユ,textYE,textヨ]
                        ),
                    bgcolor='#ffffff',
                    border_radius=10
                )
    grupoRA = ft.Container(
                    ft.Column(
                         wrap=True,
                           controls = [textラ,textリ,textル,textレ,textロ]
                        ),
                    bgcolor='#ffffff',
                    border_radius=10
                )
    grupoWA = ft.Container(
                    ft.Column(
                         wrap=True,
                           controls = [textワ,textWI,textWU,textWE,textヲ]
                        ),
                    bgcolor='#ffffff',
                    border_radius=10
                )
    grupoN = ft.Container(
                    ft.Column(
                         wrap=True,
                           controls = [textン]
                        ),
                    bgcolor='#ffffff',
                    border_radius=10
                )

    grupoPaiRow = ft.Container(
                    ft.Row(
                        wrap=True,
                        controls = [grupoVogal,grupoKA,grupoSA,grupoTA,grupoNA,grupoHA,grupoMA,grupoYA,grupoRA,grupoWA,grupoN],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=50

                    ),
                    bgcolor='#f2f2f2',
                    padding=15,
                    border_radius=25,

            )


    page.add(
    grupoTextHiragana,
    grupoPaiRow,
    textInfo
    )
ft.app(target=main)
