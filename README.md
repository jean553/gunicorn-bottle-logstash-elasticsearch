# gunicorn-kibana-logstash

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
