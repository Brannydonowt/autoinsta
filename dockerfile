FROM python:3.9

ENV DEBIAN_FRONTEND noninteractive
ENV GECKODRIVER_VER v0.29.0
ENV FIREFOX_VER 87.0

WORKDIR /

# Copy Project
COPY autoinsta/src /autoinsta/src/
COPY autoinsta/cookies /autoinsta/cookies
COPY autoinsta/profiles /autoinsta/profiles

# COPY driver.py /app/src
# COPY instagram.py /app/src/
# COPY scheduler.py /app/src/
# COPY tiktok.py /app/src/
# COPY utils.py /app/src/

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD exec python autoinsta/src/bot.py