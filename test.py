import parser
from token import Token
from parser import Parser


tokens = [Token('print', ''), Token('left_paren', ''), Token('string', 'Hello, World!'), 
          Token('right_paren', ''), Token('print', ''), Token('left_paren', ''), 
          Token('string', 'I love Python!'), Token('right_paren', ''), Token('EOF', '')]
parser = Parser(tokens=tokens)

ast = parser.parse()
print(ast)