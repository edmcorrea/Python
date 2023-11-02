# Restaurant Orders

  Neste projeto implementou-se uma ferramenta de construção de cardápios, considerando organizações específicas e disponibilidade de estoque dos ingredientes. Foi utilizada a Programação Orientada a Objetos em **Python** e biblioteca **Pandas**.

<br>

## Tecnologias usadas
---

- Linguagem Principal: **Python, Pandas**
- Outra tecnologias: **Pandas, PyTest, Flake8, POO, CSV**

<br>

## Características Gerais
---

-`Gerador de Cardápio`: recebe como entrada arquivos CSV do tipo cardápio, com dados como o nome do prato, seu preço no cardápio, um dos ingredientes, dentre outros.

-`Relaciona pratos e receitas`: Após leitura do arquivo, a aplicação faz o relacionamento do prato do cardápio com sua respectiva receita.

-`Exibição de pratos especiais`: Exibe os pratos do cardápio de acordo com uma determinada restrição alimentar.

<br>

## Características Técnicas
---

Durante o processo de criação do projeto, alguns pontos foram levados em consideração para otimização da aplicação e garantia das devidas funcionalidades.

  -`Hashmaps`: Foram praticados os conceitos de Hashmaps através das estruturas de dados **Dict** e **Set** do Python.

  -`Pandas`: Foram usadas as ferramentas **Pandas** junto a sua estrutura de dados **DataFrame**.

  -`Padrões de Projeto`: Foram aplicados os conceitos de **padrões de projeto e POO**.

  -`Implementação de Testes`: Durante o desenvolvimento do projeto, foram criados testes unitários para garantia das devidas funcionalidades da aplicação.

  -`Linter`: Utilizado através do Flake8, para garantia das boas práticas de código e legibilidade / manutenção.


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
    
    cd restaurant-orders (with Pandas)

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