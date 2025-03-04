# Usando a imagem base do Python
FROM python:3.10-slim AS base

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo de dependências para o container
COPY requirements.txt .

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para dentro do container
COPY . .

# Expor a porta em que o Flask estará rodando (padrão: 5000)
EXPOSE 5000

# Definir a variável de ambiente para o Flask
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Rodar a aplicação Flask
CMD ["flask", "run", "--host=0.0.0.0"]
