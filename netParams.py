"""
netParams.py 

netParams is a dict containing a set of network parameters using a standardized structure

simConfig is a dict containing a set of simulation configurations using a standardized structure

refs:
Destexhe, A., Contreras, D., & Steriade, M. (1998). Mechanisms underlying the 
synchronizing action of corticothalamic feedback through inhibition of thalamic 
relay cells. Journal of neurophysiology, 79(2), 999-1016.

Destexhe, A. (1998). Spike-and-wave oscillations based on the properties of 
GABAB receptors. Journal of Neuroscience, 18(21), 9099-9111.


Contributors: xxx@xxxx.com
"""

from netpyne import specs
from netpyne import sim

netParams = specs.NetParams()   # object of class NetParams to store the network parameters


import random as rnd
import numpy as np

import json
from settings import nav_type, drug, dose

def smallWorldConn(NPre, NPost, p, K, selfConn=True):
    ''' k is smallwordness parameters
    K is ratio of connections from each pre cell to post cells
    if p=0 regular network
    if p between 0 and 1 small-world network and
    if p=1 random network 
    '''
    connMat=[]
    for i in range(NPre):
        for j in np.arange(i-int(np.ceil(NPost*K/2)),i+int(np.ceil(NPost*K/2))+1): # line-like neighborhood
            jbound = j
            if jbound < 0: jbound = abs(j) - 1
            if jbound > NPost-1: jbound = 2 * NPost - jbound - 1 
            #if (jbound >= 0 and jbound <= NPost-1):
            if i!=jbound or selfConn:
                connMat.append([i,jbound])
            
    if p:
        connects = [x for x in range(len(connMat))]
        rnd_ind = rnd.sample(connects, int(len(connMat)*p))
        for i in rnd_ind:
            connMat[i][1]=rnd.randint(0,NPost-1)
    return connMat

def smallWorldConnL(NPre, NPost, p, K):
    ''' k is smallwordness parameters
    K is ratio of connections from each pre cell to post cells
    if p=0 regular network
    if p between 0 and 1 small-world network and
    if p=1 random network 
    '''
    connMat=[]
    for i in range(NPre):
        #for j in np.arange(-1*int(np.ceil(NPost*K/2)),int(np.ceil(NPost*K/2))+1): # ring-like neighborhood
            #connMat.append([i,(NPost + i + j) % NPost]) # ring like
        for j in np.arange(i-0*int(np.ceil(NPost*K/2)),i+0*int(np.ceil(NPost*K/2))+1): # line-like neighborhood
            jbound = j
            #if jbound < 0: jbound = abs(j) - 1
            #if jbound > NPost-1: jbound = 2 * NPost - jbound - 1 
            if (jbound >= 0 and jbound <= NPost-1):
                connMat.append([i,jbound])
            
    if p:
        connects = [x for x in range(len(connMat))]
        rnd_ind = rnd.sample(connects, int(len(connMat)*p))
        for i in rnd_ind:
            connMat[i][1]=rnd.randint(0,NPost-1)
    return connMat

def RegularConn2005(NPre, NPost):
    ''' 
        trying a 1-1 connection, from NPre[i] to NPost[i+100] and vice versa	
    '''
    connMat=[]
    mid=int(NPost/2)
    for i in range(mid):
        connMat.append([i,mid+i])
        connMat.append([mid+i,i])
    return connMat

def printWeight():
    # intra-cortical
    print("PYPY-AMPA_weight = ", netParams.connParams['PY->PY_AMPA']['weight'])
    print("PYIN-AMPA_weight = ", netParams.connParams['PY->IN_AMPA']['weight'])
    print("ININ-GABAA_weight = ", netParams.connParams['IN->IN_GABAA']['weight'])
    print("INPY-GABAA_weight = ", netParams.connParams['IN->PY_GABAA']['weight'])
    print("INPY-GABAB_weight = ", netParams.synMechParams['GABAB_S1']['gmax'])
    #print("INPY-GABAB_weight = ", netParams.connParams['IN->PY_GABAB']['weight'])
    
    # intra-thalamic
    print("TCRE-AMPA_weight = ", netParams.connParams['TC->RE']['weight'])
    print("RETC-GABAA_weight = ", netParams.connParams['RE->TC_GABAA']['weight'])
    print("RETC-GABAB_weight = ", netParams.synMechParams['GABAB_S2']['gmax'])
    #print("RETC-GABAB_weight = ", netParams.connParams['RE->TC_GABAB']['weight'])
    print("RERE-GABAA_weight = ", netParams.connParams['RE->RE']['weight'])
    
    # thalamo-cortical 
    print("PYTC-AMPA_weight = ", netParams.connParams['PY->TC']['weight'])
    print("PYRE-AMPA_weight = ", netParams.connParams['PY->RE']['weight'])
    print("TCPY-AMPA_weight = ", netParams.connParams['TC->PY']['weight'])
    print("TCIN-AMPA_weight = ", netParams.connParams['TC->IN']['weight'])

