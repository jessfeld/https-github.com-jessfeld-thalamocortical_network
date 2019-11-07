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
from pprint import pprint
nav_type, drug, dose = cfg.nav_type, cfg.drug, cfg.dose

def mkConnList( n, diam ):
    connList = []
    for i in range(n):
        for j in range(i-diam, i+diam+1):
            jbound = j                      # boundary cell conditions
            if (jbound < 0):
                jbound = abs(j) - 1
            if (jbound > (n-1)):
                jbound = 2 * n - jbound - 1
            connList.append( [i, jbound] )
    return connList

def mkConnListIN( n, diam ):
    connList = []
    for i in range(n):
        for j in range(i-diam, i+diam+1):
            jbound = j                      # boundary cell conditions
            if (jbound < 0):
                jbound = abs(j) - 1
            if (jbound > (n-1)):
                jbound = 2 * n - jbound - 1
            connList.append( [i, jbound] )
            connList.append( [i + 100, jbound])
    return connList

def mkConnListCT( nPre, nPost, diam, divergence):   #corticothalamic
    connList = []
    for i in range(0, nPre, divergence):        #divergence should be integer
        for j in range( int(i/divergence)-diam, int(i/divergence)+diam+1):
            jbound = j
            if (jbound < 0):
                jbound = abs(j) - 1
            if (jbound > (nPost - 1)):
                jbound = 2 * nPost - jbound - 1
            connList.append( [ int(i+divergence/2), jbound ] )
    return connList

def mkConnListTC( nPre, nPost, diam, divergence):   #thalamocortical
    connList = []
    for i in range(nPre):
        for j in range( ( divergence * (i-diam) ), ( divergence * (i+diam+1) ), divergence ): #divergence should be integer
            jbound = j
            if (jbound < 0):
                jbound = abs(j) - divergence
            if (jbound > (nPost - 1)):
                jbound = 2 * nPost - jbound - divergence
            connList.append( [i , int(jbound + divergence / 2)])
    return connList
                


###############################################################################
#
# MPI HH TUTORIAL PARAMS
#
###############################################################################

ININweight = 0.00

gabaapercent = 1
gababpercent = 1

###############################################################################
# NETWORK PARAMETERS
###############################################################################

ncorticalcells = 100
nthalamiccells = 100
narrowdiam = 5
widediam = 10

nRERE = 2 * narrowdiam + 1
nRETC = 2 * narrowdiam + 1
nTCRE = 2 * narrowdiam + 1
nPYPY = 2 * narrowdiam + 1
nINPY = 2 * narrowdiam + 1
nPYIN = 2 * narrowdiam + 1
nPYRE = 2 * widediam + 1
nPYTC = 2 * widediam + 1
nTCPY = 2 * widediam + 1

netParams.xspacing = 20 # um
netParams.yspacing = 100 # um

netParams.axondelay = 2

netParams.defaultThreshold = 0

###############################################################################
# Population parameters
###############################################################################
### Cortical Cells
netParams.popParams['PY'] = {'cellType': 'PY', 'numCells': ncorticalcells, 'cellModel': 'HH_PY'} #, 'ynormRange': [0.1, 0.3]} #, 'yRange': [1*netParams.yspacing,1*netParams.yspacing], 'gridSpacing': netParams.xspacing}
netParams.popParams['IN'] = {'cellType': 'IN', 'numCells': (ncorticalcells * 2), 'cellModel': 'HH_IN'} #, 'ynormRange': [0.35, 0.55]} #, 'yRange': [2*netParams.yspacing,2*netParams.yspacing], 'gridSpacing': netParams.xspacing} 

### Thalamic cells    
netParams.popParams['TC'] = {'cellType': 'TC', 'numCells': nthalamiccells, 'cellModel': 'HH_TC'} #, 'ynormRange': [0.65, 0.75]} #, 'yRange': [2+3*netParams.yspacing,2+3*netParams.yspacing], 'gridSpacing': netParams.xspacing}
netParams.popParams['RE'] = {'cellType': 'RE', 'numCells': nthalamiccells, 'cellModel': 'HH_RE'} #, 'ynormRange': [0.8, 0.9]} #, 'yRange': [2+4*netParams.yspacing,2+4*netParams.yspacing], 'gridSpacing': netParams.xspacing}


###############################################################################
# Cell parameters list
###############################################################################
celsius = 36
v_init = -70

taummax = 0.15
tauhmax = 23.12
tausmax = 140400

### PY (single compartment)
PYcellRule = netParams.importCellParams(label='PYrule', conds={'cellType': 'PY', 'cellModel': 'HH_PY'},	fileName='sPY.tem', cellName='sPY')

