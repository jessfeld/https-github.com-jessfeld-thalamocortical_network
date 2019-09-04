#------------------------------------------------------------------------------
# SIMULATION CONFIGURATION
#------------------------------------------------------------------------------

from netpyne import specs
from settings import nav_type, drug, dose

str_nav_type = ['WT', 'T875M', 'W1204R', 'R1648H', 'R859C', 'knock out']
str_drug = ['no drug', 'carbamazepine', 'oxcarbazepine', 'lamictal', 'eslicarb', 'VPA', 'diazepam'] 
watchneuron = 11
simConfig = specs.SimConfig()   # object of class SimConfig to store the simulation configuration

celsius = 36
v_init = -70
# Simulation parameters
simConfig.checkErrors=False # True # 
simConfig.trans = 0000
simConfig.Dt = 0.1
simConfig.steps_per_ms = 1/simConfig.Dt
simConfig.npoints = 5000

simConfig.duration = simConfig.npoints * simConfig.Dt # simConfig.trans + simConfig.npoints * simConfig.Dt # Duration of the simulation, in ms
simConfig.dt = simConfig.Dt # Internal integration timestep to use
simConfig.hParams['celsius'] = celsius
simConfig.hParams['v_init'] = v_init
simConfig.seeds = {'conn': 1, 'stim': 1, 'loc': 1} # Seeds for randomizers (connectivity, input stimulation and cell locations)
simConfig.verbose = False # True  # show detailed messages 

# Recording 
simConfig.recordCells = []  # which cells to record from

simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}
                          #'i_AMPA': {'sec':'soma', 'loc':0.5, 'synMech': 'AMPA_S', 'var': 'i', 'conds': {'pop': ['RE', 'TC', 'IN', 'PY']}},
                          #'g_AMPA': {'sec':'soma', 'loc':0.5, 'synMech': 'AMPA_S', 'var': 'g', 'conds': {'pop': ['RE', 'TC', 'IN', 'PY']}},
                          #'i_GABAA': {'sec':'soma', 'loc':0.5, 'synMech': 'GABAA_S', 'var': 'i', 'conds': {'pop': ['TC', 'PY', 'RE']}},
                          #'g_GABAA': {'sec':'soma', 'loc':0.5, 'synMech': 'GABAA_S', 'var': 'g', 'conds': {'pop': ['TC', 'PY', 'RE']}},
                          #'i_GABAB1': {'sec':'soma', 'loc':0.5, 'synMech': 'GABAB_S1', 'var': 'i'},
                          #'g_GABAB1': {'sec':'soma', 'loc':0.5, 'synMech': 'GABAB_S1', 'var': 'g'},
                          #'i_GABAB2': {'sec':'soma', 'loc':0.5, 'synMech': 'GABAB_S2', 'var': 'i'},
                          #'g_GABAB2': {'sec':'soma', 'loc':0.5, 'synMech': 'GABAB_S2', 'var': 'g'}
                          }

#simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}

simConfig.recordStim = True  # record spikes of cell stims
simConfig.recordStep = 0.1 # Step size in ms to save data (eg. V traces, LFP, etc)
#simConfig.cvode_active = True

# Saving
simConfig.simLabel = "knox"
simConfig.saveFolder = "data_knox_v1"
simConfig.filename = 'knox_v1'  # Set file output name
simConfig.saveFileStep = 1000 # step size in ms to save data to disk
#simConfig.savePickle = True # Whether or not to write spikes etc. to a .mat file
#simConfig.saveJson = True
#simConfig.saveMat = True
#simConfig.saveDpk = False

# Analysis and plotting 
#simConfig.analysis['plotRaster'] = {'include': ['PY', 'IN', 'TC', 'RE'], 'orderInverse': True} #True # Whether or not to plot a raster
simConfig.analysis['plotRaster'] = {'include': ['RE', 'TC', 'IN', 'PY'], 'orderInverse': False, 'showFig' : False, 'saveFig':'./images/raster%d%d%d_%s_%s_dose%d.png'%(nav_type,drug, dose*100, str_nav_type[nav_type], str_drug[drug], dose*100)} #True # Whether or not to plot a raster

#simConfig.analysis['plotRaster'] = True  # Plot raster
simConfig.analysis['plotTraces'] = {'include': [('PY',[0+watchneuron]),('IN',[0+watchneuron]),('TC',[0+watchneuron]),('RE',[0+watchneuron])], 'timeRange': [0,simConfig.duration], 'oneFigPer': 'trace', 'overlay': False, 'showFig' : False, 'saveFig':'./images/plotTraces%d%d%d_%s_%s_dose%d.png'%(nav_type, drug, dose*100, str_nav_type[nav_type], str_drug[drug], dose*100)} # plot recorded traces for this list of cells

#simConfig.analysis['plotRatePSD'] = {'include': ['PY', 'IN', 'TC', 'RE'], 'Fs': 50, 'smooth': 10} # plot recorded traces for this list of cells

#simConfig.addAnalysis('plot2Dnet', {'include': ['PY', 'IN', 'TC', 'RE'],  'showConns': True, 'saveFig': './images/plot2Dnet.png', 'showFig': False})
#simConfig.addAnalysis('plotShape', {'showSyns': True})
#simConfig.addAnalysis('plotConn', {'include': ['allCells'], 'feature': 'strength'})
#simConfig.analysis.plotConn(include=['allCells'], feature='strength', groupBy='pop', figSize=(9,9), showFig=True)
#simConfig.analysis['plotConn'] = True           # plot connectivity matrix

# netParams
simConfig.stimtime = 10050
simConfig.randomstim = 0

simConfig.field = 0

simConfig.runStopAt = simConfig.duration

