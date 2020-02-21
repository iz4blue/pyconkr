# PyCon Korea Homepage

![test-deploy](https://github.com/pythonkr/pyconkr/workflows/test-deploy/badge.svg)

## Contribution
pyconkr-api contribution을 제출할 때에는 반드시 다음 [가이드라인](./.github/CONTRIBUTING.md)을 따라주세요.

## Requiremensts

- Python 3.7.6

## Getting started

```bash
$ git clone git@github.com:pythonkr/pyconkr.git
$ cd pyconkr
$ pip install -r requirements.txt
$ python manage.py compilemessages
$ python manage.py makemigrations  # flatpages
$ python manage.py migrate
$ python manage.py loaddata ./pyconkr/fixtures/flatpages.json
$ bower install
$ python manage.py runserver
```

