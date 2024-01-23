import defopt

from my_little_package.talk import greeting


def main(name: str):
    defopt.run(greeting)
