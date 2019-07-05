"""
Provide access to endpoints listed under https://iextrading.com/developer/docs/#iex-stats.

Note: The order of function definitions follows the API documentation and should be maintained accordingly.
      This eases tracking of API changes.
"""
from datetime import datetime
from typing import Union

from iexdata.common import get_json, string_or_date


def intraday(filter: str = ''):
    """
    https://iextrading.com/developer/docs/#intraday

    Args:
        filter: https://iextrading.com/developer/docs/#filter-results

    Returns:
        dict: result
    """
    return get_json('stats/intraday', filter=filter)


def recent(filter: str = ''):
    """
    https://iextrading.com/developer/docs/#recent

    Args:
        filter: https://iextrading.com/developer/docs/#filter-results

    Returns:
        dict: result
    """
    return get_json('stats/recent', filter=filter)


def records(filter: str = ''):
    """
    https://iextrading.com/developer/docs/#records

    Args:
        filter: https://iextrading.com/developer/docs/#filter-results

    Returns:
        dict: result
    """
    return get_json('stats/records', filter=filter)


def historical_summary(date: Union[None, str, datetime] = None, filter: str = ''):
    """
    https://iextrading.com/developer/docs/#historical-summary

    Args:
        date: fixme
        filter: https://iextrading.com/developer/docs/#filter-results

    Returns:
        dict: result
    """
    if date:
        if isinstance(date, str):
            return get_json('stats/historical?date=' + date, filter=filter)
        elif isinstance(date, datetime):
            return get_json('stats/historical?date=' + date.strftime('%Y%m'), filter=filter)
        else:
            raise TypeError(f"Can't handle type : {str(type(date))}. Filter: {filter}")
    return get_json('stats/historical', filter=filter)


def historical_daily(date=None, last='', filter: str = ''):
    """
    https://iextrading.com/developer/docs/#historical-daily

    Args:
        date: fixme
        last: fixme
        filter: https://iextrading.com/developer/docs/#filter-results

    Returns:
        dict: result
    """
    if date:
        date = string_or_date(date)
        return get_json('stats/historical/daily?date=' + date, filter=filter)
    elif last:
        return get_json('stats/historical/daily?last=' + last, filter=filter)
    return get_json('stats/historical/daily', filter=filter)
