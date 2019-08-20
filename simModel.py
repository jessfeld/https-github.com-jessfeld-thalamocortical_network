# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 15:57:43 2017

@author: rt
"""

#from cellModels import sINpy
import numpy as np
from neuron import h, gui
from math import sin, cos, pi
from matplotlib import pyplot

from neuronpy.graphics import spikeplot
from neuronpy.util import spiketrain

def ncon(diam, ncells):       # function to get the number of connections 
    nc = 2 * diam + 1
    if nc>ncells: nc = ncells
    return nc

def assign_synapses(gRERE_GABAA,gRETC_GABAA,gRETC_GABAB,gTCRE_AMPA,gPYPY_AMPA,gPYIN_AMPA,gINPY_GABAA,gINPY_GABAB,gPYRE_AMPA,gPYTC_AMPA,gTCPY_AMPA,gTCIN_AMPA): # procedure to assign syn conductances 
    # params: 1=intraRE (RERE), 2=GABAa in TC (RETC),
    # 3=GABAb in TC, 4=AMPA in RE (TCRE)
    # 5=PYPY 6=PYIN 7=GABAa INPY
    # 8=GABAb INPY 9=PYRE 10=PYTC
    # 11=TCPY 12=TCIN

    print "nRERE:", nRERE, "nRETCa:", nRETCa, "nRETCb:", nRETCb, "nTCRE:", nTCRE, "nPYPY:", nPYPY, "nINPYa:", nINPYa, "nINPYb:", nINPYb, "nPYRE:", nPYRE, "nPYTC:", nPYTC, "nTCPY:", nTCPY, "nTCIN:", nTCIN
    for i in range(nthalamiccells):
        for j in range(int(RE[i].REgabaalist.count())):
            RE[i].REgabaalist[j].weight[0] = gRERE_GABAA / nRERE               
    
        for j in range(int(TC[i].REgabaalist.count())):
            TC[i].REgabaalist[j].weight[0] = gRETC_GABAA / nRETCa
    
        for j in range(int(TC[i].gababpost.count())):
            TC[i].gababpost.object(j).gmax = gRETC_GABAB / nRETCb
            #TC[i].REgabablist[j].weight[0] = gRETC_GABAB / nRETCb
        
        for j in range(int(RE[i].TClist.count())):
            RE[i].TClist[j].weight[0] = gTCRE_AMPA / nTCRE
        
        for j in range(int(RE[i].PYlist.count())):  		
            RE[i].PYlist[j].weight[0] = gPYRE_AMPA / nPYRE
        
        for j in range(int(TC[i].PYlist.count())):  
            TC[i].PYlist[j].weight[0] = gPYTC_AMPA / nPYTC
        
    for i in range(ncorticalcells):
        for j in range(int(PY[i].PYlist.count())):
            PY[i].PYlist[j].weight[0] = gPYPY_AMPA / nPYPY
        
        for j in range(int(IN[i].PYlist.count())):
            IN[i].PYlist[j].weight[0] = gPYIN_AMPA / nPYIN
        
        for j in range(int(PY[i].INgabaalist.count())):
            PY[i].INgabaalist[j].weight[0] = gINPY_GABAA / nINPYa
        
        for j in range(int(PY[i].INgabablist.count())):
            PY[i].gababpost[j].gmax = gINPY_GABAB / nINPYb
            #PY[i].INgabablist[j].weight[0] = gINPY_GABAB / nINPYb
        
        for j in range(int(PY[i].TClist.count())):
            PY[i].TClist[j].weight[0]  = gTCPY_AMPA / nTCPY
        
        for j in range(int(IN[i].TClist.count())):
            IN[i].TClist[j].weight[0] = gTCIN_AMPA / nTCIN


def printWeight(indx):
    # intra-cortical
    print "PYPY-AMPA_weight = ", PY[indx].PYlist.object(0).weight[0]
    print "PYIN-AMPA_weight = ", IN[indx].PYlist.object(0).weight[0]
    print "INPY-GABAA_weight = ", PY[indx].INgabaalist.object(0).weight[0]
    print "INPY-GABAB_weight = ", PY[indx].gababpost.object(0).gmax
    #print "INPY-GABAB_weight = ", PY[indx].INgabablist.object(0).weight[0]
    
    # intra-thalamic
    print "TCRE-AMPA_weight = ", RE[indx].TClist.object(0).weight[0]
    print "RETC-GABAA_weight = ", TC[indx].REgabaalist.object(0).weight[0]
    print "RETC-GABAB_weight = ", TC[indx].gababpost.object(0).gmax
    #print "RETC-GABAB_weight = ", TC[indx].REgabablist.object(0).weight[0]
    print "RERE-GABAA_weight = ", RE[indx].REgabaalist.object(0).weight[0]
    
    # thalamo-cortical 
    print "PYTC-AMPA_weight = ", TC[indx].PYlist.object(0).weight[0]
    print "PYRE-AMPA_weight = ", RE[indx].PYlist.object(0).weight[0]
    print "TCPY-AMPA_weight = ", PY[indx].TClist.object(0).weight[0]
    print "TCIN-AMPA_weight = ", IN[indx].TClist.object(0).weight[0]

def printTCinfo(indx):
    index=indx
    print " "
    print "----- TC Parameter values (index=",index,") -------"
    print " "
    
    print "diam=",TC[index].soma.diam,"\t L=",TC[index].soma.L," \t Cm=",TC[index].soma.cm," \t Ra=",TC[index].soma.Ra
    print "kl_gmax=",TC[index].kl.gmax,"\t Erev_kleak="#,TC[index].Erev_kleak
    print "g_pas=",TC[index].soma.g_pas," \t e_pas=",TC[index].soma.e_pas," \t vinit=", TC[index].soma(0.5).v
    print "gnabar_hh2=",TC[index].soma.gnabar_hh2," \t ena=", TC[index].soma.ena
    print "gkbar_hh2=",TC[index].soma.gkbar_hh2," \t ek=",TC[index].soma.ek," \t vtraub_hh2=", TC[index].soma.vtraub_hh2
    print "gcabar_it=",TC[index].soma.gcabar_it," \t eca=",TC[index].soma.eca," \t cai=", TC[index].soma.cai," \t cao=", TC[index].soma.cao
    print "shift_it=",TC[index].soma.shift_it," \t taubase_it=",TC[index].soma.taubase_it
    print "depth_cad=",TC[index].soma.depth_cad," \t taur_cad=",TC[index].soma.taur_cad," \t cainf_cad=", TC[index].soma.cainf_cad," \t kt_cad=", TC[index].soma.kt_cad
    print "ghbar_iar=",TC[index].soma.ghbar_iar," \t eh=",TC[index].soma.eh," \t nca_iar=", TC[index].soma.nca_iar," \t k2_iar=", TC[index].soma.k2_iar
    print "cac_iar=",TC[index].soma.cac_iar," \t nexp_iar=",TC[index].soma.nexp_iar," \t k4_iar=", TC[index].soma.k4_iar," \t Pc_iar=", TC[index].soma.Pc_iar," \t ginc_iar=", TC[index].soma.ginc_iar

    print " "
    print "----- TC Parameter values (end) -------"
    print " "


def printREinfo(indx):
    index=indx
    print " "
    print "------ RE Parameter values (index=",index,") ---------"
    print " "
    
    print "diam=",RE[index].soma.diam,"\t L=",RE[index].soma.L," \t Cm=",RE[index].soma.cm," \t Ra=",RE[index].soma.Ra
    print "g_pas=",RE[index].soma.g_pas," \t e_pas=",RE[index].soma.e_pas," \t vinit=", RE[index].soma(0.5).v
    print "gnabar_hh2=",RE[index].soma.gnabar_hh2," \t ena=", RE[index].soma.ena
    print "gkbar_hh2=",RE[index].soma.gkbar_hh2," \t ek=",RE[index].soma.ek," \t vtraub_hh2=", RE[index].soma.vtraub_hh2
    print "gcabar_it2=",RE[index].soma.gcabar_it2," \t eca=",RE[index].soma.eca," \t cai=", RE[index].soma.cai," \t cao=", RE[index].soma.cao
    print "shift_it2=",RE[index].soma.shift_it2," \t taubase_it2=",RE[index].soma.taubase_it2," \t qm_it2=", RE[index].soma.qm_it2," \t qh_it2=", RE[index].soma.qh_it2
    print "depth_cad=",RE[index].soma.depth_cad," \t taur_cad=",RE[index].soma.taur_cad," \t cainf_cad=", RE[index].soma.cainf_cad," \t kt_cad=", RE[index].soma.kt_cad
    
    print " "
    print "-------- RE Parameter values (end) --------"
    print " "

def printPYinfo(indx):
    index=indx
    print " "
    print "------ PY Parameter values (index=",index,") ---------"
    print " "
    
    print "diam=",PY[index].soma.diam,"\t L=",PY[index].soma.L," \t Cm=",PY[index].soma.cm," \t Ra=",PY[index].soma.Ra
    print "g_pas=",PY[index].soma.g_pas," \t e_pas=",PY[index].soma.e_pas," \t vinit=", PY[index].soma(0.5).v
    print "gnabar_hh2=",PY[index].soma.gnabar_hh2," \t ena=", PY[index].soma.ena
    print "gkbar_hh2=",PY[index].soma.gkbar_hh2," \t ek=",PY[index].soma.ek," \t vtraub_hh2=", PY[index].soma.vtraub_hh2
    print "gkbar_im=",PY[index].soma.gkbar_im," \t taumax_im=",PY[index].soma.taumax_im
    
    print " "
    print "-------- PY Parameter values (end) --------"
    print " "

def printINinfo(indx):
    index=indx
    print " "
    print "------ IN Parameter values (index=",index,") ---------"
    print " "
    
    print "diam=",IN[index].soma.diam,"\t L=",IN[index].soma.L," \t Cm=",IN[index].soma.cm," \t Ra=",IN[index].soma.Ra
    print "g_pas=",IN[index].soma.g_pas," \t e_pas=",IN[index].soma.e_pas," \t vinit=", IN[index].soma(0.5).v
    print "gnabar_hh2=",IN[index].soma.gnabar_hh2," \t ena=", IN[index].soma.ena
    print "gkbar_hh2=",IN[index].soma.gkbar_hh2," \t ek=",IN[index].soma.ek," \t vtraub_hh2=", IN[index].soma.vtraub_hh2
    
    print " "
    print "-------- IN Parameter values (end) --------"
    print " "

#---------------------------------------------------------------------------
#  Code for dealing with field potentials
#---------------------------------------------------------------------------

def xfield(Re, x, Ni):
    # Re, x is distance from nearest neuron, Ni is neuron to which probe is closest
    # assumes field comes from PY neurons, which are in a row spaced 20um apart
    total_field = 0
    #Re = $1
    #x = $2
    #Ni = $3
    
    for i in np.arange(fieldlower, fieldupper+1):
        tmp = 0
        for j in range(int(PY[i].gababpost.count())):
            tmp = tmp + PY[i].gababpost.object(j).i
        tmp = tmp + PY[i].gabaapost.i  + PY[i].soma.ik_im + PY[i].ampapostPY.i + PY[i].ampapostTC.i
        #tmp = tmp + PY[i].gababpost.i + PY[i].gabaapost.i  + PY[i].soma.ik_im + PY[i].ampapostPY.i + PY[i].ampapostTC.i
        total_field = total_field + tmp / np.sqrt(x**2 + 400*(Ni-i)**2)
    
    #print "t=", h.t, "total_field = ", total_field * Re/4./np.pi
    return total_field * Re/4./np.pi


ncorticalcells = 100
nthalamiccells = 100
narrowdiam = 5
widediam = 10

fieldlower = 30
fieldupper = 70
fielddist = 50
field = []

watchneuron = 11
axondelay = 0

smallPY = 1
stimtime = 10050

gabaapercent = 1*0
gababpercent = 1

randInit = False
selfConn = False

PYPY    = 1*1
PYIN    = 1*1
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

celsius = 36
v_init = -70

randvolt = h.Random()
randvolt.uniform(-80,-65)

recncs = []

#----------------------------------------------------------------------------
#  Create Cells
#----------------------------------------------------------------------------
print " "
print "<<==================================>>"
print "<<            CREATE CELLS          >>"
print "<<==================================>>"
print " "

h.load_file("sPY.tem")
#h.xopen("sPY.tem")      # read geometry file
PY = []     # create PY cells
PYVtrace = [] 
for i in range(ncorticalcells):
    cell = h.sPY()
    #cell.soma.v = randvolt.repick()
    PY.append(cell)

h.load_file("sIN.tem")
#h.xopen("sIN.tem")      # read geometry file
IN = []     # create IN cells
INVtrace = [] 
for i in range(ncorticalcells):
    cell = h.sIN()
    #cell.soma.v = randvolt.repick()
    IN.append(cell)

h.load_file("TC.tem")
#h.xopen("TC.tem")
TC = []     # create TC cells
TCVtrace = [] 
for i in range(nthalamiccells):
    cell = h.sTC()
    #cell.soma.v = randvolt.repick()
    TC.append(cell)

h.load_file("RE.tem")
#h.xopen("RE.tem")
RE = []     # create RE cells
REVtrace = [] 
for i in range(nthalamiccells):
    cell = h.sRE()
    #cell.soma.v = randvolt.repick()
    RE.append(cell)


#----------------------------------------------------------------------------
# set up recording stuff
#----------------------------------------------------------------------------

PYtimevec = h.Vector()
PYidvec = h.Vector()
INtimevec = h.Vector()
INidvec = h.Vector()
REtimevec = h.Vector()
REidvec = h.Vector()
TCtimevec = h.Vector()
TCidvec = h.Vector()


######################## intra Cortical synapses #############################
# -----------------------------------------------------
#   Glutamate AMPA receptors in synapses from PY to PY
# -----------------------------------------------------
diamPYPY = narrowdiam		# diameter of connectivity for PY->PY
nPYPY = ncon(diamPYPY, ncorticalcells)	# nb of PY cells receiving synapses from one PY cell

for i in range(ncorticalcells):
    for j in range(i-diamPYPY,i+diamPYPY+1):
        jbound = j
        if jbound < 0: jbound = abs(j) - 1
        if jbound > ncorticalcells-1: jbound = 2 * ncorticalcells - jbound - 1 
        if i!=jbound or selfConn: 
            src = PY[i]
            tgt = PY[jbound]
            syn = tgt.ampapostPY #h.AMPA_S(tgt.soma(0.5))
            syn.Alpha = 0.94
            syn.Beta = 0.18
            syn.Cmax = 0.5
            syn.Cdur = 0.3
            syn.Erev = 0
            nc = h.NetCon(src.soma(0.5)._ref_v, syn, 0, axondelay, 1, sec=src.soma)
            #nc.weight[i] = 1
            #nc.delay = axondelay
            #nc.threshold = 0
            #nc.record(PYtimevec, PYidvec, i)
            tgt.PYlist.append(nc)
            #print "[%d,%d], "%(i,jbound)

print " "
print "<< ",int(PY[0].PYlist.count())," AMPA-MEDIATED SYNAPTIC CONTACTS FROM PY TO PY >>"
print " "


#----------------------------------------------------------------------------
#  Glutamate AMPA receptors in synapses from PY to IN
#----------------------------------------------------------------------------

diamPYIN = narrowdiam		# diameter of connectivity for PY->IN
nPYIN = ncon(diamPYIN, ncorticalcells)	

for i in range(ncorticalcells):
    for j in range(i-diamPYIN,i+diamPYIN+1):
        jbound = j
        if jbound < 0: jbound = abs(j) - 1
        if jbound > ncorticalcells-1: jbound = 2 * ncorticalcells - jbound - 1 
        src = PY[i]
        tgt = IN[jbound]
        syn = tgt.ampapost
        syn.Alpha = 0.94
        syn.Beta = 0.18
        syn.Cmax = 0.5
        syn.Cdur = 0.3
        syn.Erev = 0
        nc = h.NetCon(src.soma(0.5)._ref_v, syn, 0, axondelay, 1, sec=src.soma)
        tgt.PYlist.append(nc)
        #print "[%d,%d], "%(i,jbound)

print " "
print "<< ",int(IN[0].PYlist.count())," AMPA-MEDIATED SYNAPTIC CONTACTS FROM PY TO IN >>"
print " "

#--------------------------------------------------
#  GABAa receptors in synapses from IN to PY cells
#--------------------------------------------------

diamINPYa = narrowdiam		# diameter of connectivity from IN->PY
nINPYa = ncon(diamINPYa,ncorticalcells)	

for i in range(ncorticalcells):
    for j in range(i-diamINPYa,i+diamINPYa+1):
        jbound = j
        if jbound < 0: jbound = abs(j) - 1
        if jbound > ncorticalcells-1: jbound = 2 * ncorticalcells - jbound - 1 
        src = IN[i]
        tgt = PY[jbound]
        syn = tgt.gabaapost
        syn.Alpha = 20		# from diffusion model
        syn.Beta = 0.162
        syn.Cmax = 0.5
        syn.Cdur = 0.3
        syn.Erev = -85		# Rinzel's Erev
        nc = h.NetCon(src.soma(0.5)._ref_v, syn, 0, axondelay, 1, sec=src.soma)
        tgt.INgabaalist.append(nc)
        #print "[%d,%d], "%(i,jbound)
	
print " "
print "<< ",int(PY[0].INgabaalist.count())," GABAa-MEDIATED SYNAPTIC CONTACTS FROM IN TO PY >>"
print " "

#--------------------------------------------------
#  GABAb receptors in synapses from IN to PY cells
#--------------------------------------------------
diamINPYb = narrowdiam		# diameter of connectivity from IN->PY
nINPYb = ncon(diamINPYb,ncorticalcells)	

for i in range(ncorticalcells):
    for j in range(i-diamINPYb,i+diamINPYb+1):
        jbound = j
        if jbound < 0: jbound = abs(j) - 1
        if jbound > ncorticalcells-1: jbound = 2 * ncorticalcells - jbound - 1 
        src = IN[i]
        tgt = PY[jbound]
        syn = h.GABAb_S(tgt.soma(0.5))
        syn.K1	= 0.09    #	(/ms mM) forward binding to receptor
        syn.K2	= 0.0012  #	(/ms)	backward (unbinding)of receptor
        syn.K3	= 0.18   # 0.098 # (/ms)	rate of G-protein production
        syn.K4	= 0.034  #	(/ms)	rate of G-protein decay  -  larger number = slower decay?
        syn.KD	= 100	#	dissociation constant of K+ channel
        syn.n	= 4	      # of binding sites of G-protein on K+
        syn.Cmax = 0.5		# short pulses
        syn.Cdur = 0.3
        syn.Erev = -95	#	(mV)	reversal potential (E_K)
        tgt.gababpost.append(syn) 
        nc = h.NetCon(src.soma(0.5)._ref_v, syn, 0, axondelay, 1, sec=src.soma)
        tgt.INgabablist.append(nc)
        #print "[%d,%d], "%(i,jbound)

print " "
print "<< ",int(PY[0].INgabablist.count())," GABAb-MEDIATED SYNAPTIC CONTACTS FROM IN TO PY >>"
print " "

"""
#--------------------------------------------------
#  GABAb receptors in synapses from IN to PY cells
#--------------------------------------------------
diamINPYb = narrowdiam		# diameter of connectivity from IN->PY
nINPYb = ncon(diamINPYb,ncorticalcells)	

