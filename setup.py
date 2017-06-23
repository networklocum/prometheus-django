from setuptools import setup

setup(
    name = 'prometheus-django',
    version = '1.0',
    description = 'Prometheus django middleware',
    packages = [
        'prometheus-django',
    ],
    install_requires = [
        'prometheus_client',
    ]
)