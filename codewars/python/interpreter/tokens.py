#!/usr/bin/python3
token_exprs = [
    (r'[ \n\t]+',  None),
    (r'#[^\n]*', None),
    (r'\(', 'LCURVE'),
    (r'\)', 'RCURVE'),
    (r'\[', 'LBRACE'),
    (r'\]', 'RBRACE'),
    (r'\+', 'PLUS'),
    (r'\-', 'MINUS'),
    (r'\*', 'MUL'),
    (r'/', 'DIV'),
    (r'[0-9]+', 'INT'),
    (r'[A-Za-z]+', 'VAR'),
]
