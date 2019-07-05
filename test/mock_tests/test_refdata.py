from unittest import TestCase
import iexdata.endpoints.refdata as refdata

from mock import patch, MagicMock


class TestAll(TestCase):

    def test_symbols(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            refdata.symbols()
            mock.return_value.json = MagicMock(return_value={'currencies': [], 'pairs': []})

    def test_corporate_actions(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            refdata.corporate_actions()
            refdata.corporate_actions(date='20170202')

    def test_dividends(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            refdata.dividends()
            refdata.dividends(date='20170202')

    def test_next_day_ex_date(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            refdata.next_day_ex_date()
            refdata.next_day_ex_date(date='20170202')

    def test_directory(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            refdata.symbol_directory()
            refdata.symbol_directory(date='20170202')
