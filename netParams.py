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
try: 
    from __main__ import cfg
except:
    from cfg import cfg

def mkConnList( n, radius ):
    connList = []
    for i in range(n):
        for j in range(i-radius, i+radius+1):
            jbound = j                      # boundary cell conditions
            if (jbound < 0):
                jbound = abs(j) - 1
            if (jbound > (n-1)):
                jbound = 2 * n - jbound - 1
            connList.append( [i, jbound] )
    return connList

def mkConnListIN( n, radius ):
    connList = []
    for i in range(n):
        for j in range(i-radius, i+radius+1):
            jbound = j                      # boundary cell conditions
            if (jbound < 0):
                jbound = abs(j) - 1
            if (jbound > (n-1)):
                jbound = 2 * n - jbound - 1
            connList.append( [i, jbound] )
            connList.append( [i + 100, jbound])
    return connList

def mkConnListCT( nPre, nPost, radius, divergence):   #corticothalamic
    connList = []
    for i in range(0, nPre, divergence):        #divergence should be integer
        for j in range( int(i/divergence)-radius, int(i/divergence)+radius+1):
            jbound = j
            if (jbound < 0):
                jbound = abs(j) - 1
            if (jbound > (nPost - 1)):
                jbound = 2 * nPost - jbound - 1
            connList.append( [ int(i+divergence/2), jbound ] )
    return connList

def mkConnListTC( nPre, nPost, radius, divergence):   #thalamocortical
    connList = []
    for i in range(nPre):
        for j in range( ( divergence * (i-radius) ), ( divergence * (i+radius+1) ), divergence ): #divergence should be integer
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

stimtime = 10050 #stimulation distributed over PY cells 
###############################################################################
# NETWORK PARAMETERS
###############################################################################

ncorticalcells = 100
nthalamiccells = 100
narrowradius = 5
wideradius = 10


nRERE = 2 * narrowradius + 1
nRETC = 2 * narrowradius + 1
nTCRE = 2 * narrowradius + 1
nPYPY = 2 * narrowradius + 1
nINPY = 2 * narrowradius + 1
nPYIN = 2 * narrowradius + 1
nPYRE = 2 * wideradius + 1
nPYTC = 2 * wideradius + 1
nTCPY = 2 * wideradius + 1

netParams.xspacing = 20 # um
netParams.yspacing = 100 # um

netParams.axondelay = 2

netParams.defaultThreshold = 0

###############################################################################
# Population parameters
###############################################################################
### Cortical Cells
netParams.popParams['PY'] = {'cellType': 'PY', 'numCells': ncorticalcells,       'cellModel': '_PY'} #, 'ynormRange': [0.1, 0.3]} #, 'yRange': [1*netParams.yspacing,1*netParams.yspacing], 'gridSpacing': netParams.xspacing}
netParams.popParams['IN'] = {'cellType': 'IN', 'numCells': (ncorticalcells * 2), 'cellModel': '_IN'} #, 'ynormRange': [0.35, 0.55]} #, 'yRange': [2*netParams.yspacing,2*netParams.yspacing], 'gridSpacing': netParams.xspacing} 

### Thalamic cells    
netParams.popParams['TC'] = {'cellType': 'TC', 'numCells': nthalamiccells,       'cellModel': '_TC'} #, 'ynormRange': [0.65, 0.75]} #, 'yRange': [2+3*netParams.yspacing,2+3*netParams.yspacing], 'gridSpacing': netParams.xspacing}
netParams.popParams['RE'] = {'cellType': 'RE', 'numCells': nthalamiccells,       'cellModel': '_RE'} #, 'ynormRange': [0.8, 0.9]} #, 'yRange': [2+4*netParams.yspacing,2+4*netParams.yspacing], 'gridSpacing': netParams.xspacing}


###############################################################################
# Cell parameters list
###############################################################################
celsius = 36
v_init = -70

taummax = 0.15
tauhmax = 23.12
tausmax = 140400

### PY (single compartment)
PYcellRule = netParams.importCellParams(label='PYrule', conds={'cellType': 'PY', 'cellModel': '_PY'},	fileName='sPY.tem', cellName='sPY')

