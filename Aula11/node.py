from symbolTable import SymbolTable

class Node():
    def __init__(self, value, children):
        self.value = value
        self.children = children
    def Evaluate(self, SymbolTable):
        pass


class BinOp(Node):
    def Evaluate(self, SymbolTable):
        value1 = self.children[0].Evaluate(SymbolTable)
        value2 = self.children[1].Evaluate(SymbolTable)
        if (self.value == "+"):
            return value1 + value2
        elif (self.value == "-"):
            return value1 - value2
        elif (self.value == "*"):
            return value1 * value2
        elif (self.value == "/"):
            return value1 // value2
        elif (self.value == ":="):
            SymbolTable.setSymbol(value1, value2)
        else:
            #tratar erro
            return

class UnOp(Node):
    def Evaluate(self, SymbolTable):
        value = self.children[0].Evaluate(SymbolTable)
        if (self.value == "-"):
            return value * -1
        else:
            #tratar erro
            return

class StrVal(Node):
    def Evaluate(self, SymbolTable):
        return self.value
        
class IntVal(Node):
    def Evaluate(self, SymbolTable):
        return int(self.value)

class Identifier(Node):
    def Evaluate(self, SymbolTable):
        return SymbolTable.getSymbol(self.value)

class NoOp(Node):
    def Evaluate(self, SymbolTable):
        return None

class Statements(Node):
    def Evaluate(self, SymbolTable):
        for child in self.children:
            child.Evaluate(SymbolTable)

class Print(Node):
    def Evaluate(self, SymbolTable):
        value = self.children[0].Evaluate(SymbolTable)
        print(value)