for i in range(ncorticalcells):
    for j in range(i-diamINPYb,i+diamINPYb+1):
        jbound = j
        if jbound < 0: jbound = abs(j) - 1
        if jbound > ncorticalcells-1: jbound = 2 * ncorticalcells - jbound - 1 
        src = IN[i]
        tgt = PY[jbound]
        syn = tgt.gababpost
        syn.K1	= 0.09    #	(/ms mM) forward binding to receptor
        syn.K2	= 0.0012  #	(/ms)	backward (unbinding)of receptor
        syn.K3	= 0.18   # 0.098 # (/ms)	rate of G-protein production
        syn.K4	= 0.034  #	(/ms)	rate of G-protein decay  -  larger number = slower decay?
        syn.KD	= 100	#	dissociation constant of K+ channel
        syn.n	= 4	      # of binding sites of G-protein on K+
        syn.Cmax = 0.5		# short pulses
        syn.Cdur = 0.3
        syn.Erev = -95	#	(mV)	reversal potential (E_K)
        nc = h.NetCon(src.soma(0.5)._ref_v, syn, 0, axondelay, 1, sec=src.soma)
        tgt.INgabablist.append(nc)
        #print "[%d,%d], "%(i,jbound)

print " "
print "<< ",int(PY[0].INgabablist.count())," GABAb-MEDIATED SYNAPTIC CONTACTS FROM IN TO PY >>"
print " "
"""

######################## intra Thalamic synapses ############################
#----------------------------------------------------------------------------
#  Glutamate AMPA receptors in synapses from TC to RE
#----------------------------------------------------------------------------

diamTCRE = narrowdiam		# diameter of connectivity for TC->RE
nTCRE = ncon(diamTCRE,nthalamiccells)	# nb of RE cells recampapost, PYlist, TClisteiving synapses from one TC cell

for i in range(nthalamiccells):
    for j in range(i-diamTCRE,i+diamTCRE+1):
        jbound = j
        if jbound < 0: jbound = abs(j) - 1
        if jbound > ncorticalcells-1: jbound = 2 * ncorticalcells - jbound - 1 
        src = TC[i]
        tgt = RE[jbound]
        syn = tgt.ampapost 
        syn.Alpha = 0.94
        syn.Beta = 0.18
        syn.Cmax = 0.5
        syn.Cdur = 0.3
        syn.Erev = 0
        nc = h.NetCon(src.soma(0.5)._ref_v, syn, 0, axondelay, 1, sec=src.soma)
        tgt.TClist.append(nc)
        #print "[%d,%d], "%(i,jbound)

print " "
print "<< ",int(RE[0].TClist.count())," AMPA-MEDIATED SYNAPTIC CONTACTS FROM TC TO RE >>"
print " "

#---------------------------------------
#  GABAa receptors in intra-RE synapses
#---------------------------------------

diamRERE = narrowdiam		# diameter of connectivity for RE->RE
nRERE = ncon(diamRERE,nthalamiccells)	# nb of RE cells receiving synapses from one RE cell

for i in range(nthalamiccells):
    for j in range(i-diamRERE,i+diamRERE+1):
        jbound = j
        if jbound < 0: jbound = abs(j) - 1
        if jbound > ncorticalcells-1: jbound = 2 * ncorticalcells - jbound - 1 
        if i!=jbound or selfConn:
            src = RE[i]
            tgt = RE[jbound]
            syn = tgt.gabaapost 
            syn.Alpha = 20		# from diffusion model
            syn.Beta = 0.162
            syn.Cmax = 0.5		# short pulses
            syn.Cdur = 0.3
            syn.Erev = -85		# Rinzel's Erev
            nc = h.NetCon(src.soma(0.5)._ref_v, syn, 0, axondelay, 1, sec=src.soma)
            tgt.REgabaalist.append(nc)
            #print "[%d,%d], "%(i,jbound)
	
print " "
print "<< ",int(RE[0].REgabaalist.count())," GABAa-MEDIATED SYNAPTIC CONTACTS FROM RE TO RE >>"
print " "

#--------------------------------------------------
#  GABAa receptors in synapses from RE to TC cells
#--------------------------------------------------

diamRETCa = narrowdiam		# diameter of connectivity from RE->TC
nRETCa = ncon(diamRETCa,nthalamiccells)	# nb of RE cells receiving synapses from one TC cell

for i in range(nthalamiccells):
    for j in range(i-diamRETCa,i+diamRETCa+1):
        jbound = j
        if jbound < 0: jbound = abs(j) - 1
        if jbound > ncorticalcells-1: jbound = 2 * ncorticalcells - jbound - 1 
        src = RE[i]
        tgt = TC[jbound]
        syn = tgt.gabaapost 
        syn.Alpha = 20		# from diffusion model
        syn.Beta = 0.162
        syn.Cmax = 0.5		# short pulses
        syn.Cdur = 0.3
        syn.Erev = -85		# Rinzel's Erev
        nc = h.NetCon(src.soma(0.5)._ref_v, syn, 0, axondelay, 1, sec=src.soma)
        tgt.REgabaalist.append(nc)
        #print "[%d,%d], "%(i,jbound)
	
print " "
print "<< ",int(TC[jbound].REgabaalist.count())," GABAa-MEDIATED SYNAPTIC CONTACTS FROM RE TO TC >>"
print " "

#--------------------------------------------------
#  GABAb receptors in synapses from RE to TC cells
#--------------------------------------------------

diamRETCb = narrowdiam		# diameter of connectivity from RE->TC
nRETCb = ncon(diamRETCb,nthalamiccells)	# nb of RE cells receiving synapses from one TC cell

#objectvar gababsyn

for i in range(nthalamiccells):
    for j in range(i-diamRETCb,i+diamRETCb+1):
        jbound = j
        if jbound < 0: jbound = abs(j) - 1
        if jbound > ncorticalcells-1: jbound = 2 * ncorticalcells - jbound - 1 
        src = RE[i]
        tgt = TC[jbound]
        syn = h.GABAb_S(tgt.soma(0.5))
        syn.K1	= 0.09    #	(/ms mM) forward binding to receptor
        syn.K2	= 0.0012  #	(/ms)	backward (unbinding)of receptor
        syn.K3	= 0.18   # 0.098 # (/ms)	rate of G-protein production
        syn.K4	= 0.034  #	(/ms)	rate of G-protein decay  -  larger number = slower decay?
        syn.KD	= 100	#	dissociation constant of K+ channel
        syn.n	= 4	      # of binding sites of G-protein on K+
        syn.Cmax = 0.5		# short pulses
        syn.Cdur = 0.3
        syn.Erev = -95	#	(mV)	reversal potential (E_K)
        tgt.gababpost.append(syn)
        nc = h.NetCon(src.soma(0.5)._ref_v, syn, 0, axondelay, 1, sec=src.soma)
        tgt.REgabablist.append(nc)
        #print "[%d,%d], "%(i,jbound)
	
print " "
print "<< ",int(TC[0].REgabablist.count())," GABAb-MEDIATED SYNAPTIC CONTACTS FROM RE TO TC >>"
print " "

"""
#--------------------------------------------------
#  GABAb receptors in synapses from RE to TC cells
#--------------------------------------------------

