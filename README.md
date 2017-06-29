# gunicorn-kibana-logstash

The POC contains a simple HTTP server built with Bottle.
Gunicorn is used to start the server worker(s).
Nginx is configured to redirect the traffic to server.

## Install the environment

```bash
vagrant up
```

## Connect to the development container

```bash
vagrant ssh
```

## Start the service

```bash
gunicorn -w 4 gunicorn-kibana-logstash.__main__:app
```

In the example above, four workers are started.

## Check the service is running

```bash
curl http://localhost/ping
```

```bash
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

The ip address of the container can be found using `docker inspect gunicorn-kibana-logstash_kibana`.

The index pattern is `data-*`.

Optionally, you can configure a time field: go into
`Advanced Settings` > `metaFields`. Add the field `timestamp`.
Go back the to the index creation page, `timestamp` can now be selected
into the `metaFields` options list.
