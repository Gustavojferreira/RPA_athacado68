import pyautogui
import time

# 1-Identificar se a pagina do banco existe, 2- direcionar para ela se precisar(Abrir maximizada na tela), e caso não FAZER O LOGIN NO BANCO#

def fazer_login_banco():
    login_banco = False
    
    if login_banco == False:
        #Tenta fazer login#
        
        login_banco = True
        return login_banco
    else:
        return login_banco
    
def fazer_login_totvs():
    login_totvs = False
    time.sleep(2)
    
def fazer_login_totvs():
    login_totvs = False
    time.sleep(2)
    
    #Tenta fazer login totvs e retorna true caso feito#
    if login_totvs == False:   
        pyautogui.doubleClick(104,35) #executar arquivo winthor
      
        #permissão de execução
        time.sleep(5)
        pyautogui.press("left")
        pyautogui.press("enter")

        time.sleep(5)
        #Inserir credencial totvs
        pyautogui.typewrite("<KEGWYRC")#senha totvs
        time.sleep(2)
        pyautogui.click(505,475)#confirmação

        login_totvs = True
        return login_totvs
    else:
        return login_totvs

if __name__ == "__main__":
    fazer_login_totvs()