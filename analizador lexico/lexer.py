
# lexer.py
import re
from dataclasses import dataclass
from typing import Iterator

# Códigos según la tabla del PDF:
TOK = {
    "IDENT": 0,
    "ENTERO": 1,
    "REAL": 2,
    "CADENA": 3,
    "TIPO": 4,            # int, float, void
    "OPSUMA": 5,          # + -
    "OPMUL": 6,           # * /
    "OPRELAC": 7,         # < <= > >=
    "OPOR": 8,            # ||
    "OPAND": 9,           # &&
    "OPNOT": 10,          # !
    "OPIGUALDAD": 11,     # == !=
    "PUNTOYCOMA": 12,     # ;
    "COMA": 13,           # ,
    "LPAREN": 14,         # (
    "RPAREN": 15,         # )
    "LBRACE": 16,         # {
    "RBRACE": 17,         # }
    "ASIGN": 18,          # =
    "IF": 19,
    "WHILE": 20,
    "RETURN": 21,
    "ELSE": 22,
    "EOF": 23,            # $
}

RESERVED_TO_CODE = {
    "if": TOK["IF"],
    "while": TOK["WHILE"],
    "return": TOK["RETURN"],
    "else": TOK["ELSE"],
    "int": TOK["TIPO"],
    "float": TOK["TIPO"],
    "void": TOK["TIPO"],
}

token_spec = [
    ("WHITESPACE", r"[ \t\r\f]+"),
    ("NEWLINE",    r"\n"),
    ("COMMENT1",   r"//[^\n]*"),
    ("COMMENT2",   r"/\*[^*]*\*+(?:[^/*][^*]*\*+)*/"),
    ("OPOR",       r"\|\|"),
    ("OPAND",      r"&&"),
    ("OPIGEQ",     r"=="),
    ("OPNOTEQ",    r"!="),
    ("OPLE",       r"<="),
    ("OPGE",       r">="),
    ("PLUS",       r"\+"),
    ("MINUS",      r"-"),
    ("STAR",       r"\*"),
    ("SLASH",      r"/"),
    ("LT",         r"<"),
    ("GT",         r">"),
    ("BANG",       r"!"),
    ("ASSIGN",     r"="),
    ("SEMI",       r";"),
    ("COMMA",      r","),
    ("LPAREN",     r"\("),
    ("RPAREN",     r"\)"),
    ("LBRACE",     r"\{"),
    ("RBRACE",     r"\}"),
    ("REAL",       r"(?:\d+\.\d+)"),
    ("ENTERO",     r"(?:\d+)"),
    ("CADENA",     r"""(?:"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')"""),
    ("IDENT",      r"[A-Za-z_][A-Za-z_0-9]*"),
    ("EOF",        r"\$"),
]

master_pat = re.compile("|".join(f"(?P<{name}>{pat})" for name, pat in token_spec))

@dataclass
class Token:
    tipo: int
    lexema: str
    linea: int
    columna: int

    def __repr__(self):
        return f"Token(tipo={self.tipo}, lexema={self.lexema!r}, linea={self.linea}, columna={self.columna})"

class LexerError(Exception):
    pass

class Lexer:
    def __init__(self, texto: str):
        self.texto = texto

    def tokens(self) -> Iterator[Token]:
        text = self.texto
        pos = 0
        linea = 1
        col = 1
        length = len(text)

        while pos < length:
            m = master_pat.match(text, pos)
            if not m:
                snippet = text[pos:pos+20]
                raise LexerError(f"Carácter inesperado {text[pos]!r} en línea {linea}, columna {col}. Cerca de: {snippet!r}")
            kind = m.lastgroup
            lex = m.group(kind)
            start_line, start_col = linea, col

            pos = m.end()
            newlines = lex.count("\n")
            if newlines:
                linea += newlines
                col = len(lex.rsplit("\\n", 1)[-1]) + 1
            else:
                col += len(lex)

            if kind in ("WHITESPACE", "COMMENT1", "COMMENT2", "NEWLINE"):
                continue

            # Mapeo a códigos finales
            if kind == "IDENT":
                low = lex.lower()
                code = RESERVED_TO_CODE.get(low, TOK["IDENT"])
                yield Token(code, lex, start_line, start_col)
            elif kind == "ENTERO":
                yield Token(TOK["ENTERO"], lex, start_line, start_col)
            elif kind == "REAL":
                yield Token(TOK["REAL"], lex, start_line, start_col)
            elif kind == "CADENA":
                yield Token(TOK["CADENA"], lex, start_line, start_col)
            elif kind == "OPOR":
                yield Token(TOK["OPOR"], lex, start_line, start_col)
            elif kind == "OPAND":
                yield Token(TOK["OPAND"], lex, start_line, start_col)
            elif kind in ("OPIGEQ", "OPNOTEQ"):
                yield Token(TOK["OPIGUALDAD"], lex, start_line, start_col)
            elif kind in ("OPLE", "OPGE", "LT", "GT"):
                yield Token(TOK["OPRELAC"], lex, start_line, start_col)
            elif kind in ("PLUS", "MINUS"):
                yield Token(TOK["OPSUMA"], lex, start_line, start_col)
            elif kind in ("STAR", "SLASH"):
                yield Token(TOK["OPMUL"], lex, start_line, start_col)
            elif kind == "BANG":
                yield Token(TOK["OPNOT"], lex, start_line, start_col)
            elif kind == "ASSIGN":
                yield Token(TOK["ASIGN"], lex, start_line, start_col)
            elif kind == "SEMI":
                yield Token(TOK["PUNTOYCOMA"], lex, start_line, start_col)
            elif kind == "COMMA":
                yield Token(TOK["COMA"], lex, start_line, start_col)
            elif kind == "LPAREN":
                yield Token(TOK["LPAREN"], lex, start_line, start_col)
            elif kind == "RPAREN":
                yield Token(TOK["RPAREN"], lex, start_line, start_col)
            elif kind == "LBRACE":
                yield Token(TOK["LBRACE"], lex, start_line, start_col)
            elif kind == "RBRACE":
                yield Token(TOK["RBRACE"], lex, start_line, start_col)
            elif kind == "EOF":
                yield Token(TOK["EOF"], lex, start_line, start_col)
            else:
                raise LexerError(f"Clase de token no manejada: {kind}")

def scan(texto: str):
    return list(Lexer(texto).tokens())

if __name__ == "__main__":
    demo = r"""
    int a = 3 + 4.5;
    float b = a >= 3; // comentario
    if (a >= 3 && b != 0) {
        return a + b;
    } else {
        while (a > 0) { a = a - 1; }
    }
    "hola mundo"
    'cadena con comillas simples'
    $
    """
    for t in scan(demo):
        print(t)
