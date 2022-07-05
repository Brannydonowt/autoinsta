FROM python:3.9

ENV DEBIAN_FRONTEND noninteractive
ENV GECKODRIVER_VER v0.29.0
ENV FIREFOX_VER 87.0

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD exec python ./bot.py