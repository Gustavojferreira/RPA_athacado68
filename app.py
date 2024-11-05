from login import fazer_login
from automacao_totvs import realizar_download

def main():
    if fazer_login():
        realizar_download()
    else:
        print('Pagina não encontrada')

if __name__ == "__main__":
    main()