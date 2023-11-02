# Job Insights

  Projeto que implementou-se análises de um conjunto de dados de empregos, utilizando Python, Jinja2 e Flask.

  Os dados foram extraídos do site [Glassdoor](https://www.glassdoor.com.br/) e obtidos através do [Kaggle](https://www.kaggle.com/atharvap329/glassdoor-data-science-job-data), uma plataforma disponiblizando conjuntos de dados para cientistas de dados.

<br>

## Tecnologias usadas
---

- Linguagem Principal: **Python**
- Outra tecnologias: **PyTest, Jinja2, Flask**

<br>

## Características Gerais
---

- `Implementação de filtros interativos`: foram implementadas funções que filtram dados por: Tipo de Emprego, tipo de indústria, salário máximo, salário mínimo,  

- `Leitura e manipulação de arquivos`: Pode ser feita a leitura de arquivos a partir de planilha **XML**.

- `Exibição de uma página HTML`: Exibição dos dados de empregos em uma página HTML utilizando Flask e Jinja2. 

<br>

## Características Técnicas
---

Durante o processo de criação do projeto, alguns pontos foram levados em consideração para otimização da aplicação e garantia das devidas funcionalidades.

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
---

 ### Para rodar o projeto localmente:


  Clone o repositório:

    git clone git@github.com:edmcorrea/python.git

  No terminal, entre na pasta do repositório que você acabou de clonar e entre no repositório em questão:
    
    cd python
    
    cd job-insights

  Crie o ambiente virtual para o projeto

    python3 -m venv .venv && source .venv/bin/activate

  Instale as dependências

    python3 -m pip install -r dev-requirements.txt

  Para finalizar o ambiente virtual do projeto

    deactivate

<br>
    
## Como usar
---

  Na raiz do projeto digite o comando:
    
    flask run

  Acesse o site gerado pelo Flask: `http://localhost:5000`

<br>
    
## Documentação externa
---

- Python: `https://docs.python.org/3/`
- Flask: `https://flask.palletsprojects.com/en/3.0.x/`
 - Jinja2: `https://jinja.palletsprojects.com/en/3.1.x/`
