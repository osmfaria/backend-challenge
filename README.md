<img src="https://img.shields.io/badge/Version-1.0-green" />
 
# :page_with_curl: Backend Challenge

Desafio Backend, um web app que permite o upload de um arquivo CNAB com os dados das movimentações financeiras de várias lojas. Estes dados são armazenados em um banco de dados relacional, e disponibilizados para consulta.

<img src="./assets/layout.png" />


💭 Features principais:
\
\
:heavy_check_mark: Busca de transações;\
:heavy_check_mark: Checa se o arquivo selecionado para upload é do formato txt.


## 📋 Instruções

Como instalar esse projeto:

- Faça um clone deste repositório;
- Na pasta raiz do projeto, rode o comando `python -m venv venv` (linux) no terminal para criar um ambiente virtual;
- Na pasta raiz do projeto, rode o comando `source venv/bin/activate` (linux) para acessar o ambiente virtual;
- Na pasta raiz do projeto, rode o comando `pip install -r requirements.txt` para installar as dependências;
- Na pasta raiz do projeto, rode o comando `python manage.py migrate`;
- Crie um arquivo `.env` na raiz do projeto e siga o exemplo do `.env.example` que também pode ser encontrado na raiz do projeto;
- Finalmente rode o comando `python manage.py runserver`
- No seu navegador, abra o link indicado no terminal.


## 💻 Tecnologias

Algumas das principais tecnologias utilizadas:

  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" /> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" /> <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" /> <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" /> <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  


## :checkered_flag: Testes

Rodando testes de componentes:

- `yarn run cypress run --component`

Rodando testes e2e:

- `yarn start` para que a aplicação esteja rodando no localhost;
- Abrir outro terminal;
- `yarn run cypress run`

Explorando testes:
  
 > Componentes:

  - Para os testes dos componentes, foram testados os que são reutilizados como Inputs, Button e Header.
  
 > e2e:

  - Funcionalidade basica de preencher os inputs e submit para obter resultados;
  - Mock do retorno da api para teste da rederização do card de resultados;
  - Teste de retorno da seção de resultados para o card inicial com o form;
  - Teste para verificação se inputs inválidos são acusado pela validação do form.


## 🔗 Uteis

> [API](https://frontend-challenge-7bu3nxh76a-uc.a.run.app)
