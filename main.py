import math
import numpy as np
import os
import time


# Function to convert a decimal number to a binary array
def tens_to_bin(num: int):
    bits_arr = [int(i) for i in list('{0:0b}'.format(num))]
    return bits_arr


# Function to convert a binary array to a decimal number
def bin_to_tens(bits_arr: list[int]):
    res = 0
    base = 0
    for bit in reversed(bits_arr):
        res = res + bit * pow(2, base)
        base = base + 1
    return int(res)


# Function to split a bit array into subvectors
def split_bit_array_into_subvectors(bits_array: list[int], subvectors_amount: int):
    result_array = np.array_split(bits_array, subvectors_amount)
    return result_array


# Function to extend a binary array with zeros (zeros are added to beginning)
def extend_bin_with_zeros(bits_arr: list[int], zeros_amount: int):
    zeros_to_add = []
    for i in range(zeros_amount):
        zeros_to_add.append(0)
    zeros_to_add.extend(bits_arr)
    return zeros_to_add


def calculate_modular_product(a: int, b: int, p: int):
    operands_len = 6
    subvectors_amount = 2
    bits_per_subvector = operands_len/2
    a_bin = tens_to_bin(a)
    b_bin = tens_to_bin(b)

    if len(a_bin) < operands_len:
        a_bin = extend_bin_with_zeros(a_bin, operands_len - len(a_bin))

    if len(b_bin) < operands_len:
        b_bin = extend_bin_with_zeros(b_bin, operands_len - len(b_bin))

    a_subvectors = split_bit_array_into_subvectors(a_bin, subvectors_amount)
    b_subvectors = split_bit_array_into_subvectors(b_bin, subvectors_amount)

    a_subvectors.reverse()
    b_subvectors.reverse()

    result = 0
    a_index = 0
    for a_sub in a_subvectors:
        a_index = a_index + 1
        b_index = 0
        for b_sub in b_subvectors:
            b_index = b_index + 1
            pow_to_raise = (a_index + b_index - 2) * bits_per_subvector
            cons = int(pow(2, pow_to_raise))
            s_tmp = bin_to_tens(a_sub) * bin_to_tens(b_sub) * cons
            s_tmp = s_tmp % p
            result = result + s_tmp
    return result


if __name__ == '__main__':
    a = 45
    b = 15
    p = 47
    res = calculate_modular_product(a, b, p)
    print(f"{a}*{b}(mod{p}) = {a*b%p}")
    print(f"algh res = {res}")
