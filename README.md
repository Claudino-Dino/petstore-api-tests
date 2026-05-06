# 🧪 Automação de Testes — PetStore API & SauceDemo

Projeto desenvolvido com o objetivo de cobrir testes automatizados de API REST e interface web, utilizando **Postman/Newman** e **Selenium**.

---

## 📦 Tecnologias Utilizadas

- Python
- Selenium
- Postman / Newman
- GitHub Actions (CI/CD)
- python-dotenv

---

## 🐾 Testes de API — PetStore (Postman + Newman)

Cobertura completa de todos os endpoints da [PetStore Swagger](https://petstore.swagger.io), organizados em três grupos: **Pet**, **Store** e **User**.

### Endpoints cobertos

#### /pet
| Método | Endpoint | Funcionalidade |
|--------|----------|---------------|
| POST | `/pet` | Adiciona um novo pet |
| PUT | `/pet` | Atualiza os dados de um pet existente |
| GET | `/pet/findByStatus` | Busca pets pelo status (available, pending, sold) |
| GET | `/pet/findByTags` | Busca pets por tags |
| GET | `/pet/{petId}` | Busca um pet pelo ID |
| POST | `/pet/{petId}` | Atualiza dados de um pet via form |
| DELETE | `/pet/{petId}` | Remove um pet pelo ID |
| POST | `/pet/{petId}/uploadFile` | Realiza upload de imagem do pet |

#### /store
| Método | Endpoint | Funcionalidade |
|--------|----------|---------------|
| GET | `/store/inventory` | Retorna o inventário de pets por status |
| POST | `/store/order` | Cria um pedido de compra |
| GET | `/store/order/{orderId}` | Busca um pedido pelo ID |
| DELETE | `/store/order/{orderId}` | Remove um pedido pelo ID |

#### /user
| Método | Endpoint | Funcionalidade |
|--------|----------|---------------|
| POST | `/user` | Cria um novo usuário |
| POST | `/user/createWithArray` | Cria múltiplos usuários via array |
| POST | `/user/createWithList` | Cria múltiplos usuários via lista |
| GET | `/user/login` | Realiza login do usuário |
| GET | `/user/logout` | Realiza logout do usuário |
| GET | `/user/{username}` | Busca um usuário pelo username |
| PUT | `/user/{username}` | Atualiza os dados de um usuário |
| DELETE | `/user/{username}` | Remove um usuário pelo username |

### O que é validado em cada endpoint

- ✅ Status code correto
- ✅ Tempo de resposta aceitável
- ✅ Verificar se a resposta é um JSON válido

---

## 🛒 Automação Web — SauceDemo (Selenium)

Automação completa do fluxo de compra no [SauceDemo](https://www.saucedemo.com), cobrindo login, adição de produtos ao carrinho e finalização da compra.

### Fluxo automatizado

1. **Login** — acesso com credenciais via variáveis de ambiente
2. **Adição de produtos** — todos os produtos disponíveis são adicionados ao carrinho
3. **Finalização da compra** — preenchimento de dados e confirmação do pedido

### Produtos adicionados

| Produto | Descrição |
|---------|-----------|
| Sauce Labs Backpack | Mochila da linha Sauce Labs |
| Sauce Labs Bike Light | Luz de bicicleta |
| Sauce Labs Bolt T-Shirt | Camiseta Bolt |
| Sauce Labs Fleece Jacket | Jaqueta de lã |
| Sauce Labs Onesie | Macacão infantil |
| Test.allTheThings() T-Shirt | Camiseta edição especial |

### Indicadores de conclusão

O projeto conta com prints no terminal para indicar o fim de cada etapa, com condicionais específicas que verificam o estado da aplicação antes de confirmar o sucesso:

```
-----------------------------------
    LOGIN EFETUADO ✅
-----------------------------------

-----------------------------------
    PRODUTOS ADICIONADOS ✅
-----------------------------------

-----------------------------------
    COMPRA FINALIZADA ✅
-----------------------------------
```

Cada mensagem só é exibida se a condição for satisfeita:
- **Login** — verifica se a URL redirecionou para `/inventory.html`
- **Produtos** — verifica se há botões disponíveis para adicionar ao carrinho
- **Compra** — verifica se a URL final é `/checkout-complete.html`

---

## ⚙️ Pipeline CI/CD — GitHub Actions

Ambas as automações rodam automaticamente via GitHub Actions a cada push na branch `main`:

1. `api-tests.yml` — executa os testes da PetStore com Newman
2. `selenium-tests.yml` — executa a automação do SauceDemo após a conclusão dos testes de API

---

## 🔐 Variáveis de Ambiente

As credenciais e dados pessoais são gerenciados via `.env` localmente e via **Secrets** no GitHub Actions:

```
USUARIO
SENHA
NOME
SOBRENOME
CODIGO_POSTAL
```
