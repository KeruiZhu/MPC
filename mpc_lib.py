import math
import mathtool as mt


def seqdis(seq1, seq2, dim, cutoff):
    # the function to calculate absolute distance between two given vectors
    # dim the vectors' dimension
    d = 0
    tol = cutoff ** 2
    for i in range(dim):
        d = d + (seq1[i] - seq2[i]) ** 2
        if d > tol:
            return math.sqrt(d)

    return math.sqrt(d)


def realcenter(v_list):

    return newcenter


def scsortncut():

    return belongs, bk, sc, sck
