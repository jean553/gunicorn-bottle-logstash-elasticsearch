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
curl http://localhost:8000/ping
```
