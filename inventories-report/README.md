# Inventory Report

  Neste projeto implementou-se algumas funções que de leitura e escrita de arquivos `JSON`, `XML` e `CSV` utilizando a Programação Orientada a Objetos em Python.

<br>

## Tecnologias usadas
---

- Linguagem Principal: **Python**
- Outra tecnologias: **PyTest, Flake8, POO, xmltodict, CSV, JSON**

<br>

## Características Gerais
---

-`Gerador de Relatórios`: recebe como entrada arquivos com dados de um estoque e tem como saída um relatório acerca destes dados.

-`Importação de arquivos variados`: Dados podem ser obtidos de diversas fontes. (**CSV, JSON, XML**).


-`Relatório final em versões variadas`: O relatório final possui duas versões: **simples** e **completa**, a critério do usuário.

<br>

## Características Técnicas
---

Durante o processo de criação do projeto, alguns pontos foram levados em consideração para otimização da aplicação e garantia das devidas funcionalidades.

  -`Padrões de Projeto`: Foram aplicados os conceitos de **padrões de projeto e POO**.

  -`Implementação de Testes`: Durante o desenvolvimento do projeto, foram criados testes unitários para garantia das devidas funcionalidades da aplicação.

  -`Linter`: Utilizado através do Flake8, para garantia das boas práticas de código e legibilidade / manutenção.
  Exemplo de entrada em **CSV**

  <details>
    <summary><strong>🛠 Testes</strong></summary><br />

    Para executar os testes certifique-se de que você está com o ambiente virtual ativado

    <strong>Executar os testes</strong>

    ```bash
    $ python3 -m pytest
    ```

    Caso precise executar apenas um arquivo de testes basta executar o comando:

    ```bash
    python3 -m pytest tests/nomedoarquivo.py
    ```
  </details>

<br>


## Instalação
 ### Para rodar o projeto localmente:


  Clone o repositório:

    git clone git@github.com:edmcorrea/python.git

  No terminal, entre na pasta do repositório que você acabou de clonar e entre no repositório em questão:
    
    cd python
    
    cd inventories-report

  Crie o ambiente virtual para o projeto

    python3 -m venv .venv && source .venv/bin/activate

  Instale as dependências

    python3 -m pip install -r dev-requirements.txt

  Para finalizar o ambiente virtual do projeto

    deactivate

<br>
    
## Como usar

  ### O programa deverá ser executável via linha de comando.

  <br>

  <details>
    <summary><strong>Sobre os arquivos com os dados de entrada</strong></summary>
    
  <details>
    <summary><strong>Exemplo de entrada em CSV</strong></summary><br />
    ```CSV
      id,nome_do_produto,nome_da_empresa,data_de_fabricacao,data_de_validade,numero_de_serie,instrucoes_de_armazenamento
      1,cadeira,Target Corporation,2021-02-18,2025-09-17,CR25,empilhadas
      2,mesa,"Galena Madeira, Inc.",2022-12-06,2026-12-25,FR29,desmontadas
      3,abajur,Keen Iluminação,2019-12-22,2025-11-07,CZ09,em caixas
    ```
  </details>

  <details>
    <summary><strong>Exemplo de entrada em JSON</strong></summary><br />
    ```json
    [
      {
        "id":1,
        "nome_do_produto":"Borracha",
        "nome_da_empresa":"Papelaria Solar",
        "data_de_fabricacao":"2021-07-04",
        "data_de_validade":"2029-02-09",
        "numero_de_serie":"FR48",
        "instrucoes_de_armazenamento":"Ao abrigo de luz solar"
      }
    ]
    ```
  </details>

  <details>
    <summary><strong>Exemplo de entrada em XML</strong></summary><br />
    ```xml
    <?xml version='1.0' encoding='UTF-8'?>
    <dataset>
      <record>
        <id>1</id>
        <nome_do_produto>Microfone</nome_do_produto>
        <nome_da_empresa>Tecno Uau LTDA</nome_da_empresa>
        <data_de_fabricacao>2021-10-27</data_de_fabricacao>
        <data_de_validade>2032-08-31</data_de_validade>
        <numero_de_serie>MT08</numero_de_serie>
        <instrucoes_de_armazenamento>Longe de fonte de calor</instrucoes_de_armazenamento>
      </record>
    </dataset>
    ```
  </details>

  </details>

<br>

  1. Instale o código como um pacote pip (é necessário para que o ambiente funcione):

      ```bash
        pip install .
      ```

  2. Execute o comando `inventory_report`:

      ```bash
        inventory_report `argumento1` `argumento2`
      ```

      OBS.:
        - **argumento1** deve receber o caminho de um arquivo a ser importado. O arquivo pode ser um `csv`, `json` ou `xml`.

        - **argumento2** pode receber duas strings: `simples` ou `completo`, cada uma gerando o respectivo relatório.

  3. Outra opção para invocar o comando:
     
      ```bash
        python3 -m inventory_report.main argumento1 argumento2
      ```


<br>
    
## Documentação externa

- Python: `https://docs.python.org/3/`
- xmltodict: `https://www.askpython.com/python-modules/xmltodict-module`