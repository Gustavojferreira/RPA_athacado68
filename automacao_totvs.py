import time
import pyautogui


# Loop para execução contínua
while True:
    #Passo 1, verificar se o banco está aberto 
    
    # Passo 2.1 - Identificar a situação e onde baixar o arquivo  # Se não funcionar com a print vai ter que USAR O PyTesseract#
    encontrar_img = pyautogui.locateCenterOnScreen('arquivo.png')  #Print do campo de situação "A recepcionar"

    if encontrar_img:
        # Defina deslocamento da print para o clique
        distancia_Img_x = 0  # Ajuste para a posição de clique correta
        distancia_Img_y = 0
        pyautogui.click(encontrar_img.x + distancia_Img_x, encontrar_img.y + distancia_Img_y)
        print("Imagem encontrada e clicada.")
         # Defina o caminho do arquivo txt se necessário
        caminho_arquivo = 'caminho/para/arquivo.txt'  # Substitua pelo caminho correto

        # Passo 3 - Preenchimento de campos
        pyautogui.click(0, 0)  # Coordenadas para o primeiro campo
        pyautogui.write('texto1')  # Substitua 'texto1' pelo conteúdo correto
        time.sleep(1)

        pyautogui.click(0, 0)  # Coordenadas para o segundo campo
        pyautogui.write('texto2')  # Substitua 'texto2' pelo conteúdo correto
        time.sleep(1)

        pyautogui.click(0, 0)  # Coordenadas para o terceiro campo
        pyautogui.write('texto3')  # Substitua 'texto3' pelo conteúdo correto
        time.sleep(1)

        # Passo 4 - Inserir o caminho do arquivo baixado
        pyautogui.click(0, 0)  # Coordenadas para o campo onde colar o caminho do arquivo
        pyautogui.hotkey('ctrl', 'v')  # Cola o caminho do arquivo
        print("Caminho do arquivo inserido.")
    else:
        print("Imagem não encontrada, tentando novamente...")
        time.sleep(1)  # Pausa antes de tentar novamente

    # Pausa final antes de recomeçar o loop
    time.sleep(2)
