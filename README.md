# MovieBase REST API

## Installation

1. Create and activate virtualenv
2. Clone repository
3. ```cd ./moviebase_rest_api/src```
4. ```pip3 install -r requirements.txt```
5. ```python3 manage.py migrate```
6. You can run server using:
```python3 manage.py runserver 0.0.0.0:8000```

### Notes
You need Sqlite >=3.25.

## Docker

1. Go to project's root directory
2. ```docker-compose build```
3. ```docker-compose up -d```
4. Now you can user following command to start:
```docker-compose start```

### Notes
You probably need ```sudo``` for docker.