### TC (Destexhe et al., 1996; Bazhenov et al.,2002)
TCcellRule = netParams.importCellParams(label='TCrule', conds={'cellType': 'TC', 'cellModel': '_TC'}, fileName='TC.tem', cellName='sTC')

### RE (Destexhe et al., 1996; Bazhenov et al.,2002)
REcellRule = netParams.importCellParams(label='RErule', conds={'cellType': 'RE', 'cellModel': '_RE'}, fileName='RE.tem', cellName='sRE')

### IN (single compartment)
INcellRule = netParams.importCellParams(label='INrule', conds={'cellType': 'IN', 'cellModel': '_IN'},	fileName='sIN.tem', cellName='sIN')

### Cell Rule to update all parameters
cellRule = {}

if (cfg.nav_type == 1):
    cellRule = {
        'svhalf'    : 61.6,
        'sk'        : 3.7,
        'staubase'  : (36200 / 106700) * 140400 }
    taummax = 0.15
    tauhmax = 23.12
    tausmax = (36200 / 106700) * 140400

if (cfg.nav_type == 2):
    cellRule = {
        'mvhalf'    : 27.4 - (21.2 - 26.3),
        'hvhalf'    : 41.9 - (39.7 - 45.4) }
    taummax = 0.15
    tauhmax = 23.12
    tausmax = 140400

if (cfg.nav_type == 3):
    cellRule = {
        'mvhalf'    : 21.2,
        'mk'        : 4.9,
        'hvhalf'    : 39.7,
        'hk'        : 7.7,
        'svhalf'    : 46.1, 
        'sk'        : 5.4,
        'mtaubase'  : 0.15,
        'htaubase'  : 11.8,
        'htauvhalf' : 57.4,
        'htauk'     : 28.8, 
        'staubase'  : 106700,
        'stauvhalf' : 52.7, 
        'stauk'     : 18.3 }
    taummax = 0.15
    tauhmax = (11.8 / 20.1) * 23.12
    tausmax = 140400

if (cfg.nav_type == 4):
    cellRule = {
        'mvhalf'    : 21.3,
        'mk'        : 57.2571,
        'staubase'  : 190200,
        'stauvhalf' : 90.4,
        'stauk'     : 38.9 }
    taummax = 0.15
    tauhmax = 23.12
    tausmax = 190200

if (cfg.nav_type == 5):
    cellRule = {
        'gnatbar'   : 0 }

INcellRule['secs']['soma']['mechs']['inak2005mut'].update(cellRule)

if (cfg.drug == 0):
    # baseline from paper
    cellRule = {
        'gnablock': 1,
        'hshift'  : 0,
        'sshift'  : 0,
        'htaubase': tauhmax,
        'staubase': tausmax }

if (cfg.drug == 1):
    # carbamazepine
    print("carbamazepine dose: ", cfg.dose)
    cellRule = {
        'gnablock': 1 - (1 - 0.763) * cfg.dose,
        'hshift'  : -7 * cfg.dose,
        'sshift'  : -4.63 * cfg.dose,
        'htaubase': tauhmax + tauhmax * (31.526 -1) * cfg.dose,
        'staubase': tausmax - tausmax * (1 - 0.5538) * cfg.dose }


if (cfg.drug == 2):
    # oxcarbazepine
    print("oxcarbazepine dose: ", cfg.dose)
    cellRule = {
        'gnablock': 1 - (1 - 0.756) * cfg.dose,
        'hshift'  : -16.58 * cfg.dose,
        'sshift'  : -28.06 * cfg.dose,
        'htaubase': tauhmax + tauhmax * (8.079 -1) * cfg.dose,
        'staubase': tausmax - tausmax * (1 - 0.3777) * cfg.dose }

if (cfg.drug == 3):
    # lamictal
    print("lamictal dose: ", cfg.dose)
    cellRule = {
        'gnablock': 1 - (1 - 0.799) * cfg.dose,
        'hshift'  : -4.76 * cfg.dose,
        'sshift'  : -53.28 * cfg.dose,
        'htaubase': tauhmax + tauhmax * (1.182 - 1) * cfg.dose,
        'staubase': tausmax + tausmax * (1.231 - 1) * cfg.dose }

