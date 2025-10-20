
import pyautogui as bot
import keyboard
import time
import webbrowser
import subprocess
import sys
def funcao(url,perfil):
	# url = 'https://web.whatsapp.com/'
	time.sleep(1)
	print('me chamou seu macharel')
	# webbrowser.open_new(url)

	caminho_chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

	# Exemplo: abrir uma URL em modo anônimo (incógnito)
	args = [
    		caminho_chrome,
    		perfil,  # Modo anônimo
			url
	]

	subprocess.Popen(args)  # URL para abrir

def acaoes(acao):
	subprocess.run(['shutdown.exe',acao,'/t','1'])

def jogo(url):
	subprocess.Popen(['pwsh','-c','Start-Process',url])

def acaoWindows(configuracao,acaoWindowsDisplay):
	print(configuracao,acaoWindowsDisplay)
	subprocess.Popen(['pwsh','-c','Start-Process',f"{configuracao}:{acaoWindowsDisplay}"])


def trocarAudio():
	print('kkkkk chamou audio')
	subprocess.Popen(['pwsh','-File','c:/users/brenner/Desktop/powershell/audio.ps1'])
	subprocess.Popen(['pwsh','-c',"New-BurntToastNotification -Text 'AUDIO','Audio alterado com sucesso!'"])

keyboard.add_hotkey('ctrl+alt+w',lambda:funcao('https://web.whatsapp.com/','--profile-directory=DIB'))
keyboard.add_hotkey('ctrl+alt+b',lambda:funcao('https://www.sistemaviverbemseguros.com/version-022iq','--profile-directory=DIB'))
keyboard.add_hotkey('ctrl+alt+y',lambda:funcao('https://www.youtube.com/','--profile-directory=Brenner'))
keyboard.add_hotkey('ctrl+alt+c',lambda:funcao('https://app.botconversa.com.br/137591/live-chat/all/3cea6f8b790f3d42b36a60853f650e0e77b077b7eca07b950a0501082375cb57','--profile-directory=DIB'))
keyboard.add_hotkey('ctrl+alt+2',lambda:acaoes('/p'))
keyboard.add_hotkey('ctrl+alt+1',lambda:acaoes('/r'))
keyboard.add_hotkey('ctrl+alt+e',lambda:jogo('steam://rungameid/2669320'))
keyboard.add_hotkey('ctrl+alt+a',lambda:trocarAudio())
keyboard.add_hotkey('ctrl+alt+n',lambda:acaoWindows('ms-settings','nightlight'))
keyboard.add_hotkey('ctrl+alt+u',lambda:acaoWindows('ms-settings','windowsupdate-action'))



keyboard.wait('esc')
