[![Build Status](https://travis-ci.org/xelonic-de/iex-data.svg?branch=master)](https://travis-ci.org/xelonic-de/iex-data)

# IEX Data API
Python interface to [IEX market data API](https://iextrading.com/developer/docs/). See 
[here](https://github.com/timkpaine/pyEX) for a client for the IEX Cloud.

# Attribution
## PyEx
This library is a hard fork of [pyEx](https://github.com/timkpaine/pyEX) which was originally designed for the IEX API
but now supports IEX cloud. Many thanks go to [Tim Paine](https://github.com/timkpaine).

## IEX Trading
If you redistribute IEX market data:

- Cite IEX using the following text and link: “Data provided for free by [IEX](https://iextrading.com/developer).”
- Provide a link to https://iextrading.com/api-exhibit-a in your terms of service.
- Additionally, if you display our TOPS price data, cite “IEX Real-Time Price” near the price.

# Getting Started
Documentation of iex-data package is manly copied from https://iextrading.com/developer/docs/. Still, we have our own 
documentation site at [Read The Docs!](https://pyEX.readthedocs.io). Further, the tests are a good starting point to see
how to use iex-data.
- [Endpoint Test](./test/test_refdata.py)
- [Streaming Test](./test/test_stream.py)