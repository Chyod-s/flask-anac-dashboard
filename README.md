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

## 🏗️ Arquitetura do Projeto

A aplicação segue uma arquitetura **em camadas**, separando responsabilidades:

```
📂 anac-flight-dashboard/
├── app/
│   ├── __init__.py       # Inicializa o Flask
│   ├── models.py         # Modelos SQLAlchemy (Banco de Dados)
│   ├── routes.py         # Endpoints da API (Controllers)
│   ├── services.py       # Lógica de Negócios
│   ├── auth.py           # Autenticação de Usuário
│   ├── utils.py          # Funções auxiliares
│   ├── templates/        # HTML (Jinja2)
│   ├── static/           # Arquivos estáticos (CSS, JS)
├── migrations/           # Arquivos de migração do banco de dados
├── data/                 # Dados CSV da ANAC
│   ├── Dados_Estatisticos.csv
├── config.py             # Configuração da aplicação
├── requirements.txt      # Dependências do projeto
├── Dockerfile            # Configuração para containerização
├── docker-compose.yml    # Configuração do Docker Compose
├── run.py                # Arquivo principal para rodar o servidor Flask
└── README.md             # Documentação do projeto
```

---

## 🛠️ Tecnologias Utilizadas

- **Back-End:** Flask, SQLAlchemy, Pandas  
- **Banco de Dados:** PostgreSQL  
- **Autenticação:** Flask-Login  
- **Gráficos:** Chart.js (ou Matplotlib, Plotly)  
- **Containerização:** Docker, Docker Compose  

---

## 🏗️ Como Rodar o Projeto

### 🔹 1. Clonar o Repositório
```sh
git clone https://github.com/seu-usuario/anac-flight-dashboard.git
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
1. Criar um banco de dados no PostgreSQL  
2. Definir a string de conexão no **config.py**  
3. Rodar as migrações:
```sh
flask db upgrade
```

### 🔹 5. Executar a Aplicação
```sh
python run.py
```
Acesse no navegador: **http://127.0.0.1:5000**

---

## 📦 Rodando com Docker

```sh
docker-compose up --build
```
Acesse no navegador: **http://localhost:5000**

---

## 📊 Sobre os Dados da ANAC

Os dados utilizados nesta aplicação são públicos e podem ser obtidos no portal da ANAC:  
👉 [Dados Estatísticos ANAC](https://sistemas.anac.gov.br/dadosabertos/Voos%20e%20opera%C3%A7%C3%B5es%20a%C3%A9reas/Dados%20Estat%C3%ADsticos%20do%20Transporte%20A%C3%A9reo/)
