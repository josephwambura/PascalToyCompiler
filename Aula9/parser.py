from tokenizer import Tokenizer
from node import BinOp, UnOp, IntVal, NoOp

class Parser():
    def __init__(self, origin):
        self.tokens = Tokenizer(origin)
    def parseExpression(self):
        token = self.tokens.selectNext()
        result = self.parseTerm(token)
        while True:
            token = self.tokens.actual
            if token == None:
                break
            if token.type == "PLUS":
                token = self.tokens.selectNext()
                second_value = self.parseTerm(token)
                result = BinOp("+", [result, second_value])
            elif token.type == "MINUS":
                token = self.tokens.selectNext()
                second_value = self.parseTerm(token)
                result = BinOp("-", [result, second_value])
            else:
                break
        return result
    def parseTerm(self, token):
        result = self.parseFactor(token)
        while True:
            token = self.tokens.selectNext()
            if token == None:
                break
            elif token.type == "MULT":
                token = self.tokens.selectNext()
                second_value = self.parseFactor(token)
                result = BinOp("*", [result, second_value])
            elif token.type == "DIV":
                token = self.tokens.selectNext()
                second_value = self.parseFactor(token)
                result = BinOp("/", [result, second_value])
            else:
                break
        return result
    def parseFactor(self, token):
        if token == None:
            raise ValueError("Invalid token, expecting a number or opening parentesis on position {}, got NULL".format(self.tokens.position))
        if token.type == "INT":
            result = IntVal(token.value, [])
        elif token.type == "OPEN_PAR":
            result = self.parseExpression()
            token = self.tokens.actual
            if token.type != "CLOSE_PAR":
                raise ValueError("Invalid token, missing parentesis close on position {}".format(self.tokens.position))
        elif token.type == "MINUS":
            token = self.tokens.selectNext()
            result = self.parseFactor(token)
            result = UnOp("-", [result])
        elif token.type == "PLUS":
            token = self.tokens.selectNext()
            result = self.parseFactor(token)
        else:
            raise ValueError("Invalid token, expecting number or opening parentesis on position {}".format(self.tokens.position))
        return result 