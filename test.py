import netParams # import parameters file
import cfg
import time

nav_type, drug, dose, duration = 0, 0, 0.05, 300

from netpyne import sim  # import netpyne init module
from neuron import h

cfg.simConfig.duration = duration = 300
sim.create(netParams = netParams.netParams, simConfig = cfg.simConfig)

seed = int(time.time() * 1e7) & 0xffffffff
rndm = sim.h.Random()
rndm.Random123(sim.rank, 0 , 0) #initialize with seed as second argument to achieve different results for each run
for TCsoma in [ x.secs.soma for x in sim.net.cells if x.tags['cellType'] == 'TC']:
    TCsoma.hObj.ghbar_iar = rndm.normal(17.5, 0.0008) * 1e-6
    TCsoma.pointps.kleak_0.hObj.gmax = rndm.normal(40, 0.003) * 1e-4

sim.simulate()
sim.analyze()
