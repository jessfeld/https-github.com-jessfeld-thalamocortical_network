# nav_type corresponds to Nav1.1 mutations. drug corresponds to AED. dose is dose of AED
# nav_type: Nav1.1 WT is 0, T875M is 1, W1204R is 2, R1648H is 3, R859C is 4, knock out is 5
# drug:     No drug is 0, carbamazepine 1, oxcarbazepine 2, lamictal 3, eslicarb. 4, VPA 5, diazepam 6
# dose:     percentage of full dose divided by 100. Full dose is 250nM (for Na channel drugs), which probably super-physiological

import time
from netpyne import sim  # import netpyne init module

cfg, netParams = sim.readCmdLineArgs(simConfigDefault='cfg.py', netParamsDefault='netParams.py')
###############################################################################
# create, simulate, and analyse network
###############################################################################
sim.create(netParams = netParams, simConfig = cfg)

# network parameter randomization  
seed = int(time.time() * 1e7) & 0xffffffff
rndm = sim.h.Random()
rndm.Random123(sim.rank, 0 , 0) #initialize with seed as second argument to achieve different results for each run
for TCsoma in [ x.secs.soma for x in sim.net.cells if x.tags['cellType'] == 'TC']:
#    TCsoma.hObj.ghbar_iar = 17.5e-6
#    TCsoma.pointps.kleak_0.hObj.gmax = 40e-4
    TCsoma.hObj.ghbar_iar = rndm.normal(17.5, 0.0008) * 1e-6
    TCsoma.pointps.kleak_0.hObj.gmax = rndm.normal(40, 0.003) * 1e-4

sim.pc.barrier()
sim.simulate()
sim.pc.barrier()
sim.analyze()

