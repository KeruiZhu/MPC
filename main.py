"""Maximize The Point Counts
Usage: python3 <script> <input.vectors> <input.accuracy> <cutoff>
"""
import os
import sys
import mpc_lib as f
import mathtool as mt
import multiproc_dismat as md
from mpc_max import maxcluster


vfn, afn, r = sys.argv[1:]

filename = vfn.split('.')[0]
r = float(r)

vectors = f.vectorreader(vnf)
dim = len(vectors[0))
accuracy = f.accuracyreader(afn)
d = md.mp_dismat(vectors)

c, cc, ck = maxcluster(vectors, d, r, dim)

del d

raw_cluster = len(ck)

mark = []
for ci in c:
    if len(c[ci]) > 4:
        mark.append(ci)

sc = []
sck = []
dustbin = []
for ci in c:
    if c not in mark:
        sc.append(c[ci])
        sck.append(ck[ci])
        dustbin.append(ci)

for ds in dustbin:
	c.pop(ds)
	cc.pop(ds)
	ck.pop(ds)

for p in c:
	d_list = mt.dist_list(c[p], cc[p], dim, r)
	n = len(c[p])
	mean_ = mt.mean(d_list, n)
	stdvar_ = mt.std_var(d_list, mean_, n)
	var_ = stdvar_ ** 2
	q = mt.q_value(r, mean_, var_)
	tor = round(len(c[p])*q)
	if tor >= 1:
		belongs, bk, sc, sck = f.scsortncut(dim, cc[p], sc, sck, tor, mean_, stdvar_)
		c[p] = c[p] + belongs
		ck[p] = ck[p] + bk

if len(sc) > 0:
	for i in range(len(sc)):
		c[raw_cluster+i] = sc[i][:]
		cc[raw_cluster+i] = sc[i][:]
		ck[raw_cluster+i] = sck[i][:]

# write report
with open('report.txt') as report:
    p = 1
    for i in ck:
        report.write('cluster{0}:\n{1}\n'.format(p, ck[i]))
        p += 1

