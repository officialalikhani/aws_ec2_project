# Create Instances  in aws with API

Create Instances in aws cloud platform services with API , This project has made with python fastapi for beckend and postgresql for database.
Also, You can use the Docker images that has been built for more convenient and stable solution , There are  Dockerfiles and Docker-compose. \
```bash
You can pull These images from my docker repository , See my repo "https://hub.docker.com/u/officialalikhani"
```
## Installation

Use the Dockerfile(postgres) for database, And use the Dockerfile(python) for beckend API.\
Also use postgres.sh for create database with tables and columns , you should copy this file onto docker image but don't worry about this, On dockerfile this problem was solved.\
At first install docker and docker-compose in your os environment.\
After that run this command 

```bash
docker-compose up
```
After that You can see containers will build with those dockerfiles .

## Docker-compose
Lets see  the Docker-compose file 
```yml
version: "3.9"
services:
 backend:
  build: ./backend
  ports:
   - 3838:3838
  environment:
   - ENVWORKERS : 2
 db:
  build: ./db
  ports:
   - 5432:5432
  volumes:
   - ./database:/var/lib/postgresql 
```


## Dockerfiles
Lets see those docker files 

This is for build postgresql image
```dockerfile
FROM postgres
ENV POSTGRES_PASSWORD P@ssw0rd
ENV POSTGRES_DB postgres
COPY postgres.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/postgres.sh
```

And this is for build fastapi python image

```dockerfile
FROM python:3.9
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install  -r requirements.txt
COPY ./main.py .
COPY ./aws_class.py .
EXPOSE 3838 
ARG WORKERS
ENV ENVWORKERS=$WORKERS
CMD ["sh", "-c","uvicorn main:app --host 0.0.0.0 --port 3838 --workers ${ENVWORKERS}"]
```

## postgres bash
Lets see postgresql bash script for

```bash
#!/bin/sh
psql << EOF
-- Table: public.aws
-- DROP TABLE public.aws;
CREATE TABLE IF NOT EXISTS public.aws
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    id_vm  character varying COLLATE pg_catalog."default" NOT NULL,
    ip_address character varying COLLATE pg_catalog."default" NOT NULL,
    username character varying COLLATE pg_catalog."default" NOT NULL,
    size_ character varying COLLATE pg_catalog."default" NOT NULL,
    location_ character varying COLLATE pg_catalog."default" NOT NULL,
    date character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT aws_pkey PRIMARY KEY (id)
)
TABLESPACE pg_default;
ALTER TABLE public.aws
    OWNER to postgres;
EOF"
```


Email me, If you have any questions...!
