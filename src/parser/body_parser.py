import json
from ..exceptions.request_exceptions import ErrorParsingRequestBody

class BodyParser():

    def __init__(self):
        """
        This class is responsible for parsing the body of a request.
        """
        pass
    
    def parse(self, body: str) -> dict[str or int, any]:
        pass

class SimpleBodyParser(BodyParser):

    def __init__(self):
        """
        This class is responsible for parsing the body of a request.
        """
        pass

    def parse(self, body: str) -> dict[str or int, any]:
        """
        This method is responsible for parsing the body of a request in the most simple form.
        key_value form:
                simpleclient post www.example.com/books title="new book" author="example"
        the body will be passed to the api as:
                {
                    "title":"new book",
                    "author":"example"
                }
        """
        try:
            body_split = body.split(" ")
            body = {}

            for field in body_split:
                field_split = field.split("=")
                key = field_split[0]
                value = field_split[1]
                body[key] = value

            return body
        
        except Exception:
            raise ErrorParsingRequestBody()

class ComplexBodyParser(BodyParser):
    """
    This class is responsible for parsing the body of a request.
    """
    def __init__(self):
        pass

    def parse(self, body: str) -> dict[str or int, any]:
        """
        This method is responsible for parsing the body of a request in the most complex form.
        key_value form: \n
                simpleclient post www.example.com/books \n { "title": {"title_1":"example_1", "title_2":"example_2"}, "author": {"author_1":"example_1", "author_2":"example_2"} } \n
        the body will be deserialized into python object as it is, jsonify and send it.
        """
        try:
            new_body = json.loads(body)
            return new_body
        
        except Exception:
            raise ErrorParsingRequestBody() 