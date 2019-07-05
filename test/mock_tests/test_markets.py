from unittest import TestCase

from mock import patch, MagicMock
import iexdata.endpoints.markets as markets


class TestAll(TestCase):
    def test_markets(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            markets.market()
