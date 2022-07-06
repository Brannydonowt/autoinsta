FROM mcr.microsoft.com/playwright:focal

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /

# Copy Project
COPY autoinsta/src /autoinsta/src/
COPY autoinsta/cookies /autoinsta/cookies
COPY autoinsta/profiles /autoinsta/profiles

RUN apt install python3.8-venv

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN python3 -m playwright install

CMD exec python autoinsta/src/bot.py