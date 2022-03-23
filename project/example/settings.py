from __future__ import annotations

from pathlib import Path

from composed_configuration import (
    ComposedConfiguration,
    ConfigMixin,
    DevelopmentBaseConfiguration,
    HerokuProductionBaseConfiguration,
    ProductionBaseConfiguration,
    TestingBaseConfiguration,
)


class ExampleMixin(ConfigMixin):
    WSGI_APPLICATION = 'example.wsgi.application'
    ROOT_URLCONF = 'example.urls'
    CELERY_BROKER_URL = None

    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

    @staticmethod
    def mutate_configuration(configuration: ComposedConfiguration) -> None:
        # Install local apps first, to ensure any overridden resources are found first
        configuration.INSTALLED_APPS = [
            'example.core.apps.CoreConfig',
        ] + configuration.INSTALLED_APPS

        # Install additional apps
        configuration.INSTALLED_APPS += [
            's3_file_field',
            'django_large_image',
        ]


class DevelopmentConfiguration(ExampleMixin, DevelopmentBaseConfiguration):
    pass


class TestingConfiguration(ExampleMixin, TestingBaseConfiguration):
    pass


class ProductionConfiguration(ExampleMixin, ProductionBaseConfiguration):
    pass


class HerokuProductionConfiguration(ExampleMixin, HerokuProductionBaseConfiguration):
    pass
