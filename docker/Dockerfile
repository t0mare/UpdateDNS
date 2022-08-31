FROM bitnami/python:latest
ADD src/*.* /app/
RUN pip install requests
WORKDIR /app
ENTRYPOINT ["sh" ,"/app/entrypoint.sh"]