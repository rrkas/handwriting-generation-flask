# syntax=docker/dockerfile:1
FROM python:3.7-alpine

ENV CHROME_BIN="/usr/bin/chromium-browser"

#RUN set -x \
#  && apk update \
#  && apk upgrade \
#  # replacing default repositories with edge ones
#  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" > /etc/apk/repositories \
#  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
#  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories \
#  \
#  # Add the packages
#  && apk add --no-cache dumb-init curl make gcc g++ linux-headers binutils-gold gnupg libstdc++ nss chromium \
#  \
#  # Do some cleanup
#  && apk del --no-cache make gcc g++ python binutils-gold gnupg libstdc++ \
#  && rm -rf /usr/include \
#  && rm -rf /var/cache/apk/* /root/.node-gyp /usr/share/man /tmp/* \
#  && echo

WORKDIR /code

ENV DISPLAY :0.0

RUN apk add --no-cache gcc musl-dev linux-headers

RUN apk add python3-dev py3-setuptools chromium chromium-chromedriver xvfb

RUN apk add tiff-dev jpeg-dev openjpeg-dev zlib-dev freetype-dev lcms2-dev \
    libwebp-dev tcl-dev tk-dev harfbuzz-dev fribidi-dev libimagequant-dev \
    libxcb-dev libpng-dev

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ADD run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 10002

COPY . .

CMD /run.sh

CMD ["python", "script.py"]