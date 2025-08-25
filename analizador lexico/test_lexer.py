
# test_lexer.py
from lexer import Lexer, scan, TOK

code = r"""
int suma(int a, float b) {
    // suma simple
    if (a < 10 || b >= 2.0) {
        return a + b;
    } else {
        a = a - 1;
    }
}
$
"""
tokens = scan(code)
for tok in tokens:
    print(tok)
