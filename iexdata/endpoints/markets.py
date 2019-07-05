"""
Provide access to endpoints listed under https://iextrading.com/developer/docs/#markets.
"""
from iexdata.common import get_json


def market(filter: str = ''):
    """
    https://iextrading.com/developer/docs/#market
    """
    return get_json('market', filter=filter)
