DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'westagram',
        'USER': 'root',
        'PASSWORD': 'liminxi',
        'HOST': '127.0.0.1',
        'PORT': '3306',
		'OPTIONS': {'charset': 'utf8mb4'}
    }
}

SECRET_KEY = 'django-insecure-5-5yz)_gi79qodf8)j&ll-^%36-(80=i@d-e$c8&g*@dhkj&5q'

ALGORITHM = 'HS256'