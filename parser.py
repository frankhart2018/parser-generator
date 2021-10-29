from program_node import ProgramNode
from print_node import PrintNode


class Parser:
    def __init__(self, tokens):
        self.__tokens = tokens
        
        self.__current_token = 0

    def __peek(self):
        return self.__tokens[self.__current_token]

    def __consume(self):
        self.__current_token += 1
        return self.__tokens[self.__current_token - 1]

    def __is_end(self):
        return self.__peek().type == "EOF"

    def __expect(self, token_type):
        if self.__peek().type == token_type:
            return self.__consume()
        else:
            raise Exception(f"Expected {self.__peek().type}, got {token_type}!")

    def __string(self):
        string_token = self.__expect("string")

        return string_token.value

    def __expr(self):
        return self.__string()

    def __print(self):
        self.__expect("print")
        self.__expect("left_paren")
        expr = self.__expr()
        self.__expect("right_paren")

        return PrintNode(expr=expr)

    def __single_line_statement(self):
        if self.__peek().type == 'print':
            return self.__print()

        return self.__expr()

    def __statement(self):
        return self.__single_line_statement()

    def __program(self):
        statements = []

        while not self.__is_end():
            statements.append(self.__statement())

        return ProgramNode("<main>", statements)

    def parse(self):
        return self.__program()