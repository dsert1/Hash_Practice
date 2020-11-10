#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author Deniz Sert
# @version September 18, 2020

PRIME = 2 ** 31 - 1


def search_lyrics(L, Q):
    """
    Input: L | an ASCII string
    Input: Q | an ASCII string where |Q| < |L|

    Return `True` if Q appears inside the lyrics L and `False` otherwise.
    """

    #################
    # f = (128 ** len(Q)) % PRIME
    f = 1

    for i in range(len(Q)):
        f *= 128
        f = f % PRIME

    L_hashed = R(L[0:len(Q)])
    Q_hashed = R(Q)
    for i in range(len(L)-len(Q)):
        # keep applying R until match. then break
        # print('i, L[i]', (i, L[i]))
        # # print('Q: ', R(Q))
        # print('hash', cur_hash)
        if L_hashed == Q_hashed:
            if L[i:i+len(Q)] == Q:
                return True
        L_hashed = R_constant_time(L, i, Q, L_hashed, f)
        print(L_hashed)
    return False

    # print(R_constant_time(L, 80, 'what '))
    # print(R('pizza'))
    

def R_constant_time(L,i,Q, prev_hash, f):
    '''Hashing function with modulo.
....Input: x | an ASCII
....Return: A hashed version of x
....'''

    return ((prev_hash * 128) % PRIME - (f * ord(L[i])) % PRIME + ord((L[i + len(Q)])) % PRIME) % PRIME


def R(s):
    '''Hashes any ASCII'''

    total = 0
    counter = 1
    for i in range(1, len(s)+1):
        total += ord(s[-i]) * counter
        counter *= 128
    return total % PRIME
