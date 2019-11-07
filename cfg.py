#------------------------------------------------------------------------------
# SIMULATION CONFIGURATION
#------------------------------------------------------------------------------

from netpyne import specs

str_nav_type = ['WT', 'T875M', 'W1204R', 'R1648H', 'R859C', 'knock out']
str_drug = ['no drug', 'carbamazepine', 'oxcarbazepine', 'lamictal', 'eslicarb', 'VPA', 'diazepam'] 
cfg = simConfig = specs.SimConfig()   # object of class SimConfig to store the simulation configuration

simConfig.nav_type, simConfig.drug, simConfig.dose, simConfig.duration = 0, 0, 0.05, 300
# Simulation parameters
simConfig.allowSelfConns = False # True doesn't actually do anything
simConfig.checkErrors=False # True # 
simConfig.dt = 0.1
simConfig.hParams['celsius'] = 36
simConfig.hParams['v_init'] = -70
simConfig.seeds = {'conn': 1, 'stim': 1, 'loc': 1} # Seeds for randomizers (connectivity, input stimulation and cell locations)
simConfig.verbose = False # True  # show detailed messages 

# Recording 
simConfig.recordCells = [0, 49, 100, 149, 300, 349, 400, 449]  # which cells to record from

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
simConfig.simLabel = "sim"
simConfig.saveFolder = "data"
simConfig.saveFileStep = 1000 # step size in ms to save data to disk
simConfig.savePickle = True # Whether or not to write spikes etc. to a .mat file
#simConfig.saveJson = True
#simConfig.saveMat = True
#simConfig.saveDpk = False

# Analysis and plotting
simConfig.analysis['plotRaster'] = {'include': ['RE', 'TC', 'IN', 'PY'], 'timeRange': [0, simConfig.duration], 'orderInverse': False, 'showFig' : False, 'saveFig':'./images/raster.png'} 
#simConfig.analysis['plotRaster'] = {'include': ['RE', 'TC', 'IN', 'PY'], 'timeRange': [graphstart, graphstop], 'orderInverse': False, 'showFig' : False, 'saveFig':'./images/raster%d%d%d_%s_%s_dose%d.png'%(nav_type,drug, dose*100, str_nav_type[nav_type], str_drug[drug], dose*100)} #True # Whether or not to plot a raster
#simConfig.analysis['plotTraces'] = {'include': ['RE', 'TC', 'IN', 'PY'], 'timeRange': [graphstart, graphstop], 'oneFigPer': 'trace', 'overlay': True, 'showFig' : False, 'saveFig':'./images/plotTraces%d%d%d_%s_%s_dose%d.png'%(nav_type, drug, dose*100, str_nav_type[nav_type], str_drug[drug], dose*100)} # plot recorded traces for this list of cells

#simConfig.analysis['plotRatePSD'] = {'include': ['PY', 'IN', 'TC', 'RE'], 'Fs': 50, 'smooth': 10} # plot recorded traces for this list of cells
#simConfig.addAnalysis('plot2Dnet', {'include': ['PY', 'IN', 'TC', 'RE'],  'showConns': True, 'saveFig': './images/plot2Dnet.png', 'showFig': False})
#simConfig.addAnalysis('plotShape', {'showSyns': True})
#simConfig.addAnalysis('plotConn', {'include': ['allCells'], 'feature': 'strength'})
#simConfig.analysis.plotConn(include=['allCells'], feature='strength', groupBy='pop', figSize=(9,9), showFig=True)
#simConfig.analysis['plotConn'] = True           # plot connectivity matrix


