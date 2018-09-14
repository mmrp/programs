#!/usr/bin/python3
import tokens
import re

def lex(text, token_exprs):
    pos = 0
    tokens = []
    while pos < len(text):
        for token_expr in token_exprs:
            expr,tag = token_expr
            match = re.match(expr, text[pos:])
            if match:
                if tag: tokens.append((match.group(0), tag))
                pos += match.end()
                break
        else:
            raise Exception('Invalid input')
    return tokens
if __name__ == '__main__':
    print(lex(raw_input(), tokens.token_exprs))

        
