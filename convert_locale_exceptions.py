class CustomFileError(Exception):
    def __init__(self, m):
        super().__init__("CustomFileError: " + m)


class CustomJsonError(Exception):
    def __init__(self, m):
        super().__init__("CustomJsonError: " + m)