def printPYinfo(cellParams):
    print(" ")
    print("------ PY Parameter values ---------")
    print(" ")
    
    print("diam=",cellParams.secs.soma.geom.diam,"\t L=",cellParams.secs.soma.geom.L," \t Cm=",cellParams.secs.soma.geom.cm," \t Ra=",cellParams.secs.soma.geom.Ra)
    print("g_pas=",cellParams.secs.soma.mechs.pas.g," \t e_pas=",cellParams.secs.soma.mechs.pas.e," \t vinit=", cellParams.secs.soma.vinit)
    print("gnabar_hh2=",cellParams.secs.soma.mechs.hh2.gnabar," \t ena=", cellParams.secs.soma.ions.na.e)
    print("gkbar_hh2=",cellParams.secs.soma.mechs.hh2.gkbar," \t ek=",cellParams.secs.soma.ions.k.e," \t vtraub_hh2=", cellParams.secs.soma.mechs.hh2.vtraub)
    print("gkbar_im=",cellParams.secs.soma.mechs.im.gkbar," \t taumax_im=",cellParams.secs.soma.mechs.im.taumax)
    
    print(" ")
    print("-------- PY Parameter values (end) --------")
    print(" ")

def printINinfo(cellParams):
    print(" ")
    print("------ IN Parameter values ---------")
    print(" ")
    
    print("diam=",cellParams.secs.soma.geom.diam,"\t L=",cellParams.secs.soma.geom.L," \t Cm=",cellParams.secs.soma.geom.cm," \t Ra=",cellParams.secs.soma.geom.Ra)
    print("g_pas=",cellParams.secs.soma.mechs.pas.g," \t e_pas=",cellParams.secs.soma.mechs.pas.e," \t vinit=", cellParams.secs.soma.vinit)
    print("ena=", cellParams.secs.soma.ions.na.e," \t ek=",cellParams.secs.soma.ions.k.e)
    print("svhalf_inak2005mut=",cellParams.secs.soma.mechs.inak2005mut.svhalf, "\t sk_inak2005mut=",cellParams.secs.soma.mechs.inak2005mut.sk," \t staubase_inak2005mut=", cellParams.secs.soma.mechs.inak2005mut.staubase)
    
    print("mvhalf_inak2005mut=",cellParams.secs.soma.mechs.inak2005mut.mvhalf, "\t mk_inak2005mut=",cellParams.secs.soma.mechs.inak2005mut.mk," \t mtaubase_inak2005mut=", cellParams.secs.soma.mechs.inak2005mut.mtaubase)
    print("hvhalf_inak2005mut=",cellParams.secs.soma.mechs.inak2005mut.hvhalf, "\t hk_inak2005mut=",cellParams.secs.soma.mechs.inak2005mut.hk," \t htaubase_inak2005mut=", cellParams.secs.soma.mechs.inak2005mut.htaubase)
    print("htauvhalf_inak2005mut=",cellParams.secs.soma.mechs.inak2005mut.htauvhalf, "\t htauk_inak2005mut=",cellParams.secs.soma.mechs.inak2005mut.htauk)
    print("stauvhalf_inak2005mut=",cellParams.secs.soma.mechs.inak2005mut.stauvhalf, "\t stauk_inak2005mut=",cellParams.secs.soma.mechs.inak2005mut.stauk)
    print("gnatbar_inak2005mut=",cellParams.secs.soma.mechs.inak2005mut.gnatbar, "\t gkfbar_inak2005mut=",cellParams.secs.soma.mechs.inak2005mut.gkfbar)

    print("gnablock_inak2005mut=",cellParams.secs.soma.mechs.inak2005mut.gnablock, "\t hshift_inak2005mut=",cellParams.secs.soma.mechs.inak2005mut.hshift)
    print("htaubase_inak2005mut=",cellParams.secs.soma.mechs.inak2005mut.htaubase, "\t staubase_inak2005mut=",cellParams.secs.soma.mechs.inak2005mut.staubase, "\t sshift_inak2005mut=",cellParams.secs.soma.mechs.inak2005mut.sshift)
    print("gnablock_inak2005=",cellParams.secs.soma.mechs.inak2005.gnablock, "\t hshift_inak2005=",cellParams.secs.soma.mechs.inak2005.hshift)
    print("htaubase_inak2005=",cellParams.secs.soma.mechs.inak2005.htaubase, "\t staubase_inak2005=",cellParams.secs.soma.mechs.inak2005.staubase, "\t sshift_inak2005=",cellParams.secs.soma.mechs.inak2005.sshift)


    print(" ")
    print("-------- IN Parameter values (end) --------")
    print(" ")

def printTCinfo(cellParams):
    print(" ")
    print("----- TC Parameter values -------")
    print(" ")
    
    print("diam=",cellParams.secs.soma.geom.diam,"\t L=",cellParams.secs.soma.geom.L," \t Cm=",cellParams.secs.soma.geom.cm," \t Ra=",cellParams.secs.soma.geom.Ra)
    print("kl_gmax=",cellParams.secs.soma.pointps.kleak_0.gmax,"\t Erev_kleak=",cellParams.secs.soma.pointps.kleak_0.Erev_kleak)
    print("g_pas=",cellParams.secs.soma.mechs.pas.g," \t e_pas=",cellParams.secs.soma.mechs.pas.e," \t vinit=", cellParams.secs.soma.vinit)
    print("gnabar_hh2=",cellParams.secs.soma.mechs.hh2.gnabar," \t ena=", cellParams.secs.soma.ions.na.e)
    print("gkbar_hh2=",cellParams.secs.soma.mechs.hh2.gkbar," \t ek=",cellParams.secs.soma.ions.k.e," \t vtraub_hh2=", cellParams.secs.soma.mechs.hh2.vtraub)
    print("gcabar_it=",cellParams.secs.soma.mechs.it.gcabar," \t eca=",cellParams.secs.soma.ions.ca.e," \t cai=", cellParams.secs.soma.ions.ca.i," \t cao=", cellParams.secs.soma.ions.ca.o)
    print("shift_it=",cellParams.secs.soma.mechs.it.shift," \t taubase_it=",cellParams.secs.soma.mechs.it.taubase)
    print("depth_cad=",cellParams.secs.soma.mechs.cad.depth," \t taur_cad=",cellParams.secs.soma.mechs.cad.taur," \t cainf_cad=", cellParams.secs.soma.mechs.cad.cainf," \t kt_cad=", cellParams.secs.soma.mechs.cad.kt)
    print("ghbar_iar=",cellParams.secs.soma.mechs.iar.ghbar," \t eh=",cellParams.secs.soma.ions.h.e," \t nca_iar=", cellParams.secs.soma.mechs.iar.nca," \t k2_iar=", cellParams.secs.soma.mechs.iar.k2)
    print("cac_iar=",cellParams.secs.soma.mechs.iar.cac," \t nexp_iar=",cellParams.secs.soma.mechs.iar.nexp," \t k4_iar=", cellParams.secs.soma.mechs.iar.k4," \t Pc_iar=", cellParams.secs.soma.mechs.iar.Pc," \t ginc_iar=", cellParams.secs.soma.mechs.iar.ginc)

    print(" ")
    print("----- TC Parameter values (end) -------")
    print(" ")


