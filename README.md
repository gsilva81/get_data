# Projeto: API de Clima com FastAPI, PostgreSQL e Docker

Este projeto foi desenvolvido como parte de um processo seletivo para a vaga de Cientista de Dados / Desenvolvedor Full Stack (com foco em Bioinformática).

O objetivo é demonstrar habilidades em:

- Consumo de API externa (OpenWeather)
- Persistência de dados em banco relacional (PostgreSQL)
- Exposição de API RESTful
- Conteinerização com Docker
- Organização de código e versionamento com Git

---

## Tecnologias utilizadas

- Python 3.11
- FastAPI
- PostgreSQL 15
- SQLAlchemy
- Docker / Docker Compose
- OpenWeather API

---

## Requisitos

2 - Cadastro na OpenWeather para gerar uma API KEY:  
    [https://home.openweathermap.org/users/sign_up]
    após cadastro acessar: (https://home.openweathermap.org/api_keys) e copiar a key default
---

### Como executar o projeto:

### 1. Clonar o repositório:

git clone https://github.com/gsilva81/get_data.git,

cd get_data

---

### 2. Configurar as variáveis de ambiente:

Crie um arquivo `.env` na raiz com o seguinte conteúdo:

```dotenv
DATABASE_URL=postgresql://postgres:postgres@db:5432/weather_db
OPENWEATHER_API_KEY=COLOQUE_SUA_KEY
```

---

### 3. Subir os containers com Docker:

```bash
docker-compose up 
```

- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs

---


## UTILIZANDO POSTMAN:

## Endpoints disponíveis:
## POST `/weather/{city}`
> Consome a OpenWeather API e salva os dados no banco.

Exemplo:
POST http://localhost:8000/weather/Manaus

Retorno:

![image](https://github.com/user-attachments/assets/3a44cfca-2829-46bf-a3e7-3e28778a4df3)

---


### GET `/weather/{city}`
> Retorna os dados salvos no banco para a cidade especificada.

Exemplo:
GET http://localhost:8000/weather/Manaus

Retorno:

![image](https://github.com/user-attachments/assets/e72163bd-7fa4-414f-8060-795c1538e086)

---
## No Navegador

![image](https://github.com/user-attachments/assets/5f4347bf-9a83-486c-82e0-687a44651d81)

---

## Autor

Gabriel de Oliveira Silva

LinkedIn: (https://www.linkedin.com/in/gabriel-silva-5331242b8/)

Repositório Github: (https://github.com/gsilva81/get_data.git)
