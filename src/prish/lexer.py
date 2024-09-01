import decimal
import re
from typing import Any


class Token:
    def __init__(self, type: str, value: Any) -> None:
        self.type = type
        self.value = value


def lexer(code):
    token_specification = [
        ("NUMBER", r"\d+(\.\d*)?"),
        ("PLUS", r"\+"),
        ("PRINT", r"print"),
        ("STRING", r'"[^"]*"'),
        ("ID", r"[A-Za-z_]\w*"),
        ("NEWLINE", r"\n"),
        ("SKIP", r"[ \t]+"),
        ("MISMATCH", r"."),
    ]
    token_pipeline = "|".join(
        [f"(?P<{group_name}>{expr})" for group_name, expr in token_specification]
    )
    tokens = []
    for match in re.finditer(token_pipeline, code):
        kind = match.lastgroup
        value = match.group()
        match kind:
            case "NUMBER":
                value = decimal.Decimal(str(value))
            case "SKIP" | "NEWLINE":
                continue
        tokens.append(Token(type=kind, value=value))
    return tokens