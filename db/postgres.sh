FROM postgres
ENV POSTGRES_PASSWORD P@ssw0rd
ENV POSTGRES_DB postgres
COPY postgres.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/postgres.sh
