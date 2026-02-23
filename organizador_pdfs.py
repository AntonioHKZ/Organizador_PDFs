import os
import shutil


def organizar_pdfs():
    pasta_origem = os.path.expanduser(r'E:/Downloads')
    pasta_destino = os.path.expanduser(r'E:/Documentos/PDFs_Organizados')

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino, exist_ok=True)
        print(f"Pasta criada: {pasta_destino}")
    arquivos = os.listdir(pasta_origem)
    contador = 0
    for arquivo in arquivos:
        if arquivo.lower().endswith('.pdf'):
            caminho_antigo = os.path.join(pasta_origem, arquivo)
            caminho_novo = os.path.join(pasta_destino, arquivo)

            shutil.move(caminho_antigo, caminho_novo)
            print(f"Arquivo movido: {arquivo}")
            contador += 1

    print(f"\nSucesso! {contador} arquivos foram movidos para {pasta_destino}")
if __name__ == "__main__":
    organizar_pdfs()