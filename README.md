# gunicorn-bottle-logstash-elasticsearch

The POC contains a simple HTTP server built with Bottle.
Gunicorn is used to start the server worker(s).
Nginx is configured to redirect the traffic to server.

## Install the environment

```sh
vagrant up
```

## Connect to the development container

```sh
vagrant ssh
```

## Start the service

```sh
gunicorn -w 4 gunicorn-bottle-logstash-elasticsearch.__main__:app
```

In the example above, four workers are started.

## Run tests

```sh
py.test
```

## Check the service is running

```sh
curl http://localhost/ping
```

```sh
curl http://localhost/post-data \
    -X POST \
    -d '{"message": "hello world", "status": "sent"}' \
    -H 'Content-Type: application/json'
```

## Configure Kibana

Connect to the Kibana web interface:

```
http://kibana-container-ip-address:5601
```

The ip address of the container can be found using `docker inspect gunicorn-bottle-logstash-elasticsearch_kibana`.

The index pattern is `data-*`.

Optionally, you can configure a time field: go into
`Advanced Settings` > `metaFields`. Add the field `timestamp`.
Go back the to the index creation page, `timestamp` can now be selected
into the `metaFields` options list.
