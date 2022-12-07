
class Config(object):
    DEBUG = True
    TESTING = False


class DevelopmentConfig(Config):
    SECRET_KEY = "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"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

# Enter your Open API Key here
OPENAI_API_KEY = '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'
