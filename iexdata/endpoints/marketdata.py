"""
Provide access to endpoints listed under https://iextrading.com/developer/docs/#iex-market-data.

Note: The order of function definitions follows the API documentation and should be maintained accordingly.
      This eases tracking of API changes.
"""
from datetime import datetime
from typing import Union, List, Optional

from iexdata.common import get_json, string_or_date


def tops(symbols: Union[None, str, List[str]] = None):
    """TOPS provides IEX’s aggregated best quoted bid and offer position in near real time for all securities on
    IEX’s displayed limit order book. TOPS is ideal for developers needing both quote and trade data.

    For an example of an app that’s using TOPS, see our TOPS viewer app.

    Args:
        symbols; Ticker to request

    Returns:
        dict: result

    See: https://iextrading.com/developer/docs/#tops
    """
    symbols = [symbols] if isinstance(symbols, str) else symbols
    if symbols:
        return get_json('tops?symbols=' + ','.join(symbols) + '%2b')
    return get_json('tops')


def last(symbols: Union[str, List[str]] = None):
    """
    Last provides trade data for executions on IEX. It is a near real time, intraday API that provides IEX last sale
    price, size and time. Last is ideal for developers that need a lightweight stock quote.

    Args:
        symbols; Ticker to request

    Returns:
        dict: result

    See: https://iextrading.com/developer/docs/#last
    """
    symbols = [symbols] if isinstance(symbols, str) else symbols
    if symbols:
        return get_json('tops/last?symbols=' + ','.join(symbols) + '%2b')
    return get_json('tops/last')


def hist(date: Union[None, str, datetime] = None):
    """
    Hist will provide the output of IEX data products for download on a T+1 basis. Data will remain available for the
    trailing twelve months.

    Args:
        date (datetime); Effective date

    Returns:
        dict: result

    See: https://iextrading.com/developer/docs/#hist
    """

    if date is None:
        return get_json('hist')
    else:
        date = string_or_date(date)
        return get_json('hist?date=' + date)


def deep(symbol: Optional[str] = None):
    """
    DEEP is used to receive real-time depth of book quotations direct from IEX. The depth of book quotations received
    via DEEP provide an aggregated size of resting displayed orders at a price and side, and do not indicate the size
    or number of individual orders at any price level. Non-displayed orders and non-displayed portions of reserve
    orders are not represented in DEEP.

    DEEP also provides last trade price and size information. Trades resulting from either displayed or non-displayed
    orders matching on IEX will be reported. Routed executions will not be reported.

    Args:
        symbol; Ticker to request

    Returns:
        dict: result

    See: https://iextrading.com/developer/docs/#deep
    """
    if symbol is not None and not isinstance(symbol, str):
        raise TypeError(f'Cannot use type {type(symbol)}')
    if symbol is not None:
        return get_json('deep?symbols=' + symbol)
    return get_json('deep')


def book(symbol: Optional[str] = None):
    """Book shows IEX’s bids and asks for given symbols.

    Args:
        symbol; Ticker to request

    Returns:
        dict: result

    See: https://iextrading.com/developer/docs/#book
    """
    if symbol is not None and not isinstance(symbol, str):
        raise TypeError(f'Cannot use type {type(symbol)}')
    if symbol is not None:
        return get_json('deep/book?symbols=' + symbol)
    return get_json('deep/book')


def trades(symbol: Optional[str] = None):
    """
    Trade report messages are sent when an order on the IEX Order Book is executed in whole or in part. DEEP sends a
    Trade report message for every individual fill.

    Args:
        symbol; Ticker to request

    Returns:
        dict: result

    See: https://iextrading.com/developer/docs/#trades
    """
    if symbol is not None and not isinstance(symbol, str):
        raise TypeError(f'Cannot use type {type(symbol)}')
    if symbol is not None:
        return get_json('deep/trades?symbols=' + symbol)
    return get_json('deep/trades')


def system_event():
    """
    The System event message is used to indicate events that apply to the market or the data feed.

    There will be a single message disseminated per channel for each System Event type within a given trading session.

    Returns:
        dict: result

    See: https://iextrading.com/developer/docs/#system-event
    """
    return get_json('deep/system-event')


def trading_status(symbol: Optional[str] = None):
    """
    The Trading status message is used to indicate the current trading status of a security. For IEX-listed
    securities, IEX acts as the primary market and has the authority to institute a trading halt or trading pause in a
    security due to news dissemination or regulatory reasons. For non-IEX-listed securities, IEX abides by any
    regulatory trading halts and trading pauses instituted by the primary or listing market, as applicable.

    IEX disseminates a full pre-market spin of Trading status messages indicating the trading status of all securities.
    In the spin, IEX will send out a Trading status message with “T” (Trading) for all securities that are eligible for
    trading at the start of the Pre-Market Session. If a security is absent from the dissemination, firms should assume
    that the security is being treated as operationally halted in the IEX Trading System.

    After the pre-market spin, IEX will use the Trading status message to relay changes in trading status for an
    individual security. Messages will be sent when a security is:

     - Halted
     - Paused*
     - Released into an Order Acceptance Period*
     - Released for trading

    *The paused and released into an Order Acceptance Period status will be disseminated for IEX-listed securities only.
    Trading pauses on non-IEX-listed securities will be treated simply as a halt.

    Args:
        symbol; Ticker to request

    Returns:
        dict: result

    See: https://iextrading.com/developer/docs/#trading-status
    """
    if symbol is not None and not isinstance(symbol, str):
        raise TypeError(f'Cannot use type {type(symbol)}')
    if symbol is not None:
        return get_json('deep/trading-status?symbols=' + symbol)
    return get_json('deep/trading-status')


