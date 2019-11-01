# nav_type corresponds to Nav1.1 mutations. drug corresponds to AED. dose is dose of AED
# nav_type: Nav1.1 WT is 0, T875M is 1, W1204R is 2, R1648H is 3, R859C is 4, knock out is 5
# drug:     No drug is 0, carbamazepine 1, oxcarbazepine 2, lamictal 3, eslicarb. 4, VPA 5, diazepam 6
# dose:     percentage of full dose divided by 100. Full dose is 250nM (for Na channel drugs), which probably super-physiological

nav_type = 3;          drug = 2;          dose = 0.05;          duration = 300 

if __name__ == "__main__":
    import netParams # import parameters file
    import cfg

    from netpyne import sim  # import netpyne init module
    from neuron import h

    ###############################################################################
    # create, simulate, and analyse network
    ###############################################################################
    cfg.simConfig.duration = duration
    sim.createSimulateAnalyze(netParams = netParams.netParams, simConfig = cfg.simConfig)

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