from datetime import datetime
from unittest import TestCase

from mock import patch, MagicMock

import iexdata.endpoints.stats as stats


class TestAll(TestCase):
    def test_intraday(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            stats.intraday()

    def test_recent(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            stats.recent()

    def test_records(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            stats.records()

    def test_summary(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            stats.historical_summary()
            stats.historical_summary('201505')
            stats.historical_summary(datetime.today())
            with self.assertRaises(TypeError):
                stats.historical_summary(date=5)

    def test_daily(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            stats.historical_daily()
            stats.historical_daily('201505')
            stats.historical_daily(last='5')
            stats.historical_daily(datetime.today())
            with self.assertRaises(TypeError):
                stats.historical_daily(date=5)