def operational_halt_status(symbol: Optional[str] = None):
    """
    The Exchange may suspend trading of one or more securities on IEX for operational reasons and indicates such
    operational halt using the Operational halt status message.

    IEX disseminates a full pre-market spin of Operational halt status messages indicating the operational halt
    status of all securities. In the spin, IEX will send out an Operational Halt Message with “N” (Not operationally
    halted on IEX) for all securities that are eligible for trading at the start of the Pre-Market Session. If a
    security is absent from  the dissemination, firms should assume that the security is being treated as
    operationally halted in the IEX Trading System at the start of the Pre-Market Session.

    After the pre-market spin, IEX will use the Operational halt status message to relay changes in operational halt
    status for an individual security.

    Args:
        symbol; Ticker to request

    Returns:
        dict: result

    See: https://iextrading.com/developer/docs/#operational-halt-status
    """
    if symbol is not None and not isinstance(symbol, str):
        raise TypeError(f'Cannot use type {type(symbol)}')
    if symbol is not None:
        return get_json('deep/op-halt-status?symbols=' + symbol)
    return get_json('deep/op-halt-status')


def short_sell_price_test_status(symbol: Optional[str] = None):
    """
    In association with Rule 201 of Regulation SHO, the Short Sale Price Test Message is used to indicate when a
    short sale price test restriction is in effect for a security.

    IEX disseminates a full pre-market spin of Short sale price test status messages indicating the Rule 201 status
    of all securities. After the pre-market spin, IEX will use the Short sale price test status message in the event
    of an intraday status change.

    The IEX Trading System will process orders based on the latest short sale price test restriction status.

    Args:
        symbol; Ticker to request

    Returns:
        dict: result

    See: https://iextrading.com/developer/docs/#short-sale-price-test-status
    """
    if symbol is not None and not isinstance(symbol, str):
        raise TypeError(f'Cannot use type {type(symbol)}')
    if symbol is not None:
        return get_json('deep/ssr-status?symbols=' + symbol)
    return get_json('deep/ssr-status')


def security_event(symbol: Optional[str] = None):
    """
    The Security event message is used to indicate events that apply to a security. A Security event message will
    be sent whenever such event occurs

    Args:
        symbol; Ticker to request

    Returns:
        dict: result

    See: https://iextrading.com/developer/docs/#security-event
    """
    if symbol is not None and not isinstance(symbol, str):
        raise TypeError(f'Cannot use type {type(symbol)}')
    if symbol is not None:
        return get_json('deep/security-event?symbols=' + symbol)
    return get_json('deep/security-event')


def trade_break(symbol: Optional[str] = None):
    """Trade break messages are sent when an execution on IEX is broken on that same trading day. Trade breaks are
    rare and only affect applications that rely upon IEX execution based data.

    Args:
        symbol; Ticker to request

    Returns:
        dict: result

    See: https://iextrading.com/developer/docs/#trade-break
    """
    if symbol is not None and not isinstance(symbol, str):
        raise TypeError(f'Cannot use type {type(symbol)}')
    if symbol is not None:
        return get_json('deep/trade-breaks?symbols=' + symbol)
    return get_json('deep/trade-breaks')


def auction(symbol: str = None):
    """
    DEEP broadcasts an Auction Information Message every one second between the Lock-in Time and the auction match
    for Opening and Closing Auctions, and during the Display Only Period for IPO, Halt, and Volatility Auctions.
    Only IEX listed securities are eligible for IEX Auctions.

    Args:
        symbol; Ticker to request

    Returns:
        dict: result

    See: https://iextrading.com/developer/docs/#auction
    """
    if symbol is not None and not isinstance(symbol, str):
        raise TypeError(f'Cannot use type {type(symbol)}')
    if symbol:
        return get_json('deep/auction?symbols=' + symbol)
    return get_json('deep/auction')


def official_price(symbol: Optional[str] = None):
    """The Official Price message is used to disseminate the IEX Official Opening and Closing Prices.

    These messages will be provided only for IEX Listed Securities.

    Args:
        symbol; Ticker to request

    Returns:
        dict: result

    See: https://iextrading.com/developer/docs/#official-price
    """
    if symbol is not None and not isinstance(symbol, str):
        raise TypeError(f'Cannot use type {type(symbol)}')
    if symbol is not None:
        return get_json('deep/official-price?symbols=' + symbol)
    return get_json('deep/official-price')
