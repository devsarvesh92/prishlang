class ASTNode:
    pass

class PrintNode(ASTNode):
    def __init__(self, value):
        self.value = value

class AddNode(ASTNode):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value

def parser(tokens):
    tokens = list(tokens)
    if tokens[0].type == 'PRINT':
        if len(tokens) != 2 or tokens[1].type != 'STRING':
            raise SyntaxError("Invalid syntax for print. Expected 'print \"message\"'")
        return PrintNode(tokens[1].value.strip('"'))
    elif len(tokens) == 3 and tokens[1].type == 'PLUS':
        if tokens[0].type != 'NUMBER' or tokens[2].type != 'NUMBER':
            raise SyntaxError("Invalid syntax for addition. Expected 'number + number'")
        return AddNode(NumberNode(tokens[0].value), NumberNode(tokens[2].value))
    else:
        raise SyntaxError("Invalid syntax")