diamRETCb = narrowdiam		# diameter of connectivity from RE->TC
nRETCb = ncon(diamRETCb,nthalamiccells)	# nb of RE cells receiving synapses from one TC cell

#objectvar gababsyn

for i in range(nthalamiccells):
    for j in range(i-diamRETCb,i+diamRETCb+1):
        jbound = j
        if jbound < 0: jbound = abs(j) - 1
        if jbound > ncorticalcells-1: jbound = 2 * ncorticalcells - jbound - 1 
        src = RE[i]
        tgt = TC[jbound]
        syn = tgt.gababpost
        syn.K1	= 0.09    #	(/ms mM) forward binding to receptor
        syn.K2	= 0.0012  #	(/ms)	backward (unbinding)of receptor
        syn.K3	= 0.18   # 0.098 # (/ms)	rate of G-protein production
        syn.K4	= 0.034  #	(/ms)	rate of G-protein decay  -  larger number = slower decay?
        syn.KD	= 100	#	dissociation constant of K+ channel
        syn.n	= 4	      # of binding sites of G-protein on K+
        syn.Cmax = 0.5		# short pulses
        syn.Cdur = 0.3
        syn.Erev = -95	#	(mV)	reversal potential (E_K)
        #syn.gmax = gRETC_GABAB / nRETCb
        nc = h.NetCon(src.soma(0.5)._ref_v, syn, 0, axondelay, 1, sec=src.soma)
        tgt.REgabablist.append(nc)
        #print "[%d,%d], "%(i,jbound)
	
