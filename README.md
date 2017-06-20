Workoutholic
============

Fixtures:
---------

```bash
./manage.py loaddata applications/core/fixtures/*.json \
    && ./libexec/fixture_images.sh
```

> Fixtures include some exercises as well as one super user

superuser: admin
password: asd123!!!

Full DB Reset:
--------------

```bash
dropdb workoutholic_dev \
    && createdb workoutholic_dev \
    && pm migrate \
    && pm loaddata applications/core/fixtures/* \
    && ./libexec/fixture_images.sh
```

