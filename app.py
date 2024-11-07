from login import fazer_login_banco, fazer_login_totvs
from automacao_totvs import realizar_download, importar_arquivo
import time

def main():
    if fazer_login_totvs():
        time.sleep(3)
        importar_arquivo()
    else:
        print("erro no main")

if __name__ == "__main__":
    main()