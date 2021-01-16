## Descrição

API REST com a funcionalidade de Produtos Favoritos dos Clientes escrito em Python com Flask, SQLAlchemy e JWT utilizando banco de dados MySQL.

Versão utilizado do Python v3.9.0

## Requisitos

* Criar, Atualizar, Visualizar e Remover ***Clientes***
  * O cadastro dos clientes deve conter apenas seu nome e endereço de e-mail
  * Um cliente não pode se registrar duas vezes com o mesmo endereço de e-mail
* Cada cliente só deverá ter uma lista de produtos favoritos
* Em uma lista de produtos favoritos podem existir uma quantidade ilimitada de produtos
  * Um produto não pode ser adicionado em uma lista caso ele não exista
  * Um produto não pode estar duplicado na lista de produtos favoritos de um cliente
  * A documentação da API de produtos pode ser visualizada neste link https://gist.github.com/Bgouveia/9e043a3eba439489a35e70d1b5ea08ec
* O acesso à api deve ser aberto ao mundo, porém deve possuir autenticação e autorização

## Estrutura do projeto

![Estrutura projeto](https://github.com/adevecchi/flask-rest-api-jwt/blob/main/screenshot/estrutura.png)

## Endpoints

* Registra usuário: `POST /api/users/register`

![Registra usuario](https://github.com/adevecchi/flask-rest-api-jwt/blob/main/screenshot/register.png)

---

* Login: `POST /api/users/login`

![Login](https://github.com/adevecchi/flask-rest-api-jwt/blob/main/screenshot/login.png)

---

* Cria cliente: `POST /api/clients/`

![Cria cliente](https://github.com/adevecchi/flask-rest-api-jwt/blob/main/screenshot/clients-create.png)

---

* Todos clientes: `GET /api/clients/`

![Todos clientes](https://github.com/adevecchi/flask-rest-api-jwt/blob/main/screenshot/clients-all.png)

---

* Cliente por Id: `GET /api/clients/{id}`

![Cliente por id](https://github.com/adevecchi/flask-rest-api-jwt/blob/main/screenshot/clients-id.png)

---

* Atualiza cliente: `PUT /api/clients/{id}`

![Atualiza cliente](https://github.com/adevecchi/flask-rest-api-jwt/blob/main/screenshot/clients-update.png)
 
---

* Remove cliente: `DELETE /api/clients/{id}`

![Remove cliente](https://github.com/adevecchi/flask-rest-api-jwt/blob/main/screenshot/clients-delete.png)

---

* Cria produtos favorito: `POST /api/clients/{client_id}/favorite/products`

![Cria produtos favoritos](https://github.com/adevecchi/flask-rest-api-jwt/blob/main/screenshot/favorite-create.png)

---

* Todos produtos favoritos: `GET /api/clients/{client_id}/favorite/products`

![Todos produtos favoritos](https://github.com/adevecchi/flask-rest-api-jwt/blob/main/screenshot/favorite-all.png)

---

* Produtos favorito por Id: `GET /api/clients/{client_id}/favorite/products/{product_id}`

![Produtos favorito por id](https://github.com/adevecchi/flask-rest-api-jwt/blob/main/screenshot/favorite-id.png)
