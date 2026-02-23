# 📂 Organizador de PDFs Automático

Este é um script em Python desenvolvido para organizar automaticamente arquivos `.pdf` de uma pasta de origem (como o seu HD Externo) para uma pasta de destino específica, mantendo seus documentos limpos e categorizados.

## 🚀 Funcionalidades

* **Varredura Automática:** Identifica todos os arquivos com extensão `.pdf` na pasta de origem.
* **Criação de Diretórios:** Cria automaticamente a pasta de destino (e pastas "pai") caso elas não existam.
* **Tratamento de Erros:** Gerencia permissões de acesso e evita interrupções caso a pasta já esteja criada.
* **Contador de Sucesso:** Exibe no terminal quantos arquivos foram movidos ao final da execução.

## 🛠️ Pré-requisitos

* Python 3.x instalado.
* Acesso de leitura e escrita no disco rígido (ex: Disco `E:`).

## 📋 Como usar

1.  **Clone ou baixe** este repositório.
2.  Abra o arquivo `organizador_pdfs.py` e ajuste os caminhos das pastas:
    ```python
    pasta_origem = r"E:\Downloads"
    pasta_destino = r"E:\Documentos\PDFs_Organizados"
    ```
3.  Abra o terminal na pasta do projeto.
4.  Execute o script com o comando:
    ```bash
    python organizador_pdfs.py
    ```

## 🧠 Lógica do Código

O script utiliza as bibliotecas nativas do Python:
* `os`: Para manipulação de caminhos e verificação de pastas.
* `shutil`: Para a movimentação física dos arquivos entre diretórios.
