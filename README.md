## Prometheus django middleware

Add middleware to django so we can record prometheus metrics on every django endpoint automatically

Based on prometheus official library https://github.com/prometheus/client_python

## How to use 
Install requirement with pip 
```
pip install git+https://github.com/networklocum/prometheus-django  
```

Add middleware to settings.py
```
MIDDLEWARE_CLASSES = [
    'prometheus-django.middleware.PrometheusMiddleware',
]

```

Add start_http_server on django on your main python file
```
from prometheus_client import start_http_server

start_http_server(8000)
```

## How to test

Make a request to any endpoint on your service, eg: http://localhost:8080/ping/

Then access metrics on prometheus, eg: http://localhost:8080/metrics

On prometheus, it should detect automatically this service under  `targets`

## Expose prometheus config on kubernetes

TODO