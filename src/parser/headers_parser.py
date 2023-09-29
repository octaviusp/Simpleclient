import json
from ..exceptions.request_exceptions import ErrorParsingRequestHeaders


class HeaderParser():
    """
        This class will be responsible for parsing the headers of a request.
    """

    def __init__(self):
        pass

    def parse(self, headers: str) -> dict[str or int, any]:
        pass

class SimpleHeaderParser(HeaderParser):

    def parse(self, headers: str) -> dict[str, str]:
        """
            This parses headers as simple form, like the body simple parser.
            \n simpleclient get www.example.com/books?name=Harry+Potter authorization="token"
            returns:
                headers{
                    "authorization": "bearer token"
                }
        """
        try:
            headers_split = headers.split(" ")
            headers = {}

            for field in headers_split:
                field_split = field.split("=")
                key = field_split[0]
                value = field_split[1]

                headers[key] = value

            return headers
        except Exception:
            raise ErrorParsingRequestHeaders()


class ComplexHeaderParser(HeaderParser):
    """
        This class will be responsible for parsing the headers of a request.
    """

    def __init__(self):
        pass

    def parse(self, headers: str) -> dict[str or int, any]:
        try:
            new_headers = json.loads(headers)
            return new_headers
        except Exception:
            raise ErrorParsingRequestHeaders()