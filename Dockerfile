FROM python:3.13.3-slim-bookworm

# 安裝基本工具和設置語言環境
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    gnupg2 \
    locales \
    default-jdk \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 設置語言環境
ENV LANG=en_US.utf8
ENV LC_ALL=en_US.utf8

# 設置 Java 環境變數
ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH=$JAVA_HOME/bin:$PATH

# 驗證安裝
RUN which java && which javac && \
    java -version && javac -version

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

# 使用 supervisord 管理多個進程
RUN pip install supervisor

# 創建 supervisord 配置文件
RUN echo "[supervisord]\n\
nodaemon=true\n\
\n\
[program:java_fetcher]\n\
command=java -Dfile.encoding=UTF-8 -cp /app/java-fetcher/out EarthquakeFetcher\n\
directory=/app/java-fetcher\n\
autorestart=true\n\
stdout_logfile=/dev/stdout\n\
stdout_logfile_maxbytes=0\n\
stderr_logfile=/dev/stderr\n\
stderr_logfile_maxbytes=0\n\
\n\
[program:uvicorn]\n\
command=uvicorn main:app --host 0.0.0.0 --port 8000\n\
directory=/app/python-api\n\
autorestart=true\n\
stdout_logfile=/dev/stdout\n\
stdout_logfile_maxbytes=0\n\
stderr_logfile=/dev/stderr\n\
stderr_logfile_maxbytes=0" > /app/supervisord.conf

# 使用 supervisord 啟動所有服務
CMD ["supervisord", "-c", "/app/supervisord.conf"]
