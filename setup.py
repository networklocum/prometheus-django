from setuptools import setup

setup(
    name = 'prometheus_django',
    version = '1.1',
    description = 'Prometheus django middleware',
    packages = [
        'prometheus-django',
        'prometheus_django',
    ],
    install_requires = [
        'prometheus_client',
    ]
)