print " "
print "<< ",int(TC[0].REgabablist.count())," GABAb-MEDIATED SYNAPTIC CONTACTS FROM RE TO TC >>"
print " "
"""

######################## Thalamo-Cortical synapses ############################
#----------------------------------------------------------------------------
#  Glutamate AMPA receptors in synapses from PY to TC
#----------------------------------------------------------------------------

diamPYTC = widediam	
nPYTC = ncon(diamPYTC,nthalamiccells)	

for i in range(ncorticalcells):
    for j in range(i-diamPYTC,i+diamPYTC+1):
        jbound = j
        if jbound < 0: jbound = abs(j) - 1
        if jbound > ncorticalcells-1: jbound = 2 * ncorticalcells - jbound - 1 
        src = PY[i]
        tgt = TC[jbound]
        syn = tgt.ampapost 
        syn.Alpha = 0.94
        syn.Beta = 0.18
        syn.Cmax = 0.5
        syn.Cdur = 0.3
        syn.Erev = 0
        nc = h.NetCon(src.soma(0.5)._ref_v, syn, 0, axondelay, 1, sec=src.soma)
        tgt.PYlist.append(nc)
        #print "[%d,%d], "%(i,jbound)

print " "
print "<< ",int(TC[0].PYlist.count())," AMPA-MEDIATED SYNAPTIC CONTACTS FROM PY TO TC >>"
print " "


#----------------------------------------------------------------------------
#  Glutamate AMPA receptors in synapses from PY to RE
#----------------------------------------------------------------------------

diamPYRE = widediam		
nPYRE = ncon(diamPYRE,nthalamiccells)	
divergence = ncorticalcells / nthalamiccells

for i in range(ncorticalcells):
    for j in range(i/divergence-diamPYRE,i/divergence+diamPYRE+1):
        jbound = j
        if jbound < 0: jbound = abs(j) - 1
        if jbound > ncorticalcells-1: jbound = 2 * ncorticalcells - jbound - 1 
        src = PY[i]
        tgt = RE[jbound]
        syn = tgt.ampapost 
        syn.Alpha = 0.94
        syn.Beta = 0.18
        syn.Cmax = 0.5
        syn.Cdur = 0.3
        syn.Erev = 0
        nc = h.NetCon(src.soma(0.5)._ref_v, syn, 0, axondelay, 1, sec=src.soma)
        tgt.PYlist.append(nc)
        #print "[%d,%d], "%(i,jbound)

print " "
print "<< ",int(RE[0].PYlist.count())," AMPA-MEDIATED SYNAPTIC CONTACTS FROM PY TO RE >>"
print " "

#----------------------------------------------------------------------------
#  Glutamate AMPA receptors in synapses from TC to PY
#----------------------------------------------------------------------------

diamTCPY = widediam		
nTCPY = ncon(diamTCPY,ncorticalcells)	
divergence = ncorticalcells / nthalamiccells

for i in range(nthalamiccells):
    for j in np.arange(divergence*(i-diamTCPY),divergence*(i+diamTCPY+1),divergence):
        jbound = j
        if jbound < 0: jbound = abs(j) - divergence
        if jbound > ncorticalcells-1: jbound = 2 * ncorticalcells - jbound - divergence 
        # presynaptic is TC[i], postsynaptic is PY[j] 
        src = TC[i]
        tgt = PY[jbound+divergence/2]
        syn = tgt.ampapostTC 
        syn.Alpha = 0.94
        syn.Beta = 0.18
        syn.Cmax = 0.5
        syn.Cdur = 0.3
        syn.Erev = 0
        nc = h.NetCon(src.soma(0.5)._ref_v, syn, 0, axondelay, 1, sec=src.soma)
        tgt.TClist.append(nc)
        #print "[%d,%d], "%(i,jbound)

print " "
print "<< ",int(PY[0].TClist.count())," AMPA-MEDIATED SYNAPTIC CONTACTS FROM TC TO PY >>"
print " "

#----------------------------------------------------------------------------
#  Glutamate AMPA receptors in synapses from TC to IN
#----------------------------------------------------------------------------

diamTCIN = widediam		# diameter of connectivity for TC->IN
nTCIN = ncon(diamTCIN,ncorticalcells)	

divergence = ncorticalcells / nthalamiccells

for i in range(nthalamiccells):
    for j in np.arange(divergence*(i-diamTCIN),divergence*(i+diamTCIN+1),divergence):
        jbound = j
        if jbound < 0: jbound = abs(j) - divergence
        if jbound > ncorticalcells-1: jbound = 2 * ncorticalcells - jbound - divergence 
        # presynaptic is TC[i], postsynaptic is IN[j] 
        src = TC[i]
        tgt = IN[jbound+divergence/2]
        syn = tgt.ampapost 
        syn.Alpha = 0.94
        syn.Beta = 0.18
        syn.Cmax = 0.5
        syn.Cdur = 0.3
        syn.Erev = 0
        nc = h.NetCon(src.soma(0.5)._ref_v, syn, 0, axondelay, 1, sec=src.soma)
        tgt.TClist.append(nc)
        #print "[%d,%d], "%(i,jbound)

print " "
print "<< ",int(IN[0].TClist.count())," AMPA-MEDIATED SYNAPTIC CONTACTS FROM TC TO IN >>"
print " "


#---------------------------------------------------------------------------
#   Assign potassium leak and Ih current strengths in TC cells 
#---------------------------------------------------------------------------
if (randInit):
    rgh = h.Random()
    rk1 = h.Random()
    rgh.normal(17.5,0.0008)        #random number generator behaves weirdly for very small numbers, so multiply by 10^-6 below
    rk1.normal(40,0.003)
    
    # setup TC cells in resting mode (no spontaneous oscillation)
    for i in range(nthalamiccells):
        TC[i].soma.ghbar_iar = rgh.repick() * 1e-6   
        TC[i].kl.gmax = rk1.repick() * 1e-4
        print "TC(",i,") gh:",TC[i].soma.ghbar_iar," gmax:",TC[i].kl.gmax

#----------------------------------------------------------------------------
#  set up current stimulus to cells
#----------------------------------------------------------------------------

PYstim = []


if smallPY==1:
    #for i in range(ncorticalcells/20):
        #stim = h.IClamp(PY[i*(ncorticalcells/5)+9].soma(0.5))
    for i in range(ncorticalcells/20):
        print "PY(",(i*(ncorticalcells/5-1)+11),") current clamp"
        #stim = h.IClamp(0.5, sec=PY[i*(ncorticalcells/5-1)+11].soma)
        stim = h.IClamp(PY[i*(ncorticalcells/5-1)+11].soma(0.5))
        stim.delay = stimtime
        stim.dur = 100
        stim.amp = 0.7*0
        PYstim.append(stim)

"""    
stim = h.NetStim() # Make a new stimulator
syn_ = h.ExpSyn(PY[0].soma(0.5))
stim.number = 1
stim.start = 100
ncstim = h.NetCon(stim, syn_)
ncstim.delay = 1
ncstim.weight[0] = 1.5*3 # NetCon weight is a vector.
syn_.tau = 0.1
"""

h("objref nil")
for i in range(ncorticalcells):
    VtracePY = h.Vector()    # Membrane potential vector at soma
    VtracePY.record(PY[i].soma(0.5)._ref_v)
    PYVtrace.append(VtracePY)
    nc = h.NetCon(PY[i].soma(0.5)._ref_v, h.nil, sec=PY[i].soma)
    nc.record(PYtimevec, PYidvec, i+1)
    recncs.append(nc)
    #
    VtraceIN = h.Vector()
    VtraceIN.record(IN[i].soma(0.5)._ref_v)
    INVtrace.append(VtraceIN)
    nc = h.NetCon(IN[i].soma(0.5)._ref_v, h.nil, sec=IN[i].soma)
    nc.record(INtimevec, INidvec, i+1)
    recncs.append(nc)

for i in range(nthalamiccells):
    VtraceTC = h.Vector()
    VtraceTC.record(TC[i].soma(0.5)._ref_v)
    TCVtrace.append(VtraceTC)
    nc = h.NetCon(TC[i].soma(0.5)._ref_v, h.nil, sec=TC[i].soma)
    nc.record(TCtimevec, TCidvec, i+1)
    recncs.append(nc)
    #
    VtraceRE = h.Vector()
    VtraceRE.record(RE[i].soma(0.5)._ref_v)
    REVtrace.append(VtraceRE)
    nc = h.NetCon(RE[i].soma(0.5)._ref_v, h.nil, sec=RE[i].soma)
    nc.record(REtimevec, REidvec, i+1)
    recncs.append(nc)


t_vec = h.Vector()        # Time stamp vector
t_vec.record(h._ref_t)
#syn_i_vec = h.Vector()
#syn_i_vec.record(syn_._ref_i)

gabaapost = TC[0].gabaapost
GABAa0_i_vec = h.Vector()
GABAa0_i_vec.record(gabaapost._ref_i)
GABAa0_g_vec = h.Vector()
GABAa0_g_vec.record(gabaapost._ref_g)
GABAa0_gmax_vec = h.Vector()
GABAa0_gmax_vec.record(gabaapost._ref_gmax)
GABAa0_Ron_vec = h.Vector()
GABAa0_Ron_vec.record(gabaapost._ref_Ron)
GABAa0_Roff_vec = h.Vector()
GABAa0_Roff_vec.record(gabaapost._ref_Roff)

#gababpost = TC[0].gababpost
gababpost = TC[0].gababpost.object(0)
GABAb0_i_vec = h.Vector()
GABAb0_i_vec.record(gababpost._ref_i)
GABAb0_g_vec = h.Vector()
GABAb0_g_vec.record(gababpost._ref_g)
GABAb0_gmax_vec = h.Vector()
GABAb0_gmax_vec.record(gababpost._ref_gmax)
GABAb0_Ron_vec = h.Vector()
GABAb0_Ron_vec.record(gababpost._ref_Ron)
GABAb0_Roff_vec = h.Vector()
GABAb0_Roff_vec.record(gababpost._ref_Roff)
GABAb0_R_vec = h.Vector()
GABAb0_R_vec.record(gababpost._ref_R)
GABAb0_G_vec = h.Vector()
GABAb0_G_vec.record(gababpost._ref_G)

#h.tstop = 1000
tstop = 3000+10000*0


# run the simulation

gRERE_GABAA     = RERE*0.2
gRETC_GABAA     = RETCa*0.02
gRETC_GABAB     = RETCb*0.04
gTCRE_AMPA      = TCRE*0.2
gPYPY_AMPA      = PYPY*0.6
gPYIN_AMPA      = PYIN*0.2
gINPY_GABAA     = INPYa*gabaapercent*0.15
gINPY_GABAB     = INPYb*gababpercent*0.03
gPYRE_AMPA      = PYRE*1.2
gPYTC_AMPA      = PYTC*0.01
gTCPY_AMPA      = TCPY*1.2
gTCIN_AMPA      = TCIN*0.4


def go():
    h.dt=0.1
    h.celsius=celsius
    h.finitialize(v_init)
    #neuron.init()

    
    # params:        RERE,        RETCa,        ***RETCb,     TCRE,        PYPY,       PYIN,       INPYa,                     ***INPYb,                  PYRE,        PYTC,        TCPY,        TCIN
    assign_synapses( RERE*0.2,    RETCa*0.02,   RETCb*0.04,   TCRE*0.2,    PYPY*0.6,   PYIN*0.2,   INPYa*gabaapercent*0.15,   INPYb*gababpercent*0.03,   PYRE*1.2,    PYTC*0.01,   TCPY*1.2,    TCIN*0.4)
    #assign_synapses(gRERE_GABAA, gRETC_GABAA,  gRETC_GABAB,  gTCRE_AMPA,  gPYPY_AMPA, gPYIN_AMPA, gINPY_GABAA,               gINPY_GABAB,               gPYRE_AMPA,  gPYTC_AMPA,  gTCPY_AMPA,  gTCIN_AMPA)

    
    h.fcurrent()
    h.cvode.re_init()
    h.frecord_init()
    
    printPYinfo(0)
    printINinfo(0)
    printTCinfo(0)
    printREinfo(0)
    printWeight(0)
    
    field.append(0)
    while h.t<tstop:
        h.fadvance()
        field.append(xfield(230,fielddist,watchneuron))

go()

"""

