# CircuMat
---
CircuMat is a modified (forked) version of Rama-Scene EIT Raw Materials project related to analyzing Environmentally Extended Input-Output (EEIO) tables. CircuMat focuses on NUTS2 level classification as opposed to Rama-Scene country level analysis tool.

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](resources/docs/CONTRIBUTING.md)

# Developers Guide
---
For more information on the tool architecture, please refer to Rama-Scene's documenation: http://rama-scene.readthedocs.io/en/latest/

# Getting started
---
### Retrieve the raw datasets


* EXIOBASE-Rama-Scene (v4 - modified version including secondary materials + CircuMat Eurostat data): 

https://surfdrive.surf.nl/files/index.php/s/bEVnoyJUeYMUiyr

pass: circumat

Download the circumat_v4_clean.zip folder.

### Install node.js (node version: 3.10.10 or higher)
``` 
$ sudo apt-get update
$ sudo apt-get install nodejs
```
> Note: On debian apt install nodejs-legacy

### Install redis (for Django Channels)
```
$ sudo apt install redis-server
```

### Install rabbitMQ (for Celery)

``$ sudo apt-get install -y erlang``

``$ sudo apt-get install rabbitmq-server``

Then enable and start the RabbitMQ service:

``$ systemctl enable rabbitmq-server``

``$ systemctl start rabbitmq-server``

Check the status to make sure everything is running:
``$ systemctl status rabbitmq-server``


> Note: Perform all next steps in the virtualenv and in the rootfolder of the project

### Set the following environment variables or update them (see sample-dev-env.sh):
```
export DJANGO_SETTINGS_MODULE=CMLMasterProject.config.dev
export DATASETS_VERSION=[version downloaded e.g. v3]
export DATASETS_DIR=my/path/to/datasets (make sure that inside this folder is a folder containing the year 2011)
export OPENBLAS_NUM_THREADS=<adjust according to how many cores you want to use>
```
If you are on Linux and using the OpenBlas library for Numpy. 
It is advised to set the number of threads Numpy uses. To find which library is used in python:
```
>>>import numpy as np
>>>np.__config__.show()
```


### Prepare the database
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

### Populate the database 
```
$ python3 manage.py populateHierarchies
```

### Prepare static resources (npm version 4.6.1 or higher)
```
$ npm install
```

### Built React bundle
```
$ ./node_modules/.bin/webpack --config dev-webpack.config.js 
```

### Start Celery
Start the celery module to enable handling of calculations:
```
$ celery -A CMLMasterProject worker -l info  --concurrency 1
```

### Start the development server
```
$ python3 manage.py runserver
```

Access the app via the webbrowser: http://127.0.0.1:8000/cmat/circumat/


### Core dependencies
---
The app uses Celery http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html), Django channels (https://channels.readthedocs.io/en/latest/)
