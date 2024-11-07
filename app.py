from login import fazer_login
from automacao_totvs import realizar_download, importar_arquivo

def main():

    if fazer_login():
        realizar_download()
        importar_arquivo()

    else:
        print('Pagina não encontrada')

if __name__ == "__main__":
    main()