### TC (Destexhe et al., 1996; Bazhenov et al.,2002)
TCcellRule = netParams.importCellParams(label='TCrule', conds={'cellType': 'TC', 'cellModel': 'HH_TC'}, fileName='TC.tem', cellName='sTC')

### RE (Destexhe et al., 1996; Bazhenov et al.,2002)
REcellRule = netParams.importCellParams(label='RErule', conds={'cellType': 'RE', 'cellModel': 'HH_RE'}, fileName='RE.tem', cellName='sRE')

### IN (single compartment)
INcellRule = netParams.importCellParams(label='INrule', conds={'cellType': 'IN', 'cellModel': 'HH_IN'},	fileName='sIN.tem', cellName='sIN')

### Cell Rule to update all parameters
cellRule = {}

if (nav_type == 1):
    #cellRule['secs']['soma']['mechs']['inak2005mut']={'svhalf': 61.6, 'sk': 3.7, 'staubase': (36200 / 106700) * 140400}
    INcellRule['secs']['soma']['mechs']['inak2005mut']['svhalf']=61.6
    INcellRule['secs']['soma']['mechs']['inak2005mut']['sk']=3.7
    INcellRule['secs']['soma']['mechs']['inak2005mut']['staubase']=(36200 / 106700) * 140400
    taummax = 0.15
    tauhmax = 23.12
    tausmax = (36200 / 106700) * 140400

if (nav_type == 2):
    #cellRule['secs']['soma']['mechs']['inak2005mut']={'mvhalf': 27.4 - (21.2 - 26.3), 'hvhalf': 41.9 - (39.7 - 45.4)}
    INcellRule['secs']['soma']['mechs']['inak2005mut']['mvhalf']=27.4 - (21.2 - 26.3)
    INcellRule['secs']['soma']['mechs']['inak2005mut']['hvhalf']=41.9 - (39.7 - 45.4)
    taummax = 0.15
    tauhmax = 23.12
    tausmax = 140400

if (nav_type == 3):
    INcellRule['secs']['soma']['mechs']['inak2005mut']['mvhalf']=21.2
    INcellRule['secs']['soma']['mechs']['inak2005mut']['mk']=4.9
    INcellRule['secs']['soma']['mechs']['inak2005mut']['hvhalf']=39.7
    INcellRule['secs']['soma']['mechs']['inak2005mut']['hk']=7.7
    INcellRule['secs']['soma']['mechs']['inak2005mut']['svhalf']=46.1 
    INcellRule['secs']['soma']['mechs']['inak2005mut']['sk']=5.4 
    INcellRule['secs']['soma']['mechs']['inak2005mut']['mtaubase']=0.15
    INcellRule['secs']['soma']['mechs']['inak2005mut']['htaubase']=11.8 
    INcellRule['secs']['soma']['mechs']['inak2005mut']['htauvhalf']=57.4
    INcellRule['secs']['soma']['mechs']['inak2005mut']['htauk']=28.8 
    INcellRule['secs']['soma']['mechs']['inak2005mut']['staubase']=106700
    INcellRule['secs']['soma']['mechs']['inak2005mut']['stauvhalf']=52.7 
    INcellRule['secs']['soma']['mechs']['inak2005mut']['stauk']=18.3 
    taummax = 0.15
    tauhmax = (11.8 / 20.1) * 23.12
    tausmax = 140400

if (nav_type == 4):
    INcellRule['secs']['soma']['mechs']['inak2005mut']['mvhalf']=21.3
    INcellRule['secs']['soma']['mechs']['inak2005mut']['mk']=57.2571
    INcellRule['secs']['soma']['mechs']['inak2005mut']['staubase']=190200
    INcellRule['secs']['soma']['mechs']['inak2005mut']['stauvhalf']=90.4
    INcellRule['secs']['soma']['mechs']['inak2005mut']['stauk']=38.9
    taummax = 0.15
    tauhmax = 23.12
    tausmax = 190200

if (nav_type == 5):
    INcellRule['secs']['soma']['mechs']['inak2005mut']['gnatbar']=0

if (drug == 0):
    # baseline from paper
    cellRule['gnablock'] = 1
    cellRule['hshift'] = 0
    cellRule['sshift'] = 0
    cellRule['htaubase'] = tauhmax
    cellRule['staubase'] = tausmax

if (drug == 1):
    # carbamazepine
    print("carbamazepine dose: ", dose)

    cellRule['gnablock'] = 1 - (1 - 0.763) * dose
    cellRule['hshift'] = -7 * dose
    cellRule['sshift'] = -4.63 * dose
    cellRule['htaubase'] = tauhmax + tauhmax * (31.526 -1) * dose
    cellRule['staubase'] = tausmax - tausmax * (1 - 0.5538) * dose


