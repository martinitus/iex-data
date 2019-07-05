import threading
from enum import Enum
from typing import Union, Set

import ujson as json
from socketIO_client_nexus import SocketIO, BaseNamespace


class Channel(Enum):
    TRADING_STATUS = 'tradingstatus'
    AUCTION = 'auction'
    OPERATIONAL_HALT_STATUS = 'ophaltstatus'
    SSR = 'ssr'
    SECURITY_EVENT = 'securityevent'
    TRADE_BREAK = 'tradebreak'
    TRADES = 'trades'
    BOOK = 'book'
    SYSTEM_EVENT = 'systemevent'
    ALL = 'deep'


class WebSocketClient:

    def __init__(self, symbols: Union[str, Set[str]] = None, channels: Set[Channel] = None, on_message=None,
                 on_connect=None, on_disconnect=None, port=443, url='https://ws-api.iextrading.com'):
        """
        :param symbols: Single symbol, or set of symbols to subscribe to.
        :param channels: The channels of interest.
        :param on_message: Callback to be invoked when data is received
        :param on_connect: Callback to be invoked when the connection is opened
        :param on_disconnect: Callback to be invoked when the connection is closed
        :param port: The port to use for the connection
        :param url: The IEX websocket URL to use
        """
        self.port = port
        self.url = url

        symbols = {} if symbols is None else symbols
        channels = {Channel.ALL} if channels is None else channels

        self.symbols = {symbols} if isinstance(symbols, str) else set(symbols)
        self.channels = {channels} if isinstance(channels, Channel) else set(channels)

        class Namespace(BaseNamespace):
            count = 0

            def on_connect(self, *data):
                if on_connect is not None:
                    on_connect(*data)
                    self.count = self.count + 1

            def on_disconnect(self, *data):
                if on_disconnect is not None:
                    on_disconnect(*data)
                    self.count = self.count + 1

            def on_message(self, data):
                if on_message is not None:
                    on_message(json.loads(data))
                    self.count = self.count + 1

        self.socket = SocketIO(host=self.url, port=self.port)
        self.namespace = self.socket.define(Namespace, '/1.0/deep')

        self.__thread = threading.Thread(target=self.__run)
        self.__terminate = threading.Event()

        for symbol in self.symbols:
            sendinit = {
                "symbols": [symbol],
                "channels": [c.value for c in channels]
            }
            self.namespace.emit('subscribe', json.dumps(sendinit))

    def start(self):
        self.__thread.start()

    def __run(self):
        while not self.__terminate.is_set():
            self.socket.wait(seconds=.1)
        self.namespace.disconnect()

    def stop(self, join=True, timeout=None):
        """Disconnect from the server and terminate the handler event loop"""
        self.__terminate.set()
        if join:
            self.__thread.join(timeout=timeout)
            if self.__thread.is_alive():
                raise RuntimeError("Failed to join thread within timeout")
