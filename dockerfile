# Use uma imagem base Python compatível com arquitetura ARM
# Para Raspberry Pi 4 (64-bit OS), use arm64v8. Para Pi mais antigos ou 32-bit OS, use arm32v7.
# Assumindo que você está usando um sistema operacional de 64 bits (arm64v8):
FROM arm64v8/python:3.10-slim-bullseye

# 1. Configurar o ambiente
# Mantenha o sistema operacional atualizado e instale dependências de compilação
# para bibliotecas como OpenCV, se necessário, e a biblioteca git.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        git \
        libgl1-mesa-glx \
        libsm6 \
        libxext6 \
        libxrender1 && \
    rm -rf /var/lib/apt/lists/*

# 2. Definir o diretório de trabalho
# Todos os comandos a seguir serão executados a partir deste diretório
WORKDIR /app

# 3. Copiar o arquivo de dependências e instalar
# Copie o 'requirements.txt' antes do resto do código para aproveitar o cache do Docker.
COPY requirements.txt .

ENV PYTHONUNBUFFERED 1
ENV CAMERA_STREAM_URL = "http://172.16.30.102:81/stream" 

# Instalar as dependências. 
# ATENÇÃO: OpenCV pode ser complicado em ARM. A flag --trusted-host pode ser necessária.
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar o restante do código da aplicação
# Copia todos os seus arquivos (main.py, http_client.py, config.py, etc.) para /app
COPY . .

# 5. Configurar variáveis de ambiente (Opcional, mas útil)
ENV PYTHONUNBUFFERED 1

# 6. Definir o comando de inicialização
# Este comando será executado quando o container for iniciado.
CMD ["python", "main.py"]