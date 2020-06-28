"""Shared interface for warnings."""

from typing import *
import httpx
import datetime
import json
import pickle

LOG_FILE = 'free_search.log'


def incompatible_argument(
        engine: str,
        argument: str,
        value: Any,
        message: str,
):
    """General interface for individual search engine to print API incompatibilities."""
    print('Warning (%s): %s' % (engine, message))
    print('\tArgument \'%s\' has value: %s' % (argument, repr(value)))


class LogGenerating(type):
    """Classes with this as metaclass will automatically dumps __str__ as log after __init__."""

    def __call__(cls, *args, **kwargs) -> Any:
        obj = type.__call__(cls, *args, **kwargs)
        open(LOG_FILE, 'a').write('%s: %s\n' % (datetime.datetime.now().isoformat(), obj))
        return obj


class SearchResult(metaclass=LogGenerating):
    """An search result entry, with title, url and (optional) snippet."""

    def __init__(self, title: str, url: str, snippet: str = None):
        self.title = title
        self.url = url
        self.snippet = snippet

    def __str__(self) -> str:
        """Convert to string representation."""
        string = 'Entry: \'%s\'(%s)' % (self.title, self.url)
        if self.snippet:
            string = '%s: \n\t\'%s\'' % (string, self.snippet)
        return string

    def __repr__(self) -> str:
        """Same as __str__."""
        return str(self)


class SearchFailure(Exception, metaclass=LogGenerating):
    """Exception thrown by individual search engines."""

    def __init__(self, message: str = '', data: Any = None):
        """Initialize exception with a message."""
        self.message = message
        self.data = data

    def __str__(self) -> str:
        """Convert to string representation."""
        if self.message:
            return '%s: \'%s\'' % (type(self).__name__, self.message)
        else:
            return type(self).__name__

    def __repr__(self) -> str:
        """String representation with optional additional data."""
        string = str(self)
        if self.data:
            try:
                string += ', with data:\n%s' % json.dumps(self.data, indent=4)
            except TypeError:
                string += ', with data:\n%s' % repr(pickle.dumps(self.data))
        return string


class ConnectionFailure(SearchFailure):
    """Failure to retrieve response from the internet."""

    def __init__(self, status: Union[int, str] = '', data: Any = None):
        """Initialize with a message or an HTTP status code."""
        if isinstance(status, str):
            super().__init__(status, data)
        else:
            super().__init__('Server responded with \'%s\' (%d)' % (httpx.StatusCode(status), status), data)


class APIFailure(SearchFailure):
    """Search engine API responded with an error."""
