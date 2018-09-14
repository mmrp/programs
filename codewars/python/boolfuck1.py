from collections import defaultdict
import sys
import argparse


__author__ = 'ipetrash'



def get_loops_block(source):
    begin_block = []
    blocks = {}
    for i, s in enumerate(source):
        if s is '[':
            begin_block.append(i)
        elif s is ']':
            b_i = begin_block.pop()  # b_i -- begin index
            blocks[i] = b_i
            blocks[b_i] = i
    return blocks


def execute(source, inp = ""):
    """
    EN:
    The function parses source code Boolfuck and execute it.
    RU:
    Функция выполняет разбор исходного кода Boolfuck и выполняет его.
    :param source: Исходный код
    :return:
    """

    i = 0  # A pointer to the row index in the code
    x = 0  # Cell index
    bf_bits = defaultdict(int)  # Dictionary, which is stored in the key index of the cell, and in the value - its value
    l = len(source)  # Number of code symbols
    loops_block = get_loops_block(source)
    bit_str = ''

    while i < l:
        s = source[i]

        if s is '>':  # Go to the next cell
            x += 1
        elif s is '<':  # Go to the previous cell
            x -= 1
        elif s is '+':  # Inverting bite in current cell
            bf_bits[x] = ~bf_bits[x] & 0b1
        elif s is ';':  # Printing the value of the current cell
            bit_str += str(bf_bits[x])
        elif s is ',':  # Enter a value in the current cell
			# TODO: operand , is not correct
            bf_bits[x] = int(input("Input = "))
        elif s is '[':  # Begin loop
            if not bf_bits[x]:  # If bf[x] == 0, then gets the index of the closing parenthesis
                i = loops_block[i]
        elif s is ']':  # End loop
            if bf_bits[x]:  # Если bf[x] != 0, then gets the index of the opening parenthesis
                i = loops_block[i]
        i += 1

    result = ''
    string_bites_byte = [bit_str[i:i+8] for i in range(0, len(bit_str), 8)]  # Splitting a string with 8 characters
    for bsb in string_bites_byte:
        bsb_be = bsb[::-1]  # Revert string. Transform to direction bits how in Big Endian
        s = chr(int(bsb_be, 2))  # Converting string with bits -> int -> char
        result += s
    print(result)