h.dt=0.1
h.celsius=celsius
h.tstop=tstop
h.finitialize(v_init)
printPYinfo(0)
printINinfo(0)
printTCinfo(0)
printREinfo(0)

# params:       RERE, RETCa,   RETCb,   TCRE,   PYPY,   PYIN, INPYa,               INPYb,                PYRE,   PYTC,   TCPY,   TCIN
assign_synapses(0.2,  0*0.02,  0*0.04,  0*0.2,  0*0.6,  0.2,  0*gabaapercent*0.15, 0*gababpercent*0.03,  0*1.2,  0*0.01, 0*1.2,  0*0.4)
printWeight(0)

h.fcurrent()
h.cvode.re_init()
h.frecord_init()
h.run()
"""
#------------------------------------------
# figures
#------------------------------------------
"""
# synaptic  param plot
fig = pyplot.figure(figsize=(8,4))
ax1 = fig.add_subplot(6,1,1)
i1 = ax1.plot(t_vec, GABAa0_i_vec, color='black')
ax1.legend(i1, ['TC[0] GABAA_i'])
ax1.set_ylabel('nA')
ax1.set_xticks([]) # Use ax2's tick labels

ax2 = fig.add_subplot(6,1,2)
g1 = ax2.plot(t_vec, GABAa0_g_vec, color='black')
ax2.legend(g1, ['TC[0] GABAA_g'])
ax2.set_ylabel('#')
#ax2.set_xlabel('time (ms)')
ax2.set_xticks([]) # Use ax2's tick labels

