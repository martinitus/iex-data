"""
Provide access to endpoints listed under https://iextrading.com/developer/docs/#reference-data.
"""
import datetime
from typing import Union

from iexdata.common import get_json, string_or_date


def symbols(filter: str = ''):
    """
    This call returns an array of symbols IEX supports for trading. This list is updated daily as of 7:45 a.m. ET.
    Symbols may be added or removed by IEX after the list was produced.

    Args:
        filter: https://iextrading.com/developer/docs/#filter-results

    Returns:
        dict: result

    See: https://iextrading.com/developer/docs/#symbols
    """
    return get_json('ref-data/symbols', filter)


def corporate_actions(date: Union[str, datetime.date, None] = None, filter: str = ''):
    """
    This call returns an array of new issues, symbol and name changes, and deleted issues, as well as new firms,
    name changes, and deleted firms for IEX-listed securities.

    Records are added once known by the Exchange and will be removed when the Effective Date is in the past.

    Updates are posted once per hour from 8:00 a.m. to 6:00 p.m. ET on each trading day

    Args:
        date: Effective date
        filter: https://iextrading.com/developer/docs/#filter-results

    Returns:
        dict: result

    See: https://iextrading.com/developer/docs/#iex-corporate-actions
    """
    if date:
        date = string_or_date(date)
        return get_json('ref-data/daily-list/corporate-actions/' + date, filter)
    return get_json('ref-data/daily-list/corporate-actions', filter)


def dividends(date: Union[str, datetime.date, None] = None, filter: str = ''):
    """
    This call details upcoming dividend information and other corporate actions, such as stock splits, for IEX-listed
    securities.

    Records are added once known by the Exchange. A new record with the same Record ID as a previously communicated
    record will appear when an existing record is being modified or deleted by the Exchange. All records will be removed
    each evening.

    Updates are posted once per hour from 8:00 a.m. to 6:00 p.m. ET on each trading day

    Args:
        date: Effective date
        filter: https://iextrading.com/developer/docs/#filter-results

    Returns:
        dict: result

    See: https://iextrading.com/developer/docs/#iex-dividends
    """
    if type(date) is str:
        date = string_or_date(date)
        return get_json('ref-data/daily-list/dividends/' + date, filter)
    return get_json('ref-data/daily-list/dividends', filter)


def next_day_ex_date(date: Union[str, datetime.date, None] = None, filter: str = ''):
    """
    This call provides advance notification of dividend declarations impacting IEX-listed securities.

    Records are added at 8:00 a.m. ET one trading day before the specified Ex-Date. Records would have been
    communicated in the IEX Dividends Daily List when they were added or modified by the Exchange. Records are
    removed when Ex-Date is equal to today or when the record is deleted by the Exchange (in this case, a new record
    will appear in the IEX Dividends Daily List with an Event Type=DELETE for the affected Record ID).

    Updates are posted once per hour from 8:00 a.m. to 6:00 p.m. ET on each trading day.

    Args:
        date: Effective date
        filter: https://iextrading.com/developer/docs/#filter-results

    Returns:
        dict: result

    See: https://iextrading.com/developer/docs/#iex-next-day-ex-date
    """
    if date:
        date = string_or_date(date)
        return get_json('ref-data/daily-list/next-day-ex-date/' + date, filter)
    return get_json('ref-data/daily-list/next-day-ex-date', filter)


def symbol_directory(date: Union[str, datetime.date, None] = None, filter: str = ''):
    """
    Args:This call returns an array of all IEX-listed securities and their corresponding data fields. The IEX-Listed
    Symbol Directory Daily List is initially generated and posted to the IEX website at 8:30 p.m. Eastern Time (ET)
    before each trading day, and then once per hour from 9 p.m. until 6 p.m. ET the following day.

    Args:
        date: Effective date
        filter: https://iextrading.com/developer/docs/#filter-results

    Returns:
        dict: result

    See: https://iextrading.com/developer/docs/#iex-listed-symbol-directory
    """
    if date:
        date = string_or_date(date)
        return get_json('ref-data/daily-list/symbol-directory/' + date, filter)
    return get_json('ref-data/daily-list/symbol-directory', filter)
