import os

models = ['aerich.models', 'models']

db_url = os.getenv('db_url')

TORTOISE_ORM = {
    'connections': {'default': db_url},
    'apps': {
        'models': {
            'models': models,
            'default_connection': 'default',
        },
    },
}
