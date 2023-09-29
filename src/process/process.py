from ..parser.parser import Parser
from ..verifiers.verifier import Verifier

class Process():
    """
        The process will be the class that process the command sent to the simpleclient.
        It will be responsible for parsing the command, send it to the sender grab the request,and returning the request.
    """

    def __init__(self, parser: Parser, verifier: Verifier):
        self.parser = parser
        self.verifier = verifier

    def process_command(self, command):
        try:
            command_parsed = self.parser.parse_command(command)
            

        except Exception as e:
            raise e