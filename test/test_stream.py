import threading
from unittest import TestCase

from retry import retry

from iexdata.stream import WebSocketClient, Channel


class TestDeepStream(TestCase):
    def test_client(self):
        event1 = threading.Event()
        event2 = threading.Event()

        connected = threading.Event()
        disconnected = threading.Event()

        def on_data(data: dict):
            """Wait until we receive a trading status message which should be one of the first."""
            if 'symbol' in data and 'messageType' in data:
                if data['symbol'] == 'AAPL' and data['messageType'] == 'tradingstatus':
                    print("APPL initial message received")
                    event1.set()
                if data['symbol'] == 'KPTI' and data['messageType'] == 'tradingstatus':
                    print("KPTI initial message received")
                    event2.set()

        def on_connect(*args):
            print("connected")
            connected.set()

        def on_disconnect(*args):
            print("disconnected")
            disconnected.set()

        @retry(Exception, tries=4, delay=1)
        def retry_client():
            return

        client = WebSocketClient(symbols={'AAPL', 'KPTI'}, channels={Channel.ALL},
                                   on_connect=on_connect,
                                   on_disconnect=on_disconnect,
                                   on_message=on_data)

        client.start()

        # wait a few seconds and see if we received the messages
        received1 = event1.wait(timeout=5)
        received2 = event1.wait(timeout=1)

        client.stop(join=True, timeout=3)

        self.assertTrue(connected.is_set(), "connect handler was not invoked")
        self.assertTrue(disconnected.is_set(), "disconnect handler was not invoked")

        self.assertTrue(received1, "did not receive initial APPL trading status message")
        self.assertTrue(received2, "did not receive initial KPTI trading status message")