def printREinfo(cellParams):
    print(" ")
    print("------ RE Parameter values ---------")
    print(" ")
    
    print("diam=",cellParams.secs.soma.geom.diam,"\t L=",cellParams.secs.soma.geom.L," \t Cm=",cellParams.secs.soma.geom.cm," \t Ra=",cellParams.secs.soma.geom.Ra)
    print("g_pas=",cellParams.secs.soma.mechs.pas.g," \t e_pas=",cellParams.secs.soma.mechs.pas.e," \t vinit=", cellParams.secs.soma.vinit)
    print("gnabar_hh2=",cellParams.secs.soma.mechs.hh2.gnabar," \t ena=", cellParams.secs.soma.ions.na.e)
    print("gkbar_hh2=",cellParams.secs.soma.mechs.hh2.gkbar," \t ek=",cellParams.secs.soma.ions.k.e," \t vtraub_hh2=", cellParams.secs.soma.mechs.hh2.vtraub)
    print("gcabar_it2=",cellParams.secs.soma.mechs.it2.gcabar," \t eca=",cellParams.secs.soma.ions.ca.e," \t cai=", cellParams.secs.soma.ions.ca.i," \t cao=", cellParams.secs.soma.ions.ca.o)
    print("shift_it2=",cellParams.secs.soma.mechs.it2.shift," \t taubase_it2=",cellParams.secs.soma.mechs.it2.taubase," \t qm_it2=", cellParams.secs.soma.mechs.it2.qm," \t qh_it2=", cellParams.secs.soma.mechs.it2.qh)
    print("depth_cad=",cellParams.secs.soma.mechs.cad.depth," \t taur_cad=",cellParams.secs.soma.mechs.cad.taur," \t cainf_cad=", cellParams.secs.soma.mechs.cad.cainf," \t kt_cad=", cellParams.secs.soma.mechs.cad.kt)
    
    print(" ")
    print("-------- RE Parameter values (end) --------")
    print(" ")


###############################################################################
#
# MPI HH TUTORIAL PARAMS
#
###############################################################################

p=0*1.0; pCrx=p; pThl=p; pThlCrx=p # small-world-ness param
#K=0.1 # connectivity param

intraCrxProb=0.1
PY_PY_AMPA_Prob=intraCrxProb;PY_IN_AMPA_Prob=intraCrxProb;
PY_PY_NMDA_Prob=intraCrxProb;PY_IN_NMDA_Prob=intraCrxProb;
IN_PY_GABAA_Prob=intraCrxProb;IN_PY_GABAB_Prob=intraCrxProb;
IN_IN_GABAA_Prob=intraCrxProb;

intraThlProb=0.1
TC_RE_AMPA_Prob=intraThlProb;RE_TC_GABAA_Prob=intraThlProb;
RE_TC_GABAB_Prob=intraThlProb;RE_RE_GABAA_Prob=intraThlProb;

ThlCrxProb=0.2
PY_TC_AMPA_Prob=ThlCrxProb;PY_RE_AMPA_Prob=ThlCrxProb;
TC_PY_AMPA_Prob=ThlCrxProb;TC_IN_AMPA_Prob=ThlCrxProb;

stimtime = 10050

randInit = True
selfConn = False

ININweight = 0.00

gabaapercent = 0.1
gababpercent = 1


PYPY    = 1*1
PYIN    = 1*1
ININa   = 1*1
INPYa   = 1*1
INPYb   = 1*1

TCRE    = 1*1
RETCa   = 1*1
RETCb   = 1*1
RERE    = 1*1

PYTC    = 1*1
PYRE    = 1*1
TCPY    = 1*1
TCIN    = 1*1

#INPYb*0.03/(N_PY*IN_PY_GABAB_Prob+1)} #0.5}#0.002727}# }  # GABAB
#RETCb*0.04/(N_TC*RE_TC_GABAB_Prob+1)} #0.5}#0.003636}# }  # GABAB
#print("INPY-GABAB_weight = ", netParams.synMechParams['GABAB_S1']['gmax'])
PYgmax = 0.03/11 * 1
#print("RETC-GABAB_weight = ", netParams.synMechParams['GABAB_S2']['gmax'])
TCgmax = 0.04/11 * 1
###############################################################################
# NETWORK PARAMETERS
###############################################################################
N=100; N_PY=N; N_IN=2*N; N_TC=N; N_RE=N;
#N=100; N_PY=N; N_IN=N/4; N_TC=N/2; N_RE=N/2;

