# exe('/u/billl/nrniv/CA3/test.py')
from neuron import h

def mechdict (sec=None, name='soma', type=0):
    '''MechanismType types are 0 for SUFFFIX; 1 for PP; replace with psec in wlutils.py'''
    mt, mstr, tstr, mdv = h.MechanismType(type), h.ref(''), h.ref(''), {}
    for i in range(mt.count()): 
        mt.select(i)
        mt.selected(tstr)
        ms=h.MechanismStandard(tstr[0], 1) # have to recreate each time
        if sec.has_membrane(tstr[0]):
            if ms.count()>0: mdv[tstr[0]]={}
            for j in range(ms.count()): 
                sz = ms.name(mstr, j) # sz>1 if nseg>1 for this sec
                val = ms.get(mstr)
                mdv[tstr[0]][mstr[0]] = val
    return mdv

# manually curated mechlist() output to just get currents -- could do by identifying ones with parameters
currs = ['hcurrent', 'kacurrent', 'kdrcurrent', 'nacurrent', 'cagk', 'Caolmw', 'capr', 'HCN1', 'HCN2', 'IA', 'ICaolmw', 'icapr', 'IhOlmKop', 'Iholmw', 'IhPyrKop', 'ihstatic',
         'kahppr', 'KaOlmKop', 'KaPyrKop', 'KCaolmw', 'kcpr', 'Kdrbwb', 'KdrOlmKop', 'kdrpr', 'KdrPyrKop', 'km', 'Nafbwb', 'NafOlmKop', 'nafpr', 'NafPyrKop', 'pas', 'fastpas', 'hh']

def setpyr0 ():
    global tydi, mohf, neef, pyr0, bas0, olm0
    tydi = {k:eval(k) for k in ['PYR','BAS','OLM']}
    try: 
        pyr0, bas0, olm0 = [net.cells[i].cell[0].soma for i in tydi.values()]    # ca3cann
        mohf, neef = True, False
    except NameError: 
        pyr0, bas0, olm0 = [sim.net.cells[sim.net.pops[x].cellGids[0]].secs.soma.hObj for x in tydi.keys()]
        mohf, neef = False, True
    except Exception:
        print("Can't figure out how to set pyr0, bas0, olm0")
    return

#setpyr0()

def mechvars (bas0):
    miln = [x for x in currs if h.ismembrane(x, sec=bas0)]
    return [(y,x) for y in dir(bas0(0.5).__getattribute__(x)) for x in miln if not re.search('__|name|ion',y)]

def trnetcons ():
    global ncl, tdi, tdf
    global ncwns, tya, asy
    ncl=h.List("NetCon")  # all netcons
    ncwns=[x for x in ncl if x.pre()] # these are all the NetCons with a NetStim
    if neef: 
        tya = [x.postcell().tags['cellType'] for x in ncwns] # specific to netpyne
    else:    
        tya = [(lambda x: 'PYR' if 'Py' in x else 'OLM' if 'Ow' in x else 'BAS')(str(y.postcell())) for y in ncwns]
    tdi = {}
    asy = [(lambda x: 'NMDA' if 'NMDA' in str(x) else 'AMPA' if x.e==0. else 'GABA')(y.syn()) for y in ncwns]
    tdi['all'] = {'ns':ncwns, 'ty':tya, 'syn': asy, 'wt': [w.weight[0] for w in ncwns]}
    tdf = pd.DataFrame(tdi['all'])
    for k in tydi.keys(): tdi[k] = tdf.query('ty == "%s"'%k).to_dict('list')
    print([len(ncl), len(ncwns), len(tya)])

def identcell (ce):
    try:
        return ce.tags['cellType']
    except:
        sce = str(ce)
        return "PYR" if "Pyr" in sce else "BAS" if "PVC" in sce else "OLM" if "Ow" in sce else "NIL"

def prpo ():
    for pr in ["PYR", "BAS", "OLM"]: 
        for po in ["PYR", "BAS", "OLM"]: 
            print(pr, po, len([x for x in ncl if identcell(x.precell()) is pr and identcell(x.postcell()) is po]))
