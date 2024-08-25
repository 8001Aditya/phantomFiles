DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': '<your_database_name>',
        'CLIENT': {
            'host': 'mongodb://localhost:27017/',
        },
    }
}
