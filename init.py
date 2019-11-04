# nav_type corresponds to Nav1.1 mutations. drug corresponds to AED. dose is dose of AED
# nav_type: Nav1.1 WT is 0, T875M is 1, W1204R is 2, R1648H is 3, R859C is 4, knock out is 5
# drug:     No drug is 0, carbamazepine 1, oxcarbazepine 2, lamictal 3, eslicarb. 4, VPA 5, diazepam 6
# dose:     percentage of full dose divided by 100. Full dose is 250nM (for Na channel drugs), which probably super-physiological

nav_type = 0;          drug = 0;          dose = 0.05;          duration = 2500

if __name__ == "__main__":
    import netParams # import parameters file
    import cfg
    import time

    from netpyne import sim  # import netpyne init module
    from neuron import h

    ###############################################################################
    # create, simulate, and analyse network
    ###############################################################################
    cfg.simConfig.duration = duration
    #sim.createSimulateAnalyze(netParams = netParams.netParams, simConfig = cfg.simConfig)

    ###############################################################################
    # network randomization
    ###############################################################################  
    sim.create(netParams = netParams.netParams, simConfig = cfg.simConfig)
    
    seed = int(time.time() * 1e7) & 0xffffffff
    rndm = sim.h.Random()
    rndm.Random123(sim.rank, seed, 0)
    for TCsoma in [ x.secs.soma for x in sim.net.cells if x.tags['cellType'] == 'TC']:
        TCsoma.hObj.ghbar_iar = rndm.normal(17.5, 0.0008) * 1e-6
        TCsoma.pointps.kleak_0.hObj.gmax = rndm.normal(40, 0.003) * 1e-4
    
    sim.pc.barrier()
    sim.simulate()

    sim.pc.barrier()
    sim.analyze()


    ###############################################################################
    # just in case to debug
    ###############################################################################
    ## PY = sim.net.cells[  0:100]
    ## IN = sim.net.cells[100:300]
    ## TC = sim.net.cells[300:400]
    ## RE = sim.net.cells[400:500]
    ## 
    ## PYsoma = [ x.secs['soma']['hObj'] for x in PYcells ]
    ## INsoma = [ x.secs['soma']['hObj'] for x in INcells ]
    ## TCsoma = [ x.secs['soma']['hObj'] for x in TCcells ]
    ## REsoma = [ x.secs['soma']['hObj'] for x in REcells ]

    #    for TCsoma in [ x.secs.soma for x in sim.net.cells if x.tags['cellType'] == 'TC']:
    #    sim.net.cells[i].secs.soma.mechs.iar.ghbar = 
    #    sim.net.cells[i].secs.soma.pointps.kleak_0.gmax = 


##In [10]: TCsomas[0].mechs.iar.ghbar
##Out[10]: 5.2499999999999995e-05
##
##In [11]: sim.net.cells[300].secs.soma.mechs.iar.ghbar
##Out[11]: 1.75e-05
