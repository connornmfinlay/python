FROM ubuntu:22.04

WORKDIR /app

RUN apt-get update && apt-get install -y \
    wget \
    software-properties-common \
    python3.11 \
    python3-pip \ 
    bzip2 \ 
    libxtst6 \ 
    libgtk-3-0 \ 
    libx11-xcb-dev \ 
    libdbus-glib-1-2 \ 
    libxt6 libpci-dev \ 
    libasound2 \
    libgl1-mesa-dri \ 
    libgl1

RUN wget https://download-installer.cdn.mozilla.net/pub/firefox/releases/125.0.1/linux-x86_64/en-US/firefox-125.0.1.tar.bz2 \
    && tar -xjf firefox-125.0.1.tar.bz2 \
    && mv firefox /opt/firefox \
    && ln -s /opt/firefox/firefox /bin/firefox

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz && \
    tar -xvzf geckodriver-v0.34.0-linux64.tar.gz && \
    mv geckodriver /bin && \ 
    chmod +x /bin/geckodriver && \
    PATH="$PATH:/bin/geckodriver:/bin/firefox"  

RUN python3.11 -m pip install selenium
RUN python3.11 -m pip install argparse

COPY group-creation.py .

RUN chmod 777 group-creation.py

ENTRYPOINT ["python3.11", "group-creation.py"]
