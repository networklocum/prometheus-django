import re
import time
from prometheus_client import Counter, Summary, Gauge


def replace_id_in_url(url):
    """
        Replace id on url so we can easily group by them
        > replace_id_in_url(/user/1234/)
        /user/:id/
    """
    return re.sub(r'/[0-9]+/', '/:id/', url)


PROMETHEUS_REQUEST_DURATION = Summary('http_request_duration_microseconds',
                                      'Request duration in microseconds',
                                      ['method', 'endpoint'])
PROMETHEUS_REQUEST_TOTAL = Counter('http_requests_total',
                                   'Request total wiht status',
                                   ['method', 'endpoint', 'http_status'])
PROMETHEUS_REQUEST_IN_PROGRESS = Gauge('http_requests_in_progress_total', 
                                       'Requests in progress',
                                       ['method', 'endpoint'])


class PrometheusMiddleware(object):
    def process_request(self, request):
        """
            Save initial time of the request when it starts
        """
        url = replace_id_in_url(request.META.get('PATH_INFO'))

        PROMETHEUS_REQUEST_IN_PROGRESS.labels(
            request.method, url).inc()

        request.prometheus_start_time = time.time()

    def process_response(self, request, response):
        """
            Calculate the request latency by looking at the time we stored
            at the beggining of the request
        """
        if hasattr(request, 'prometheus_start_time'):
            request_latency = time.time() - request.prometheus_start_time
            latency_microseconds = request_latency / 1000000
            url = replace_id_in_url(request.META.get('PATH_INFO'))

            PROMETHEUS_REQUEST_DURATION.labels(
                request.method, url).observe(latency_microseconds)
            PROMETHEUS_REQUEST_TOTAL.labels(
                request.method, url, response.status_code).inc()
            PROMETHEUS_REQUEST_IN_PROGRESS.labels(
                request.method, url).dec()
                
        return response
