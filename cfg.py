from netpyne import specs

str_nav_type = ['WT', 'T875M', 'W1204R', 'R1648H', 'R859C', 'knock out']
str_drug = ['no drug', 'carbamazepine', 'oxcarbazepine', 'lamictal', 'eslicarb', 'VPA', 'diazepam'] 
cfg = simConfig = specs.SimConfig()   # object of class SimConfig to store the simulation configuration

#------------------------------------------------------------------------------
# NA CHANNEL PARAMETERS
#------------------------------------------------------------------------------
cfg.nav_type = 3
cfg.drug = 2
cfg.dose = 0.05
cfg.perc = 0.0

#------------------------------------------------------------------------------
# SIMULATION CONFIGURATION
#------------------------------------------------------------------------------
# Simulation parameters
cfg.allowSelfConns = False # True doesn't actually do anything
cfg.checkErrors=False # True # 
cfg.duration = 700 # Duration of the simulation, in ms
cfg.dt = 0.1
cfg.hParams['celsius'] = 36
cfg.hParams['v_init'] = -70
cfg.seeds = {'conn': 1, 'stim': 1, 'loc': 1} # Seeds for randomizers (connectivity, input stimulation and cell locations)
cfg.verbose = False # True  # show detailed messages 

# Recording 
#cfg.recordCells = [0, 50, 100, 200, 300, 350, 400, 450]  # which cells to record from
cfg.recordCells = [0, 49, 100, 149, 300, 349, 400, 449]
cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}
cfg.recordStim = True  # record spikes of cell stims
cfg.recordStep = 0.1 # Step size in ms to save data (eg. V traces, LFP, etc)

# Saving
cfg.simLabel = "sim"
cfg.saveFolder = "data"
cfg.saveFileStep = 1000 # step size in ms to save data to disk
cfg.savePickle = True # Whether or not to write spikes etc. to a .mat file

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
=======
cfg.analysis['plotRaster'] = {'include': ['RE', 'TC', 'IN', 'PY'], 'orderInverse': False, 'showFig' : False, 'saveFig':'./images/raster.png'} 



