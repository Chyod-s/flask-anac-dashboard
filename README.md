# 📊 ANAC Flight Data Dashboard

Este projeto é uma aplicação web desenvolvida com **Python (Flask)** para análise de dados públicos da **ANAC** (Agência Nacional de Aviação Civil).  
A aplicação permite visualizar informações de voos regulares da companhia aérea **GOL**, com filtros personalizados e gráficos interativos.

---

## 🚀 Funcionalidades

✔ **Autenticação de Usuário** (Login)  
✔ **Filtragem de Dados** por mercado (origem/destino) e intervalo de datas  
✔ **Gráficos Interativos** de RPK ao longo do tempo  
✔ **Banco de Dados SQL** para armazenar os dados processados  
✔ **Containerização com Docker**  

---

## 🛠️ Tecnologias Utilizadas

- **Back-End:** Flask, Flask-SQLAlchemy, Pandas  
- **Banco de Dados & Migração:** Sqlite, Alembic, Flask-Migrate
- **Requisições & APIs:** Flask-Login, Requests, Urllib3 
- **Visualização & Dashboards:**  Plotly, Dash 
- **Manipulação de Dados & Performance:**  NumPy, Python-Dateutil, Pytz / Tzdata
- **Containerização:** Docker, Docker Compose  

---

## 🏗️ Como Rodar o Projeto

### 🔹 1. Clonar o Repositório
```sh
git clone https://github.com/Chyod-s/anac-flight-dashboard.git
cd anac-flight-dashboard
```

### 🔹 2. Criar e Ativar um Virtual Environment
```sh
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 🔹 3. Instalar as Dependências
```sh
pip install -r requirements.txt
```

### 🔹 4. Configurar o Banco de Dados
1. Rodar os comandos:
```sh
-flask run-migrations: Roda as migrações do banco de dados.
-flask inserir-dados-csv: Insere os dados do CSV no banco de dados.
```

### 🔹 5. Executar a Aplicação
```sh
python run.py
```
Acesse no navegador: **http://127.0.0.1:5500**

---

## 📦 Rodando com Docker
1. Rode os CMD

```sh
docker build -t flask-app .

docker run -p 5000:5000 flask-app:latest

```
Acesse no navegador: **http://localhost:5000**

---

## 📊 Sobre os Dados da ANAC

Os dados utilizados nesta aplicação são públicos e podem ser obtidos no portal da ANAC:  
👉 [Dados Estatísticos ANAC](https://sistemas.anac.gov.br/dadosabertos/Voos%20e%20opera%C3%A7%C3%B5es%20a%C3%A9reas/Dados%20Estat%C3%ADsticos%20do%20Transporte%20A%C3%A9reo/)
