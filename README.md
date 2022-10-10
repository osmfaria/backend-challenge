<img src="https://img.shields.io/badge/Version-1.0-green" />
 
# :page_with_curl: Backend Challenge

Desafio Backend, um web app que permite o upload de um arquivo CNAB com os dados das movimentações financeiras de várias lojas. Estes dados são armazenados em um banco de dados relacional, e disponibilizado para consulta

<img src="./assets/layout.png" />


💭 Features principais:
\
:heavy_check_mark: Busca de transações\
:heavy_check_mark: Checa se o arquivo é do formato txt


## 📋 Instruções

Como instalar esse projeto:

- Faça um clone deste repositório;
- Na pasta raiz do projeto, rode o comando `python -m venv venv` (linux) no terminal para criar um ambiente virtual;
- Na pasta raiz do projeto, rode o comando `source venv/bin/activate` (linux) para acessar o ambiente virtual;
- Na pasta raiz do projeto, rode o comando `pip install -r requirements` para installar as dependências;
- Finalmente rode o comando `python manage.py runserver`
- No seu navegador, abra o link indicado no terminal.


## 💻 Tecnologias

Algumas das principais tecnologias utilizadas:

  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" /> <img src="https://img.shields.io/badge/Cypress-17202C?style=for-the-badge&logo=cypress&logoColor=white" /> <img src="https://img.shields.io/badge/styled--components-DB7093?style=for-the-badge&logo=styled-components&logoColor=white" /> <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" /> <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  


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
