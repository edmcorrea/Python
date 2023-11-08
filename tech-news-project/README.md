# Tech News

  Neste projeto implementou-se o conceito de raspagem de dados do blog [_Trybe_](https://blog.betrybe.com). Além disso, as notícias são salvas no banco de dados `MongoDB` utilizando as funções `Python`.

<br>

## Tecnologias usadas
---

- Linguagem Principal: **Python**
- Outra tecnologias: **Raspagem de Dados, MongoDB, PyTest, Flake8, POO**

<br>

## Características Gerais
---

- `Raspagem de Dados`: As notícias são extraídas de um blog web.

- `Armazenamento em Banco de Dados`: As notícias serão armazenadas em uma coleção chamada **news**, utilizando o MongoDB.

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
    
    cd tech-news

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
    <summary><strong>Instale o MongoDB (com Docker)</strong></summary>

  Na raiz do projeto, execute o comando:
    
    docker-compose up -d mongodb
  
  Ou

    docker compose up -d mongodb

   Importe o módulo `tech_news/database.py` e chame as funções contidas nele.

<br>

    
## Documentação externa

- [Python](https://docs.python.org/3/): `https://docs.python.org/3/`
- [MongoDB](https://https://www.mongodb.com/pt-br.betrybe.com): `https://www.mongodb.com/pt-br`