ax3 = fig.add_subplot(6,1,3)
gmax1 = ax3.plot(t_vec, GABAa0_gmax_vec, color='black')
ax3.legend(gmax1, ['TC[0] GABAA_gmax'])
ax3.set_ylabel('#')
#ax3.set_xlabel('time (ms)')
ax3.set_xticks([]) # Use ax2's tick labels
              
ax4 = fig.add_subplot(6,1,4)
Ron1 = ax4.plot(t_vec, GABAa0_Ron_vec, color='black')
ax4.legend(Ron1, ['TC[0] GABAA_Ron'])
ax4.set_ylabel('#')
#ax4.set_xlabel('time (ms)')
ax4.set_xticks([]) # Use ax2's tick labels

ax5 = fig.add_subplot(6,1,5)
Roff1 = ax5.plot(t_vec, GABAa0_Roff_vec, color='black')
ax5.legend(Roff1, ['TC[0] GABAA_Roff'])
ax5.set_ylabel('#')
ax5.set_xlabel('time (ms)')
#ax5.set_xticks([]) # Use ax2's tick labels



fig = pyplot.figure(figsize=(8,4))
ax1 = fig.add_subplot(7,1,1)
i2 = ax1.plot(t_vec, GABAb0_i_vec, color='black')
ax1.legend(i1, ['TC[0] GABAB_i'])
ax1.set_ylabel('nA')
ax1.set_xticks([]) # Use ax2's tick labels

