#!/usr/bin/python
def base64_to_base10(str):
    b64 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

    v = 0
    for c in str:
        v = v * 64 + b64.index(c)
    return v

print base64_to_base10("WIN")

