import os
from SyntaxError import SyntaxError


class Command:
    """command that will get executed and shown based on @ symbol"""
    isHidden = False

    def __init__(self, command: str, line_number: int, isHidden: bool):
        self.command = command
        self.isHidden = isHidden
        self.line_number = line_number

    def execute(self):
        '''executes the command'''
        try:
            if not self.isHidden:
                print(self.command)
            os.system(self.command)
            print("\n")
        except SyntaxError as e:
            print(f"Error while executing this command: {e} \n {self}", "suggestion:" + e.suggestion)

    def __str__(self) -> str:
        return f"\tcommand : {self.command}  , line number : {self.line_number}"
