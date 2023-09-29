from ..exceptions.request_exceptions import ErrorParsingRequest, ErrorParsingRequestBody

class Parser():
    """
        The parser is a class that only behaves like parser, only
        returns the parsed request.
        Example: 
            -> simpleclient get https://www.books.com/books
            returns:
                request_method = "GET" ||
                request_url = "https://www.books.com/books

            -> simpleclient post https://www.books.com/books title="The Lord of the Rings" author="J.R.R. Tolkien"
            returns:
                request_method = "POST ||
                request_url = "https://www.books.com/books" ||
                request_body = {
                    "title": "The Lord of the Rings",
                    "author": "J.R.R. Tolkien"
                }
    """

    def __init__(self):
        pass
    
    # get {url} {headers}
    def parse_GET_REQUEST(self, request):
        try:
            request_split = request.split("")

            request_method = request_split[0]
            request_url = request_split[1]
            # append headers
            request_headers = ''.join(request_split[2:])
        except Exception:
            raise ErrorParsingRequest()
        
        return request_method, request_url, request_headers
    
    # post {url} headers|h  {headers} body|b {body}
    def parse_POST_REQUEST(self, request):
        try:
            request_split = request.split(" ")
            request_method = request_split[0]
            request_url = request_split[1]

            body_start = self.__get_body_start(request_split)
            header_start = self.__get_headers_start(request_split)

            if body_start < header_start:
                request_body = 1
            request_headers = self.__get_headers(request_split)
            request_body = self.__get_body(request_split)
        except Exception:
            raise ErrorParsingRequest()
        
        return request_method, request_url, request_headers, request_body

    def parse_PUT_REQUEST(self, request):
        return self.parse_POST_REQUEST(request)
    
    def parse_PATCH_REQUEST(self, request):
        return self.parse_POST_REQUEST(request)

    def parse_DELETE_REQUEST(self, request):
        return self.parse_POST_REQUEST(request)

    def __get_index_of(self, request_split: list, **tags) -> int:
        index_of_body: int = 0
        try:
            index_of_body = request_split.index(tags[0])
        except:
            try:
                index_of_body = request_split.index(tags[1])
            finally:
                pass
        return index_of_body

    def __get_body_start(self, request_split:list) -> list[str]:
        return self.__get_index_of(self, request_split, "body", "b")
    
    def __get_headers_start(self, request_split:list) -> list[str]:
        return self.__get_index_of(self, request_split, "headers", "h")
 
    def __get_headers(self, request_split: list, headers_start) -> dict[str or int, any] or None:
        headers = []

        if headers_start == 0:
            return None

        for field in request_split[headers_start:]:
            headers.append(field)
            if field in ["body", "b"]:
                break

        return headers

    def __get_body(self, request_split: list, body_start) -> dict[str or int, any] or None:
        body = []

        if body_start == 0:
            return None
        
        for field in request_split[body_start:]:
            body.append(field)
            if field in ["body", "b"]:
                break

        return body