if (cfg.drug == 4):
    # eslicarbazepine
    print("esli dose: ", cfg.dose)
    cellRule = {
        'gnablock': 1 - (1 - 0.944) * cfg.dose,
        'hshift'  : 3.54 * cfg.dose,
        'sshift'  : -31.16 * cfg.dose,
        'htaubase': tauhmax + tauhmax * (1.778 - 1) * cfg.dose,
        'staubase': tausmax - tausmax * (1 - 0.986) * cfg.dose }

if (cfg.drug == 5):
    # valproic acid
    print("VPS dose: ", cfg.dose)
    # gabaapercent=200
    cellRule = {
        'gnablock': 1 - (1 - 0.8) * cfg.dose,
        'hshift'  : 10.0 * cfg.dose,
        'sshift'  : -31.16 * cfg.dose,
        'htaubase': tauhmax + tauhmax * (2.0 - 1) * cfg.dose,
        'staubase': tausmax - tausmax * (1 - 0.986) * cfg.dose }

if (cfg.drug == 6):
    # diazepam
    print("diazepam dose: ", cfg.dose)
    gabaapercent = 200

PYcellRule['secs']['soma']['mechs']['inak2005'].update(cellRule)
TCcellRule['secs']['soma']['mechs']['inak2005'].update(cellRule)
REcellRule['secs']['soma']['mechs']['inak2005'].update(cellRule)
INcellRule['secs']['soma']['mechs']['inak2005'].update(cellRule)
INcellRule['secs']['soma']['mechs']['inak2005mut'].update(cellRule)

PYcellRule['secs']['soma']['vinit']=v_init
netParams.cellParams['PYrule'] = PYcellRule

TCcellRule['secs']['soma']['vinit']=v_init
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
#netParams.stimSourceParams['Input_1'] = {'type': 'IClamp', 'del': stimtime, 'dur': 100, 'amp': 0.7}
# smallPY=1
#netParams.stimTargetParams['Input_1->PY'] = {'source': 'Input_1', 'sec':'soma', 'loc': 0.5, 
#                                              'conds': {'pop':'PY', 'cellList': [i*int(ncorticalcells/5-1)+11 for i in range(int(ncorticalcells/20))]}}

###############################################################################
# Connectivity parameters
###############################################################################

####################### intra cortical projections ############################
divergence = int(ncorticalcells/nthalamiccells) # which is 1 right now
cLcortical = mkConnList( ncorticalcells, narrowradius)                                #cortical -> cortical projections
cLthalamic = mkConnList( nthalamiccells, narrowradius)                                #thalamic -> thalamic projections
cLcortthal = mkConnListCT( ncorticalcells, nthalamiccells, wideradius, divergence)    #cortical -> thalamic projections
cLthalcort = mkConnListTC( nthalamiccells, ncorticalcells, wideradius, divergence)    #thalamic -> cortical projections

#######################      IN connectivity       ############################ 
###### handled slightly differently, with larger population of IN cells  ######

INPYconnlist = mkConnListIN( ncorticalcells, narrowradius )                           #IN connections with instantiation matching original model
# INPYconnlist = cLcortical + [ [x + 100, y] for x, y in cLcortical ]               #order of instantiation matters when it comes to nonlinear receptors
ININconnlist = [ [ x, x + 100] for x in range(100) ] + [ [ x + 100, x] for x in range(100) ] 
PYINconnlist = cLcortical + [ [x, y + 100] for x, y in cLcortical ]

###########################################################
##   Glutamate AMPA receptors in synapses from TC to RE  ##
###########################################################

netParams.connParams['TC->RE'] = {
    'preConds': {'popLabel': 'TC'}, 
    'postConds': {'popLabel': 'RE'},
    'weight': 0.2/nTCRE,         # (Destexhe, 1998)  
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'AMPA_S',
    'connList': cLthalamic}
    

###########################################################
##   GABAa receptors in intra-RE synapses                ##
###########################################################

netParams.connParams['RE->RE'] = {
    'preConds': {'popLabel': 'RE'}, 
    'postConds': {'popLabel': 'RE'},
    'weight': 0.2/nRERE,            # (Destexhe, 1998)
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'sec': 'soma',
    'synMech': 'GABAA_S',
    'connList': cLthalamic} 

