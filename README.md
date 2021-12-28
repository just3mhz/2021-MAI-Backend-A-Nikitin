## ER-diagram

![](./media/craigslist_er_diagram.png "ER-diagram")


## Coverage

```
Name                                Stmts   Miss  Cover
-------------------------------------------------------
api_v0/__init__.py                      0      0   100%
api_v0/admin.py                         5      0   100%
api_v0/forms.py                        11      0   100%
api_v0/migrations/0001_initial.py      10      0   100%
api_v0/migrations/__init__.py           0      0   100%
api_v0/models.py                       20      0   100%
api_v0/serializers.py                  16      0   100%
api_v0/tests/__init__.py                0      0   100%
api_v0/tests/test_models.py            13      0   100%
api_v0/tests/test_views.py             66      0   100%
api_v0/urls.py                         11      0   100%
api_v0/views.py                        29      1    97%
craigslist/__init__.py                  0      0   100%
craigslist/settings.py                 29      0   100%
craigslist/urls.py                      4      0   100%
manage.py                              12      2    83%
web/__init__.py                         0      0   100%
web/admin.py                            1      0   100%
web/migrations/__init__.py              0      0   100%
web/models.py                           1      0   100%
web/tests.py                            1      0   100%
web/urls.py                             7      0   100%
web/views.py                           21      6    71%
-------------------------------------------------------
TOTAL                                 257      9    96%
```

## Useful links

[Using docker with nginx, postgres and django](https://fixmypc.ru/post/sozdanie-i-zapusk-konteinera-docker-s-django-postgressql-gunicorn-i-nginx/)
