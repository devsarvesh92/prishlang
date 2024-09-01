
from prish.parser import parser
from prish.lexer import lexer
from prish.interpreter import interpreter


def execute_code(*, text: str):
    tokens = lexer(code=text)
    ast = parser(tokens=tokens)
    result = interpreter(ast=ast)
    if result:
        print(result)


def repl():
    print("Welcome to PrishLang! Type 'exit' to quit!")
    while True:
        try:
            text = input("prish> ")
            if text.lower() == "exit":
                break
            execute_code(text=text)
        except Exception:
            pass


def main():
    repl()


if __name__ == "__main__":
    main()