if (drug == 2):
    # oxcarbazepine
    print("oxcarbazepine dose: ", dose)
    cellRule['gnablock'] = 1 - (1 - 0.756) * dose
    cellRule['hshift'] = -16.58 * dose
    cellRule['sshift'] = -28.06 * dose
    cellRule['htaubase'] = tauhmax + tauhmax * (8.079 -1) * dose
    cellRule['staubase'] = tausmax - tausmax * (1 - 0.3777) * dose

if (drug == 3):
    # lamictal
    print("lamictal dose: ", dose)
    cellRule['gnablock'] = 1 - (1 - 0.799) * dose
    cellRule['hshift'] = -4.76 * dose
    cellRule['sshift'] = -53.28 * dose
    cellRule['htaubase'] = tauhmax + tauhmax * (1.182 - 1) * dose
    cellRule['staubase'] = tausmax + tausmax * (1.231 - 1) * dose

if (drug == 4):
    # eslicarbazepine
    print("esli dose: ", dose)
    cellRule['gnablock'] = 1 - (1 - 0.944) * dose
    cellRule['hshift'] = 3.54 * dose
    cellRule['sshift'] = -31.16 * dose
    cellRule['htaubase'] = tauhmax + tauhmax * (1.778 - 1) * dose
    cellRule['staubase'] = tausmax - tausmax * (1 - 0.986) * dose

if (drug == 5):
    # valproic acid
    print("VPS dose: ", dose)
    # gabaapercent=200
    cellRule['gnablock'] = 1 - (1 - 0.8) * dose
    cellRule['hshift'] = 10.0 * dose
    cellRule['sshift'] = -31.16 * dose
    cellRule['htaubase'] = tauhmax + tauhmax * (2.0 - 1) * dose
    cellRule['staubase'] = tausmax - tausmax * (1 - 0.986) * dose

if (drug == 6):
    # diazepam
    print("diazepam dose: ", dose)
    gabaapercent = 200

PYcellRule['secs']['soma']['mechs']['inak2005'].update(cellRule)
TCcellRule['secs']['soma']['mechs']['inak2005'].update(cellRule)
REcellRule['secs']['soma']['mechs']['inak2005'].update(cellRule)
INcellRule['secs']['soma']['mechs']['inak2005'].update(cellRule)
INcellRule['secs']['soma']['mechs']['inak2005mut'].update(cellRule)

print("tauhmax=", tauhmax, "htaubase_inak2005=", PYcellRule['secs']['soma']['mechs']['inak2005']['htaubase'])

PYcellRule['secs']['soma']['vinit']=v_init
netParams.cellParams['PYrule'] = PYcellRule

TCcellRule['secs']['soma']['vinit']=v_init
TCcellRule['secs']['soma']['mechs']['iar']['ghbar']      = 17.5e-6
TCcellRule['secs']['soma']['pointps']['kleak_0']['gmax'] = 40e-4
netParams.cellParams['TCrule'] = TCcellRule

REcellRule['secs']['soma']['vinit']=v_init
netParams.cellParams['RErule'] = REcellRule

INcellRule['secs']['soma']['vinit']=v_init
netParams.cellParams['INrule'] = INcellRule

###############################################################################
# Synaptic mechanism parameters
###############################################################################

PYgmax = 0.03/nINPY # gmax instead of weight for GABAB due to nonlinearity
TCgmax = 0.04/nRETC # gmax instead of weight for GABAB due to nonlinearity

# AMPA_S
netParams.synMechParams['AMPA_S'] = {'mod': 'AMPA_S', 'Alpha': 0.94, 'Beta': 0.18, 'Cmax': 0.5, 'Cdur': 0.3, 'Erev': 0}
netParams.synMechParams['AMPA_S_PYPY'] = {'mod': 'AMPA_S', 'Alpha': 0.94, 'Beta': 0.18, 'Cmax': 0.5, 'Cdur': 0.3, 'Erev': 0}

# GABAa_S
netParams.synMechParams['GABAA_S'] = {'mod': 'GABAa_S', 'Alpha': 20, 'Beta': 0.162, 'Cmax': 0.5, 'Cdur': 0.3, 'Erev': -85}

