# Conversor de PDF para Markdown

Este script converte um arquivo PDF para Markdown e salva o resultado em um arquivo `.md` com o mesmo nome do arquivo original.

## Requisitos

Este script utiliza a biblioteca [Docling](https://pypi.org/project/docling/) para realizar a conversão. Certifique-se de instalar as dependências antes de executar o script.

### Instalação das dependências

Para instalar o Docling, execute o seguinte comando:

```sh
pip install docling
```

## Como usar

1. Adicione o path do arquivo que vai ser convertido em `source`.
2. O arquivo pode ser de qualquer tipo, incluindo documentos como PDF, DOCX, XLSX, HTML ou outros formatos, podendo estar localizado localmente ou online.
3. Execute o script Python.
4. O arquivo convertido será salvo no mesmo diretório com a extensão `.md`.

## Exemplo de Execução

Suponha que você tenha um arquivo chamado `documento.pdf`. Após executar o script, ele gerará um arquivo `documento.md` com o conteúdo convertido para Markdown.

```sh
python converter.py
```

Após a execução, você verá a mensagem:

```
Arquivo salvo como: documento.md
```

## Licença

Este projeto está sob a licença MIT.
