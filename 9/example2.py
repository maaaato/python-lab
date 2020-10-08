import sys
from functools import lru_cache
from time import sleep


@lru_cache(maxsize=32)
def heavy_function(n):
    sleep(3)
    return n + 1


print(heavy_function(2))


def decol(f):
    print('decol called')

    def wrapper(*args, **kwargs):
        print('before exec')
        v = f(*args, **kwargs)
        print('after exec')
        return v

    def hoge():
        print("hoge")

    def fuga():
        print("fuga")

    wrapper.hoge = hoge
    wrapper.fuga = fuga
    return wrapper


@decol
def hoge(max=2, min=1):
    print(max+min)


hoge()
