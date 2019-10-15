import netParams # import parameters file
import cfg

from netpyne import sim  # import netpyne init module
from neuron import h

###############################################################################
# create, simulate, and analyse network
###############################################################################
sim.createSimulateAnalyze(netParams = netParams.netParams, simConfig = cfg.simConfig)
