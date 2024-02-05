ARG VARIANT="3.11-alpine3.17"
FROM python:${VARIANT}

WORKDIR .

RUN apk add --no-cache bash

COPY entrypoint.sh /entrypoint.sh
COPY main.py /main.py

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]