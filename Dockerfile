FROM python:3.13.3-bookworm

# 安裝基本工具和設置語言環境
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    gnupg2 \
    locales \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 設置語言環境
ENV LANG=en_US.utf8
ENV LC_ALL=en_US.utf8

# 安裝 OpenJDK
RUN curl -L -o openjdk21.tar.gz https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.2%2B13/OpenJDK21U-jdk_aarch64_linux_hotspot_21.0.2_13.tar.gz \
    && mkdir -p /opt/java/openjdk21 \
    && tar -xzf openjdk21.tar.gz -C /opt/java/openjdk21 --strip-components=1 \
    && rm openjdk21.tar.gz

# 設置 Java 環境變數
ENV JAVA_HOME=/opt/java/openjdk21
ENV PATH=$JAVA_HOME/bin:$PATH

# 驗證 Java 安裝
RUN java -version && javac -version

WORKDIR /app
COPY . .

# 創建必要的目錄
RUN mkdir -p static

# 安裝 Python 套件
WORKDIR /app/python-api
RUN pip install --no-cache-dir -r requirements.txt

# 編譯 Java 程式
WORKDIR /app/java-fetcher
RUN mkdir -p out \
    && javac -verbose -encoding UTF-8 -d out src/EarthquakeFetcher.java

# 切換回 Python API 目錄並啟動服務
WORKDIR /app/python-api
CMD ["sh", "-c", "cd /app/java-fetcher && java -Dfile.encoding=UTF-8 -cp out EarthquakeFetcher & cd /app/python-api && uvicorn main:app --host 0.0.0.0 --port 8000"]
