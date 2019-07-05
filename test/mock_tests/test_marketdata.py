from unittest import TestCase

from mock import patch, MagicMock

import iexdata.endpoints.marketdata as mdata


class TestMarketDataMocks(TestCase):
    def test_tops(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mdata.tops()
            mdata.tops(symbols='test')
            mdata.tops(symbols=['test'])
            mdata.tops(symbols=['test', 'foo'])

    def test_last(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mdata.last()
            mdata.last(symbols='test')
            mdata.last(symbols=['test'])
            mdata.last(symbols=['test', 'foo'])

    def test_hist(self):
        from datetime import datetime
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mdata.hist()
            mdata.hist(date='201505')
            mdata.hist(date=datetime.today())

    def test_deep(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mdata.deep()
            mdata.deep(symbol='test')

    def test_book(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mdata.book()
            mdata.book(symbol='test')

    def test_trades(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mdata.trades()
            mdata.trades(symbol='test')

    def test_system_event(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mdata.system_event()

    def test_trading_status(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mdata.trading_status()
            mdata.trading_status(symbol='test')

    def test_operational_halt_status(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mdata.operational_halt_status()
            mdata.operational_halt_status(symbol='test')

    def test_short_sell_price_test_status(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mdata.short_sell_price_test_status()
            mdata.short_sell_price_test_status(symbol='test')

    def test_security_event(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mdata.security_event()
            mdata.security_event(symbol='test')

    def test_trade_break(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mdata.trade_break()
            mdata.trade_break(symbol='test')

    def test_auction(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mdata.auction()
            mdata.auction(symbol='test')

    def test_official_price(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mdata.official_price()
            mdata.official_price(symbol='test')