netParams.narrowdiam = 5
netParams.widediam = 10

netParams.xspacing = 20 # um
netParams.yspacing = 100 # um

netParams.axondelay = 2

netParams.defaultThreshold = 0

###############################################################################
# LOAD NETCONS
###############################################################################
with open('netcons.json', 'r') as fp:
    netcons = json.load(fp)

###############################################################################
# Population parameters
###############################################################################
### Cortical Cells
netParams.popParams['PY'] = {'cellType': 'PY', 'numCells': N_PY, 'cellModel': 'HH_PY', 'ynormRange': [0.1, 0.3]} #, 'yRange': [1*netParams.yspacing,1*netParams.yspacing], 'gridSpacing': netParams.xspacing}
netParams.popParams['IN'] = {'cellType': 'IN', 'numCells': N_IN, 'cellModel': 'HH_IN', 'ynormRange': [0.35, 0.55]} #, 'yRange': [2*netParams.yspacing,2*netParams.yspacing], 'gridSpacing': netParams.xspacing} 

### Thalamic cells    
netParams.popParams['TC'] = {'cellType': 'TC', 'numCells': N_TC, 'cellModel': 'HH_TC', 'ynormRange': [0.65, 0.75]} #, 'yRange': [2+3*netParams.yspacing,2+3*netParams.yspacing], 'gridSpacing': netParams.xspacing}
netParams.popParams['RE'] = {'cellType': 'RE', 'numCells': N_RE, 'cellModel': 'HH_RE', 'ynormRange': [0.8, 0.9]} #, 'yRange': [2+4*netParams.yspacing,2+4*netParams.yspacing], 'gridSpacing': netParams.xspacing}


###############################################################################
# Cell parameters list
###############################################################################
celsius = 36
v_init = -70

taummax = 0.15
tauhmax = 23.12
tausmax = 140400

### PY (single compartment)
cellRule = netParams.importCellParams(label='PYrule', conds={'cellType': 'PY', 'cellModel': 'HH_PY'},	fileName='sPY.tem', cellName='sPY')

cellRule['secs']['soma']['vinit']=v_init
netParams.cellParams['PYrule'] = cellRule

### TC (Destexhe et al., 1996; Bazhenov et al.,2002)
cellRule = netParams.importCellParams(label='TCrule', conds={'cellType': 'TC', 'cellModel': 'HH_TC'}, fileName='TC.tem', cellName='sTC')

cellRule['secs']['soma']['vinit']=v_init
cellRule['secs']['soma']['ghbar_iar']=17.5e-6
cellRule['secs']['soma']['pointps']['kleak_0']['gmax']=40e-4
netParams.cellParams['TCrule'] = cellRule

### RE (Destexhe et al., 1996; Bazhenov et al.,2002)
cellRule = netParams.importCellParams(label='RErule', conds={'cellType': 'RE', 'cellModel': 'HH_RE'}, fileName='RE.tem', cellName='sRE')

cellRule['secs']['soma']['vinit']=v_init
netParams.cellParams['RErule'] = cellRule

### IN (single compartment)
cellRule = netParams.importCellParams(label='INrule', conds={'cellType': 'IN', 'cellModel': 'HH_IN'},	fileName='sIN.tem', cellName='sIN')


if (nav_type == 1):
    #cellRule['secs']['soma']['mechs']['inak2005mut']={'svhalf': 61.6, 'sk': 3.7, 'staubase': (36200 / 106700) * 140400}
    cellRule['secs']['soma']['mechs']['inak2005mut']['svhalf']=61.6
    cellRule['secs']['soma']['mechs']['inak2005mut']['sk']=3.7
    cellRule['secs']['soma']['mechs']['inak2005mut']['staubase']=(36200 / 106700) * 140400
    taummax = 0.15
    tauhmax = 23.12
    tausmax = (36200 / 106700) * 140400

if (nav_type == 2):
    #cellRule['secs']['soma']['mechs']['inak2005mut']={'mvhalf': 27.4 - (21.2 - 26.3), 'hvhalf': 41.9 - (39.7 - 45.4)}
    cellRule['secs']['soma']['mechs']['inak2005mut']['mvhalf']=27.4 - (21.2 - 26.3)
    cellRule['secs']['soma']['mechs']['inak2005mut']['hvhalf']=41.9 - (39.7 - 45.4)
    taummax = 0.15
    tauhmax = 23.12
    tausmax = 140400

if (nav_type == 3):
    cellRule['secs']['soma']['mechs']['inak2005mut']['mvhalf']=21.2
    cellRule['secs']['soma']['mechs']['inak2005mut']['mk']=4.9
    cellRule['secs']['soma']['mechs']['inak2005mut']['hk']=7.7
    cellRule['secs']['soma']['mechs']['inak2005mut']['svhalf']=46.1 
    cellRule['secs']['soma']['mechs']['inak2005mut']['sk']=5.4 
    cellRule['secs']['soma']['mechs']['inak2005mut']['mtaubase']=0.15
    cellRule['secs']['soma']['mechs']['inak2005mut']['htaubase']=11.8 
    cellRule['secs']['soma']['mechs']['inak2005mut']['htauvhalf']=57.4
    cellRule['secs']['soma']['mechs']['inak2005mut']['htauk']=28.8 
    cellRule['secs']['soma']['mechs']['inak2005mut']['staubase']=106700
    cellRule['secs']['soma']['mechs']['inak2005mut']['stauvhalf']=52.7 
    cellRule['secs']['soma']['mechs']['inak2005mut']['stauk']=18.3 
    taummax = 0.15
    tauhmax = (11.8 / 20.1) * 23.12
    tausmax = 140400

