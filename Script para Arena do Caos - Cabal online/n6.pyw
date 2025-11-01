# bibliotecas
import pyautogui
import keyboard
import time
import pydirectinput

# começa rodar o Script
print("Pressione F8 para executar a sequência uma vez!")

# espera até você apertar F8
keyboard.wait("F8")
time.sleep(5)

# sequencia de cliques para entrar no calabouço

# clica em "Arena do caos nivel 6"
pyautogui.moveTo(785,355, duration=0.7)
pyautogui.click()
time.sleep(5)

# clica em "Entrar"
pyautogui.moveTo(1131, 889, duration=0.7)
pyautogui.click()
time.sleep(5)

# clica em "Desafio"
pyautogui.moveTo(814, 767, duration=0.7)
pyautogui.click()
time.sleep(5)

# clica para andar
pyautogui.moveTo(1182, 240, duration=0.7)
pyautogui.click()
time.sleep(5)

# clica para andar
pyautogui.moveTo(1343, 400, duration=0.7)
pyautogui.click()
time.sleep(5)

print("Sequência executada!")