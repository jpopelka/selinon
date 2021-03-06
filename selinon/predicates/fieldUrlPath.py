#!/usr/bin/env python3
# pragma: no cover

from functools import reduce
from urllib.parse import urlparse


def fieldUrlPath(message, key, path):
    try:
        val = reduce(lambda m, k: m[k], key if isinstance(key, list) else [key], message)
        return urlparse(val).path == path
    except:
        return False
