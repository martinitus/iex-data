from datetime import datetime
from unittest import TestCase

from mock import patch, MagicMock

from iexdata.common import get_json, string_or_date


class TestCommon(TestCase):
    def test_get_json(self):
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200

            get_json(url='')
            get_json(url='', filter='test')

            mock.return_value.status_code = 404
            with self.assertRaises(RuntimeError):
                get_json(url='')

            with self.assertRaises(RuntimeError):
                get_json(url='', filter='test')

    def test_string_or_date(self):
        string_or_date('test')
        string_or_date(datetime.now())
        with self.assertRaises(TypeError):
            string_or_date(s=5)
