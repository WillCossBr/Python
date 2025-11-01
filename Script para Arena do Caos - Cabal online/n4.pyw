# bibliotecas
import pyautogui
import keyboard
import time
import pydirectinput

# INICIO ****************************************************************************************************************************************

print("Pressione F8 para executar a sequência 5 vezes!")

# espera até você apertar F8
keyboard.wait("F8")
time.sleep(5)

# REPETE 7 VEZES
for i in range(7):
    print(f"Arena do Caos nivel 4 - {i+1}/7")

    # SEQUENCIA DE CLIQUES PARA ENTRAR NO CALABOUÇO ************************************************************************************************

    # clica em "Arena do caos nivel 4"
    pyautogui.moveTo(785,355, duration=0.7)
    pyautogui.click()
    time.sleep(1)

    # clica em "Entrar"
    pyautogui.moveTo(1131, 889, duration=0.7)
    pyautogui.click()
    time.sleep(1)

    # clica em "Desafio"
    pyautogui.moveTo(814, 767, duration=0.7)
    pyautogui.click()
    time.sleep(1)

    # SEQUENCIA DE CLIQUES E TECLAS PARA ANDAR ATE O PORTÃO ****************************************************************************************

    # clica para andar
    pyautogui.moveTo(1182, 240, duration=0.7)
    pyautogui.click()
    time.sleep(3)

    pyautogui.moveTo(1343, 302, duration=0.7)
    pyautogui.click()
    time.sleep(3)

    pyautogui.moveTo(1605, 167, duration=0.7)
    pyautogui.click()
    time.sleep(4)

    pydirectinput.keyDown('a')
    time.sleep(1)
    pydirectinput.keyUp('a')
    time.sleep(1)

    pyautogui.moveTo(1100, 133, duration=0.7)
    pyautogui.click()
    time.sleep(3)

    pyautogui.moveTo(1030, 117, duration=0.7)
    pyautogui.click()
    time.sleep(2)

    # DESTRUIÇÃO DO PORTÃO E ENTRAR *****************************************************************************************************************

    pydirectinput.press('z')
    time.sleep(1)

    pydirectinput.press('3')
    time.sleep(10)

    pydirectinput.keyDown('e')
    time.sleep(0.1)
    pydirectinput.keyUp('e')
    time.sleep(1)

    pydirectinput.keyDown('w')
    time.sleep(1)
    pydirectinput.keyUp('w')
    time.sleep(1)

    # MATAR OS MOBS DENTRO DO CALABOUÇO **************************************************************************************************************

    pydirectinput.keyDown('w')
    time.sleep(5)
    pydirectinput.keyUp('w')
    time.sleep(1)

    duracao = 13 * 60  
    inicio = time.time()
    while True:
        if time.time() - inicio >= duracao:
            break

        pydirectinput.press('z')
        time.sleep(1)
        pydirectinput.press('3')
        time.sleep(1)
        pydirectinput.press('space')
        time.sleep(1)

    print(f"Loop de ataque finalizado da execução {i+1}/5!")

    # SAIR DA ARENA E VOLTAR PARA A CIDADE **************************************************************************************************************

    pyautogui.moveTo(855,825, duration=0.7)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(766,268, duration=0.7)
    pyautogui.click()
    time.sleep(1)

print("Sequência executada 5 vezes!")