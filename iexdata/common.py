from __future__ import print_function

from datetime import datetime
from typing import Union
from urllib.parse import urlparse

import requests


def get_json(url, filter=''):
    """Get a JSON from IEX market data API with given filters applied."""
    url = 'https://api.iextrading.com/1.0/' + url
    if filter:
        url += '?filter={filter}'.format(filter=filter)
    resp = requests.get(urlparse(url).geturl(), proxies=None)
    if resp.status_code == 200:
        return resp.json()
    raise RuntimeError(f'Response {resp.status_code}', resp.text)


def string_or_date(s: Union[str, datetime]):
    """Convert given datetime to IEX conforming string or return given string (YYYYMMDD)"""
    if isinstance(s, str):
        return s
    elif isinstance(s, datetime):
        return s.strftime('%Y%m%d')
    raise TypeError(f'Neither datetime, nor string: {s}')
