FROM python:3.13.3-bookworm
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    gnupg2 \
    && curl -L -o openjdk21.tar.gz https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.2%2B13/OpenJDK21U-jdk_x64_linux_hotspot_21.0.2_13.tar.gz \
    && mkdir -p /opt/java/openjdk21 \
    && tar -xzf openjdk21.tar.gz -C /opt/java/openjdk21 --strip-components=1 \
    && rm openjdk21.tar.gz \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME=/opt/java/openjdk21
ENV PATH="$JAVA_HOME/bin:$PATH"

WORKDIR /app
# 複製原始碼
COPY . .

WORKDIR /app/python-api

# 安裝 Python 套件
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/java-fetcer/src
RUN javac -d out src/EarthquakeFetcher.java

CMD ["java -cp out EarthquakeFetcher & uvicorn main:app --host 0.0.0.0 --port 8000"]
