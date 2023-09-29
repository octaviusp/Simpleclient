import re

class Verifier():
    """
        This class will be the responsible to verify if the url is valid,
        if the method is valid, if the body is valid, and other validations.
    """

    def __init__(self):
        self.url_regex = r'^(https?://)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*/?$'

    def is_a_request_method(self, method: str) -> bool:
        return True if method in ["GET", "POST", "PUT", "PATCH", "DELETE"] else False    

    def is_a_valid_url(self, url: str) -> bool:
        url_pattern = re.compile(self.url_regex)

        return True if url_pattern.match(url) else False