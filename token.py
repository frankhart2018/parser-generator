class Token:
    def __init__(self, type, value):
        self.__type = type
        self.__value = value

    def __str__(self):
        return f"Token(type='{self.__type}', value='{self.__value}')"

    @property
    def type(self):
        return self.__type

    @property
    def value(self):
        return self.__value