ax2 = fig.add_subplot(7,1,2)
g1 = ax2.plot(t_vec, GABAb0_g_vec, color='black')
ax2.legend(g1, ['TC[0] GABAB_g'])
ax2.set_ylabel('#')
#ax2.set_xlabel('time (ms)')
ax2.set_xticks([]) # Use ax2's tick labels

ax3 = fig.add_subplot(7,1,3)
gmax1 = ax3.plot(t_vec, GABAb0_gmax_vec, color='black')
ax3.legend(g1, ['TC[0] GABAB_gmax'])
ax3.set_ylabel('#')
#ax3.set_xlabel('time (ms)')
ax3.set_xticks([]) # Use ax2's tick labels
              
ax4 = fig.add_subplot(7,1,4)
Ron1 = ax4.plot(t_vec, GABAb0_Ron_vec, color='black')
ax4.legend(Ron1, ['TC[0] GABAB_Ron'])
ax4.set_ylabel('#')
#ax4.set_xlabel('time (ms)')
ax4.set_xticks([]) # Use ax2's tick labels

ax5 = fig.add_subplot(7,1,5)
Roff1 = ax5.plot(t_vec, GABAb0_Roff_vec, color='black')
ax5.legend(Roff1, ['TC[0] GABAB_Roff'])
ax5.set_ylabel('#')
#ax5.set_xlabel('time (ms)')
ax5.set_xticks([]) # Use ax2's tick labels

ax6 = fig.add_subplot(7,1,6)
R1 = ax6.plot(t_vec, GABAb0_R_vec, color='black')
ax6.legend(R1, ['TC[0] GABAB_R'])
ax6.set_ylabel('#')
#ax6.set_xlabel('time (ms)')
ax6.set_xticks([]) # Use ax2's tick labels

