#! /usr/bin/zsh

export $(grep -v '^#' .dev.env | xargs -d '\n')

docker run --rm --name django_sample \
  -e POSTGRES_USER=$POSTGRES_USER \
  -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
  -e POSTGRES_DB=$POSTGRES_DB -p $PORT:5432 \
  -v $VOLUME_NAME:/var/lib/postgresql/data \
  -d postgres:15.1-alpine3.17