if (nav_type == 4):
    cellRule['secs']['soma']['mechs']['inak2005mut']['mvhalf']=21.3
    cellRule['secs']['soma']['mechs']['inak2005mut']['mk']=57.2571
    cellRule['secs']['soma']['mechs']['inak2005mut']['staubase']=190200
    cellRule['secs']['soma']['mechs']['inak2005mut']['stauvhalf']=90.4
    cellRule['secs']['soma']['mechs']['inak2005mut']['stauk']=38.9
    taummax = 0.15
    tauhmax = 23.12
    tausmax = 190200

if (nav_type == 5):
    cellRule['secs']['soma']['mechs']['inak2005mut']['gnatbar']=0

if (drug == 0):
    # baseline from paper
    cellRule['secs']['soma']['mechs']['inak2005']['gnablock'] = 1
    cellRule['secs']['soma']['mechs']['inak2005']['hshift'] = 0
    cellRule['secs']['soma']['mechs']['inak2005']['sshift'] = 0
    cellRule['secs']['soma']['mechs']['inak2005']['htaubase'] = tauhmax
    cellRule['secs']['soma']['mechs']['inak2005']['staubase'] = tausmax

    cellRule['secs']['soma']['mechs']['inak2005mut']['gnablock'] = 1
    cellRule['secs']['soma']['mechs']['inak2005mut']['hshift'] = 0
    cellRule['secs']['soma']['mechs']['inak2005mut']['sshift'] = 0
    cellRule['secs']['soma']['mechs']['inak2005mut']['htaubase'] = tauhmax
    cellRule['secs']['soma']['mechs']['inak2005mut']['staubase'] = tausmax

if (drug == 1):
    # carbamazepine
    print("carbamazepine dose: ", dose)
    cellRule['secs']['soma']['mechs']['inak2005']['gnablock'] = 1 - (1 - 0.763) * dose
    cellRule['secs']['soma']['mechs']['inak2005']['hshift'] = -7 * dose
    cellRule['secs']['soma']['mechs']['inak2005']['sshift'] = -4.63 * dose
    cellRule['secs']['soma']['mechs']['inak2005']['htaubase'] = tauhmax + tauhmax * (31.526 -1) * dose
    cellRule['secs']['soma']['mechs']['inak2005']['staubase'] = tausmax - tausmax * (1 - 0.5538) * dose

    cellRule['secs']['soma']['mechs']['inak2005mut']['gnablock'] = 1 - (1 - 0.763) * dose
    cellRule['secs']['soma']['mechs']['inak2005mut']['hshift'] = -7 * dose
    cellRule['secs']['soma']['mechs']['inak2005mut']['sshift'] = -4.63 * dose
    cellRule['secs']['soma']['mechs']['inak2005mut']['htaubase'] = tauhmax + tauhmax * (31.526 -1) * dose
    cellRule['secs']['soma']['mechs']['inak2005mut']['staubase'] = tausmax - tausmax * (1 - 0.5538) * dose

if (drug == 2):
    # oxcarbazepine
    print("oxcarbazepine dose: ", dose)
    cellRule['secs']['soma']['mechs']['inak2005']['gnablock'] = 1 - (1 - 0.756) * dose
    #cellRule['secs']['soma']['mechs']['inak2005']['hk'] = 6.7 + 2.31
    #cellRule['secs']['soma']['mechs']['inak2005']['sk'] = 6.6 + 9.82
    cellRule['secs']['soma']['mechs']['inak2005']['hshift'] = -16.58 * dose
    cellRule['secs']['soma']['mechs']['inak2005']['sshift'] = -28.06 * dose
    cellRule['secs']['soma']['mechs']['inak2005']['htaubase'] = tauhmax + tauhmax * (8.079 -1) * dose
    cellRule['secs']['soma']['mechs']['inak2005']['staubase'] = tausmax - tausmax * (1 - 0.3777) * dose

    cellRule['secs']['soma']['mechs']['inak2005mut']['gnablock'] = 1 - (1 - 0.756) * dose
    cellRule['secs']['soma']['mechs']['inak2005mut']['hshift'] = -16.58 * dose
    cellRule['secs']['soma']['mechs']['inak2005mut']['sshift'] = -28.06 * dose
    # cellRule['secs']['soma']['mechs']['inak2005mut']['hk'] = 6.7 + 2.31
    # cellRule['secs']['soma']['mechs']['inak2005mut']['sk'] = 6.6 + 9.82
    cellRule['secs']['soma']['mechs']['inak2005mut']['htaubase'] = tauhmax + tauhmax * (8.079 - 1) * dose
    cellRule['secs']['soma']['mechs']['inak2005mut']['staubase'] = tausmax - tausmax * (1 - 0.3777) * dose