# GABAb_S
netParams.synMechParams['GABAB_S1'] = {'mod': 'GABAb_S', 'Cmax': 0.5, 'Cdur': 0.3, 'K1': 0.09, 'K2': 0.0012, 'K3': 0.18, 'K4': 0.034, 'KD': 100, 'n': 4, 'Erev': -95, 'gmax': PYgmax }
netParams.synMechParams['GABAB_S2'] = {'mod': 'GABAb_S', 'Cmax': 0.5, 'Cdur': 0.3, 'K1': 0.09, 'K2': 0.0012, 'K3': 0.18, 'K4': 0.034, 'KD': 100, 'n': 4, 'Erev': -95, 'gmax': TCgmax }


###############################################################################
# Stimulation parameters
###############################################################################

# IClamp PY
netParams.stimSourceParams['Input_1'] = {'type': 'IClamp', 'del': 0, 'dur': 10, 'amp': -0.7}
# smallPY=1
netParams.stimTargetParams['Input_1->TC'] = {'source': 'Input_1', 'sec':'soma', 'loc': 0.5, 'conds': {'pop':'TC'}}

###############################################################################
# Connectivity parameters
###############################################################################

####################### intra cortical projections ############################
divergence = int(ncorticalcells/nthalamiccells) # which is 1 right now
cLcortical = mkConnList( ncorticalcells, narrowdiam)
cLthalamic = mkConnList( nthalamiccells, narrowdiam)
cLcortthal = mkConnListCT( ncorticalcells, nthalamiccells, widediam, divergence) #cortical -> thalamic projections
cLthalcort = mkConnListTC( nthalamiccells, ncorticalcells, widediam, divergence) #thalamic -> cortical projections



###########################################################
##   Glutamate AMPA receptors in synapses from TC to RE  ##
###########################################################

netParams.connParams['TC->RE'] = {
    'preConds': {'popLabel': 'TC'}, 
    'postConds': {'popLabel': 'RE'},
    #'weight': 0.018182,     # TCRE*0.2/(N_RE*TC_RE_AMPA_Prob+1),         # (Destexhe, 1998)  
    'weight': 0.2/nTCRE,         # (Destexhe, 1998)  
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'AMPA_S',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': TC_RE_AMPA_Prob}
    'connList': cLthalamic}
    #'connList': netcons['AMPA_S']['sTCsRE']}

###########################################################
##   GABAa receptors in intra-RE synapses                ##
###########################################################

netParams.connParams['RE->RE'] = {
    'preConds': {'popLabel': 'RE'}, 
    'postConds': {'popLabel': 'RE'},
    #'weight': 0.018182,        # RERE*0.2/(N_RE*RE_RE_GABAA_Prob+1),            # (Destexhe, 1998)
    'weight': 0.2/nRERE,            # (Destexhe, 1998)
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'sec': 'soma',
    'synMech': 'GABAA_S',
    #'synsPerConn': 1,
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': RE_RE_GABAA_Prob}
    'connList': cLthalamic}
    #'connList': netcons['GABAa_S']['sREsRE']} 

###########################################################
##   GABAa receptors in in synapses from RE to TC cells  ##
###########################################################

netParams.connParams['RE->TC_GABAA'] = {
    'preConds': {'popLabel': 'RE'}, 
    'postConds': {'popLabel': 'TC'},
    #'weight': 0.00182 * gabaapercent,   # RETCa*gabaapercent*0.02/(N_TC*RE_TC_GABAA_Prob+1),         # (Destexhe, 1998)
    'weight': gabaapercent*0.02/nRETC,                    # (Destexhe, 1998)
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'GABAA_S',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': RE_TC_GABAA_Prob}
    'connList': cLthalamic}
    #'connList': netcons['GABAa_S']['sREsTC']} 

###########################################################
##   GABAb receptors in in synapses from RE to TC cells  ##
###########################################################


netParams.connParams['RE->TC_GABAB'] = {
    'oneSynPerNetcon': True,
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
    'connList': cLthalamic}
    #'connList': netcons['GABAb_S']['sREsTC']}


###########################################################
##   Glutamate AMPA receptors in synapses from PY to PY  ##
###########################################################

netParams.connParams['PY->PY_AMPA'] = {
    'preConds': {'popLabel': 'PY'}, 
    'postConds': {'popLabel': 'PY'},
    #'weight': 0.054545,        # PYPY*0.6/(N_PY*PY_PY_AMPA_Prob+1),            # (Destexhe, 1998)
    'weight': 0.6/nPYPY,            # (Destexhe, 1998)
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'AMPA_S_PYPY',
    'connList': cLcortical}
    #'connList': netcons['AMPA_S']['sPYsPY']}

###########################################################
##   Glutamate AMPA receptors in synapses from PY to IN  ##
###########################################################
     
