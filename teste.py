import time
import pyautogui

time.sleep(2)
encontrar_img = pyautogui.locateCenterOnScreen('teste.png')  #Print do campo de situação "A recepcionar"

if encontrar_img:
    print("funcionou")
