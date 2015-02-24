MongoDB Flask API
=================

A simple API built on top of MongoDB and Flask

Install
-------

System dependencies:
* Python 3.4
* MongoDB (See ./install_mongodb_ubuntu1404.sh)

```
pip install -e .
```

Test
----

```
tox
```

Run
---

```
run
curl http://127.0.0.1:5000/api/hello
```
