class SyntaxError(Exception):

    def __init__(self, message, suggestion):
        self.message = message
        self.suggestion = suggestion

    def __str__(self):
        return self.message + "\n" + self.suggestion
