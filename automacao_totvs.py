import time
import pyautogui

# Desativar o failsafe
pyautogui.FAILSAFE = False

# Função que realiza o processo de download dos arquivos do banco
def realizar_download():
    try:
        # Loop para execução
        for _ in range(2):    
            time.sleep(2)
            # Passo 2.1 - Identificar a situação e onde baixar o arquivo
            print_salvar = 'teste.png'
            encontrar_img = pyautogui.locateCenterOnScreen(print_salvar, confidence=0.9)  # Print do campo de situação "A recepcionar"
            if encontrar_img:
                # Defina deslocamento da print para o clique
                distancia_Img_x = 0  # Ajuste para a posição de clique correta se for necessário.
                distancia_Img_y = 0
                pyautogui.moveTo(encontrar_img.x + distancia_Img_x, encontrar_img.y + distancia_Img_y)
                pyautogui.click()  #clique após mover o mouse
                print("Imagem encontrada e download realizado.")
            else:
                print('Erro em (automacao_totvs) in line 16')     
        #Fecha a pagina do banco quando concluir os downloads        
        pyautogui.moveTo(1004,11)
        pyautogui.click()
    except pyautogui.ImageNotFoundException:
        print('Imagem não encontrada')

# vai fazer as inserção de dados no totvs
def importar_arquivo():
    
    print('A')