###########################################################
##   GABAa receptors in in synapses from RE to TC cells  ##
###########################################################

netParams.connParams['RE->TC_GABAA'] = {
    'preConds': {'popLabel': 'RE'}, 
    'postConds': {'popLabel': 'TC'},
    'weight': gabaapercent*0.02/nRETC,                    # (Destexhe, 1998)
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'GABAA_S',
    'connList': cLthalamic}

###########################################################
##   GABAb receptors in in synapses from RE to TC cells  ##
###########################################################


netParams.connParams['RE->TC_GABAB'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'RE'}, 
    'postConds': {'popLabel': 'TC'},
    'weight': 1,
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'GABAB_S2',
    'connList': cLthalamic}


###########################################################
##   Glutamate AMPA receptors in synapses from PY to PY  ##
###########################################################

netParams.connParams['PY->PY_AMPA'] = {
    'preConds': {'popLabel': 'PY'}, 
    'postConds': {'popLabel': 'PY'},
    'weight': 0.6/nPYPY,            # (Destexhe, 1998)
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'AMPA_S_PYPY',
    'connList': cLcortical}
    

###########################################################
##   Glutamate AMPA receptors in synapses from PY to IN  ##
###########################################################
     
netParams.connParams['PY->IN_AMPA'] = {
    'preConds': {'popLabel': 'PY'}, 
    'postConds': {'popLabel': 'IN'},     
    'weight': 0.2/nPYIN,            # (Destexhe, 1998)       
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'AMPA_S',
    'connList': PYINconnlist}
    

###########################################################
##   GABAa receptors in synapses from IN to PY cells     ##
###########################################################


netParams.connParams['IN->PY_GABAA'] = {
    'preConds': {'popLabel': 'IN'}, 
    'postConds': {'popLabel': 'PY'},
    'weight': gabaapercent*0.3/nINPY,         # (Destexhe, 1998)
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'GABAA_S',
    'connList': INPYconnlist}

###########################################################
##   GABAb receptors in in synapses from IN to PY cells  ##
###########################################################

netParams.connParams['IN->PY_GABAB'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'IN'}, 
    'postConds': {'popLabel': 'PY'},
    'weight': 1,
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'GABAB_S1',
    'connList': INPYconnlist}


###########################################################
##   GABAa receptors in synapses from IN to IN cells     ##
###########################################################


netParams.connParams['IN->IN_GABAA'] = {
    'preConds': {'popLabel': 'IN'}, 
    'postConds': {'popLabel': 'IN'},
    'weight': 0,               # ININa*1/(N_IN*IN_IN_GABAA_Prob+1),       
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'GABAA_S',
    'connList': ININconnlist}

###########################################################
##   Glutamate AMPA receptors in synapses from PY to RE  ##
###########################################################

netParams.connParams['PY->RE'] = {
    'preConds': {'popLabel': 'PY'}, 
    'postConds': {'popLabel': 'RE'},  
    'weight': 1.2/nPYRE,           # (Destexhe, 1998)  
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'AMPA_S',
    'connList': cLcortthal}
     

###########################################################
##   Glutamate AMPA receptors in synapses from PY to TC  ##
###########################################################

netParams.connParams['PY->TC'] = {
    'preConds': {'popLabel': 'PY'}, 
    'postConds': {'popLabel': 'TC'},   
    'weight': 0.01/nPYTC,           # (Destexhe, 1998)    
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'AMPA_S',
    'connList': cLcortthal}
       

###########################################################
##   Glutamate AMPA receptors in synapses from TC to PY  ##
###########################################################

netParams.connParams['TC->PY'] = {
    'preConds': {'popLabel': 'TC'}, 
    'postConds': {'popLabel': 'PY'},   
    'weight': 1.2/nTCPY,        # (Destexhe, 1998)   
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'AMPA_S',
    'connList': cLthalcort}
    

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
#    #'probability': '1.0 if dist_x <= narrows*xspacing else 0.0'}   
#    #'probability': TC_IN_AMPA_Prob}
#    'connList': smallWorldConn(N_TC,N_IN,pThlCrx,TC_IN_AMPA_Prob)}
#