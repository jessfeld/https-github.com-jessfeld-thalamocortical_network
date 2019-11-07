from netpyne import specs

str_nav_type = ['WT', 'T875M', 'W1204R', 'R1648H', 'R859C', 'knock out']
str_drug = ['no drug', 'carbamazepine', 'oxcarbazepine', 'lamictal', 'eslicarb', 'VPA', 'diazepam'] 
cfg = specs.SimConfig()

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
cfg.analysis['plotRaster'] = {'include': ['RE', 'TC', 'IN', 'PY'], 'orderInverse': False, 'showFig' : False, 'saveFig':'./images/raster.png'} 
