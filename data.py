import pickle

with open('/home/jchen/CompNeuro/myKnoxRepo/data/sim.pkl', 'rb') as fp:
    nppkl = pickle.load( fp )

np = {}
pyv = {}
inv = {}
tcv = {}
rev = {}

pyv['bound'] = [x for x in nppkl['simData']['V_soma']['cell_0']]
pyv['mid']   = [x for x in nppkl['simData']['V_soma']['cell_49']]

inv['bound'] = [x for x in nppkl['simData']['V_soma']['cell_100']]
inv['mid']   = [x for x in nppkl['simData']['V_soma']['cell_149']]

tcv['bound'] = [x for x in nppkl['simData']['V_soma']['cell_300']]
tcv['mid']   = [x for x in nppkl['simData']['V_soma']['cell_349']]

rev['bound'] = [x for x in nppkl['simData']['V_soma']['cell_400']]
rev['mid']   = [x for x in nppkl['simData']['V_soma']['cell_449']]

np['pyv'] = pyv
np['inv'] = inv
np['tcv'] = tcv
np['rev'] = rev

np['spkt'] = nppkl['simData']['spkt']
np['spkid'] = nppkl['simData']['spkid']

with open('/home/jchen/CompNeuro/shared/np.pkl', 'wb') as fp:
    pickle.dump(np, fp)

print('pkl files created')