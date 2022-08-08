FROM python:3.10.1-alpine3.15

# para printar output direto no console sem buferizar
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./src /src
COPY ./traineddata /traineddata

WORKDIR /src

#porta para acessar a aplicação
EXPOSE 8100

RUN apk update &&  \
    apk add tesseract-ocr && \
    python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base mysql-dev musl-dev linux-headers && \
    apk add --no-cache jpeg-dev zlib-dev && \
    /venv/bin/pip install -r /requirements.txt


# adiciona o venv py
ENV PATH="/scripts:/venv/bin:$PATH"