if (drug == 3):
    # lamictal
    print("lamictal dose: ", dose)
    cellRule['secs']['soma']['mechs']['inak2005']['gnablock'] = 1 - (1 - 0.799) * dose
    cellRule['secs']['soma']['mechs']['inak2005']['hshift'] = -4.76 * dose
    cellRule['secs']['soma']['mechs']['inak2005']['sshift'] = -53.28 * dose
    cellRule['secs']['soma']['mechs']['inak2005']['htaubase'] = tauhmax + tauhmax * (1.182 - 1) * dose
    cellRule['secs']['soma']['mechs']['inak2005']['staubase'] = tausmax + tausmax * (1.231 - 1) * dose

    cellRule['secs']['soma']['mechs']['inak2005mut']['gnablock'] = 1 - (1 - 0.799) * dose
    cellRule['secs']['soma']['mechs']['inak2005mut']['hshift'] = -4.76 * dose
    cellRule['secs']['soma']['mechs']['inak2005mut']['sshift'] = -53.28 * dose
    cellRule['secs']['soma']['mechs']['inak2005mut']['htaubase'] = tauhmax + tauhmax * (1.182 - 1) * dose
    cellRule['secs']['soma']['mechs']['inak2005mut']['staubase'] = tausmax + tausmax * (1.231 - 1) * dose


if (drug == 4):
    # eslicarbazepine
    print("esli dose: ", dose)
    cellRule['secs']['soma']['mechs']['inak2005']['gnablock'] = 1 - (1 - 0.944) * dose
    cellRule['secs']['soma']['mechs']['inak2005']['hshift'] = 3.54 * dose
    cellRule['secs']['soma']['mechs']['inak2005']['sshift'] = -31.16 * dose
    cellRule['secs']['soma']['mechs']['inak2005']['htaubase'] = tauhmax + tauhmax * (1.778 - 1) * dose
    cellRule['secs']['soma']['mechs']['inak2005']['staubase'] = tausmax - tausmax * (1 - 0.986) * dose
    print("tauhmax=", tauhmax, "htaubase_inak2005=", cellRule['secs']['soma']['mechs']['inak2005']['htaubase'])

    cellRule['secs']['soma']['mechs']['inak2005mut']['gnablock'] = 1 - (1 - 0.944) * dose
    cellRule['secs']['soma']['mechs']['inak2005mut']['hshift'] = 3.54 * dose
    cellRule['secs']['soma']['mechs']['inak2005mut']['sshift'] = -31.16 * dose
    cellRule['secs']['soma']['mechs']['inak2005mut']['htaubase'] = tauhmax + tauhmax * (1.778 - 1) * dose
    cellRule['secs']['soma']['mechs']['inak2005mut']['staubase'] = tausmax - tausmax * (1 - 0.986) * dose

if (drug == 5):
    # valproic acid
    print("VPS dose: ", dose)
    # gabaapercent=200
    cellRule['secs']['soma']['mechs']['inak2005']['gnablock'] = 1 - (1 - 0.8) * dose
    cellRule['secs']['soma']['mechs']['inak2005']['hshift'] = 10.0 * dose
    cellRule['secs']['soma']['mechs']['inak2005']['sshift'] = -31.16 * dose
    cellRule['secs']['soma']['mechs']['inak2005']['htaubase'] = tauhmax + tauhmax * (2.0 - 1) * dose
    cellRule['secs']['soma']['mechs']['inak2005']['staubase'] = tausmax - tausmax * (1 - 0.986) * dose
    print("tauhmax=", tauhmax, "htaubase_inak2005=", cellRule['secs']['soma']['mechs']['inak2005']['htaubase'])

    cellRule['secs']['soma']['mechs']['inak2005mut']['gnablock'] = 1 - (1 - 0.8) * dose
    cellRule['secs']['soma']['mechs']['inak2005mut']['hshift'] = 10 * dose
    cellRule['secs']['soma']['mechs']['inak2005mut']['sshift'] = -31.16 * dose
    cellRule['secs']['soma']['mechs']['inak2005mut']['htaubase'] = tauhmax + tauhmax * (2.0 - 1) * dose
    cellRule['secs']['soma']['mechs']['inak2005mut']['staubase'] = tausmax - tausmax * (1 - 0.986) * dose

if (drug == 6):
    # diazepam
    print("diazepam dose: ", dose)
    gabaapercent = 200

cellRule['secs']['soma']['vinit']=v_init
netParams.cellParams['INrule'] = cellRule




###############################################################################
# Synaptic mechanism parameters
###############################################################################
# AMPA
netParams.synMechParams['AMPA'] = {'mod': 'ExpSyn', 'tau': 0.1, 'e': 0}

# AMPA_S
#netParams.synMechParams['AMPA_S'] = {'mod': 'Exp2Syn', 'tau1': 0.05, 'tau2': 5.3, 'e': 0}  # AMPA
netParams.synMechParams['AMPA_S'] = {'mod': 'AMPA_S', 'Cmax': 0.5, 'Cdur': 0.3, 'Alpha': 0.94, 'Beta': 0.18, 'Erev': 0} #}

# NMDA
#netParams.synMechParams['NMDA'] = {'mod': 'Exp2Syn', 'tau1': 0.15, 'tau2': 15, 'e': 0}  # NMDA
#netParams.synMechParams['NMDA'] = {'mod': 'NMDA_S', 'Cdur': 1.0, 'Alpha': 0.11, 'Beta': 0.0066, 'Erev': 0, 'mg': 2} #} # Destexhe, 1998
netParams.synMechParams['NMDA_S'] = {'mod': 'NMDA_S', 'Cdur': 0.3, 'Alpha': 0.11, 'Beta': 0.0066, 'Erev': 0, 'mg': 2} #} # Destexhe, 1998