PYINconnlist = cLcortical + [ [x, y + 100] for x, y in cLcortical ]
netParams.connParams['PY->IN_AMPA'] = {
    'preConds': {'popLabel': 'PY'}, 
    'postConds': {'popLabel': 'IN'},
    #'weight': 0.018182,        # PYIN*0.2/(N_IN*PY_IN_AMPA_Prob+1),            # (Destexhe, 1998)       
    'weight': 0.2/nPYIN,            # (Destexhe, 1998)       
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'AMPA_S',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': PY_IN_AMPA_Prob}
    'connList': PYINconnlist}
    #'connList': netcons['AMPA_S']['sPYsIN']}

###########################################################
##   GABAa receptors in synapses from IN to PY cells     ##
###########################################################
INPYconnlist = mkConnListIN( ncorticalcells, narrowdiam )             #IN connections with instantiation matching original model
# INPYconnlist = cLcortical + [ [x + 100, y] for x, y in cLcortical ] #order of instantiation matters when it comes to nonlinear receptors
netParams.connParams['IN->PY_GABAA'] = {
    'preConds': {'popLabel': 'IN'}, 
    'postConds': {'popLabel': 'PY'},
    #'weight': 0.02727 * gabaapercent,     # INPYa*gabaapercent*0.3/(N_PY*IN_PY_GABAA_Prob+1),         # (Destexhe, 1998)
    'weight': gabaapercent*0.3/nINPY,         # (Destexhe, 1998)
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'GABAA_S',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': IN_PY_GABAA_Prob}
    'connList': INPYconnlist}
    #'connList': netcons['GABAa_S']['sINsPY']}

###########################################################
##   GABAb receptors in in synapses from IN to PY cells  ##
###########################################################

netParams.connParams['IN->PY_GABAB'] = {
    'oneSynPerNetcon': True,
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
    'connList': INPYconnlist}
    #'connList': netcons['GABAa_S']['sINsPY']}


###########################################################
##   GABAa receptors in synapses from IN to IN cells     ##
###########################################################

ININconnlist = [ [ x, x + 100] for x in range(100) ] + [ [ x + 100, x] for x in range(100) ]
netParams.connParams['IN->IN_GABAA'] = {
    'preConds': {'popLabel': 'IN'}, 
    'postConds': {'popLabel': 'IN'},
    'weight': 0,               # ININa*1/(N_IN*IN_IN_GABAA_Prob+1),       
    #'weight': gabaapercent*0.15,         # (Destexhe, 1998)
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'GABAA_S',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': IN_PY_GABAA_Prob}
    'connList': ININconnlist}
    #'connList': netcons['GABAa_S']['sINsIN']}

###########################################################
##   Glutamate AMPA receptors in synapses from PY to RE  ##
###########################################################

netParams.connParams['PY->RE'] = {
    'preConds': {'popLabel': 'PY'}, 
    'postConds': {'popLabel': 'RE'},
    #'weight': 0.057143,       # PYRE*1.2/(N_RE*PY_RE_AMPA_Prob+1),           # (Destexhe, 1998)  
    'weight': 1.2/nPYRE,           # (Destexhe, 1998)  
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'AMPA_S',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': PY_RE_AMPA_Prob}
    'connList': cLcortthal}
    #'connList': netcons['AMPA_S']['sPYsRE']} 

###########################################################
##   Glutamate AMPA receptors in synapses from PY to TC  ##
###########################################################

netParams.connParams['PY->TC'] = {
    'preConds': {'popLabel': 'PY'}, 
    'postConds': {'popLabel': 'TC'},
    #'weight': 0.000476,        # PYTC*0.01/(N_TC*PY_TC_AMPA_Prob+1),           # (Destexhe, 1998)    
    'weight': 0.01/nPYTC,           # (Destexhe, 1998)    
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'AMPA_S',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': PY_TC_AMPA_Prob}
    'connList': cLcortthal}
    #'connList': netcons['AMPA_S']['sPYsTC']}   

###########################################################
##   Glutamate AMPA receptors in synapses from TC to PY  ##
###########################################################

netParams.connParams['TC->PY'] = {
    'preConds': {'popLabel': 'TC'}, 
    'postConds': {'popLabel': 'PY'},
    #'weight': 0.057143,    # TCPY*1.2/(N_PY*TC_PY_AMPA_Prob+1),        # (Destexhe, 1998)   
    'weight': 1.2/nTCPY,        # (Destexhe, 1998)   
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'AMPA_S',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': TC_PY_AMPA_Prob}
    'connList': cLthalcort}
    #'connList': netcons['AMPA_S']['sTCsPY']}

###########################################################
##   Glutamate AMPA receptors in synapses from TC to IN  ##
###########################################################

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
