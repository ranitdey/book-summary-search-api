import os

class Config:
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    AUTHOR_SERVICE = "https://ie4djxzt8j.execute-api.eu-west-1.amazonaws.com/coding"
    TESTING = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    AUTHOR_SERVICE = "https://ie4djxzt8j.execute-api.eu-west-1.amazonaws.com/coding"


class ProductionConfig(Config):
    DEBUG = False
    AUTHOR_SERVICE = "https://ie4djxzt8j.execute-api.eu-west-1.amazonaws.com/coding"


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)