# GABAa_S
#netParams.synMechParams['GABAA'] = {'mod': 'Exp2Syn', 'tau1': 0.07, 'tau2': 9.1, 'e': -80}  # GABAA
netParams.synMechParams['GABAA_S'] = {'mod': 'GABAa_S', 'Cmax': 0.5, 'Cdur': 0.3, 'Alpha': 20, 'Beta': 0.162, 'Erev': -85} # }  # GABAA

# GABAb_S
#netParams.synMechParams['GABAB'] = {'mod': 'Exp2Syn', 'tau1': 0.07, 'tau2': 9.1, 'e': -80}  # GABAB
netParams.synMechParams['GABAB_S1'] = {'mod': 'GABAb_S', 'Cmax': 0.5, 'Cdur': 0.3, 'K1': 0.09, 'K2': 0.0012, 'K3': 0.18, 'K4': 0.034, 'KD': 100, 'n': 4, 'Erev': -95, 'gmax': PYgmax }#INPYb*0.03/(N_PY*IN_PY_GABAB_Prob+1)} #0.5}#0.002727}# }  # GABAB
netParams.synMechParams['GABAB_S2'] = {'mod': 'GABAb_S', 'Cmax': 0.5, 'Cdur': 0.3, 'K1': 0.09, 'K2': 0.0012, 'K3': 0.18, 'K4': 0.034, 'KD': 100, 'n': 4, 'Erev': -95, 'gmax': TCgmax }#RETCb*0.04/(N_TC*RE_TC_GABAB_Prob+1)} #0.5}#0.003636}# }  # GABAB

#netParams.synMechParams['GABAB_S'] = {'mod': 'GABAb_S', 'Cmax': 0.5, 'Cdur': 0.3, 'K1': 0.52, 'K2': 0.0045, 'K3': 0.18, 'K4': 0.034, 'KD': 100, 'Erev': -95} # }  # GABAB

# gap
netParams.synMechParams['GAP'] = {'mod': 'GAP_S', 'r': 1.25e6}

###############################################################################
# Stimulation parameters
###############################################################################

# IClamp PY
netParams.stimSourceParams['Input_1'] = {'type': 'IClamp', 'del': stimtime, 'dur': 100, 'amp': 0.7}
# smallPY=1
netParams.stimTargetParams['Input_1->PY'] = {'source': 'Input_1', 'sec':'soma', 'loc': 0.5, 
                                              'conds': {'pop':'PY', 'cellList': [i*int(N_PY/5-1)+11 for i in range(int(N_PY/20))]}}

###############################################################################
# Connectivity parameters
###############################################################################

####################### intra cortical projections ############################

netParams.connParams['PY->PY_AMPA'] = {
    'preConds': {'popLabel': 'PY'}, 
    'postConds': {'popLabel': 'PY'},
    'weight': PYPY*0.6/(N_PY*PY_PY_AMPA_Prob+1),            # (Destexhe, 1998)
    #'weight': 0.6,            # (Destexhe, 1998)
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'AMPA_S',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': PY_PY_AMPA_Prob}
    'connList': netcons['AMPA_S']['sPY->sPY']}
    #'connList': smallWorldConn(N_PY,N_PY,pCrx,PY_PY_AMPA_Prob,selfConn)}
       

netParams.connParams['PY->IN_AMPA'] = {
    'preConds': {'popLabel': 'PY'}, 
    'postConds': {'popLabel': 'IN'},
    'weight': PYIN*0.2/(N_IN*PY_IN_AMPA_Prob+1),            # (Destexhe, 1998)       
    #'weight': 0.2,            # (Destexhe, 1998)       
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'AMPA_S',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': PY_IN_AMPA_Prob}
    'connList': netcons['AMPA_S']['sPY->sIN']}
    #'connList': smallWorldConn(N_PY,N_IN,pCrx,PY_IN_AMPA_Prob)}   


netParams.connParams['IN->IN_GABAA'] = {
    'preConds': {'popLabel': 'IN'}, 
    'postConds': {'popLabel': 'IN'},
    'weight': ININa*1/(N_IN*IN_IN_GABAA_Prob+1),       
    #'weight': gabaapercent*0.15,         # (Destexhe, 1998)
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'GABAA_S',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': IN_PY_GABAA_Prob}
    'connList': netcons['GABAa_S']['sIN->sIN']}
    #'connList': RegularConn2005(N_IN,N_PY)}   


netParams.connParams['IN->PY_GABAA'] = {
    'preConds': {'popLabel': 'IN'}, 
    'postConds': {'popLabel': 'PY'},
    'weight': INPYa*gabaapercent*0.3/(N_PY*IN_PY_GABAA_Prob+1),         # (Destexhe, 1998)
    #'weight': gabaapercent*0.15,         # (Destexhe, 1998)
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'GABAA_S',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': IN_PY_GABAA_Prob}
    'connList': netcons['GABAa_S']['sIN->sPY']}
    #'connList': smallWorldConn(N_IN,N_PY,pCrx,IN_PY_GABAA_Prob)}   
"""
netParams.connParams['IN->PY_GABAB'] = {
    'preConds': {'popLabel': 'IN'}, 
    'postConds': {'popLabel': 'PY'},
    #'weight': INPYb*gababpercent*0.03/(N_PY*IN_PY_GABAB_Prob+1),         # (Destexhe, 1998)
    #'weight': 0.03,         # (Destexhe, 1998)
    'weight': 1,
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'GABAB_S1',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': IN_PY_GABAB_Prob}
    'connList': netcons['GABAb_S']['sIN->sPY']}
    #'connList': smallWorldConn(N_IN,N_PY,pCrx,IN_PY_GABAB_Prob)}
"""

