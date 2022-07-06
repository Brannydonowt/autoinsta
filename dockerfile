FROM mcr.microsoft.com/playwright:focal

ENV FIREFOX_VER 87.0

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /

RUN set -x \
   && apt update \
   && apt upgrade -y \
   && apt install -y \
   && pip install  \
       requests
# Add latest FireFox

RUN set -x \
   && apt install -y \
       libx11-xcb1 \
       libdbus-glib-1-2 \
   && curl -sSLO https://download-installer.cdn.mozilla.net/pub/firefox/releases/${FIREFOX_VER}/linux-x86_64/en-US/firefox-${FIREFOX_VER}.tar.bz2 \
   && tar -jxf firefox-* \
   && mv firefox /opt/ \
   && chmod 755 /opt/firefox \
   && chmod 755 /opt/firefox/firefox

# Copy Project
COPY autoinsta/src /autoinsta/src/
COPY autoinsta/cookies /autoinsta/cookies/
COPY autoinsta/profiles /autoinsta/profiles/
COPY autoinsta/videos /autoinsta/videos/

RUN apt install python3.8-venv

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"
 
# Install dependencies:
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN python3 -m playwright install

CMD exec python autoinsta/src/bot.py