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
