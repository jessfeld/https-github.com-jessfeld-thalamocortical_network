from neuron import h

from netpyne import sim

import netParams
import cfg

sim.create(netParams = netParams.netParams, simConfig = cfg.simConfig)

sim.pc.barrier()

rndm = sim.h.Random()
rndm.Random123(sim.rank, sim.rank, sim.rank)

rndm.normal(10, 10)
x = [ [sim.rank, rndm.repick()] for x in range(5) ]

print(x)