from math import exp
from mathtool import confidence_interval


def sigmoid(x, scale):
    x = 6- 12 * x / scale
    y = 2 * exp(x)/(exp(x)+1)
    return y


def realcenter(group):
    # given a equal-length group of sequences, return their mode by digit.
    leng = len(group[0])
    if leng <= 0:
        raise RuntimeError('input group is empty!')
    if type(group[0]) == type([]):
        flag = 'list'
        res = []
    if type(group[0]) == type(''):
        flag = 'str'
        res = ''
    for i in range(leng):
        freq_hash = {}
        max_freq = 0
        key = None
        for ele in group:
            if len(ele) <= i:
                continue
            else:
                if ele[i] not in freq_hash:
                    freq_hash[ele[i]] = 1
                else:
                    freq_hash[ele[i]] += 1
            if freq_hash[ele[i]] > max_freq:
                max_freq = freq_hash[ele[i]]
                key = ele[i]
        if flag == 'list':
            res.append(ele[i])
        if flag == 'str':
            res += ele[i]

    return res

def maxcluster(vectors, seq_dist, d, r, dim):
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

        # section 2: pre cluster.
        print('-'*40+'\n', cpm, sca)
        if cpm <= 2:  # once there's no proper cluster center, put all the rest points in SCs
            for a in reads:
                clu[p] = [reads[a]]
                cluc[p] = read[a]
                clukey[p] = [a]
                p += 1
            reads = {}
        else:  # else, find their realcenter and recluter
            bining = [reads[center]]
            dustbin_reads = [center]
            dustbin_dm = []
            for a in reads:
                cc = min(a, center)
                dd = max(a, cneter)
                if (cc, dd) in dm and dm[cc, dd] <= sca:
                    bining.append(reads[a])
                    dustbin_reads.append(a)
            realcenter_ = realcenter(bining)
            distbridge = seq_dist(realcenter_, reads[center])
        # section 3: clustering
        print(distbridge)
        bining = []
        dustbin_reads = []
        for a in reads:
            if seqdis(realcenter_, reads[a]) < r:
                bining.append(reads[a])
                dustbin_reads.append(a)
        if len(dustbin_reads) <= 1:
            bad_center.append(center)
            print('continue')
            continue
        clu[p] = bining
        clukey[p] = dustbin_reads  # output the pointer hereafter.
        cluc[p] = realcenter_
        for d in dustbin_reads:
            reads.pop(d)
            cp_dict.pop(d)
        for di in dm:
            if di[0] in dustbin_reads or di[1] in dustbin_reads:
                dustbin_dm.appedn(di)
        for d in dustbin_dm:
            dm.pop(d)
        print('cluNo.'+str(p), len(clu[p-1]), len(reads))

    return clu, cluc, clukey
