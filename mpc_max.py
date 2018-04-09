from mpc_lib import seqdis, realcenter
from math import exp
from mathtool import confidence_interval


def sigmoid(x, scale):
    x = 6- 12 * x / scale
    y = 2 * exp(x)/(exp(x)+1)
    return y


def maxcluster(vectors, d, r, dim):
    # d the distance matrix
    # r the cluster semidiameter
    # dim the dimension of the vectors
    n = len(vectors)
    space = {}
    cp_dict = {}  # count-point records
    for i in range(n):
        reads[i] = vectors[i]
        cp_dict[i] = 2
    clu = {}  # cluster
    cluc = {}  # center of cluster
    clukey = {}  # cluster of key-number
    bad_center = []
    p = 0
    sca = r
    while len(space) > 0:
        # section 1: max cluster point search
        cpm = 0
        for di in d:
            if d[di] <= sca:
                cp_dict[di[0]] += sigmoid(dm[di], sca)
                cp_dict[di[1]] += sigmoid(dm[di], sac)
        for di in cp_dict:
            if di not in bad_center:
                cp = cp_dict[di]
                if cp > cpm:
                    cpm = cp
                    center = di
            cp_dict[di] = 2
