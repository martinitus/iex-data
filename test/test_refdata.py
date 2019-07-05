from unittest import TestCase
import iexdata.endpoints.refdata as refdata


class TestAll(TestCase):

    def test_symbols(self):
        symbols = refdata.symbols()
        self.assertIsNotNone(symbols)
        self.assertLess(0, len(symbols))
        self.assertIn('AAPL', {s['symbol'] for s in symbols})

    def test_corporate_actions(self):
        actions = refdata.corporate_actions()
        self.assertIsNotNone(actions)
        actionsd = refdata.corporate_actions(date='20170202')
        self.assertIsNotNone(actionsd)

    def test_dividends(self):
        dividends = refdata.dividends()
        self.assertIsNotNone(dividends)
        dividendsd = refdata.dividends(date='20170202')
        self.assertIsNotNone(dividendsd)

    def test_next_day_ex_date(self):
        ex_date = refdata.next_day_ex_date()
        self.assertIsNotNone(ex_date)
        ex_dated = refdata.next_day_ex_date(date='20170202')
        self.assertIsNotNone(ex_dated)

    def test_directory(self):
        directory = refdata.symbol_directory()
        self.assertIsNotNone(directory)
        directoryd = refdata.symbol_directory(date='20170202')
        self.assertIsNotNone(directoryd)

    def pretty_print(self, json: dict):
        import pprint
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(json)
