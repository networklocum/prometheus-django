"""
@deprecated
This module will exist until I've gone round all our codebase and deleted everything
that references it, then it's getting deleted
"""
import warnings

from prometheus_django.middleware import PrometheusMiddleware

warnings.warn(
    "Use prometheus_django not prometheus-django",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = ["PrometheusMiddleware"]
