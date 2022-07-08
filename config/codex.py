# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods,invalid-name,missing-docstring
from .base import (
    DATA_ROOT,
    AssetGroupConfig,
    BaseConfig,
    EDMConfig,
    ElasticsearchConfig,
    EmailConfig,
    FlatfileConfig,
    GoogleConfig,
    ReCaptchaConfig,
    SageConfig,
    SentryConfig,
    TransloaditConfig,
    WildbookDatabaseConfig,
)
from .utils import _getenv


class BaseCodexConfig(
    BaseConfig,
    EmailConfig,
    ReCaptchaConfig,
    GoogleConfig,
    SageConfig,
    EDMConfig,
    AssetGroupConfig,
    ElasticsearchConfig,
    WildbookDatabaseConfig,
    FlatfileConfig,
    TransloaditConfig,
    SentryConfig,
):
    PROJECT_NAME = 'Codex'

    ASSET_GROUP_DATABASE_PATH = str(DATA_ROOT / 'asset_group')

    # fmt: off
    ENABLED_EXTENSIONS = (
        'sage',
        'edm',
        'cors',
        'elasticsearch',
        'gitlab',
        'tus',
        'mail',
        'stripe',
        'sentry',
        'intelligent_agent',
    )

    ENABLED_MODULES = (
        'users',
        'organizations',
        'auth',
        'asset_groups',
        'assets',

        'keywords',
        'fileuploads',
        'collaborations',
        'notifications',
        'encounters',
        'projects',
        'sightings',
        'individuals',
        'relationships',
        'names',
        'complex_date_time',
        'annotations',
        'social_groups',
        'site_settings',
        'job_control',

        'app_ui',
        'swagger_ui',

        'emails',
        'audit_logs',
        'integrity',
        'progress',
    )
    # fmt: on


class ProductionConfig(BaseCodexConfig):
    TESTING = False

    MAIL_OVERRIDE_RECIPIENTS = None
    MAIL_ERROR_RECIPIENTS = [
        'mail-errors@wildme.org',
    ]


class DevelopmentConfig(BaseCodexConfig):
    DEBUG = True

    MAIL_OVERRIDE_RECIPIENTS = _getenv(
        'MAIL_OVERRIDE_RECIPIENTS', 'testing@wildme.org'
    ).split(',')
    MAIL_ERROR_RECIPIENTS = _getenv(
        'MAIL_ERROR_RECIPIENTS', 'mail-errors@wildme.org'
    ).split(',')

    SECRET_KEY = 'DEVELOPMENT_SECRET_KEY'


class TestingConfig(DevelopmentConfig):
    TESTING = True

    # Use in-memory database for testing if SQLALCHEMY_DATABASE_URI and TEST_DATABASE_URI are not specified
    SQLALCHEMY_DATABASE_URI = _getenv('TEST_DATABASE_URI') or _getenv(
        'SQLALCHEMY_DATABASE_URI'
    )

    MAIL_SUPPRESS_SEND = True
