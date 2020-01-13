{"changed":true,"filter":false,"title":"settings.py","tooltip":"/django_todo/settings.py","value":"\"\"\"\nDjango settings for django_todo project.\n\nGenerated by 'django-admin startproject' using Django 1.11.24.\n\nFor more information on this file, see\nhttps://docs.djangoproject.com/en/1.11/topics/settings/\n\nFor the full list of settings and their values, see\nhttps://docs.djangoproject.com/en/1.11/ref/settings/\n\"\"\"\n\nimport os\nimport dj_database_url\n\n# Build paths inside the project like this: os.path.join(BASE_DIR, ...)\nBASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n\n\n# Quick-start development settings - unsuitable for production\n# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/\n\n# SECURITY WARNING: keep the secret key used in production secret!\nSECRET_KEY = '4e5y3-)(*lv27*_31q^khsx@^35%au9u@x5odckae=ts@2biqz'\n\n# SECURITY WARNING: don't run with debug turned on in production!\nDEBUG = True\n\nALLOWED_HOSTS = ['c8efc1c2ce3a43cd9dcb63099159cf99.vfs.cloud9.us-west-2.amazonaws.com']\n\n\n# Application definition\n\nINSTALLED_APPS = [\n    'django.contrib.admin',\n    'django.contrib.auth',\n    'django.contrib.contenttypes',\n    'django.contrib.sessions',\n    'django.contrib.messages',\n    'django.contrib.staticfiles',\n    \n]\n\nMIDDLEWARE = [\n    'django.middleware.security.SecurityMiddleware',\n    'django.contrib.sessions.middleware.SessionMiddleware',\n    'django.middleware.common.CommonMiddleware',\n    'django.middleware.csrf.CsrfViewMiddleware',\n    'django.contrib.auth.middleware.AuthenticationMiddleware',\n    'django.contrib.messages.middleware.MessageMiddleware',\n    'django.middleware.clickjacking.XFrameOptionsMiddleware',\n]\n\nROOT_URLCONF = 'django_todo.urls'\n\nTEMPLATES = [\n    {\n        'BACKEND': 'django.template.backends.django.DjangoTemplates',\n        'DIRS': [],\n        'APP_DIRS': True,\n        'OPTIONS': {\n            'context_processors': [\n                'django.template.context_processors.debug',\n                'django.template.context_processors.request',\n                'django.contrib.auth.context_processors.auth',\n                'django.contrib.messages.context_processors.messages',\n            ],\n        },\n    },\n]\n\nWSGI_APPLICATION = 'django_todo.wsgi.application'\n\n\n# Database\n# https://docs.djangoproject.com/en/1.11/ref/settings/#databases\n\n#DATABASES = {\n#    'default': {\n#        'ENGINE': 'django.db.backends.sqlite3',\n#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),\n#    }\n#}\nDATABASES = {\n    'default': dj_database_url.parse(\"postgres://xcerkayqxcjwhx:7c98a56a397c40466544a6ce7b5d12a4dee4dfde893dfb284d55548da34bb847@ec2-174-129-33-2.compute-1.amazonaws.com:5432/ddqjku8ln4f755\")\n}\n\n# Password validation\n# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators\n\nAUTH_PASSWORD_VALIDATORS = [\n    {\n        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',\n    },\n]\n\n\n# Internationalization\n# https://docs.djangoproject.com/en/1.11/topics/i18n/\n\nLANGUAGE_CODE = 'en-us'\n\nTIME_ZONE = 'UTC'\n\nUSE_I18N = True\n\nUSE_L10N = True\n\nUSE_TZ = True\n\n\n# Static files (CSS, JavaScript, Images)\n# https://docs.djangoproject.com/en/1.11/howto/static-files/\n\nSTATIC_URL = '/static/'\n","undoManager":{"mark":5,"position":44,"stack":[[{"start":{"row":38,"column":33},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":6},"action":"insert","lines":["''"],"id":3}],[{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"insert","lines":["t"],"id":4},{"start":{"row":39,"column":6},"end":{"row":39,"column":7},"action":"insert","lines":["o"]},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"insert","lines":["d"]},{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"insert","lines":["o"]}],[{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"remove","lines":["o"],"id":5},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"remove","lines":["d"]},{"start":{"row":39,"column":6},"end":{"row":39,"column":7},"action":"remove","lines":["o"]},{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"remove","lines":["t"]}],[{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"remove","lines":["'"],"id":6}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":5},"action":"remove","lines":["'"],"id":7}],[{"start":{"row":27,"column":86},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":8}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":1},"action":"remove","lines":["]"],"id":9},{"start":{"row":28,"column":0},"end":{"row":29,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":27,"column":86},"end":{"row":27,"column":87},"action":"insert","lines":["]"],"id":10}],[{"start":{"row":27,"column":86},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":11}],[{"start":{"row":27,"column":86},"end":{"row":28,"column":0},"action":"remove","lines":["",""],"id":12}],[{"start":{"row":76,"column":0},"end":{"row":76,"column":1},"action":"insert","lines":["#"],"id":13}],[{"start":{"row":77,"column":0},"end":{"row":77,"column":1},"action":"insert","lines":["#"],"id":14}],[{"start":{"row":78,"column":0},"end":{"row":78,"column":1},"action":"insert","lines":["#"],"id":15}],[{"start":{"row":79,"column":0},"end":{"row":79,"column":1},"action":"insert","lines":["#"],"id":16}],[{"start":{"row":80,"column":0},"end":{"row":80,"column":1},"action":"insert","lines":["#"],"id":17}],[{"start":{"row":81,"column":0},"end":{"row":81,"column":1},"action":"insert","lines":["#"],"id":18}],[{"start":{"row":82,"column":0},"end":{"row":82,"column":1},"action":"insert","lines":["D"],"id":24},{"start":{"row":82,"column":1},"end":{"row":82,"column":2},"action":"insert","lines":["A"]},{"start":{"row":82,"column":2},"end":{"row":82,"column":3},"action":"insert","lines":["T"]},{"start":{"row":82,"column":3},"end":{"row":82,"column":4},"action":"insert","lines":["A"]},{"start":{"row":82,"column":4},"end":{"row":82,"column":5},"action":"insert","lines":["S"]}],[{"start":{"row":82,"column":4},"end":{"row":82,"column":5},"action":"remove","lines":["S"],"id":25}],[{"start":{"row":82,"column":0},"end":{"row":82,"column":4},"action":"remove","lines":["DATA"],"id":26},{"start":{"row":82,"column":0},"end":{"row":82,"column":9},"action":"insert","lines":["DATABASES"]}],[{"start":{"row":82,"column":9},"end":{"row":82,"column":10},"action":"insert","lines":[" "],"id":27},{"start":{"row":82,"column":10},"end":{"row":82,"column":11},"action":"insert","lines":["="]}],[{"start":{"row":82,"column":11},"end":{"row":82,"column":12},"action":"insert","lines":[" "],"id":28},{"start":{"row":82,"column":12},"end":{"row":82,"column":13},"action":"insert","lines":["{"]}],[{"start":{"row":82,"column":13},"end":{"row":84,"column":1},"action":"insert","lines":["","    ","}"],"id":29}],[{"start":{"row":83,"column":4},"end":{"row":83,"column":5},"action":"insert","lines":["D"],"id":30},{"start":{"row":83,"column":5},"end":{"row":83,"column":6},"action":"insert","lines":["E"]},{"start":{"row":83,"column":6},"end":{"row":83,"column":7},"action":"insert","lines":["F"]},{"start":{"row":83,"column":7},"end":{"row":83,"column":8},"action":"insert","lines":["A"]}],[{"start":{"row":83,"column":7},"end":{"row":83,"column":8},"action":"remove","lines":["A"],"id":31},{"start":{"row":83,"column":6},"end":{"row":83,"column":7},"action":"remove","lines":["F"]},{"start":{"row":83,"column":5},"end":{"row":83,"column":6},"action":"remove","lines":["E"]},{"start":{"row":83,"column":4},"end":{"row":83,"column":5},"action":"remove","lines":["D"]}],[{"start":{"row":83,"column":4},"end":{"row":83,"column":5},"action":"insert","lines":["d"],"id":32},{"start":{"row":83,"column":5},"end":{"row":83,"column":6},"action":"insert","lines":["e"]},{"start":{"row":83,"column":6},"end":{"row":83,"column":7},"action":"insert","lines":["f"]},{"start":{"row":83,"column":7},"end":{"row":83,"column":8},"action":"insert","lines":["a"]},{"start":{"row":83,"column":8},"end":{"row":83,"column":9},"action":"insert","lines":["u"]},{"start":{"row":83,"column":9},"end":{"row":83,"column":10},"action":"insert","lines":["l"]},{"start":{"row":83,"column":10},"end":{"row":83,"column":11},"action":"insert","lines":["t"]}],[{"start":{"row":83,"column":10},"end":{"row":83,"column":11},"action":"remove","lines":["t"],"id":33},{"start":{"row":83,"column":9},"end":{"row":83,"column":10},"action":"remove","lines":["l"]},{"start":{"row":83,"column":8},"end":{"row":83,"column":9},"action":"remove","lines":["u"]},{"start":{"row":83,"column":7},"end":{"row":83,"column":8},"action":"remove","lines":["a"]},{"start":{"row":83,"column":6},"end":{"row":83,"column":7},"action":"remove","lines":["f"]},{"start":{"row":83,"column":5},"end":{"row":83,"column":6},"action":"remove","lines":["e"]},{"start":{"row":83,"column":4},"end":{"row":83,"column":5},"action":"remove","lines":["d"]}],[{"start":{"row":83,"column":4},"end":{"row":83,"column":6},"action":"insert","lines":["''"],"id":34}],[{"start":{"row":83,"column":5},"end":{"row":83,"column":6},"action":"insert","lines":["d"],"id":35},{"start":{"row":83,"column":6},"end":{"row":83,"column":7},"action":"insert","lines":["e"]},{"start":{"row":83,"column":7},"end":{"row":83,"column":8},"action":"insert","lines":["f"]},{"start":{"row":83,"column":8},"end":{"row":83,"column":9},"action":"insert","lines":["a"]},{"start":{"row":83,"column":9},"end":{"row":83,"column":10},"action":"insert","lines":["u"]},{"start":{"row":83,"column":10},"end":{"row":83,"column":11},"action":"insert","lines":["l"]},{"start":{"row":83,"column":11},"end":{"row":83,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":83,"column":13},"end":{"row":83,"column":14},"action":"insert","lines":[":"],"id":36}],[{"start":{"row":83,"column":14},"end":{"row":83,"column":15},"action":"insert","lines":[" "],"id":37},{"start":{"row":83,"column":15},"end":{"row":83,"column":16},"action":"insert","lines":["{"]}],[{"start":{"row":83,"column":15},"end":{"row":83,"column":16},"action":"remove","lines":["{"],"id":38}],[{"start":{"row":83,"column":15},"end":{"row":83,"column":16},"action":"insert","lines":["d"],"id":39},{"start":{"row":83,"column":16},"end":{"row":83,"column":17},"action":"insert","lines":["j"]},{"start":{"row":83,"column":17},"end":{"row":83,"column":18},"action":"insert","lines":["_"]},{"start":{"row":83,"column":18},"end":{"row":83,"column":19},"action":"insert","lines":["d"]},{"start":{"row":83,"column":19},"end":{"row":83,"column":20},"action":"insert","lines":["a"]},{"start":{"row":83,"column":20},"end":{"row":83,"column":21},"action":"insert","lines":["t"]},{"start":{"row":83,"column":21},"end":{"row":83,"column":22},"action":"insert","lines":["a"]}],[{"start":{"row":83,"column":22},"end":{"row":83,"column":23},"action":"insert","lines":["b"],"id":40},{"start":{"row":83,"column":23},"end":{"row":83,"column":24},"action":"insert","lines":["a"]},{"start":{"row":83,"column":24},"end":{"row":83,"column":25},"action":"insert","lines":["s"]},{"start":{"row":83,"column":25},"end":{"row":83,"column":26},"action":"insert","lines":["e"]},{"start":{"row":83,"column":26},"end":{"row":83,"column":27},"action":"insert","lines":["_"]}],[{"start":{"row":83,"column":27},"end":{"row":83,"column":28},"action":"insert","lines":["u"],"id":41},{"start":{"row":83,"column":28},"end":{"row":83,"column":29},"action":"insert","lines":["r"]},{"start":{"row":83,"column":29},"end":{"row":83,"column":30},"action":"insert","lines":["l"]}],[{"start":{"row":83,"column":30},"end":{"row":83,"column":31},"action":"insert","lines":["."],"id":42},{"start":{"row":83,"column":31},"end":{"row":83,"column":32},"action":"insert","lines":["p"]},{"start":{"row":83,"column":32},"end":{"row":83,"column":33},"action":"insert","lines":["a"]},{"start":{"row":83,"column":33},"end":{"row":83,"column":34},"action":"insert","lines":["r"]},{"start":{"row":83,"column":34},"end":{"row":83,"column":35},"action":"insert","lines":["s"]},{"start":{"row":83,"column":35},"end":{"row":83,"column":36},"action":"insert","lines":["e"]},{"start":{"row":83,"column":36},"end":{"row":83,"column":37},"action":"insert","lines":["*"]}],[{"start":{"row":83,"column":37},"end":{"row":83,"column":39},"action":"insert","lines":["()"],"id":43}],[{"start":{"row":83,"column":37},"end":{"row":83,"column":39},"action":"remove","lines":["()"],"id":44},{"start":{"row":83,"column":36},"end":{"row":83,"column":37},"action":"remove","lines":["*"]}],[{"start":{"row":83,"column":36},"end":{"row":83,"column":38},"action":"insert","lines":["()"],"id":45}],[{"start":{"row":83,"column":37},"end":{"row":83,"column":39},"action":"insert","lines":["\"\""],"id":46}],[{"start":{"row":83,"column":38},"end":{"row":83,"column":189},"action":"insert","lines":["postgres://xcerkayqxcjwhx:7c98a56a397c40466544a6ce7b5d12a4dee4dfde893dfb284d55548da34bb847@ec2-174-129-33-2.compute-1.amazonaws.com:5432/ddqjku8ln4f755"],"id":47}],[{"start":{"row":12,"column":9},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":48},{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["i"]},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":["m"]},{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"insert","lines":["p"]},{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"insert","lines":["o"]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["r"]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":[" "],"id":49}],[{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["d"],"id":50},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["j"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["_"]}],[{"start":{"row":13,"column":7},"end":{"row":13,"column":10},"action":"remove","lines":["dj_"],"id":51},{"start":{"row":13,"column":7},"end":{"row":13,"column":22},"action":"insert","lines":["dj_database_url"]}]]},"ace":{"folds":[],"scrolltop":1071.5,"scrollleft":0,"selection":{"start":{"row":13,"column":22},"end":{"row":13,"column":22},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1578086281479}