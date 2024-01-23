# My Little Package

An example of a very minimal Python package.


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
python3 -m pip install git+https://github.com/jennan/my_little_package@v0.1.2
```

We can now use import it and use it:

```bash
$ python3
>>> from my_little_package.talk import greeting
>>> greeting("Pinkie Pie")
Hello Pinkie Pie!
```

The package also provides a command line tool `mlp` that we can make use of:

```bash
mlp  # issue an error as it is missing a parameter
mlp -h  # display help message
mlp Applejack
```


## Development

During development, it is useful to install the local clone of the repository in [development mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html):

```bash
git clone https://github.com/jennan/my_little_package.git
cd my_little_package

python3 -m venv venv
. venv/bin/activate

python3 -m pip install -e .
```

In development mode (or editable installs), any change to the source files is readily available in the virtual environment without reinstalling the package.

This package also defines additional dependencies for development, for example the formatter and linter [ruff](https://github.com/astral-sh/ruff).

To install these additional dependencies, add the `[dev]` statement to the installation command:

```bash
python3 -m pip install -e .[dev]
```

Now we can use `ruff` to format our code and keep it nice and tidy:

```
ruff src/
```


## References

- https://packaging-guide.openastronomy.org/en/latest/minimal.html
- https://www.scivision.dev/python-minimal-package/
- https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html
