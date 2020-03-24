FROM python:3

ADD ./src/entrypoint.py /entrypoint.py
RUN chmod +x /entrypoint.py
ENTRYPOINT ["/entrypoint.py"]
