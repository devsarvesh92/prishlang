from prish.parser import AddNode, NumberNode, PrintNode


def interpreter(ast):
    if isinstance(ast, PrintNode):
        print(ast.value)
    elif isinstance(ast, AddNode):
        left_value = interpreter(ast.left)
        right_value = interpreter(ast.right)
        return left_value + right_value
    elif isinstance(ast, NumberNode):
        return ast.value
    else:
        raise RuntimeError(f"Unknown AST node type: {type(ast)}")