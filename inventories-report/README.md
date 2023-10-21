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

<details>
  <summary><strong>Clique aqui para mais detalhes</strong></summary><br />

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
  
</details>
<br>
<br>


## Instalação
 ### Para rodar o projeto localmente:

  Clone o repositório:

    ```bash
      git clone git@github.com:edmcorrea/python.git
    ```

  -No terminal, entre na pasta do repositório que você acabou de clonar e entre no repositório em questão:

    ```bash
      cd python
    ```

    ```bash
      cd inventories-report
    ```

  -Crie o ambiente virtual para o projeto

    ```bash
      python3 -m venv .venv && source .venv/bin/activate
    ```

  -Instale as dependências

    ```bash
      python3 -m pip install -r dev-requirements.txt
    ```

  - Para finalizar o ambiente virtual do projeto

    ```bash
      deactivate
    ```

    
## Como usar

  ### O programa deverá ser executável via linha de comando.

  1. Instale o código como um pacote pip (é necessário para que o ambiente funcione):

      ```bash
        pip install .
      ```

  2. Execute o comando `inventory_report`:

      ```bash
        inventory_report `argumento1` `argumento2`
      ```

      <details>
        <summary>🛠 OBSERVAÇÃO sobre os <strong>ARGUMENTOS</strong></summary><br />

        - **argumento1** deve receber o caminho de um arquivo a ser importado. O arquivo pode ser um `csv`, `json` ou `xml`.

        - **argumento2** pode receber duas strings: `simples` ou `completo`, cada uma gerando o respectivo relatório.
      </details>

      <details>
        <summary><strong>Sobre os arquivos com os dados de entrada</strong></summary><br />
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

  3. Outra opção para invocar o comando:

      ```bash
         python3 -m inventory_report.main argumento1 argumento2
      ```
     
<details>
  <summary><strong>🛼Executando o Projeto</strong></summary>
  Após implementar o requisito bônus, seu programa deverá ser executável <strong>via linha de comando</strong>.
  
  O comando a ser executado será `inventory_report`. Para que ele funcione em seu ambiente é preciso antes instalar o próprio código como um pacote pip:
  <code>pip install .</code>

  Agora você poderá chamar o comando `inventory_report` passando seus argumentos:
  
  <code>inventory_report `argumento1` `argumento2`</code>

  - **argumento1** deve receber o caminho de um arquivo a ser importado. O arquivo pode ser um `csv`, `json` ou `xml`.

  - **argumento2** pode receber duas strings: `simples` ou `completo`, cada uma gerando o respectivo relatório.
  
  Outra opção é invocar o comando assim:

  <code>python3 -m inventory_report.main argumento1 argumento2</code>

</details>

<details>
  <summary><strong>🗃️ Arquivos com os dados de entrada</strong></summary><br />
  Três formatos de importação estão disponíveis no diretório <code>data</code> dentro do diretório <code>inventory_report</code>. Confira o exemplo de formato eles:
  
  <strong>Arquivos CSV</strong>
  Os arquivos **CSV** são separados por vírgula, como no exemplo abaixo:

```CSV
id,nome_do_produto,nome_da_empresa,data_de_fabricacao,data_de_validade,numero_de_serie,instrucoes_de_armazenamento
1,cadeira,Target Corporation,2021-02-18,2025-09-17,CR25,empilhadas
2,mesa,"Galena Madeira, Inc.",2022-12-06,2026-12-25,FR29,desmontadas
3,abajur,Keen Iluminação,2019-12-22,2025-11-07,CZ09,em caixas
```

<strong>Arquivos JSON</strong>
Os arquivos JSON seguem o seguinte modelo:

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

<strong>Arquivos XML</strong>
Os arquivos **XML** seguem o seguinte modelo:

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