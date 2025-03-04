# Etapa 1: Definindo a imagem base
FROM python:3.10-slim AS base

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo de dependências (requirements.txt) para o container
COPY requirements.txt .

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código para o container
COPY . .

# Expor a porta 5000 para o Flask (padrão)
EXPOSE 5000

# Definir o comando para rodar o aplicativo Flask
CMD ["flask", "run", "--host=0.0.0.0"]