###################### intra thalamic projections #############################


netParams.connParams['TC->RE'] = {
    'preConds': {'popLabel': 'TC'}, 
    'postConds': {'popLabel': 'RE'},
    'weight': TCRE*0.2/(N_RE*TC_RE_AMPA_Prob+1),         # (Destexhe, 1998)  
    #'weight': 0.2,         # (Destexhe, 1998)  
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'threshold': 0,
    'synMech': 'AMPA_S',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': TC_RE_AMPA_Prob}
    'connList': netcons['AMPA_S']['sTC->sRE']}
    #'connList': smallWorldConn(N_TC,N_RE,pThl,TC_RE_AMPA_Prob)}

netParams.connParams['RE->TC_GABAA'] = {
    'preConds': {'popLabel': 'RE'}, 
    'postConds': {'popLabel': 'TC'},
    'weight': RETCa*gabaapercent*0.02/(N_TC*RE_TC_GABAA_Prob+1),         # (Destexhe, 1998)
    #'weight': 0.02,         # (Destexhe, 1998)
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'GABAA_S',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': RE_TC_GABAA_Prob}
    'connList': netcons['GABAa_S']['sRE->sTC']}
    #'connList': smallWorldConn(N_RE,N_TC,pThl,RE_TC_GABAA_Prob)}   
"""
netParams.connParams['RE->TC_GABAB'] = {
    'preConds': {'popLabel': 'RE'}, 
    'postConds': {'popLabel': 'TC'},
    #'weight': RETCb*0.04/(N_TC*RE_TC_GABAB_Prob+1),         # (Destexhe, 1998)
    #'weight': 0.04,         # (Destexhe, 1998)
    'weight': 1,
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'GABAB_S2',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': RE_TC_GABAB_Prob}
    'connList': netcons['GABAb_S']['sRE->sTC']}
    #'connList': smallWorldConn(N_RE,N_TC,pThl,RE_TC_GABAB_Prob)}
"""

#netParams.connParams['RE->TC_GABAB']['gmax']=0.04/(N_TC*RE_TC_GABAB_Prob+1)

netParams.connParams['RE->RE'] = {
    'preConds': {'popLabel': 'RE'}, 
    'postConds': {'popLabel': 'RE'},
    'weight': RERE*0.2/(N_RE*RE_RE_GABAA_Prob+1),            # (Destexhe, 1998)
    #'weight': 0.2,            # (Destexhe, 1998)
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'sec': 'soma',
    #'threshold': 0,
    'synMech': 'GABAA_S',
    #'synsPerConn': 1,
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': RE_RE_GABAA_Prob}
    'connList': netcons['GABAa_S']['sRE->sRE']}
    #'connList': smallWorldConn(N_RE,N_RE,pThl,RE_RE_GABAA_Prob,selfConn)}   

################# thalamo-cortical projections ################################


netParams.connParams['PY->TC'] = {
    'preConds': {'popLabel': 'PY'}, 
    'postConds': {'popLabel': 'TC'},
    'weight': PYTC*0.01/(N_TC*PY_TC_AMPA_Prob+1),           # (Destexhe, 1998)    
    #'weight': 0.01,           # (Destexhe, 1998)    
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'AMPA_S',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': PY_TC_AMPA_Prob}
    'connList': netcons['AMPA_S']['sPY->sTC']}
    #'connList': smallWorldConn(N_PY,N_TC,pThlCrx,PY_TC_AMPA_Prob)}   

netParams.connParams['PY->RE'] = {
    'preConds': {'popLabel': 'PY'}, 
    'postConds': {'popLabel': 'RE'},
    'weight': PYRE*1.2/(N_RE*PY_RE_AMPA_Prob+1),           # (Destexhe, 1998)  
    #'weight': 1.2,           # (Destexhe, 1998)  
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'AMPA_S',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': PY_RE_AMPA_Prob}
    'connList': netcons['AMPA_S']['sPY->sRE']}
    #'connList': smallWorldConn(N_PY,N_RE,pThlCrx,PY_RE_AMPA_Prob)}   

netParams.connParams['TC->PY'] = {
    'preConds': {'popLabel': 'TC'}, 
    'postConds': {'popLabel': 'PY'},
    'weight': TCPY*1.2/(N_PY*TC_PY_AMPA_Prob+1),        # (Destexhe, 1998)   
    #'weight': 1.2,        # (Destexhe, 1998)   
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'AMPA_S',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': TC_PY_AMPA_Prob}
    'connList': netcons['AMPA_S']['sTC->sPY']}
    #'connList': smallWorldConn(N_TC,N_PY,pThlCrx,TC_PY_AMPA_Prob)}   


# REMOVED THESE, not physiological and didn't change oscillations?
#
#netParams.connParams['TC->IN'] = {
#    'preConds': {'popLabel': 'TC'}, 
#    'postConds': {'popLabel': 'IN'},
#    'weight': TCIN*0/(N_IN*TC_IN_AMPA_Prob+1),        # (Destexhe, 1998)  
#    #'weight': 0.4,        # (Destexhe, 1998)  
#    'delay': netParams.axondelay, 
#    'loc': 0.5,
#    'synMech': 'AMPA_S',
#    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
#    #'probability': TC_IN_AMPA_Prob}
#    'connList': smallWorldConn(N_TC,N_IN,pThlCrx,TC_IN_AMPA_Prob)}
#