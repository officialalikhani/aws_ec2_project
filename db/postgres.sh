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
