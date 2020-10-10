FROM python:3-alpine

RUN apk update && apk upgrade

RUN apk add \
    gcc \
    jpeg-dev \
    musl-dev \
    zlib-dev

COPY requirements.txt /LayoutGenerator/
RUN pip install -r /LayoutGenerator/requirements.txt

COPY . /LayoutGenerator
WORKDIR /LayoutGenerator/src

ENTRYPOINT ["python", "generate.py", "-o", "/output"]
CMD ["-h"]
