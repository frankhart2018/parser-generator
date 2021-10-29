class ProgramNode:
    def __init__(self, method, statements):
        self.__method = method
        self.__statements = statements

    def __str__(self):
        statements = ", ".join(str(statement) for statement in self.__statements)
        return f"ProgramNode(method={self.__method}, statements='{statements}')"