# My Little Package

A example of a very minimal Python package.


## Getting started

You can directly install this minimal package from its repository using pip.

Let's illustrate this using a [Python virtual environment](https://docs.python.org/3/library/venv.html):

First create a virtual environment `venv` and activate it:

```bash
python3 -m venv venv
. venv/bin/activate
```

then install this package in it:

```bash
python3 -m pip install git+https://TODO
```

We can now use import it and use it:

```bash
$ python3
>>> from my_little_package.talk import greeting
>>> greeting("Pinkie Pie")
TODO
```

The package also provides a command line tool `mlp` that we can make use of:

```bash
mlp Applejack
```


## Development

During development, we can use the same approach but installing the cloned repository in development mode:

```
git clone
```


## References

Sources of inspiration:

- https://packaging-guide.openastronomy.org/en/latest/minimal.html
- https://www.scivision.dev/python-minimal-package/