ax7 = fig.add_subplot(7,1,7)
G1 = ax7.plot(t_vec, GABAb0_G_vec, color='black')
ax7.legend(G1, ['TC[0] GABAB_G'])
ax7.set_ylabel('#')
ax7.set_xlabel('time (ms)')
"""

"""
ax2 = fig.add_subplot(2,1,2)
syn_plot = ax2.plot(t_vec, syn_i_vec, color='blue')
ax2.legend(syn_plot, ['synaptic current'])
ax2.set_ylabel(h.units('ExpSyn.i'))
ax2.set_xlabel('time (ms)')
pyplot.show()
"""

# voltage traces
fig = pyplot.figure(figsize=(8,4))
ax1 = fig.add_subplot(1,1,1)
PY1 = ax1.plot(t_vec, PYVtrace[watchneuron], color='black')
ax1.legend(PY1, ['PY[%d]'%(watchneuron)])
#PY2 = ax1.plot(t_vec, PYVtrace[1], color='red')
#PY3 = ax1.plot(t_vec, PYVtrace[nthalamiccells/3-1], color='blue')
#PY4 = ax1.plot(t_vec, PYVtrace[nthalamiccells/2-1], color='green')
#ax1.legend(PY1 + PY2 + PY3 + PY4, ['PY1', 'PY2', 'PY%d'%(ncorticalcells/3), 'PY%d'%(ncorticalcells/2)])
ax1.set_ylabel('mV')
#ax1.set_xticks([]) # Use ax2's tick labels
ax1.set_xlabel('time (ms)')
"""
ax2 = fig.add_subplot(2,1,2)
syn_plot = ax2.plot(t_vec, syn_i_vec, color='blue')
ax2.legend(syn_plot, ['synaptic current'])
ax2.set_ylabel(h.units('ExpSyn.i'))
ax2.set_xlabel('time (ms)')
pyplot.show()
"""

fig = pyplot.figure(figsize=(8,4))
ax1 = fig.add_subplot(1,1,1)
IN1 = ax1.plot(t_vec, INVtrace[watchneuron], color='black')
ax1.legend(IN1, ['IN[%d]'%(watchneuron)])
#IN2 = ax1.plot(t_vec, INVtrace[1], color='red')
#IN3 = ax1.plot(t_vec, INVtrace[ncorticalcells/3-1], color='blue')
#IN4 = ax1.plot(t_vec, INVtrace[ncorticalcells/2-1], color='green')
#ax1.legend(IN1 + IN2 + IN3 + IN4, ['IN1', 'IN2', 'IN%d'%(ncorticalcells/3), 'IN%d'%(ncorticalcells/2)])
ax1.set_ylabel('mV')
#ax1.set_xticks([]) # Use ax2's tick labels
ax1.set_xlabel('time (ms)')

fig = pyplot.figure(figsize=(8,4))
ax1 = fig.add_subplot(1,1,1)
TC1 = ax1.plot(t_vec, TCVtrace[0], color='black')
ax1.legend(TC1, ['TC[%d]'%(watchneuron)])
#TC2 = ax1.plot(t_vec, TCVtrace[1], color='red')
#TC3 = ax1.plot(t_vec, TCVtrace[nthalamiccells/3-1], color='blue')
#TC4 = ax1.plot(t_vec, TCVtrace[nthalamiccells/2-1], color='green')
#ax1.legend(TC1 + TC2 + TC3 + TC4, ['TC1', 'TC2', 'TC%d'%(nthalamiccells/3), 'TC%d'%(nthalamiccells/2)])
ax1.set_ylabel('mV')
#ax1.set_xticks([]) # Use ax2's tick labels
ax1.set_xlabel('time (ms)')

fig = pyplot.figure(figsize=(8,4))
ax1 = fig.add_subplot(1,1,1)
RE1 = ax1.plot(t_vec, REVtrace[0], color='black')
ax1.legend(RE1, ['RE[%d]'%(watchneuron)])
#RE2 = ax1.plot(t_vec, REVtrace[1], color='red')
#RE3 = ax1.plot(t_vec, REVtrace[nthalamiccells/3-1], color='blue')
#RE4 = ax1.plot(t_vec, REVtrace[nthalamiccells/2-1], color='green')
#ax1.legend(RE1 + RE2 + RE3 + RE4, ['RE1', 'RE2', 'RE%d'%(nthalamiccells/3), 'RE%d'%(nthalamiccells/2)])
ax1.set_ylabel('mV')
#ax1.set_xticks([]) # Use ax2's tick labels
ax1.set_xlabel('time (ms)')

#----------------------------------------------------------------------------
# field plot
#----------------------------------------------------------------------------
fig = pyplot.figure(figsize=(8,4))
ax1 = fig.add_subplot(1,1,1)
field = ax1.plot(t_vec, field, color='black')
ax1.legend(field, ['field'])
ax1.set_ylabel('mV')
ax1.set_xlabel('time (ms)')

#----------------------------------------------------------------------------
# Raster plot
#----------------------------------------------------------------------------
labels = ['PY', 'IN', 'TC', 'RE']
y=[50,150,250,350]
fig_handle = pyplot.figure(figsize=(8,4))
ax = fig_handle.add_subplot(111)
ax.set_title('Raster plot')
ax.set_xlabel('$t$ (ms)') # Note LaTeX
ax.set_yticks([])


sp = spikeplot.SpikePlot(fig=fig_handle)
sp.set_markerscale(2)
sp.set_marker('.')

PYspikes = spiketrain.netconvecs_to_listoflists(PYtimevec, PYidvec)
sp.set_markercolor('black')
sp.plot_spikes(PYspikes, draw=False, label='PY')

INspikes = spiketrain.netconvecs_to_listoflists(INtimevec, INidvec)
sp.set_markercolor('blue')
sp.plot_spikes(INspikes, cell_offset=len(PYspikes), label='IN')

TCspikes = spiketrain.netconvecs_to_listoflists(TCtimevec, TCidvec)
sp.set_markercolor('red')
sp.plot_spikes(TCspikes, cell_offset=len(PYspikes)+len(INspikes), label='TC')

REspikes = spiketrain.netconvecs_to_listoflists(REtimevec, REidvec)
sp.set_markercolor('green')
sp.plot_spikes(REspikes, cell_offset=len(PYspikes)+len(INspikes)+len(TCspikes), label='RE')
pyplot.xlim(0,tstop)
pyplot.yticks(y, labels)
