import netParams # import parameters file
import cfg

from netpyne import sim  # import netpyne init module
from neuron import h

sim.createSimulateAnalyze(netParams = netParams.netParams, simConfig = cfg.simConfig)  # create and simulate network(pops, cells, conns, rxd, stims, simData) = sim.create(netParams.netParams, cfg.simConfig, output=True)

###############################################################################
# create, simulate, and analyse network
###############################################################################
"""
(pops, cells, conns, rxd, stims, simData) = sim.create(netParams.netParams, cfg.simConfig, output=True)

#create, puts the network together but doesn't run
ncl = h.List("NetCon")

asy = [x for x in ncl if 'GABAb' in str(x.syn())]
print([x.syn() for x in asy])
precellRE = [x for x in asy if x.precell().tags['cellType'] == 'RE']
postcellTC = [x for x in asy if x.postcell().tags['cellType'] == 'TC']
precellIN = [x for x in asy if x.precell().tags['cellType'] == 'IN']
postcellPY = [x for x in asy if x.postcell().tags['cellType'] == 'PY']
print( 'RE->:%d'%(len(precellRE)) )
print( '->TC:%d'%(len(postcellTC)))
print( 'IN->:%d'%(len(precellIN)) )
print( '->PY:%d'%(len(postcellPY)))
"""


"""
if (randInit):
    rgh = sim.h.Random()
    rk1 = sim.h.Random()
    rgh.normal(17.5,0.0008)        #random number generator behaves weirdly for very small numbers, so multiply by 10^-6 below
    rk1.normal(40,0.003)
    for i in range(N_TC):
        print(rgh.repick())
        a.append(rgh.repick() * 1e-6)
        b.append(rgh.repick() * 1e-6)        
        sim.net.cells[200+i].secs.soma.mechs.iar.ghbar = rgh.repick() * 1e-6
        sim.net.cells[200+i].secs.soma.pointps.kleak_0.gmax = rk1.repick() * 1e-4
        #print("TC(",i,") gh:", sim.net.cells[200+i].secs.soma.mechs.iar.ghbar, " gmax:", sim.net.cells[200+i].secs.soma.pointps.kleak_0.gmax)

print(len(sim.net.cells) )
print(len(sim.net.cells) )
print("------------------------------------DONE------------------------------------")
print(a)
print(b)

##### sim.simulate() ################
##### sim.runSim()   ################

###############################################################################
### Run Simulation
###############################################################################
sim.pc.barrier()
sim.timing('start', 'runTime')
sim.preRun()
#sim.h.init()

sim.pc.set_maxstep(10)
#sim.h.stdinit()
sim.h.dt = 0.1 # Fixed dt
sim.h.fcurrent()
#sim.h.cvode.re_init()
sim.h.frecord_init()

#printPYinfo(sim.net.cells[0])
#printINinfo(sim.net.cells[100])
#printTCinfo(sim.net.cells[200])
#printREinfo(sim.net.cells[300])
#printWeight()


if sim.rank == 0: print('\nRunning simulation for %s ms...'%sim.cfg.duration)
sim.pc.psolve(sim.cfg.duration)

sim.pc.barrier() # Wait for all hosts to get to this point
sim.timing('stop', 'runTime')
if sim.rank==0:
    print('  Done; run time = %0.2f s; real-time ratio: %0.2f.' %
        (sim.timingData['runTime'], sim.cfg.duration/1000/sim.timingData['runTime']))
########################################
sim.gatherData()                  # gather spiking data and cell info from each node
#####################################
sim.analyze()
"""


