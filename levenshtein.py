#!/usr/bin/env python
# coding: utf-8

'''
Created: 2014-9-17
Author: niR@github (https://github.com/hentaiPanda)
Version: 0.0.1
License: MIT


This is a straightforward implementation of Levenshitein
Distance and Damerau-Levenshtein Distance.

The code is based on the examples on the Wikipedia
You can get more infomation from
http://en.wikipedia.org/wiki/Levenshtein_distance
http://en.wikipedia.org/wiki/Damerau-Levenshtein_distance
'''


# Levenshtein Distance
def lev(str1, str2):
    """Make a Levenshtein Distances Matrix"""
    n1, n2 = len(str1), len(str2)
    lev_matrix = [ [ 0 for i1 in range(n1 + 1) ] for i2 in range(n2 + 1) ]
    for i1 in range(1, n1 + 1):
        lev_matrix[0][i1] = i1
    for i2 in range(1, n2 + 1):
        lev_matrix[i2][0] = i2
    for i2 in range(1, n2 + 1):
        for i1 in range(1, n1 + 1):
            cost = 0 if str1[i1-1] == str2[i2-1] else 1
            elem = min( lev_matrix[i2-1][i1] + 1,
                        lev_matrix[i2][i1-1] + 1,
                        lev_matrix[i2-1][i1-1] + cost )
            lev_matrix[i2][i1] = elem
    return lev_matrix[-1][-1]


# Optimal string alignment distance
def osa(str1, str2):
    n1, n2 = len(str1), len(str2)
    matrix = [ [ 0 for i1 in range(n1 + 1) ] for i2 in range(n2 + 1) ]
    for i1 in range(1, n1 + 1):
        matrix[0][i1] = i1
    for i2 in range(1, n2 + 1):
        matrix[i2][0] = i2
    for i2 in range(1, n2 + 1):
        for i1 in range(1, n1 + 1):
            cost = 0 if str1[i1-1] == str2[i2-1] else 1
            elem = min( matrix[i2-1][i1] + 1,
                        matrix[i2][i1-1] + 1,
                        matrix[i2-1][i1-1] + cost )
            if (i1 > 1 and i2 > 1 and
                str1[i1-2] == str2[i2-1] and
                str1[i1-1] == str2[i2-2]):
                elem = min( elem,
                            matrix[i2-3][i1-3] + cost )
            matrix[i2][i1] = elem
    return matrix[-1][-1]


# Damerau-Levenshtein Distance
def dalev(str1, str2):
    # Suppose we have two strings 'ac' and 'cba'
    # This is the initialized matrix:
    #
    #                    str1
    #                    a c
    #              * * * * * *
    #              * 5 5 5 5 *
    #              * 5 0 1 2 *
    #            c * 5 1 5 5 *
    #      str2  b * 5 2 5 5 *
    #            a * 5 3 5 5 *
    #              * * * * * *
    #
    # If we wanna transpose 'ac' to 'ca', the starting point is (2, 2),
    # And we need to compute the distance, so we must start at the point
    # (1, 1), that's where the number 0 is, and it's the initial position
    # of (p2-1, p1-1).
    # The reason we use p2=ORIGIN, p1=ORIGIN (here ORIGIN is 1) as the
    # initial value is that we must ensure if we don't have the proper
    # pair of strings ('abc' and 'ga' etc.), the distance with adjacent
    # transposition is always bigger than the number of other edit operations
    # ( because no matter which variable (p2 or p1) is 0, matrix[p2-1][p1-1]
    # is always the biggest number, here it is 5).
    # (i1-p1-1) / (i2-p2-1) is the edit distance of the substrings.
    n1, n2 = len(str1), len(str2)
    max_dis = n1 + n2
    letters = {} # pointer of the last row where a[i] == b[j]
    INIT_POS = 2 # initial position of two str ('some'[0] etc.) in the matrix
    ORIGIN = INIT_POS - 1 # the position of '0' in the matrix
    matrix = [ [ max_dis for i1 in range(n1 + INIT_POS) ]
               for i2 in range(n2 + INIT_POS) ]
    for i1 in range(ORIGIN, n1 + INIT_POS):
        matrix[1][i1] = i1 -ORIGIN
    for i2 in range(ORIGIN, n2 + INIT_POS):
        matrix[i2][1] = i2 -ORIGIN
    for i2 in range(INIT_POS, n2 + INIT_POS):
        temp = ORIGIN # pointer of the last column where b[j] == a[i]
        for i1 in range(INIT_POS, n1 + INIT_POS):
            p2 = letters.get(str1[i1-INIT_POS], ORIGIN)
            p1 = temp
            cost = 0 if str1[i1-INIT_POS] == str2[i2-INIT_POS] else 1
            if not cost:
                temp = i1
            elem = min( matrix[i2-1][i1] + 1,
                        matrix[i2][i1-1] + 1,
                        matrix[i2-1][i1-1] + cost,
                        matrix[p2-1][p1-1] + 1 + (i1-p1-1) + (i2-p2-1) )
            matrix[i2][i1] = elem
        letters[str2[i2-INIT_POS]] = i2
    return matrix[-1][-1]

